
def health_check():
    return {
        "application": "talent-acquisition",
        "status": "healthy"
    }


if __name__ == "__main__":
    print(health_check())
