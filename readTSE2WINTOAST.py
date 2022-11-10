
#* só copiei desse cara pq achei interessante o uso de toast notification do windows
# *(tanto que usei no outro projetinho junto com o do trayicon)
# TODO da pra deixar mais simples sem usar esse monte de funções mas tem q fazer com outra API

#! Author: Jean Jacques Barros
#! Github: https://github.com/jjeanjacques10
from time import sleep
import requests
from win10toast import ToastNotifier


LAST_READ = ""


def get_data():
    url = "https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json"
    response = requests.get(url)
    data = response.json()
    return data


def create_message(candidates, status):
    text = ""
    for candidate in candidates:
        name = candidate.get("nm")
        votes = candidate.get("pvap")
        text = text + f"{name} - {votes}% \n"
    text = text + f"\n Seções apuradas: {status}%"

    toaster=ToastNotifier()
    toaster.show_toast("Resultados Eleições", text, duration = 50)
    print(text)


def is_recent(data):
    return data != LAST_READ


def main():
    while True:
        results=get_data()
        if is_recent(results["hg"]):
            create_message(results["cand"], results["pst"])
            LAST_READ=results["hg"]
            print("Última atualização: ", LAST_READ)
        sleep(60)


if __name__ == "__main__":
    main()