
var toggleNav = () =>{
    var navbar = document.getElementsByClassName("navbar")[0];
    var login = document.getElementsByClassName('login')[0];
    var ul = navbar.getElementsByTagName('ul')[0];
    var arrows = document.getElementsByClassName("fa-angle-double-down")[0];
    if (ul.style.display == 'flex'){
        console.log('was none');
        ul.style.display= 'none';
        login.style.display='none';
        arrows.style.transform = "rotate(0deg)";
        
    }
    else{
        console.log('was displayed');
        
        ul.style.display= 'flex';
        login.style.display='block';
        arrows.style.transform = "rotate(180deg)";

    }
    

}

