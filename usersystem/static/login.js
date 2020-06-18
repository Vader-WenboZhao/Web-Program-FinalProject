document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#login_button').disabled = true;

    document.querySelector('#username_input').onkeyup  = () => {
        if (document.querySelector('#username_input').value.length > 0 &&
            document.querySelector('#password_input').value.length > 0)
            document.querySelector('#login_button').disabled = false;
        else
            document.querySelector('#login_button').disabled = true;
    };

    document.querySelector('#password_input').onkeyup  = () => {
        if (document.querySelector('#username_input').value.length > 0 &&
            document.querySelector('#password_input').value.length > 0)
            document.querySelector('#login_button').disabled = false;
        else
            document.querySelector('#login_button').disabled = true;
    };
});
