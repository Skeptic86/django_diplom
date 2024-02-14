document.addEventListener('DOMContentLoaded', function() {
    const tableRows = document.querySelectorAll('#postsTable tbody tr');
    const postsData = Array.from(tableRows).map(row => {
        const cells = row.querySelectorAll('td');
        return {
            id: cells[0].textContent.trim(),
            date: cells[1].textContent.trim(),
            theme: cells[2].textContent.trim()
        };
    });

    const selectButtons = document.querySelectorAll('.select-btn');
    const submitButton = document.getElementById('submit-btn');
    let selectedItems = [];

    selectButtons.forEach(button => {
        button.addEventListener('click', function() {
            const itemId = this.getAttribute('data-id');
            if (selectedItems.includes(itemId)) {
                selectedItems = selectedItems.filter(id => id !== itemId);
                this.classList.remove('selected');
            } else {
                selectedItems.push(itemId);
                this.classList.add('selected');
            }
            submitButton.disabled = selectedItems.length === 0;
        });
    });

    submitButton.addEventListener('click', function() {
        const csrfToken = getCookie('csrftoken');
        const formData = new FormData();
        const selectedPostsData = postsData.filter(post => selectedItems.includes(post.id.toString()));
        console.log(JSON.stringify(selectedPostsData))

        // Добавляем в formData строку, представляющую массив отфильтрованных объектов
        formData.append('selectedPosts', JSON.stringify(selectedPostsData));

        fetch("http://127.0.0.1:8000/posts/model_page", {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': csrfToken
            },
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
