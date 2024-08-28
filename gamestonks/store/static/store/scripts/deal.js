$(document).ready(function () {
    $("#video").empty()

    var API_KEY = "AIzaSyA54j24aux4bT3l6IrW58OWR6VkrJhRxjw"

    var title = $("#title").text()
    title = title + " 3djuegos"
    var video = ''

    $.get("https://www.googleapis.com/youtube/v3/search?key=" + API_KEY + "&part=snippet&q=" + title + "type=video&maxResults=1", function (data) {

        data.items.forEach(item => {
            video = '<iframe src="http://www.youtube.com/embed/' + item.id.videoId + '" frameborder="0" allowfullscreen></iframe>'

            $("#video").append(video)
        });
    })
})

function add_alert(email, gameID) {

    var price = $("#price").val()

    var url = "https://www.cheapshark.com/api/1.0/alerts?action=set&email=" + email + "&gameID=" + gameID + "&price=" + price

    var settings = {
        "url": url,
        "method": "GET",
        "timeout": 0,
        "processData": false,
        "mimeType": "multipart/form-data",
        "contentType": false,
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
    });
}
