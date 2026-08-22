from AGENTS.deployment_governance_agent import DeploymentGovernanceAgent
from AGENTS.perception_agent import PerceptionAgent
from AGENTS.planning_simulation_agent import PlanningSimulationAgent
from AGENTS.safety_case_agent import SafetyCaseAgent
from AGENTS.system_architecture_agent import SystemArchitectureAgent
from AGENTS.verification_agent import VerificationAgent
from safety.gate import authorize

AGENTS = [
    SystemArchitectureAgent(),
    PerceptionAgent(),
    PlanningSimulationAgent(),
    VerificationAgent(),
    SafetyCaseAgent(),
    DeploymentGovernanceAgent(),
]


def run(context: dict) -> dict:
    """Run all specialists and apply the fail-closed autonomous-vehicle release gate."""
    results = [agent.run(context) for agent in AGENTS]
    governance = authorize("analysis_release", context)
    return {
        "system": "F74",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "vehicle_control": False,
        "autonomous_deployment": False,
    }
