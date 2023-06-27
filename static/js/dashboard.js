
const $button  = document.querySelector('#sidebar-toggle');
const $wrapper = document.querySelector('#wrapper');
$button.addEventListener('click', (e) => {
  e.preventDefault();
  $wrapper.classList.toggle('toggled');
});


// image input
function previewImage(event) {
  var input = event.target;
  var reader = new FileReader();
  reader.onload = function(){
    var img = document.getElementById("imagePreview");
    img.src = reader.result;
     };
  reader.readAsDataURL(input.files[0]);
          }

       