// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
    document.getElementById("btn-to-top").style.display = "block";
  } else {
    document.getElementById("btn-to-top").style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
}


// Navigation bar

var dropdowns = document.getElementsByClassName("dropbtn");
var i;

for (i = 0; i < dropdowns.length; i++) {
    dropdowns[i].addEventListener("click", function() {

    this.classList.toggle("active");
    var panel = this.nextElementSibling;
    panel.classList.toggle("show");

});
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for(i = 0 ; i < dropdowns.length; i++){
        if (dropdowns[i].classList.contains('show')) {
            dropdowns[i].classList.remove('show');
        }
    }
  }
}

let navSlide = () => {
    let nav = document.getElementById("side-nav");
    let navlinks = nav.querySelectorAll("li");
    let burger = document.querySelector(".burgers");
    burger.addEventListener("click", () => {
        nav.classList.toggle("side-nav-active");
        nav.style.transition = "all 0.4s";
        navlinks.forEach((link, index) => {
            if (link.style.animation) {
                link.style.animation = "";
            } else {
                link.style.animation = `navLinkFade 0.4s ease forwards ${index / 6 + 0.5}s`;
            }
        });
    });
};

navSlide();

// end Navigation bar