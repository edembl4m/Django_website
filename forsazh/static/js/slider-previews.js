$(document).ready(function(){

    $('.product-all-imgs').slick({
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 1,
        swipeToSlide: true,
        vertical: true,
        prevArrow: "<div class='prev-ar'><i class='fa fa-angle-up' aria-hidden='true'></i></div>",
        nextArrow: "<div class='next-ar'><i class='fa fa-angle-down' aria-hidden='true'></i></div>",
        responsive: [
            {
                breakpoint: 670,
                settings: {
                    vertical: false,
                    arrows: false,
                }
            }
        ]
    });

    // cod narimana
      $('.product-more-img').click(function() {
        let foo = $(this).children('img').attr('src');
        let num = $(this).attr('data-slick-index');
        console.log(num);
        $('.product-main-img-item').children('img').attr('src',  foo);
        $('.product-main-img-item').attr('alt',  num);
      });
});