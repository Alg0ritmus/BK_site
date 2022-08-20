// load script after page is loaded

window.onload = function () {
    console.log("adding script");
    var origin = window.location.origin;
    /* origin napr. -> http://192.168.0.249:8000 */
  
    var tag = document.createElement("script");
  
    tag.src = origin + "/static/base/js/galery.js";
    document.getElementsByTagName("head")[0].appendChild(tag);
  
  }