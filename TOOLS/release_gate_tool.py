def gate(evidence,approved=False): return {"ready":bool(evidence) and approved,"human_approval":approved}
