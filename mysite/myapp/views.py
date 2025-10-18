from django.shortcuts import render
from django.http import HttpRequest,HttpResponse

def main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World :P")

def pozdrav(request: HttpRequest) -> HttpResponse:
    return render(request,'pozdrav.html')

def mypage(request: HttpRequest) -> HttpResponse:
    return render(request, 'mojepage.html')


def article_main(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Tohle je hlavni article.")

def article_uniq(request: HttpRequest,article_id: int) -> HttpResponse:
    return HttpResponse(f"Tohle je clanek c.{article_id}")

def article(request: HttpRequest,article_id: int,name: str = '') -> HttpResponse:
    return HttpResponse(
        "Tohle je clanek c.{}. {}".format(article_id, "Nazev tohoto clanku je: {}".format(
            name) if name else "Tenhle clanek nema nazev."
        ))

