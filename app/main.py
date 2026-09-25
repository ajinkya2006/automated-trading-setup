from app.config import ENVIRONMENT, TRADING_MODE, AI_PROVIDER


def main():
    print("Trading System")
    print("----------------")
    print(f"Environment : {ENVIRONMENT}")
    print(f"Trading Mode: {TRADING_MODE}")
    print(f"AI Provider : {AI_PROVIDER}")


if __name__ == "__main__":
    main()