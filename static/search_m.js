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
                location.href = location.href.split('/')[0] + 's=relavence&q=' + search_box.value;
            }
        }
        else {
            location.href = location.href.split('/')[0] + 's=relavence&q=' + search_box.value;
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
                location.href = location.href.split('/')[0] + 's=relavence&q=null';
            }
        }
        else {
            location.href = location.href.split('/')[0] + 's=relavence&q=null';
        }
    }
}

document.addEventListener("keydown", (evt) => {
    if (evt.code === 'Enter'){
        search()
    }
});


menu_open = false

addEventListener('scroll', (evt) => {
    distance_top = document.documentElement.scrollTop
    if (distance_top > window.innerHeight*0.05) {
        search_box.style.backgroundColor = 'var(--tint_color)'
    }
    else {
        search_box.style.backgroundColor = 'transparent'
    }
});

addEventListener('DOMContentLoaded', (evt) => {
    search_box = document.getElementById('search box')
});

function search_appear() {
    search_box.style.visibility = 'visible'
}

addEventListener('click', (evt) => {
    console.log(evt.target)
    if (evt.target == document.getElementById('search_icon_h')) {
        document.getElementById('search_h').style.visibility = 'visible'
        document.getElementById('header').style.visibility = "hidden"
        console.log('search')
    }
    else if (search_box.style.visibility == 'visible') {
        if (evt.target != search_box && evt.target != document.getElementById('search_icon_h')) {
            document.getElementById('search_h').style.visibility = 'hidden'
            document.getElementById('header').style.visibility = 'visible'
            console.log('header')
        }
    }
});