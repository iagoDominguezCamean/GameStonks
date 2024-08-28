import requests
import pandas as pd
import urllib.parse as urp
import plotly.express as px
from .forms import NewUser
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from plotly.offline import plot

URL = "https://www.cheapshark.com/api/1.0/"


def register(request):
    if request.method == "POST":
        form = NewUser(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successfull")
            return redirect("/")
        else:
            messages.error(request, "Unseccessfull registration")

    form = NewUser()
    return render(request, 'store/registration.html', context={"register_form": form})


def login_req(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            uname = form.cleaned_data.get("username")
            passwd = form.cleaned_data.get("password")

            user = authenticate(username=uname, password=passwd)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in {uname}.")
                return redirect("/")
            else:
                messages.error(request, "Invalid credentials")
        else:
            messages.error(request, "Invalid credentials")

    form = AuthenticationForm()
    return render(request, 'store/login.html', context={"login_form": form})


def logout_req(request):
    logout(request)
    messages.info(request, "You have successfully logout.")
    return redirect("/")


@login_required(login_url='/login/')
def account(request):

    return render(request, 'store/account.html', context={})


def stores_list():
    stores = URL + "stores"

    headers = {}
    payload = {}
    files = {}

    response = requests.request(
        "GET", stores, headers=headers, data=payload, files=files)
    len_stores = len(response.json())

    list = []

    for i in range(len_stores):
        if(response.json()[i]["isActive"] == 1):
            list.append(response.json()[i])

    return list


def index(request):
    deals_url = URL + "deals"

    headers = {}
    payload = {}
    files = {}

    response = requests.request("GET",
                                deals_url, headers=headers, data=payload, files=files)
    deals_list = response.json()

    list = stores_list()

    context = {'stores_list': list, 'deals_list': deals_list}
    return render(request, 'store/index.html', context)


def store(request, store_id):
    list = stores_list()

    for i in range(len(list)):
        if(list[i]["storeID"] == store_id):
            store_info = list[i]
            break

    store_deals_url = URL + "deals?storeID=" + store_id

    headers = {}
    payload = {}
    files = {}

    response = requests.request(
        "GET", store_deals_url, headers=headers, data=payload, files=files)
    store_deals = response.json()

    context = {'store_info': store_info, 'store_deals': store_deals}
    return render(request, 'store/store.html', context)


def deal(request, deal_id):
    deal_url = URL + "deals?id=" + str(urp.quote_plus(deal_id))

    headers = {}
    payload = {}
    files = {}

    response = requests.request(
        "GET", deal_url, headers=headers, data=payload, files=files)
    deal_info = response.json()

    steam_id = None
    precio_medio = round(calculoPrecioMedioJuego(
        deal_info["gameInfo"]["gameID"]))
    print(precio_medio)

    if deal_info != []:
        steam_id = deal_info['gameInfo']['steamAppID']

    if (steam_id is not None):
        game_info = steam_info(steam_id)

        if game_info is not None:
            context = {'deal_info': deal_info,
                       'deal_id': deal_id, 'game_info': game_info, 'precio_medio': precio_medio}
        else:
            context = {'deal_info': deal_info,
                       'deal_id': deal_id, 'precio_medio': precio_medio}
    else:
        context = {'deal_info': deal_info,
                   'deal_id': deal_id, 'precio_medio': precio_medio}

    return render(request, 'store/deal.html', context)


def steam_info(steam_id):
    steam_url = "https://store.steampowered.com/api/appdetails/"

    payload = {'appids': steam_id}

    resp = requests.get(steam_url, params=payload)
    game = resp.json()

    if game[str(steam_id)]['success'] == True:
        return game[str(steam_id)]['data']
    else:
        return None


def sBn(request):

    context = {}

    return render(request, 'store/sBn.html', context)


def analisis(request):
    deals_url = URL + "deals"

    headers = {}
    payload = {}
    files = {}

    response = requests.request("GET",
                                deals_url, headers=headers, data=payload, files=files)
    # compare o precio de cada deal co da media pa cada xogo

    df = pd.DataFrame(response.json())
    df["price_numeric"] = pd.to_numeric(df["salePrice"])
    # df["mean_price_numeric"] = df["gameID"].apply(
    #    lambda x: calculoPrecioMedioJuego(x))
    df["mean_price_numeric"] = pd.to_numeric(df["normalPrice"])

    df["dif_mean_price"] = df["price_numeric"] - df["mean_price_numeric"]
    df = df.groupby("storeID")['dif_mean_price'].mean()
    df = df.sort_values("index")

    data = pd.DataFrame()
    data["storeID"] = df.index
    data["precio"] = df.values.round()

    data["logo"] = data['storeID'].apply(
        lambda x: returnThumbName(x))
    data["indice"] = data.index
    data["n_ranking"] = data['indice'].apply(lambda x: x+1)

    fig = px.line(data, x='n_ranking', y='precio', markers=True)
    # fig.show()
    plot_div = plot(fig, output_type="div")
    data = data.to_dict(orient="index")

    #a = {"k1": "1", "k2": "2"}
    context = {'data': data, 'plot': plot_div}
    return render(request, 'store/analisis.html', context)


def returnThumbName(store_id):

    store_list = stores_list()
    for i in range(len(store_list)):
        if(store_list[i]["storeID"] == store_id):
            store_info = store_list[i]
            break
    return store_info["images"]["logo"]


def calculoPrecioMedioJuego(game_id):

    game_url = URL + "games?id=" + game_id

    headers = {}
    payload = {}
    files = {}

    response = requests.request(
        "GET", game_url, headers=headers, data=payload, files=files)
    game_info = response.json()

    df = pd.DataFrame(game_info["deals"])
    df['price_numeric'] = pd.to_numeric(df['price'])
    return df.price_numeric.mean()
