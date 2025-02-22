from aqua import CF_Solver

def get_cookies():
    """
    Retrieves the Cloudflare clearance cookie from gmgn.ai using CF_Solver.
    Returns:
        dict: A dictionary containing the 'cf_clearance' cookie if successful, otherwise an empty dict.
    """
    try:
        # Define custom headers to mimic a real browser
        headers = {
            'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/133.0.0.0 Safari/537.36'),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://gmgn.ai/'
        }

        # Instantiate the solver for the target website with our custom headers
        cf = CF_Solver('https://gmgn.ai', headers=headers)

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
