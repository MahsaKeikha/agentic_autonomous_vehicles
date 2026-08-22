from orchestration.orchestrator import run

context = {
    "objective": "review simulated autonomous vehicle scenarios",
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

print(run(context))
