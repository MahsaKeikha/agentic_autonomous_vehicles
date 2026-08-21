def evaluate(r): return {"passed":r.get("vehicle_control") is False and len(r.get("results",[]))==6}
