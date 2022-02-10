$(document).ready(function () {
    var counter = 1;
    $("#addNewField").click(function () {
        $("#languages").append('<li><input type="text" id="languages-' + counter + '"' + 'name="languages-' + counter + '"' + 'required ' + 'value' + "/>" + "<input type='button' value='Remove' class='remove'></input>" + "</li>");
        counter += 1;
    });

    $("body").on("click", ".remove", function () {
        $(this).closest("li").remove();
        counter -= 1;
    });
});