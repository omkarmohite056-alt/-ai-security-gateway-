from gateway import AISecurityGateway

gateway = AISecurityGateway()

if __name__ == "__main__":
    while True:
        user_input = input("\nEnter prompt (or type exit): ")
        
        if user_input.lower() == "exit":
            break
        
        result = gateway.process(user_input)
        
        print("\nResult:")
        for k, v in result.items():
            print(f"{k}: {v}")
