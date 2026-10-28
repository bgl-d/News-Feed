function openForm() {
  document.getElementById("createNewPost").style.display = "flex";
  document.getElementById("overlay").style.display = "block";
}

function closeForm() {
  document.getElementById("createNewPost").style.display = "none";
  document.getElementById("overlay").style.display = "none";
}

async function feedData() {
  const page = Number(document.querySelector('.page-btn.active')?.getAttribute('value'));
  const url = `/load-posts/posts/${page}`;
  console.log(page);
  try{
    const response = await fetch(url);
    if (!response.ok){
      throw new Error(`Response status: ${response.status}`);
    }

    // remove await see what happens
    const result = await response.json(); 
    post_img = [];
    post_title = [];
    post_text = [];

    for (var i = 1; i <= 3; i++) {
      post_img.push(document.getElementById(`media-${i}-img`));
      post_title.push(document.getElementById(`media-body-title-${i}`));
      post_text.push(document.getElementById(`media-body-text-${i}`));
    }

    for (var i = 0; i < 3; i++) {
      post_img[i].src = result[i].media_link;
      post_title[i].innerHTML = result[i].title;
      post_text[i].innerHTML = result[i].text;
    }
  } catch(error) {
    console.error(error.stack);
    console.error(error.message);
  }
}


async function createPost(){
  const post_img = document.getElementById('new-media-link').value;
  const post_title = document.getElementById('new-title').value;
  const post_text = document.getElementById('new-text').value;
  const post = { 
    title: post_title,
    text_content: post_text,
    media_link: post_img
  };

  try {
    const response = await fetch(
      '/create-post',
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json"
        },

        body: JSON.stringify(post)
      }
    );

    if (!response.ok) {
      throw new Error(
        "Failed to send data"
      );
    }
    closeForm();
    feedData();
    document.getElementById('new-media-link').value = '';
    document.getElementById('new-title').value = '';
    document.getElementById('new-text').value = '';

  } catch (error) {
    alert("Error: " + error.message);
  }
}

function setActive(element) {
    const buttons = document.querySelectorAll('.page-btn');
    buttons.forEach(button => button.classList.remove('active'));
    element.classList.add('active');
    
    feedData()
}

async function createPagination(){
  const postsPerPage = 3;

  // Request total number of posts
  const url = '/load-posts/total-posts';
  try{
    const response = await fetch(url);
    if (!response.ok){
      throw new Error(`Response status: ${response.status}`);
    }

    // Show whole number of pages
    const totalPosts = await response.json(); 
    const numPages = Math.ceil(totalPosts/postsPerPage)
    const pagination = document.getElementsByClassName('pagination')[0];
    const currentNumPages = 1 + 1

    for(let i=currentNumPages; i<=numPages; i++){
      const element = document.createElement("a");
      element.className = 'page-btn';
      element.setAttribute('value', i);
      element.textContent = i;
      element.addEventListener('click', () => setActive(element));
      pagination.appendChild(element);
    };
  }
  catch(error){
    console.log(error)
  }
}

feedData()
createPagination()
