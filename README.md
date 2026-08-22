# F74 | Agentic Autonomous Vehicles | L3 Gold Standard | v1.0

A governed multi-agent reference implementation for autonomous vehicle architecture, perception review, planning and scenario simulation, verification, safety-case development, and deployment governance.

## Six-agent architecture

- [System Architecture](AGENTS/system_architecture_agent.py)
- [Perception](AGENTS/perception_agent.py)
- [Planning Simulation](AGENTS/planning_simulation_agent.py)
- [Verification](AGENTS/verification_agent.py)
- [Safety Case](AGENTS/safety_case_agent.py)
- [Deployment Governance](AGENTS/deployment_governance_agent.py)

Tools are in `TOOLS/`, skills are in `SKILLS/`, and supporting layers include orchestration, memory, state, schemas, prompts, config, safety, observability, evals, benchmarks, examples, tests, docs, and CI.

## Gold-standard governance

F74 is fail closed. Analysis release requires system-architecture, perception, scenario-simulation, verification, safety-case, operational-design-domain, fallback, cybersecurity, and deployment-governance review plus explicit qualified human approval.

Release is blocked for perception coverage gaps, safety-critical scenario failures, failed verification evidence, unjustified ODD expansion, unverified minimum-risk fallback behavior, cybersecurity gaps, or unresolved high-risk hazards.

The system has no authority to steer, accelerate, brake, issue vehicle commands, perform remote driving, override safety systems, or authorize autonomous deployment.

Vehicle control authority: **false**  
Autonomous deployment authority: **false**

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

The behavioral verification layer includes eight direct governance tests plus a ten-scenario held-out safety suite.
