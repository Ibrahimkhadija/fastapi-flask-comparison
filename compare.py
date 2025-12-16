import requests
import time

def test_endpoint(url, name):
    print(f"\nTesting {name} at {url}")
    
    # Test root endpoint
    start = time.time()
    response = requests.get(url)
    elapsed = (time.time() - start) * 1000
    
    if response.status_code == 200:
        print(f"  ✓ Root endpoint: {elapsed:.2f}ms")
        print(f"  Response: {response.json()['message']}")
    else:
        print(f"  ✗ Failed: {response.status_code}")
    
    # Test health endpoint
    health_url = f"{url}/health"
    start = time.time()
    response = requests.get(health_url)
    elapsed = (time.time() - start) * 1000
    
    if response.status_code == 200:
        print(f"  ✓ Health check: {elapsed:.2f}ms")
        print(f"  Status: {response.json()['status']}")
    
    return True

def main():
    print("=" * 50)
    print("FASTAPI VS FLASK COMPARISON")
    print("=" * 50)
    
    # Make sure both servers are running!
    print("\n⚠️  Make sure both servers are running:")
    print("  - FastAPI: http://localhost:8000")
    print("  - Flask:   http://localhost:5000")
    
    input("\nPress Enter when both servers are running...")
    
    try:
        test_endpoint("http://localhost:8000", "FastAPI")
        test_endpoint("http://localhost:5000", "Flask")
        
        print("\n" + "=" * 50)
        print("COMPARISON COMPLETE!")
        print("=" * 50)
        print("\nKey Differences:")
        print("1. FastAPI has auto-docs at /docs")
        print("2. Flask uses simpler syntax")
        print("3. Both handle same requests")
        
    except requests.ConnectionError:
        print("\n❌ ERROR: Could not connect to server")
        print("Make sure servers are running!")

if __name__ == "__main__":
    main()