function manage(email) {

    var url = "https://www.cheapshark.com/api/1.0/alerts?action=manage&email=" + email

    var settings = {
        "url": url,
        "method": "GET"
    };

    $.ajax(settings).done(function (response) {
        alert(response)
    })
}