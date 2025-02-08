function showDeleteModal(url) {
    fetch(url, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        // Insert modal HTML
        document.getElementById('modal-container').innerHTML = data.html_form;
        const modal = document.getElementById('deleteModal');

        // Show modal (assuming Bootstrap)
        bootstrap.Modal.getOrCreateInstance(modal).show();

        // Handle form submission
        const form = modal.querySelector('form');
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            // Get form data
            const formData = new FormData(form);
            console.log(formData);

            // Second AJAX request to handle deletion
            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'Accept': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.success) {
                    bootstrap.Modal.getInstance(modal).hide();
                    window.location.href = data.redirect_url;
                }
            });
        });
    });
}
