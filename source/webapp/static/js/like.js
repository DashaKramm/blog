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
    let action = button.dataset.action;
    if (articleId) {
        let url = `/article/${articleId}/${action}/`;
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
            let likesCountElement = document.getElementById(`likes-count-${articleId}`);
            likesCountElement.innerText = `${data.likes_count} likes`;
        } catch (error) {
            console.error('Error handling like button click:', error);
        }
    }
}

function onLoad() {
    let likeButtons = document.querySelectorAll('[data-js="like-button"]');
    for (let button of likeButtons) {
        button.addEventListener('click', onClickLike);
    }
}

window.addEventListener('load', onLoad);