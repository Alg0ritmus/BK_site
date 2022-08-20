var quillBody = () => {
    var texts = document.querySelectorAll(".archiv-card-text");

    for (let card = 0; card < texts.length; card++) {
        currentCard = texts[card];
        var rawtext = currentCard.querySelectorAll('span')[0];


        rawdataObj = rawtext.textContent.replaceAll(`'`, `"`).replaceAll(`True`, `true`).replaceAll(`Flase`, `false`);

        rawdataObj = JSON.parse(rawdataObj);
        body = "";


        for (var i in rawdataObj.ops) {
            if (rawdataObj.ops[i].insert && typeof (rawdataObj.ops[i].insert) == "string") {

                body += (rawdataObj.ops[i].insert);

            }

        }
        rawtext.textContent = body;
        rawtext.style.display = "block";
    }

}

quillBody()




