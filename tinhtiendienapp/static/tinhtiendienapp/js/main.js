(function ($) {
    $(document).on('ready', function () {
        "use strict";
        /**Preload**/
        $('#page-loader').delay(800).fadeOut(600, function () {
            $('body').fadeIn();
        });


        $('.acc-caption .acc-icon').click(function () {
            var content = $(this).parents(".accordion").find(".acc-content");
            if ($(content).is(":visible")) {
                $(content).slideUp();
                $(this).removeClass("active");

            } else {
                $(content).slideDown();
                $(this).addClass("active");
            }
        });



    });
})(jQuery);
