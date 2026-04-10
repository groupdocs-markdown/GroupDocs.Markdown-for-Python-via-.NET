from groupdocs.markdown import Metered

def set_metered_license():
    """Set up metered (usage-based) licensing and query consumption."""

    # Step 1: Provide your metered license keys
    public_key = ""   # your public license key
    private_key = ""  # your private license key

    # Step 2: Create a Metered instance and activate the keys (skip if keys not set)
    if public_key and private_key:
        metered = Metered()
        metered.set_metered_key(public_key, private_key)

        # Step 3: Query amount (MB) consumed
        amount_consumed = Metered.get_consumption_quantity()
        print("Amount (MB) consumed: " + str(amount_consumed))

        # Step 4: Query count of credits consumed
        credits_consumed = Metered.get_consumption_credit()
        print("Credits consumed: " + str(credits_consumed))

if __name__ == "__main__":
    set_metered_license()