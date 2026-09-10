from client import KZG10Scheme
import json

def handle_request(req):
    kzg = KZG10Scheme()
    action = req.get("action")
    if action == "commit":
        poly = req.get("poly", [0])
        c = kzg.commit(poly)
        return {"status": "ok", "commitment": c}
    elif action == "open":
        poly = req.get("poly", [0])
        z = req.get("z", 0)
        y, pi = kzg.open(poly, z)
        return {"status": "ok", "y": y, "pi": pi}
    elif action == "verify":
        comm = req.get("commitment", 0)
        z = req.get("z", 0)
        y = req.get("y", 0)
        pi = req.get("pi", 0)
        res = kzg.verify(comm, z, y, pi)
        return {"status": "ok", "valid": res}
    return {"status": "error", "message": "Unknown action"}

if __name__ == "__main__":
    print(json.dumps(handle_request({"action": "commit", "poly": [3, 2, 1]})))
