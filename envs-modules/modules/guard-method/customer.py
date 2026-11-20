
def register_customer(name):
    print(f"Customer registered: {name}")
    return {"name": name}


def main():
    print("Customer module running")
    register_customer("Veera")


if __name__ == "__main__":
    main()
