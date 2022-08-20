
/* CREATE CLANOK */

var toolbarOptions = [
  ['bold', 'italic', 'underline', 'strike'],        // toggled buttons
  ['blockquote', 'code-block'],

  [{ 'header': 1 }, { 'header': 2 }],               // custom button values
  [{ 'list': 'ordered' }, { 'list': 'bullet' }],
  [{ 'script': 'sub' }, { 'script': 'super' }],      // superscript/subscript
  [{ 'indent': '-1' }, { 'indent': '+1' }],          // outdent/indent
  [{ 'direction': 'rtl' }],                         // text direction

  [{ 'size': ['small', false, 'large', 'huge'] }],  // custom dropdown
  [{ 'header': [1, 2, 3, 4, 5, 6, false] }],

  [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
  [{ 'font': [] }],
  [{ 'align': [] }],

  ['clean']                                         // remove formatting button
];


var quill_edit = new Quill('#editor-edit', {
  modules: {
    toolbar: toolbarOptions
  },
  theme: 'snow',
  image: true
});
imgIconToolbar()


/* ADD IMG ICON TO TOOLBAR */
function imgIconToolbar() {
  var images = document.querySelectorAll(".ql-toolbar .ql-formats")[0];
  var code = '<button type="button" class="ql-image" onclick="addPhoto()"><svg viewBox="0 0 18 18"> <rect class="ql-stroke" height="10" width="12" x="3" y="4"></rect> <circle class="ql-fill" cx="6" cy="7" r="1"></circle> <polyline class="ql-even ql-fill" points="5 12 5 11 7 9 8 10 11 7 13 9 13 12 5 12"></polyline></svg></button>';
  var el = document.createElement("span");
  el.innerHTML = code;
  images.appendChild(el);
}

/* GET AND ADD PHOTO */
function addPhoto() {
  let defURL = "C:\\Users\\Patrik\\Desktop\\fotky\\1573127565063.jpg" // replace with fetch for url
  let URL = prompt("Please enter image URL:", defURL); // get url from alert

  if (!(URL == null || URL == "")) {

    setPhotoNatively(URL);
  }
}

/* ADD PHOTO TO QUILL */
function setPhotoNatively(defURL) {
  var range = quill_edit.getSelection();

  if (range) {
    console.log('User cursor is at index', range.index, defURL);
    quill_edit.insertEmbed(range.index, 'image', defURL);
  }

}


/* SAVE ARTICLE */

// get token

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
async function articleSave(article_id) {

  var delta = quill_edit.getContents();
  var temp_title = document.getElementsByClassName("clanok_title")[0].value;

  var msg = JSON.stringify({
    "title": temp_title,
    "body": delta,
    "pk": article_id
  });

  var myURL = window.location.protocol + "//" + window.location.hostname + ":" + window.location.port + "/archiv/clanok/update/";
  const TOKEN = await getToken();

  var data_from_response_raw = await fetch(url = (myURL), {
    method: 'POST',
    // credentials : 'include' -> all origins
    credentials: 'include',
    headers: {
      'Content-Type': 'appliaction/json',
      "X-CSRFToken": TOKEN,
    },
    body: msg,
  });
  // return json obj (not sure why I need to use await everywhere)
  //return await data_from_response_raw.json();
  // not returning just posting
  window.location.replace(window.origin + "/archiv/");
}



// send fetch post
async function getClanokBody(article_id) {
  var myURL = window.location.protocol + "//" + window.location.hostname + ":" + window.location.port + "/archiv/clanok/clanok_body_RO/" + article_id + "/";
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

  quill_edit.setContents(body.clanok);
  imgHandler();
  // not returning just posting
}


function imgHandler() {
  var editorQuill = document.getElementById('editor-edit');
  var images = editorQuill.getElementsByTagName('img');



  for (var i = 0; i < images.length; i++) {
    images[i].parentNode.classList.add("resizable");

    var imgBg = images[i].parentNode;

    imgBg.addEventListener('mousemove', function () {
      if (this.style.width) {

        this.children[0].width = parseInt(this.style.width, 10);
      }
    });

  }
}




async function sendOznamReq(Mypath,clanok_id){


  var myURL = window.location.origin+Mypath;
  const TOKEN = await getToken();
  var msg = '{"clanok_id":'+clanok_id+'}'
  var data_from_response_raw = await fetch(url = (myURL), {
    method: 'POST',
    // credentials : 'include' -> all origins
    credentials: 'include',
    headers: {
      'Content-Type': 'appliaction/json',
      "X-CSRFToken": TOKEN,
    },
    body: msg,
  });
  // return json obj (not sure why I need to use await everywhere)
  //return await data_from_response_raw.json();
  // not returning just posting
}

function is_oznam_req(clanok_id){
  var oznam =  document.getElementById('is_oznam');
  
  if (oznam.checked){
    sendOznamReq("/oznam_add/",clanok_id);
    console.log("checked");
  }
  
  else{
    sendOznamReq("/oznam_del/",clanok_id);
    console.log("unchecked");
  }

  
}

