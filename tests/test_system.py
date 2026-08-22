from orchestration.orchestrator import run
from safety.gate import authorize


def valid_context():
    return {
        "objective": "review autonomous vehicle safety architecture",
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


def test_reference_run_never_controls_vehicle():
    result = run(valid_context())
    assert result["vehicle_control"] is False
    assert result["autonomous_deployment"] is False


def test_complete_review_can_release_analysis():
    assert run(valid_context())["release_allowed"] is True


def test_missing_human_approval_fails_closed():
    context = valid_context()
    context["human_approval"] = False
    assert run(context)["release_allowed"] is False


def test_braking_command_is_never_authorized():
    assert authorize("brake", valid_context())["allowed"] is False


def test_perception_gap_blocks_release():
    context = valid_context()
    context["perception_coverage_gap"] = True
    assert run(context)["release_allowed"] is False


def test_scenario_failure_blocks_release():
    context = valid_context()
    context["scenario_failure"] = True
    assert run(context)["release_allowed"] is False


def test_fallback_gap_blocks_release():
    context = valid_context()
    context["fallback_not_verified"] = True
    assert run(context)["release_allowed"] is False


def test_odd_or_cybersecurity_gap_blocks_release():
    context = valid_context()
    context["unsafe_odd_expansion"] = True
    assert run(context)["release_allowed"] is False
