import requests

def main():
    response = requests.get("https://api.github.com")
    print("Código de estado:", response.status_code)
    print("Respuesta:", response.json())

if __name__ == "__main__":
    main()
