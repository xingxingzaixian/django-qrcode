$(function () {
    $("#b_btn").click(function () {
        var info = $(".b_txt").val();

        $.ajax({
            type: "post",
            url: "/",
            data: {'data': info},
            success: function (data) {
                $(".b_qrcode").html("<img id='qrcodeImg' alt='二维码' width='235' height='235' class='animated rollIn'/>");
                $("#qrcodeImg").attr("src", data);
            }
        });
    });
});