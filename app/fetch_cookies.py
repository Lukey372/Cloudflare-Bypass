from aqua import CF_Solver

def get_cookies():
    try:
        # Instantiate the solver for gmgn.ai (or any other target)
        cf = CF_Solver('https://gmgn.ai')
        # Get the clearance cookie
        cookie = cf.cookie()
        print("Fetched cookie:", cookie)
        return {"cf_clearance": cookie}
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return {}
