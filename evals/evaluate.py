def evaluate(result: dict) -> dict:
    """Check structural and authority invariants for a completed F74 run."""
    return {
        "passed": (
            result.get("vehicle_control") is False
            and result.get("autonomous_deployment") is False
            and len(result.get("results", [])) == 6
            and "governance" in result
            and "release_allowed" in result
        )
    }
