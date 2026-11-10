import json
from core.ingester import MultiModalIngester
from core.behavioral_proxy import BehavioralProxy
from core.epistemic_baseline import EpistemicBaseline

class CognitiveTwinEngine:
    """Core runtime combining multi-modal ingestion with personalized execution logic."""
    
    def __init__(self, data_path: str = "./data"):
        self.ingester = MultiModalIngester(data_path)
        self.proxy = None
        self.epistemic = None
        self.profile_style = {}

    def bootstrap(self, repo_path: str, watch_log_file: str, telemetry_file: str):
        print("[*] Bootstrapping cognitive twin from user baseline...")
        self.profile_style = self.ingester.parse_codebase(repo_path)
        watch_nodes = self.ingester.parse_watch_history(watch_log_file)
        telemetry = self.ingester.parse_telemetry(telemetry_file)

        self.proxy = BehavioralProxy(telemetry)
        self.epistemic = EpistemicBaseline(watch_nodes)
        print("[+] Bootstrap complete. Cognitive profile locked.")

    def run_task(self, task_description: str, technical_concepts: list) -> str:
        if not self.proxy or not self.epistemic:
            raise RuntimeError("Engine must be bootstrapped before running tasks.")

        strategy = self.proxy.evaluate_problem({"task": task_description})
        explanations_needed = [c for c in technical_concepts if self.epistemic.requires_explanation(c)]
        bypassed = [c for c in technical_concepts if c not in explanations_needed]

        output = {
            "task": task_description,
            "operational_strategy": strategy,
            "code_paradigm": self.profile_style.get("paradigm"),
            "bypassed_preamble": bypassed,
            "targeted_deep_dives": explanations_needed
        }
        return json.dumps(output, indent=2)

if __name__ == "__main__":
    engine = CognitiveTwinEngine()
    engine.bootstrap(
        repo_path="./mock_repo",
        watch_log_file="watch_history.json",
        telemetry_file="telemetry.csv"
    )
    
    result = engine.run_task(
        task_description="Refactor asynchronous concurrency loop for low-latency state sync.",
        technical_concepts=["low-level memory management", "async deadlock prevention", "custom GLSL shaders"]
    )
    print("\n--- Execution Result ---")
    print(result)
