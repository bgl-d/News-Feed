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


async function feeed_data() {
  const url = 'http://localhost:5001/api/posts';

  try{
    const response = await fetch(url);
    if (!response.ok){
      throw new Error(`Response status: ${response.status}`);
    }

    const result = await response.json();
    console.log(result);
    const post_img = document.getElementById('media-2-img');
    const post_title = document.getElementById('media-body-title-2');
    const post_text = document.getElementById('media-body-text-2');
    const [post] = result;

    post_img.src = post.mediaLink;
    post_title.innerHTML = post.title
    post_text.innerHTML = post.text;
  } catch(error) {
    console.error(error.message);
  }
}

feeed_data()