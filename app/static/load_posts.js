const post_img = document.getElementById('media-2-img');
const post_title = document.getElementById('media-body-title-2');
const post_text = document.getElementById('media-body-text-2');

post_img.src = "media/images/df7o6opc_nobel-price-in-physics-_650x400_06_October_26.jpg.webp";
post_title.innerHTML = 'Nobel Prize 2026 in Physics'
post_text.innerHTML = 'lorum ipsem';

function openForm() {
  document.getElementById("createNewPost").style.display = "flex";
  document.getElementById("overlay").style.display = "block";
}

function closeForm() {
  document.getElementById("createNewPost").style.display = "none";
  document.getElementById("overlay").style.display = "none";
}