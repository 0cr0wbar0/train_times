import requests
import webbrowser

def menu(question: str, choices: list[str]) -> str:
    choice = None
    # ["UK", "France", "Switzerland"] -> {"1" : "UK", "2" : "France", "3" : "Switzerland"}
    choices = {str(i) : c for i, c in enumerate(choices, 1)}
    while choice is None or (choice not in choices.keys() and choice.lower() not in map(lambda x: x.lower(), choices.values())):
        choice = input(f"{question}\n" + "\n".join(f"{k}: {v}" for k, v in choices.items()) + "\n> ")
    if choice.lower() in [k.lower() for k in choices.keys()]:
        return choices.get(choice).lower()
    return choice.lower()

def single_input(question: str) -> str:
    return input(f"{question}: ")

if __name__ == '__main__':
    current_url = "/"
    while True:
        try:
            response = requests.get(f"http://127.0.0.1:8000{current_url}").json()
        except Exception:
            continue
        match response.get("type"):
            case "menu":
                current_url += menu(response.get("question"), response.get("choices")) + "/"
            case "input":
                current_url += single_input(response.get("question")) + "/"
            case "open":
                webbrowser.open_new_tab(response.get("url"))
                break
