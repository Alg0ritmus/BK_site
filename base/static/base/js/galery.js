function closeGalery() {
    var modal_image = document.getElementsByClassName("modal-image")[0];

    modal_image.style.display = "none";
    document.getElementsByTagName('body')[0].style.overflowY = 'scroll';

}



function openGalery(current_card) {
    var modal_image = document.getElementsByClassName("modal-image")[0];
    var modal_image_img = modal_image.getElementsByTagName('img')[0];
    document.getElementsByTagName('body')[0].style.overflowY = 'hidden';

    var img = current_card.getElementsByClassName("card-img-top")[0];
    modal_image_img.src = img.src;
    modal_image.style.display = "block";

    var left_arrow = document.getElementsByClassName("fa-arrow-left")[0];
    var rigth_arrow = document.getElementsByClassName("fa-arrow-right")[0];

    rigth_arrow.addEventListener("click",function() {
        if (current_card.nextElementSibling != null){
            current_card = current_card.nextElementSibling;
        }
        console.log(current_card);
        var img = current_card.getElementsByClassName("card-img-top")[0];
        modal_image_img.src = img.src;  
    });

    left_arrow.addEventListener("click",function() {
        if (current_card.previousElementSibling != null){
            current_card = current_card.previousElementSibling;
        }
        console.log(current_card);
        var img = current_card.getElementsByClassName("card-img-top")[0];
        modal_image_img.src = img.src;  
    });

}


console.log("SUCCESSFULY ADDED GALERY.JS")


var modal_image = document.getElementsByClassName("modal-image")[0];

allImages = document.getElementsByClassName("grid-item-galeria");


