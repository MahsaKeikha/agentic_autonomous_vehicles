"""Fail-closed governance for F74 autonomous vehicle analysis."""

BLOCKED_ACTIONS = {
    "steer",
    "accelerate",
    "brake",
    "vehicle_command",
    "safety_override",
    "autonomous_deployment",
    "remote_drive",
}

REQUIRED_REVIEWS = (
    "system_architecture_reviewed",
    "perception_reviewed",
    "scenario_simulation_reviewed",
    "verification_reviewed",
    "safety_case_reviewed",
    "odd_reviewed",
    "fallback_reviewed",
    "cybersecurity_reviewed",
    "deployment_governance_reviewed",
    "human_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    """Authorize analysis-only release and never authorize live vehicle control."""
    context = context or {}
    if action in BLOCKED_ACTIONS:
        return {"allowed": False, "reason": "live or consequential vehicle control is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required review", "missing": missing}

    blockers = []
    if context.get("perception_coverage_gap"):
        blockers.append("perception coverage gap unresolved")
    if context.get("scenario_failure"):
        blockers.append("safety-critical scenario failure unresolved")
    if context.get("verification_failure"):
        blockers.append("verification evidence failed")
    if context.get("unsafe_odd_expansion"):
        blockers.append("operational design domain expansion not justified")
    if context.get("fallback_not_verified"):
        blockers.append("minimum-risk fallback not verified")
    if context.get("cybersecurity_gap"):
        blockers.append("cybersecurity gap unresolved")
    if context.get("unresolved_high_risk_hazard"):
        blockers.append("high-risk hazard unresolved")

    if blockers:
        return {"allowed": False, "reason": "governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "analysis/review release approved by qualified human"}
