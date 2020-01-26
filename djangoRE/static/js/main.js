const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// maka alert messages fade away
setTimeout(function(){
    $('#message').fadeOut('slow')
}, 3000);