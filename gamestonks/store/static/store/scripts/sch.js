function add2html(list) {
    var div = document.getElementById('dinfo');
    div.innerHTML = "";

    const p = document.createElement("p");

    for (let i = 0; i < list.length; i++) {
        var item = list[i];

        console.log(item["cheapestDealID"])

        var img = item["thumb"]
        var name = item["external"]
        var price = item["cheapest"]
        var dealID = item["cheapestDealID"]

        var format = "<div class=\"deal\"><p>" + name + "</p> <a href=\"/deals/" + dealID + "\"> <img src=" + img + "></a><p>" + price + "</p></div>"

        div.innerHTML += format
    }
}

function search() {
    var doc = document;
    var search = doc.getElementById('search').value;

    var url = "https://www.cheapshark.com/api/1.0/games?title=" + search;

    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

    fetch(url, requestOptions)
        .then(response => response.json())
        .then(result => add2html(result))
        .catch(error => console.log('error', error));
}