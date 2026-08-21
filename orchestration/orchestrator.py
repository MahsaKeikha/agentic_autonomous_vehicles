from AGENTS.system_architecture_agent import SystemArchitectureAgent
from AGENTS.perception_agent import PerceptionAgent
from AGENTS.planning_simulation_agent import PlanningSimulationAgent
from AGENTS.verification_agent import VerificationAgent
from AGENTS.safety_case_agent import SafetyCaseAgent
from AGENTS.deployment_governance_agent import DeploymentGovernanceAgent
A=[SystemArchitectureAgent(),PerceptionAgent(),PlanningSimulationAgent(),VerificationAgent(),SafetyCaseAgent(),DeploymentGovernanceAgent()]
def run(c): return {"system":"F74","results":[a.run(c) for a in A],"vehicle_control":False}
