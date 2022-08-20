var arrayOfBodies = [];
var quillBodyUniversal = (rawdataObj) => {
    var rawdataObj = rawdataObj.replaceAll(`'`, `"`).replaceAll(`True`, `true`).replaceAll(`Flase`, `false`).replaceAll(/[\r\n]/gm, '').replace(new RegExp("&"+"#"+"x27;", "g"), '"');
  
    console.log(rawdataObj);
    rawdataObj = JSON.parse(rawdataObj);
    body = "";


    for (var i in rawdataObj.ops) {
        if (rawdataObj.ops[i].insert && typeof (rawdataObj.ops[i].insert) == "string") {

            body += (rawdataObj.ops[i].insert);

        }

    }
    
    arrayOfBodies.push(body);

}