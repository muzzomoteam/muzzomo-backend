


 
  if (window.location.href.indexOf("Productdetial.html") > -1){
    var swiper = new Swiper('.swiper-container', {
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      pagination: {
        el: '.swiper-pagination',
        clickable: true,
      },
    });
    
    function rate(value) {
      for (var i = 1; i <= 5; i++) {
        var star = document.getElementById("star" + i);
        var label = document.querySelector('label[for="star' + i + '"]');
    
        if (i <= value) {
          star.checked = true;
          label.style.color = 'gold';
        } else {
          star.checked = false;
          label.style.color = 'gray';
        }
      }
    }
  }
 
  function previewImage(event) {
    var input = event.target;
    var reader = new FileReader();
    reader.onload = function(){
      var img = document.getElementById("imagePreview");
      img.src = reader.result;
       };
    reader.readAsDataURL(input.files[0]);
  }
  
  // listing
const container = document.querySelector('.con-cards');
const prevBtn = document.querySelector('.prev');
const nextBtn = document.querySelector('.next');
const itemWidth = container.querySelector('.con-col').clientWidth;
let scrollPosition = 0;

prevBtn.addEventListener('click', () => {
  if (scrollPosition > 0) {
    scrollPosition -= itemWidth;
    container.scrollTo({
      top: 0,
      left: scrollPosition,
      behavior: 'smooth'
    });
  }
});

nextBtn.addEventListener('click', () => {
  if (scrollPosition < container.scrollWidth - container.clientWidth) {
    scrollPosition += itemWidth;
    container.scrollTo({
      top: 0,
      left: scrollPosition,
      behavior: 'smooth'
    });
  }
});