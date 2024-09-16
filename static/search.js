function search() {
    if (search_box.value != "'" && search_box.value != '') {
        arr=location.href.split('=').slice(0, -1);
        if (arr.length > 0) {
            if (arr[0].slice(-1) === 's') {
                arr[0] = arr[0]+'=';
                arr[1] = arr[1]+'=';
                location.href = arr.join('') + search_box.value;
            }
            else {
                location.href = location.href.split('/')[0] + 's=relavenceq=' + search_box.value;
            }
        }
        else {
            location.href = location.href.split('/')[0] + 's=relavenceq=' + search_box.value;
        }
    }
    else {
        arr=location.href.split('=').slice(0, -1);
        if (arr.length > 0) {
            if (arr[0].slice(-1) === 's') {
                arr[0] = arr[0]+'=';
                arr[1] = arr[1]+'=';
                location.href = arr.join('') + 'null';
            }
            else{
                location.href = location.href.split('/')[0] + 's=relavenceq=null';
            }
        }
        else {
            location.href = location.href.split('/')[0] + 's=relavenceq=null';
        }
    }
}

document.addEventListener("keydown", (evt) => {
    if (evt.code === 'Enter'){
        search()
    }
});

addEventListener('DOMContentLoaded', (evt) => {
    search_box = document.getElementById('search box')
});