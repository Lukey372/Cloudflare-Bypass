from aqua import CF_Solver

def get_cookies():
    """
    Retrieves the Cloudflare clearance cookie from gmgn.ai using CF_Solver.
    Returns:
        dict: A dictionary containing the 'cf_clearance' cookie if successful, otherwise an empty dict.
    """
    try:
        # Instantiate the solver for the target website
        cf = CF_Solver('https://gmgn.ai')
        # Retrieve the clearance cookie
        cookie = cf.cookie()
        if cookie:
            print("Fetched cookie:", cookie)
            return {"cf_clearance": cookie}
        else:
            print("❌ No cookie was retrieved.")
            return {}
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return {}

if __name__ == "__main__":
    cookies = get_cookies()
    print("Cookies:", cookies)
