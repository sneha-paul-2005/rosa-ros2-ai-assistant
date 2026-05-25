from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
from rag.knowledge_base import ROS2_KNOWLEDGE
import uuid

COLLECTION_NAME = "ros2_knowledge"

class RAGEngine:
    def __init__(self):
        # Run Qdrant in memory — no server needed!
        self.client = QdrantClient(":memory:")
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self._setup_collection()
        self._load_knowledge()

    def _setup_collection(self):
        self.client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=384,  # all-MiniLM-L6-v2 output size
                distance=Distance.COSINE
            )
        )

    def _load_knowledge(self):
        points = []
        for i, item in enumerate(ROS2_KNOWLEDGE):
            text = f"{item['topic']}: {item['content']}"
            vector = self.model.encode(text).tolist()
            points.append(PointStruct(
                id=i,
                vector=vector,
                payload={"topic": item["topic"], "content": item["content"]}
            ))
        self.client.upsert(
            collection_name=COLLECTION_NAME,
            points=points
        )
        

    def search(self, query: str, top_k: int = 2) -> str:
        vector = self.model.encode(query).tolist()
        results = self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=vector,
            limit=top_k
        )
        if not results.points:
            return "No relevant knowledge found."
        
        output = []
        for point in results.points:
            output.append(f"Topic: {point.payload['topic']}\n{point.payload['content']}")
        return "\n\n".join(output)

# Global instance
rag = RAGEngine()

def search_ros2_knowledge(query: str) -> str:
    return rag.search(query)