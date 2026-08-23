# F74 Agentic Autonomous Vehicles

**Maturity:** L3 Gold Standard  
**Version:** 1.0.0

A governed six-agent reference architecture for autonomous vehicle engineering across system architecture, perception review, planning and scenario simulation, verification, safety-case development, and deployment governance.

F74 is designed as an engineering and safety reference for autonomous driving systems. It helps structure evidence around the operational design domain, sensor coverage, perception performance, planning behavior, safety-critical scenarios, fallback behavior, verification, cybersecurity, and release governance.

This repository is not a driving system and has no authority to steer, accelerate, brake, issue vehicle commands, perform remote driving, override vehicle safety systems, or authorize autonomous deployment.

## Autonomous driving system model

```text
operational design domain
          |
          v
system architecture
          |
          v
sensor + perception review
          |
          v
planning / behavior simulation
          |
          v
verification evidence
          |
          v
safety case
          |
          v
deployment governance
          |
          v
qualified human approval
```

The architecture keeps simulation and review separate from real-world vehicle control.

## Six-agent architecture

| Agent | Responsibility | Core question |
|---|---|---|
| System Architecture Agent | System boundaries, interfaces, redundancy, compute, communications and ODD assumptions | Is the vehicle architecture consistent with the intended autonomous-driving scope? |
| Perception Agent | Sensor coverage, perception capability, uncertainty and failure modes | Can the system reliably perceive the required environment within the stated ODD? |
| Planning Simulation Agent | Behavior planning, scenario simulation and policy review | Does planned behavior remain safe across representative and safety-critical scenarios? |
| Verification Agent | Requirements traceability and objective evidence | Has each safety-relevant requirement been verified with appropriate evidence? |
| Safety Case Agent | Hazard arguments, residual risk, fallback and safety justification | Is there a coherent, evidence-backed case for the claimed operating scope? |
| Deployment Governance Agent | Release boundaries, field readiness and human approval | Is the evidence sufficient to consider deployment within the explicitly approved ODD? |

No agent can independently authorize a vehicle to operate autonomously.

## Repository structure

```text
AGENTS/
├── system_architecture_agent.py
├── perception_agent.py
├── planning_simulation_agent.py
├── verification_agent.py
├── safety_case_agent.py
└── deployment_governance_agent.py

SKILLS/
├── system_architecture.py
├── perception_review.py
├── scenario_simulation.py
├── safety_case.py
└── deployment_governance.py

TOOLS/
├── sensor_coverage_tool.py
├── scenario_matrix_tool.py
├── hazard_register_tool.py
├── traceability_tool.py
└── release_gate_tool.py

orchestration/
memory/
state/
schemas/
prompts/
config/
safety/
observability/
evals/
benchmarks/
examples/
tests/
docs/
.github/workflows/ci.yml
run.py
pyproject.toml
README.md
```

The separation between agents, deterministic tools, state, safety, observability and evaluation makes the review process auditable and reproducible.

## Operational Design Domain

The operational design domain, or ODD, defines the conditions in which an autonomous-driving function is intended to operate.

A useful ODD record can include:

```text
road_types
geographies
speed_range
weather
visibility
lighting
traffic_conditions
construction_conditions
road_surface_conditions
map_dependencies
localization_requirements
connectivity_assumptions
allowed_maneuvers
restricted_zones
minimum_infrastructure_requirements
```

The system should never assume capability outside the stated ODD.

Expanding the ODD requires additional evidence. A new road type, weather condition, geography, speed range or operational condition should trigger impact analysis across perception, planning, verification, fallback and safety case.

## System architecture

The System Architecture Agent reviews the end-to-end autonomous-driving stack.

Typical subsystems can include:

- perception sensors
- localization
- mapping
- sensor fusion
- object tracking
- prediction
- behavior planning
- trajectory planning
- control interfaces
- vehicle state estimation
- health monitoring
- fallback logic
- driver or operator interfaces
- communications
- logging
- cybersecurity
- remote-assistance interfaces where applicable

The architecture review should identify single points of failure, redundancy assumptions, timing dependencies and interface contracts.

## Sensor coverage

`TOOLS/sensor_coverage_tool.py` provides the deterministic reference abstraction for sensor coverage.

Potential sensing modalities include:

- cameras
- radar
- lidar
- ultrasonic sensors
- GNSS
- inertial sensors
- wheel odometry
- vehicle-state sensors

Coverage should be evaluated across the ODD, not only under nominal daylight conditions.

Important considerations include:

- field of view
- range
- resolution
- blind zones
- occlusion
- overlap
- weather sensitivity
- lighting sensitivity
- contamination
- calibration
- degradation
- sensor dropout
- latency

A coverage map should make unsupported regions visible.

## Perception review

The Perception Agent reviews whether the system can represent relevant road users, objects and environmental conditions.

Examples include:

- vehicles
- pedestrians
- cyclists
- motorcycles
- emergency vehicles
- animals
- debris
- road boundaries
- lane markings
- traffic lights
- traffic signs
- construction zones
- temporary traffic control
- stopped objects
- occluded road users

Perception review should report uncertainty and known blind spots rather than converting every uncertain observation into a confident label.

## Sensor fusion

Multi-sensor systems should document how observations are fused and how disagreement is handled.

Relevant questions include:

- What happens when sensors disagree?
- Which measurements are trusted under which conditions?
- How are stale observations detected?
- What happens when one modality is degraded?
- How is localization uncertainty propagated?
- Are confidence values calibrated?

Sensor redundancy is only useful if common-cause failures are considered.

## Calibration and health monitoring

Perception validity depends on sensor calibration and health.

Production systems should account for:

- intrinsic calibration
- extrinsic calibration
- time synchronization
- calibration drift
- sensor obstruction
- lens contamination
- radar blockage
- lidar degradation
- temperature effects
- component replacement

An unverified calibration state should block safety-critical operation.

## Planning and behavior

The Planning Simulation Agent reviews autonomous behavior without issuing control commands.

Behavior-planning scenarios can include:

- lane keeping
- lane changes
- merges
- yielding
- intersections
- unprotected turns
- pedestrian crossings
- cyclist interactions
- stop signs
- traffic signals
- emergency vehicles
- blocked lanes
- construction
- double-parked vehicles
- occlusions
- cut-ins
- sudden braking
- stalled vehicles

The system should distinguish desired behavior from verified behavior.

## Scenario matrix

`TOOLS/scenario_matrix_tool.py` provides structured scenario coverage.

A scenario record can include:

```text
scenario_id
ODD_conditions
initial_state
actors
actor_behaviors
traffic_rules
hazards
expected_behavior
safety_constraints
pass_fail_criteria
result
evidence_reference
```

Scenario coverage should include nominal, boundary, degraded and adversarial conditions.

## Rare and long-tail events

Autonomous-driving validation must account for low-frequency but high-consequence events.

Examples include:

- unusual pedestrian behavior
- erratic cyclists
- temporary road closures
- emergency responders
- unusual vehicles
- road debris
- sensor obstruction
- sudden weather transitions
- ambiguous lane geometry
- unexpected traffic control
- unusual construction layouts

A system should not claim broad safety merely because common scenarios perform well.

## Simulation

Simulation is an important validation tool but does not prove real-world safety on its own.

Simulation evidence should document:

- simulator version
- map version
- sensor model
- vehicle dynamics model
- scenario generator
- traffic agents
- environmental conditions
- randomness and seeds
- pass/fail criteria

Simulation results should be linked to the requirement or hazard they address.

## Verification

The Verification Agent uses `TOOLS/traceability_tool.py` to connect requirements, hazards and evidence.

A useful traceability chain is:

```text
ODD requirement
      |
      v
system requirement
      |
      v
safety requirement
      |
      v
implementation or architecture
      |
      v
verification evidence
      |
      v
safety-case claim
```

Verification should combine methods such as analysis, simulation, software-in-the-loop, hardware-in-the-loop, closed-course testing and controlled road testing as appropriate to the program.

F74 does not authorize road testing.

## Hazard register

`TOOLS/hazard_register_tool.py` supports explicit hazard tracking.

A hazard record can include:

```text
hazard_id
hazard
scenario
causal_factors
severity
exposure
controllability_or_mitigation
risk_level
safety_requirement
mitigation
verification_evidence
residual_risk
status
```

Open high-risk hazards are release blockers.

## Fallback behavior

Autonomous systems require defined behavior when the nominal driving function can no longer continue safely.

Potential triggers include:

- sensor failure
- localization failure
- map inconsistency
- compute fault
- planning failure
- ODD exit
- severe weather
- communications loss
- actuator fault
- cybersecurity event

Fallback behavior should be specified, tested and bounded.

## Minimum-risk condition

A minimum-risk condition is the state the vehicle attempts to reach when safe continuation of autonomous operation is no longer possible.

The correct behavior depends on the system and operating context.

The system should document:

- trigger conditions
- target condition
- available fallback maneuvers
- stopping assumptions
- shoulder availability
- hazard-light behavior
- operator notification
- escalation path
- degraded-control assumptions

Unverified fallback behavior is a release blocker.

## Remote assistance boundary

Some autonomous systems may use remote assistance or fleet operations support.

F74 distinguishes informational assistance from remote driving.

The repository may support review of:

- escalation logic
- incident context
- remote-support interfaces
- communication reliability
- operator workload
- auditability

It must not perform remote driving, generate steering/throttle/brake commands, or bypass vehicle safety systems.

## Safety case

The Safety Case Agent organizes claims, arguments and evidence.

A safety case should make explicit:

- the claim being made
- the scope and ODD
- supporting requirements
- hazard controls
- verification evidence
- scenario coverage
- fallback evidence
- assumptions
- limitations
- unresolved risks

A safety case is not a marketing statement. It is only as strong as the traceable evidence supporting it.

## Cybersecurity

Connected vehicles require cybersecurity to be integrated into the safety architecture.

Relevant considerations include:

- secure boot
- software integrity
- ECU authentication
- in-vehicle network security
- secure communications
- update mechanisms
- key management
- intrusion detection
- remote-interface protection
- fleet-service authentication
- logging
- vulnerability management
- supply-chain security

A cybersecurity weakness that can influence driving behavior should be treated as a safety concern.

## Data and privacy

Autonomous-vehicle systems can collect video, location, telemetry and environmental data.

Production deployments should address:

- data minimization
- location privacy
- bystander privacy
- retention
- access control
- encryption
- secure upload
- incident-log handling
- camera-data governance
- model-training permissions

## Deployment governance

The Deployment Governance Agent evaluates whether the evidence supports the requested deployment scope.

Deployment review can include:

- ODD version
- software version
- hardware configuration
- map version
- safety-case version
- open hazards
- verification status
- scenario coverage
- fallback evidence
- cybersecurity status
- field-monitoring readiness
- rollback capability
- qualified human approval

A deployment approval applies only to the reviewed configuration and ODD.

## Change management

Changes to hardware, software, models, maps, sensors, calibration, ODD or planning logic should trigger impact analysis.

A useful workflow is:

```text
proposed change
      |
      v
architecture impact
      |
      v
ODD impact
      |
      v
perception impact
      |
      v
planning impact
      |
      v
hazard impact
      |
      v
verification impact
      |
      v
safety-case update
      |
      v
deployment review
```

Prior evidence should not be assumed valid after a material change without review.

## Observability and field monitoring

The `observability/` layer supports traceable workflow execution and can be extended with field-monitoring evidence.

Useful monitoring concepts include:

- disengagements
- fallback activations
- perception uncertainty
- localization failures
- sensor health events
- planning anomalies
- safety-driver interventions where applicable
- incident reports
- software version
- ODD boundary events

Operational telemetry should inform safety review but does not automatically prove safety.

## Fail-closed release governance

`TOOLS/release_gate_tool.py` enforces a fail-closed release state.

Release blockers include:

- ODD not defined
- unsupported ODD expansion
- perception coverage gaps
- sensor health or calibration unknown
- high perception uncertainty
- safety-critical scenario failures
- verification evidence incomplete
- unresolved high-risk hazards
- fallback behavior unverified
- minimum-risk behavior unverified
- cybersecurity gaps
- safety case incomplete
- deployment-governance review incomplete
- vehicle-control request
- remote-driving request
- safety-system override request
- autonomous deployment request
- qualified human approval missing

Human approval is required after technical and safety gates pass. Human approval does not erase unresolved blockers.

## Human authority boundaries

F74 must not autonomously:

- steer a vehicle
- accelerate or brake a vehicle
- send actuation commands
- perform remote driving
- bypass driver monitoring
- override safety systems
- disable emergency behavior
- expand the ODD
- authorize public-road testing
- authorize autonomous deployment
- approve a safety case

Final engineering, safety, regulatory, testing and deployment authority remains with qualified and authorized humans and organizations.

## End-to-end reference workflow

A typical F74 review follows this sequence:

1. Define the intended autonomous-driving function and ODD.
2. Review system architecture and interfaces.
3. Map sensor coverage to ODD conditions.
4. Review perception capability, uncertainty and failure modes.
5. Build nominal, boundary, degraded and rare-event scenario matrices.
6. Run planning and behavior simulations.
7. Trace requirements and hazards to evidence.
8. Verify fallback and minimum-risk behavior.
9. Review cybersecurity and data governance.
10. Build or update the safety case.
11. Review field-monitoring and rollback readiness.
12. Apply fail-closed deployment gates.
13. Require qualified human approval.

## Evaluation and held-out safety suite

The repository includes:

```text
evals/evaluate.py
evals/held_out.py
benchmarks/reference_case.json
```

Evaluation should test governance behavior as well as scenario coverage.

Useful dimensions include:

- ODD enforcement
- sensor-coverage gap detection
- perception-uncertainty handling
- scenario-failure propagation
- hazard tracking
- verification-evidence enforcement
- fallback verification
- minimum-risk-condition review
- cybersecurity enforcement
- unauthorized vehicle-control blocking
- remote-driving blocking
- autonomous-deployment blocking
- human-approval enforcement

The behavioral verification layer includes eight direct governance tests plus a ten-scenario held-out safety suite.

## Failure states

Useful explicit states include:

```text
ODD UNDEFINED
ODD EXPANSION NOT JUSTIFIED
SENSOR COVERAGE GAP
SENSOR HEALTH UNKNOWN
PERCEPTION UNCERTAINTY HIGH
SAFETY-CRITICAL SCENARIO FAILED
VERIFICATION INCOMPLETE
HIGH-RISK HAZARD OPEN
FALLBACK UNVERIFIED
MINIMUM-RISK CONDITION UNVERIFIED
CYBERSECURITY REVIEW REQUIRED
SAFETY CASE INCOMPLETE
VEHICLE CONTROL PROHIBITED
REMOTE DRIVING PROHIBITED
AUTONOMOUS DEPLOYMENT PROHIBITED
HUMAN APPROVAL REQUIRED
```

The system should never fabricate scenario results, sensor coverage, verification evidence, safety-case approval or deployment authorization.

## Reproduce the reference implementation

Install development dependencies:

```bash
python -m pip install -e '.[dev]'
```

Run CI-equivalent checks:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python examples/example.py
python run.py
```

CI under `.github/workflows/ci.yml` runs on Python 3.10, 3.11 and 3.12.

## Reproducibility

Version at minimum:

- ODD definition
- vehicle hardware configuration
- sensor configuration
- calibration state
- software version
- model version
- map version
- simulation environment
- scenario suite
- verification procedures
- hazard register
- safety case
- cybersecurity configuration
- release-gate decision

A changed vehicle configuration should generate a new evidence state rather than silently inheriting the prior one.

## L3 Gold Standard

F74 follows the library's L3 Gold Standard structure through six specialist agents, deterministic evidence tools, explicit state and safety layers, scenario-based evaluation, held-out governance tests, CI, observability, fail-closed release gating and mandatory qualified human approval.

This maturity designation describes the repository's engineering and governance structure. It is not regulatory approval, vehicle certification, a safety guarantee, permission for public-road operation, or authorization for autonomous deployment.

## Extending F74

Common extensions include:

- simulation platforms
- scenario databases
- digital twins
- SIL/HIL test systems
- sensor-calibration systems
- perception evaluation pipelines
- map and localization validation
- safety-case tooling
- cybersecurity monitoring
- fleet telemetry
- incident management
- release-management systems
- field-monitoring dashboards
- versioned ODD registries

New integrations should preserve traceability, configuration control, safety boundaries, auditability and human deployment authority.

## Example applications

F74 can serve as a reference architecture for:

- autonomous-driving architecture review
- ADAS research
- perception coverage analysis
- scenario simulation
- safety-case development
- ODD governance
- fallback analysis
- autonomous-fleet safety research
- verification planning
- autonomous-vehicle governance studies

Real-world driving and deployment require additional engineering, testing, regulatory and organizational controls.

## Design principles

1. Define the ODD before claiming capability.
2. Treat sensor coverage and calibration as safety evidence.
3. Preserve perception uncertainty instead of hiding it.
4. Validate planning across nominal and long-tail scenarios.
5. Trace hazards and requirements to objective evidence.
6. Verify fallback and minimum-risk behavior explicitly.
7. Integrate cybersecurity into the safety case.
8. Version the full vehicle, software, map and ODD configuration.
9. Fail closed when safety evidence is incomplete.
10. Keep physical vehicle control and deployment authority outside the agentic system.

## Documentation

Additional architecture documentation is available under `docs/`, including `docs/ARCHITECTURE.md`.

## Citation and reuse

Use the repository metadata and citation information supplied by the project when referencing this implementation. The repository can be studied, cited, adapted and extended subject to its license terms.

## Responsible use

Use F74 as an autonomous-vehicle engineering and multi-agent governance reference. Validate architecture, ODD assumptions, perception, scenario coverage, verification, fallback behavior, cybersecurity, safety case, field monitoring and regulatory requirements against the actual vehicle program before deployment. Final vehicle-control and deployment authority remains with qualified and authorized humans and organizations.