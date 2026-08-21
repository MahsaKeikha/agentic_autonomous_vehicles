from orchestration.orchestrator import run
from safety.gate import authorize
def test_run(): assert run({"objective":"x"})["vehicle_control"] is False
def test_gate(): assert authorize("brake")["allowed"] is False
