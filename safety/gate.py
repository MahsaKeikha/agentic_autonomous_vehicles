def authorize(action):
    blocked={"steer","accelerate","brake","vehicle_command","safety_override"}
    return {"allowed":action not in blocked,"reason":"live vehicle control outside scope" if action in blocked else "reviewable"}
