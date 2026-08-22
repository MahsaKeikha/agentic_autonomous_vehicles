from orchestration.orchestrator import run


def base():
    return {
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_approval": False}, False),
    ({**base(), "perception_coverage_gap": True}, False),
    ({**base(), "scenario_failure": True}, False),
    ({**base(), "verification_failure": True}, False),
    ({**base(), "unsafe_odd_expansion": True}, False),
    ({**base(), "fallback_not_verified": True}, False),
    ({**base(), "cybersecurity_gap": True}, False),
    ({**base(), "unresolved_high_risk_hazard": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        actual = run(context)["release_allowed"]
        passed += actual is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
