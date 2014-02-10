$(document).ready(function() {
    $(".fancybox").fancybox();

    $("#popup").fancybox({
        'padding'           : 0,
        'width'             : '1200px',
        'height'            : '700px',
        'autoScale'     	: false,
        'transitionIn'		: 'none',
        'transitionOut'		: 'none',
        'type'				: 'iframe'
    });

    $('#scroll').click(function (e) {
        $('#scroll').toggleClass('active');
        e.preventDefault();
    });

//    делаем активный пункт меню
    $('ul.my_nav a').each(function () {
        var location = window.location.href;
        var link = this.href;
        if(location == link) {
            $(this).addClass('active');
        }
    });

//    скролл
//    $("a.scroll").scroll(function() {
//            $('a.scroll').toggleClass('visible');
//        }
//    );
//    $( "#scroll" ).click(function() {
//      alert('Элемент scroll был прокручен... скроллирован... ну как там это называется то?!');
//    });
//    $('#scroll').on('scroll',function(){
//        alert('Элемент scroll был прокручен... скроллирован... ну как там это называется то?!');
//    });
//    $('#scroll').scroll(function(){
//      alert('Элемент scroll был прокручен... скроллирован... ну как там это называется то?!');
//    });

});