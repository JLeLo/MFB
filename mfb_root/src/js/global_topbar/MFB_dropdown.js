import "../vendor/jquery/jquery-3.6.0.min.js";

$(function () {
    // var value = $(this).val();
    // location.href = value ; //or .php, etc. This will go to a page called en.html
    $("#MFB_dropdown_list_id")
        .on("change", function () {
            $(".data").hide();
            $("#" + $(this).val()).fadeIn(700);
        })
        .change();
});

// $(document).ready(function () {
//     $("button").click(function () {
//         $("p").hide();
//     });
// });
