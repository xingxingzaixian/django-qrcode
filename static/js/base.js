function on_qrcode_click(event) {
    let cus_id = $(event).prop('id');
    let url = '/';
    if (cus_id == 'b_btn1') {
        url = '/qrcode';
    }

    var info = $(".b_txt").val();
    $.ajax({
        type: "post",
        url: url,
        data: {'data': info},
        success: function (data) {
            $(".b_qrcode").html("<img id='qrcodeImg' alt='二维码' width='235' height='235' class='animated rollIn'/>");
            $("#qrcodeImg").attr("src", data);
        }
    });
}
