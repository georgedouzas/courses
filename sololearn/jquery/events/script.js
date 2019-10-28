$(function () {

    $("#add").on(
        "click", function () {
            let val = $("input").val();
            if (val !== "") {
                let elem = $("<li></li>").text(val);
                let button = $("<button>X</button>").addClass("remove");
                $(elem).append(button);
                $("#mylist").append(elem);
                $("input").val("");
            }

            $(".remove").on(
                "click", function () {
                    $(this).parent().remove();
                }
            );

        }
    );

});
