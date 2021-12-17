$(document).ready(function() {
    var counter=1;
    $("#addNewField").click(function() {
        var newInput = $("<li><input required type='text' value=''></input><input type='button' value='Remove' class='remove'></input></li>")
            .attr("id", "languages" + "-" + counter)
            .attr("name", "languages" + "-" + counter)
        $("#languages").append(newInput);
        counter += 1;
    });

    $("body").on("click", ".remove", function () {
        $(this).closest("li").remove();
        counter -= 1;
    });
});