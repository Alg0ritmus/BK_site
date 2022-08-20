/* READ CLANOK */
var quill = new Quill('#editor', {
    modules: {
        toolbar: false
    },
    theme: 'snow',
    image: true,
    readOnly: true,
});

async function getToken(){
    var value = null;
    if (window.cookieStore == undefined){
        var data = document.cookie.split('=')[1];
        return data;
    }

    var data = await window.cookieStore.getAll();   
    
    for (let i = 0; i < data.length; i++) {

        if (data[i].name == "csrftoken") {
            value = data[i].value;

        }
    }
    return value;
}


// send fetch post
async function getClanokBody(article_id) {
    console.log("FETCHING FOR QUILL BODY");
    var myURL = window.location.origin + "/archiv/clanok/clanok_body_RO/"+article_id+"/";
    const TOKEN = await getToken();


    var data_from_response_raw = await fetch(url = (myURL), {
        method: 'GET',
        // credentials : 'include' -> all origins
        credentials: 'include',
        headers: {
            'Content-Type': 'appliaction/json',
            "X-CSRFToken": TOKEN,
        },
    });
    // return json obj (not sure why I need to use await everywhere)
    var body = await data_from_response_raw.json();

    quill.setContents(body.clanok);
    // not returning just posting
}



