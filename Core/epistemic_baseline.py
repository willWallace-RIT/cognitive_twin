from typing import List, Set

class EpistemicBaseline:
    """Tracks known information vectors to calibrate the depth of generated explanations."""
    
    def __init__(self, absorbed_nodes: List[str]):
        self.knowledge_graph: Set[str] = set(node.lower() for node in absorbed_nodes)

    def requires_explanation(self, concept: str) -> bool:
        return concept.lower() not in self.knowledge_graph
