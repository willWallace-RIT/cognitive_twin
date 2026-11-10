from typing import Dict, Any

class BehavioralProxy:
    """Applies extracted heuristics to shape the algorithm's problem-solving strategy."""
    
    def __init__(self, heuristics: Dict[str, float]):
        self.risk_tolerance = heuristics.get("risk_tolerance", 0.5)
        self.triage_bias = heuristics.get("structural_triage_bias", 0.5)
        self.tempo = heuristics.get("execution_tempo", 0.5)

    def evaluate_problem(self, problem_space: Dict[str, Any]) -> str:
        if self.triage_bias > 0.7:
            return "Strategy: Reject quick band-aids; enforce structural, long-term architectural refactoring."
        return "Strategy: Execute rapid iterative prototyping."
