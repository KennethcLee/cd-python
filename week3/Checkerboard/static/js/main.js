$('.box').hover(function() {
    var color = $(this).css("color");
    $(this).fadeOut(0, function() {
        $(this).css("color", $(this).css("background-color"));
    });
    $(this).fadeIn(0, function() {
        $(this).css("background-color", color);
    });
}, function() {
    var color = $(this).css("color");
    $(this).fadeOut(0, function() {
        $(this).css("color", $(this).css("background-color"));
    });
    $(this).fadeIn(0, function() {
        $(this).css("background-color", color);
    });
});
