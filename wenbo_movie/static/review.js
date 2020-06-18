document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#submit_review').disabled = true;

    document.querySelector('#message').onkeyup = () => {
        if (document.querySelector('#message').value.length > 0)
            document.querySelector('#submit_review').disabled = false;
        else
            document.querySelector('#submit_review').disabled = true;
    };
});
