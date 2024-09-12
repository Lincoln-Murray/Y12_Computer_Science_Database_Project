menu_open = false

addEventListener('scroll', (evt) => {
    distance_top = document.documentElement.scrollTop
    if (distance_top > window.innerHeight*0.05) {
        document.getElementById('header').style.backgroundColor = 'var(--highlight_color)'
    }
    else {
        document.getElementById('header').style.backgroundColor = 'transparent'
    }
    if (distance_top > 2*934){
        scroll_top_element.style.visibility = 'visible'
        scroll_top_element.style.backgroundColor = 'var(--highlight_color)'
        scroll_top_element.style.width = '10%'
        scroll_top_element.style.height = '5%'
        scroll_top_element.style.minWidth = '150px'
        scroll_top_link_element.style.Color = 'var(--background_color)'
    }
    else {
        scroll_top_element.style.visibility = 'hidden'
        scroll_top_element.style.backgroundColor = 'transparent'
        scroll_top_element.style.width = '0%'
        scroll_top_element.style.height = '0%'
        scroll_top_element.style.minWidth = '0'
        scroll_top_link_element.style.Color = 'var(--highlight_color)'
    }
    });

addEventListener('DOMContentLoaded', (evt) => {
    menu_element = document.getElementById('menu')
    menu_button = document.getElementById('menu_button')
    scroll_top_element =  document.getElementById('scroll top')
    scroll_top_link_element = document.getElementById('scroll top link')
    window_div = document.getElementById('window div')
});