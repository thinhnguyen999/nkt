(function($) {
    "use strict";
    /*==================================================================
    [ Focus input ]*/
    var matinh = "";
    var mahuyen = "";
    var maphuong = "";

    $('#select_tinh').on('change', function() {
        $(`#select_quan option[id_tinh='${matinh}']`).addClass("hiden")
        matinh = this.value;
        $("#chon_huyen_block").removeClass("hiden");
        $(`#select_quan option[id_tinh="${matinh}"]`).removeClass("hiden")
    });
    $('#select_quan').on('change', function() {
        $(`#select_phuong option[id_phuong='${mahuyen}']`).addClass("hiden")
        mahuyen = this.value;
        $(`#select_phuong option[id_phuong='${mahuyen}']`).removeClass("hiden")
        $("#chon_phuong_block").removeClass("hiden")
    });
    $('#select_phuong').on('change', function() {
        maphuong = this.value;
        console.log(maphuong)
    });
    $('.input100').each(function() {
            $(this).on('blur', function() {
                if ($(this).val().trim() != "") {
                    $(this).addClass('has-val');
                } else {
                    $(this).removeClass('has-val');
                }
            })
        })
        /*==================================================================
        [ Validate ]*/
    var input = $('.validate-input .input100');
    $('.validate-form').on('submit', function() {
        var check = true;
        for (var i = 0; i < input.length; i++) {
            if (validate(input[i]) == false) {
                showValidate(input[i]);
                check = false;
            }
        }
        return check;
    });
    $('.validate-form .input100').each(function() {
        $(this).focus(function() {
            hideValidate(this);
        });
    });

    function validate(input) {
        if ($(input).attr('type') == 'email' || $(input).attr('name') == 'email') {
            if ($(input).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
                return false;
            }
        } else {
            if ($(input).val().trim() == '') {
                return false;
            }
        }
    }

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }

    function removeTTDK(so_dinh_danh) {
        console.log("remove " + so_dinh_danh)
        var thongtin = JSON.stringify({ "sodinhdanh": so_dinh_danh })
        $.ajax({
            type: "POST",
            url: "/removeTTNKT",
            data: thongtin,
            success: function(resp) {},
            error: function(resp) {}
        });
    }
    $("#saveInformation").on('click', function() {
            var form = $("#myForm");
            var data = form.serialize();
            var so_dinh_danh = form[0][7].value;
            $.ajax({
                type: "POST",
                url: "/insertTab1",
                data: data,
                success: function(resp) {
                    if (resp.code == 200) { // them model 1 thanh cong
                        var form = $("#myForm1");
                        var data = form.serialize();
                        data = data + "&so_dinh_danh=" + so_dinh_danh
                        $.ajax({
                            type: "POST",
                            url: "/insertKhuyetTatForm",
                            data: data,
                            success: function(resp) {
                                if (resp.code == 200) { // them nguoi khuyet tat thanh cong
                                    var form = $("#myForm2");
                                    var data = form.serialize();
                                    data = data + "&so_dinh_danh=" + so_dinh_danh
                                    $.ajax({
                                        type: "POST",
                                        url: "/insertNhuCauForm",
                                        data: data,
                                        success: function(resp) {
                                            if (resp.code == 200) { // them model nhu cau thanh cong
                                                var form = $("#myForm3");
                                                var data = form.serialize();
                                                data = data + "&so_dinh_danh=" + so_dinh_danh
                                                $.ajax({
                                                    type: "POST",
                                                    url: "/insertNhuCauDNForm",
                                                    data: data,
                                                    success: function(resp) {
                                                        if (resp.code == 200) {
                                                            alert("Thêm người khuyết tật thành công") // them model nhu cau thanh cong
                                                        } else {
                                                            removeTTDK(so_dinh_danh)
                                                            alert(resp.msg)
                                                        }
                                                    },
                                                    error: function(data) {
                                                        console.log(data)
                                                        alert(data);
                                                    }
                                                });
                                            } else {
                                                removeTTDK(so_dinh_danh)
                                                alert(resp.msg)
                                            }

                                        },
                                        error: function(data) {
                                            console.log(data)
                                            alert(data);
                                        }
                                    });
                                } else {
                                    removeTTDK(so_dinh_danh)
                                    alert(resp.msg)

                                }
                            },
                            error: function(data) {
                                console.log(data)
                                alert(data);
                            }
                        });
                    } else {
                        removeTTDK(so_dinh_danh)
                        alert(resp.msg)
                    }
                },
                error: function(data) {
                    console.log(data)
                    alert(data);
                }
            });
            console.log("Click");
        })
        // var values = [];
        // $("#vandongform input").each(function(i, sel) {
        //     var selectedVal = $(sel).val();
        //     values.push(selectedVal);
        // });
    $('input[type="checkbox"]').change(function() {
        if (this.checked) {
            $(this).attr("value", 1);
        } else {
            $(this).attr("value", 0);
        }
    });
    $("#nhapTTKT").on('click', function() {
        $(".nav-link.active").removeClass("active");
        $("a[href='#menu1']").addClass("active")
        $("#home").removeClass("active")
        $("#menu1").addClass("active show")
        $(".tabbar")[0].setAttribute("data-toggle", "tab")
        $(".tabbar")[1].setAttribute("data-toggle", "tab")
        console.log("Click");
    })

    $("#nhapNhuCau").on('click', function() {
        $(".nav-link.active").removeClass("active");
        $("a[href='#menu2']").addClass("active")
        $("#menu1").removeClass("active")
        $("#menu2").addClass("active show")
        $(".tabbar")[2].setAttribute("data-toggle", "tab")
        console.log("Click");
    })
    $("#nhapHoTroDaNhan").on('click', function() {
        $(".nav-link.active").removeClass("active");
        $("a[href='#menu3']").addClass("active")
        $("#menu2").removeClass("active")
        $("#menu3").addClass("active show")
        $(".tabbar")[3].setAttribute("data-toggle", "tab")
        console.log("Click");
    })

    $("#nhapHuongNghiep").on('click', function() {
        $(".nav-link.active").removeClass("active");
        $("a[href='#menu4']").addClass("active")
        $("#menu3").removeClass("active")
        $("#menu4").addClass("active show")
        $(".tabbar")[4].setAttribute("data-toggle", "tab")
        $(".tabbar").attr("data-toggle", "tab")
        console.log("Click");
    })


})(jQuery);

// var values = [];
// $("#vandongform input").each(function(i, sel) {
//     var selectedVal = $(sel).attr("name");
//     values.push(selectedVal);
// });
// $("#nhinform input").each(function(i, sel) {
//     var selectedVal = $(sel).attr("name");
//     values.push(selectedVal);
// });
// $("#nhanthucform input").each(function(i, sel) {
//     var selectedVal = $(sel).attr("name");
//     values.push(selectedVal);
// });
// $("#khuyettatkhacform input").each(function(i, sel) {
//     var selectedVal = $(sel).attr("name");
//     values.push(selectedVal);
// });
// $("#nguyennhan_khuyettatform input").each(function(i, sel) {
//     var selectedVal = $(sel).attr("name");
//     values.push(selectedVal);
// });