async function makeRequest(url, method = "GET") {
    const response = await fetch(url);
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.text);
        console.log(error);
        throw error;
    }
}

async function onClickLike(event) {
    event.preventDefault();
    let button = event.target;
    let articleId = button.dataset.articleId;
    let commentId = button.dataset.commentId;
    let action = button.dataset.action;
    let url;
    if (articleId) {
        url = `/article/${articleId}/${action}/`;
    } else if (commentId) {
        url = `/comment/${commentId}/${action}/`;
    }
    try {
        let data = await makeRequest(url);
        if (action === 'like') {
            button.innerText = 'Unlike';
            button.classList.remove('btn-primary');
            button.classList.add('btn-danger');
            button.dataset.action = 'unlike';
        } else if (action === 'unlike') {
            button.innerText = 'Like';
            button.classList.remove('btn-danger');
            button.classList.add('btn-primary');
            button.dataset.action = 'like';
        }
        let likesCountElement;
        if (articleId) {
            likesCountElement = document.getElementById(`likes-count-${articleId}`);
        } else if (commentId) {
            likesCountElement = document.getElementById(`likes-count-${commentId}`);
        }
        likesCountElement.innerText = `${data.likes_count} likes`;
    } catch (error) {
        console.error('Error handling like button click:', error);
    }
}

function onLoad() {
    let likeButtons = document.querySelectorAll('[data-js="like-button"]');
    for (let button of likeButtons) {
        button.addEventListener('click', onClickLike);
    }
}

window.addEventListener('load', onLoad);