const submitButtons = document.querySelectorAll('.sendMessageBtn');


function handleSubmit(e) {
    e.preventDefault();
    const sendUrl = this.dataset.url;
    const commentTextArea = this.parentElement.parentElement.querySelector('textarea');
    const csrftoken = document.cookie.match(/csrftoken=([\w-]+)/)[1];
    const commentContainer = this.parentElement.parentElement.parentElement.previousElementSibling;

    const data = {
        'csrfmiddlewaretoken': csrftoken,
        'comment': commentTextArea.value,

    }

    fetch(sendUrl, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        }
    })
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                console.log(response)
            }
        })
        .then(data => {
            const newCommentEle = (`<div style="--bs-bg-opacity: .75;" class="card my-2 offset-2 text-white bg-primary">
                    <div class="card-body">
                        ${data.comment}
                    </div>
                </div>`);

            commentContainer.insertAdjacentHTML('beforeend', newCommentEle);
            commentTextArea.value = '';

        })
        .catch(error => {
            console.log(error)
        })
}

submitButtons.forEach(button => {
    button.addEventListener('click', handleSubmit)
})