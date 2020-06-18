document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#start_search').disabled = true;

    document.querySelector('#search_input').onkeyup = () => {
        if (document.querySelector('#search_input').value.length > 0)
            document.querySelector('#start_search').disabled = false;
        else
            document.querySelector('#start_search').disabled = true;
    };
});
