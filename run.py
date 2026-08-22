from orchestration.orchestrator import run

REFERENCE_CONTEXT = {
    "objective": "autonomous vehicle engineering review",
    "system_architecture_reviewed": True,
    "perception_reviewed": True,
    "scenario_simulation_reviewed": True,
    "verification_reviewed": True,
    "safety_case_reviewed": True,
    "odd_reviewed": True,
    "fallback_reviewed": True,
    "cybersecurity_reviewed": True,
    "deployment_governance_reviewed": True,
    "human_approval": True,
}

if __name__ == "__main__":
    print(run(REFERENCE_CONTEXT))
