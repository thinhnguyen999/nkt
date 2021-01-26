$(document).ready(function() {
    // HỌ TÊN KHAI SINH NKT
    $.validator.addMethod('ho_ten_khai_sinh_nkt', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');

    $.validator.addMethod('noi_dk_khai_sinh', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, '');

    $.validator.addMethod('que_quan', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, '');

    $.validator.addMethod('dia_chi_thuong_tru', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, '');

    $.validator.addMethod('so_tt_nkt', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập kí tự số');

    $.validator.addMethod('so_dinh_danh', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập kí tự số');

    $.validator.addMethod('so_hieu_giay_xac_nhan', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập kí tự số');

    // $.validator.addMethod('so_cmnd', function(value, element, param) {
    //     var nameRegex = /[0-9]/;
    //     return value.match(nameRegex);
    // }, 'Số CMND bao gồm 9 chữ số');

    $.validator.addMethod('quoc_tich', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');

    $.validator.addMethod('tong_so_con', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập kí tự số');

    $.validator.addMethod('so_con_duoi_16', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập kí tự số');

    $.validator.addMethod('dia_chi', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, '');

    $.validator.addMethod('so_dt_lh', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Số điện thoại bao gồm 10 chữ số');

    $.validator.addMethod('nguoi_cap_nhat', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');

    $.validator.addMethod('ho_ten_nguoi_ql', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');

    $.validator.addMethod('don_vi_cong_tac', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, '');

    $.validator.addMethod('linh_vuc', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, '');

    $.validator.addMethod('ho_ten_chu_ho', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');

    $.validator.addMethod('so_cmnd_chu_ho', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Số CMND bao gồm 9 chữ số');

    $.validator.addMethod('ma_so_dinh_danh_chu_ho', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập kí tự số');

    $.validator.addMethod('quoc_tich_chu_ho', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');

    $.validator.addMethod('sdt_lien_lac_ho_gia_dinh', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Số điện thoại bao gồm 10 chữ số');

    $.validator.addMethod('ho_ten_nguoi_dai_dien', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');

    $.validator.addMethod('sdt_nguoi_dai_dien', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Số điện thoại bao gồm 10 chữ số');

    $.validator.addMethod('so_cmnd_nguoi_dai_dien', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Số CMND bao gồm 9 chữ số');

    $.validator.addMethod('ma_so_dinh_danh_nguoi_dai_dien', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập kí tự số');

    $.validator.addMethod('quoc_tich_nguoi_dai_dien', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');

    $.validator.addMethod('ho_ten_nguoi_cham_soc', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');

    $.validator.addMethod('so_cmnd_nguoi_cham_soc', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Số CMND bao gồm 9 chữ số');

    $.validator.addMethod('ma_so_dinh_danh_nguoi_cham_soc', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập kí tự số');

    $.validator.addMethod('quoc_tich_nguoi_cham_soc', function(value, element, param) {
        var nameRegex = /[a-zA-Z\u00C0-\u017F\s]+/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');

    $.validator.addMethod('so_dt_nguoi_cham_soc', function(value, element, param) {
        var nameRegex = /[0-9]/;
        return value.match(nameRegex);
    }, 'Số điện thoại bao gồm 10 chữ số');





    var val = {
        // Specify validation rules
        rules: {

            ho_ten_khai_sinh_nkt: {
                ho_ten_khai_sinh_nkt: true,
                required: true,
                minlength: 8,
                maxlength: 50,
            },
            noi_dk_khai_sinh: {
                noi_dk_khai_sinh: true,
                required: true,
                minlength: 8,
                maxlength: 50,
            },
            que_quan: {
                que_quan: true,
                required: true,
                minlength: 10,
                maxlength: 100,
            },
            dia_chi_thuong_tru: {
                dia_chi_thuong_tru: true,
                required: true,
                minlength: 10,
                maxlength: 100,
            },
            so_tt_nkt: {
                so_tt_nkt: true,
                required: true,
                minlength: 2,
                maxlength: 10,
            },
            so_dinh_danh: {
                so_dinh_danh: true,
                required: true,
                minlength: 12,
                maxlength: 12,
            },
            so_hieu_giay_xac_nhan: {
                so_hieu_giay_xac_nhan: true,
                required: true,
                minlength: 12,
                maxlength: 12,
            },
            // so_cmnd: {
            //     so_cmnd: true,
            //     required: true,
            //     minlength: 9,
            //     maxlength: 9,
            // },
            quoc_tich: {
                quoc_tich: true,
                required: true,
                minlength: 1,
                maxlength: 30,
            },
            tong_so_con: {
                tong_so_con: true,
                required: true,
                minlength: 0,
                maxlength: 5,
            },
            so_con_duoi_16: {
                so_con_duoi_16: true,
                required: true,
                minlength: 0,
                maxlength: 5,
            },
            dia_chi: {
                dia_chi: true,
                required: true,
                minlength: 10,
                maxlength: 100,
            },
            so_dt_lh: {
                so_dt_lh: true,
                required: true,
                minlength: 10,
                maxlength: 10,
            },
            nguoi_cap_nhat: {
                nguoi_cap_nhat: true,
                required: true,
                minlength: 8,
                maxlength: 50,
            },
            ho_ten_nguoi_ql: {
                ho_ten_nguoi_ql: true,
                required: true,
                minlength: 8,
                maxlength: 50,
            },
            don_vi_cong_tac: {
                don_vi_cong_tac: true,
                required: true,
                minlength: 2,
                maxlength: 50,
            },
            linh_vuc: {
                linh_vuc: true,
                required: true,
                minlength: 2,
                maxlength: 50,
            },
            ho_ten_chu_ho: {
                ho_ten_chu_ho: true,
                required: true,
                minlength: 8,
                maxlength: 50,
            },
            so_cmnd_chu_ho: {
                so_cmnd_chu_ho: true,
                required: true,
                minlength: 9,
                maxlength: 9,
            },
            ma_so_dinh_danh_chu_ho: {
                ma_so_dinh_danh_chu_ho: true,
                required: true,
                minlength: 12,
                maxlength: 12,
            },
            quoc_tich_chu_ho: {
                quoc_tich_chu_ho: true,
                required: true,
                minlength: 1,
                maxlength: 30,
            },
            sdt_lien_lac_ho_gia_dinh: {
                sdt_lien_lac_ho_gia_dinh: true,
                required: true,
                minlength: 10,
                maxlength: 10,
            },
            ho_ten_nguoi_dai_dien: {
                ho_ten_nguoi_dai_dien: true,
                required: true,
                minlength: 8,
                maxlength: 50,
            },
            sdt_nguoi_dai_dien: {
                sdt_nguoi_dai_dien: true,
                required: true,
                minlength: 10,
                maxlength: 10,
            },
            so_cmnd_nguoi_dai_dien: {
                so_cmnd_nguoi_dai_dien: true,
                required: true,
                minlength: 9,
                maxlength: 9,
            },
            ma_so_dinh_danh_nguoi_dai_dien: {
                ma_so_dinh_danh_nguoi_dai_dien: true,
                required: true,
                minlength: 12,
                maxlength: 12,
            },
            quoc_tich_nguoi_dai_dien: {
                quoc_tich_nguoi_dai_dien: true,
                required: true,
                minlength: 1,
                maxlength: 30,
            },
            ho_ten_nguoi_cham_soc: {
                ho_ten_nguoi_cham_soc: true,
                required: true,
                minlength: 8,
                maxlength: 50,
            },
            so_cmnd_nguoi_cham_soc: {
                so_cmnd_nguoi_cham_soc: true,
                required: true,
                minlength: 9,
                maxlength: 9,
            },
            ma_so_dinh_danh_nguoi_cham_soc: {
                ma_so_dinh_danh_nguoi_cham_soc: true,
                required: true,
                minlength: 12,
                maxlength: 12,
            },
            quoc_tich_nguoi_cham_soc: {
                quoc_tich_nguoi_cham_soc: true,
                required: true,
                minlength: 1,
                maxlength: 30,
            },
            so_dt_nguoi_cham_soc: {
                so_dt_nguoi_cham_soc: true,
                required: true,
                minlength: 10,
                maxlength: 10,
            },


        },

        // Specify validation error messages
        messages: {
            ho_ten_khai_sinh_nkt: {
                required: "Tên NKT không được để trống",
                minlength: "Tên NKT phải nhập ít nhất là 8 kí tự",
                maxlength: "Tên NKT không được vượt quá 50 kí tự",
            },
            noi_dk_khai_sinh: {
                required: "Nơi ĐKKS không được để trống",
                minlength: "Nơi ĐKKS phải nhập ít nhất là 10 kí tự",
                maxlength: "Nơi ĐKKS không được vượt quá 100 kí tự",
            },
            que_quan: {
                required: "Quê quán không được để trống",
                minlength: "Quê quán phải nhập ít nhất là 10 kí tự",
                maxlength: "Quê quán không được vượt quá 100 kí tự",
            },
            dia_chi_thuong_tru: {
                required: "Địa chỉ thường trú không được để trống",
                minlength: "Địa chỉ thường trú phải nhập ít nhất là 10 kí tự",
                maxlength: "Địa chỉ thường trú không được vượt quá 100 kí tự",
            },
            so_tt_nkt: {
                required: "Số thứ tự không được để trống",
                minlength: "Số thứ tự phải nhập ít nhất là 2 kí tự",
                maxlength: "Số thứ tự không được vượt quá 10 kí tự",
            },
            so_dinh_danh: {
                required: "Số định danh không được để trống",
                minlength: "Số định danh bao gồm 12 chữ số",
                maxlength: "Số định danh không được vượt quá 12 kí tự",
            },
            so_hieu_giay_xac_nhan: {
                required: "Số hiệu xác nhận không được để trống",
                minlength: "Số hiệu xác nhận bao gồm 12 chữ số",
                maxlength: "Số hiệu xác nhận không được vượt quá 12 kí tự",
            },
            gioi_tinh: {
                required: "Giới tính không được để trống",
            },
            // so_cmnd: {
            //     required: "Số CMND không được để trống",
            //     minlength: "Số CMND bao gồm 9 chữ số",
            //     maxlength: "Số CMND không được vượt quá 9 kí tự",
            // },
            quoc_tich: {
                required: "Quốc tịch không được để trống",
                minlength: "Quốc tịch phải nhập ít nhất là 1 kí tự",
                maxlength: "Quốc tịch không được vượt quá 30 kí tự",
            },
            dan_toc: {
                required: "Dân tộc không được để trống",
            },
            ton_giao: {
                required: "Tôn giáo không được để trống",
            },
            nhom_mau: {
                required: "Nhóm máu không được để trống",
            },
            trinh_do: {
                required: "Trình độ không được để trống",
            },
            chuyen_mon: {
                required: "Chuyên môn không được để trống",
            },
            nghen_ghiep: {
                required: "Nghề nghiệp không được để trống",
            },
            nan_nhan_da_cam: {
                required: "Nạn nhân không được để trống",
            },
            hon_nhan: {
                required: "Hôn nhân không được để trống",
            },
            tong_so_con: {
                required: "Tổng số con không được để trống",
                minlength: "Tổng số con phải nhập ít nhất là 0 kí tự",
                maxlength: "Tổng số con không được vượt quá 5 kí tự",
            },
            so_con_duoi_16: {
                required: "Số con dưới 16 tuổi không được để trống",
                minlength: "Số con dưới 16 tuổi phải nhập ít nhất là 0 kí tự",
                maxlength: "Số con dưới 16 tuổi không được vượt quá 5 kí tự",
            },
            dia_chi: {
                required: "Địa chỉ không được để trống",
                minlength: "Địa chỉ phải nhập ít nhất là 10 kí tự",
                maxlength: "Địa chỉ không được vượt quá 100 kí tự",
            },
            so_dt_lh: {
                required: "Số điện thoại không được để trống",
                minlength: "Số điện thoại bao gồm 10 chữ số",
                maxlength: "Số điện thoại không được vượt quá 10 kí tự",
            },
            nguoi_cap_nhat: {
                required: "Người cập nhật không được để trống",
                minlength: "Người cập nhật phải nhập ít nhất là 8 kí tự",
                maxlength: "Người cập nhật không được vượt quá 50 kí tự",
            },
            ho_ten_nguoi_ql: {
                required: "Họ tên người quản lý không được để trống",
                minlength: "Họ tên người quản lý phải nhập ít nhất là 8 kí tự",
                maxlength: "Họ tên người quản lý không được vượt quá 50 kí tự",
            },
            don_vi_cong_tac: {
                required: "Đơn vị công tác không được để trống",
                minlength: "Đơn vị công tác phải nhập ít nhất là 2 kí tự",
                maxlength: "Đơn vị công tác không được vượt quá 10 kí tự",
            },
            linh_vuc: {
                required: "Đơn vị công tác không được để trống",
                minlength: "Đơn vị công tác phải nhập ít nhất là 2 kí tự",
                maxlength: "Đơn vị công tác không được vượt quá 50 kí tự",
            },

            ho_ten_chu_ho: {
                required: "Tên chủ hộ không được để trống",
                minlength: "Tên chủ hộ phải nhập ít nhất là 8 kí tự",
                maxlength: "Tên chủ hộ không được vượt quá 50 kí tự",
            },
            so_cmnd_chu_ho: {
                required: "Số CMND không được để trống",
                minlength: "Số CMND bao gồm 9 chữ số",
                maxlength: "Số CMND không được vượt quá 9 kí tự",
            },
            ma_so_dinh_danh_chu_ho: {
                required: "Số định danh không được để trống",
                minlength: "Số định danh bao gồm 12 chữ số",
                maxlength: "Số định danh không được vượt quá 12 kí tự",
            },
            quoc_tich_chu_ho: {
                required: "Quốc tịch không được để trống",
                minlength: "Quốc tịch phải nhập ít nhất là 1 kí tự",
                maxlength: "Quốc tịch không được vượt quá 30 kí tự",
            },
            quan_he_voi_nkt: {
                required: "Quan hệ với NKT không được để trống",
            },
            sdt_lien_lac_ho_gia_dinh: {
                required: "Số điện thoại không được để trống",
                minlength: "Số điện thoại bao gồm 10 chữ số",
                maxlength: "Số điện thoại không được vượt quá 10 kí tự",
            },

            ho_ten_nguoi_dai_dien: {
                required: "Tên người đại dện không được để trống",
                minlength: "Tên người đại dện phải nhập ít nhất là 8 kí tự",
                maxlength: "Tên người đại dện không được vượt quá 50 kí tự",
            },
            sdt_nguoi_dai_dien: {
                required: "Số điện thoại không được để trống",
                minlength: "Số điện thoại bao gồm 10 chữ số",
                maxlength: "Số điện thoại không được vượt quá 10 kí tự",
            },
            so_cmnd_nguoi_dai_dien: {
                required: "Số CMND không được để trống",
                minlength: "Số CMND bao gồm 9 chữ số",
                maxlength: "Số CMND không được vượt quá 9 kí tự",
            },
            ma_so_dinh_danh_nguoi_dai_dien: {
                required: "Số định danh không được để trống",
                minlength: "Số định danh bao gồm 12 chữ số",
                maxlength: "Số định danh không được vượt quá 12 kí tự",
            },
            quoc_tich_nguoi_dai_dien: {
                required: "Quốc tịch không được để trống",
                minlength: "Quốc tịch phải nhập ít nhất là 1 kí tự",
                maxlength: "Quốc tịch không được vượt quá 30 kí tự",
            },
            ndd_quan_he_voi_nkt: {
                required: "Quan hệ với NKT không được để trống",
            },

            ho_ten_nguoi_cham_soc: {
                required: "Tên người chăm sóc không được để trống",
                minlength: "Tên người chăm sóc phải nhập ít nhất là 8 kí tự",
                maxlength: "Tên người chăm sóc không được vượt quá 50 kí tự",
            },
            so_cmnd_nguoi_cham_soc: {
                required: "Số CMND không được để trống",
                minlength: "Số CMND bao gồm 9 chữ số",
                maxlength: "Số CMND không được vượt quá 9 kí tự",
            },
            ma_so_dinh_danh_nguoi_cham_soc: {
                required: "Số định danh không được để trống",
                minlength: "Số định danh bao gồm 12 chữ số",
                maxlength: "Số định danh không được vượt quá 12 kí tự",
            },
            quoc_tich_nguoi_cham_soc: {
                required: "Quốc tịch không được để trống",
                minlength: "Quốc tịch phải nhập ít nhất là 1 kí tự",
                maxlength: "Quốc tịch không được vượt quá 30 kí tự",
            },
            so_dt_nguoi_cham_soc: {
                required: "Số điện thoại không được để trống",
                minlength: "Số điện thoại bao gồm 10 chữ số",
                maxlength: "Số điện thoại không được vượt quá 10 kí tự",
            },
            ncs_quan_he_voi_nkt: {
                required: "Quan hệ với NKT không được để trống",
            },
        }
    }
    $("#myForm").multiStepForm({
        // defaultStep:0,
        beforeSubmit: function(form, submit) {
            console.log("called before submiting the form");
            console.log(form);
            console.log(submit);
        },
        validations: val,
    }).navigateTo(0);
});

//------------ FORM 2 ---------------
$(document).ready(function() {
    $.validator.addMethod('username', function(value, element, param) {
        var nameRegex = /^[a-zA-Z]+$/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');


    var val = {
        // Specify validation rules
        rules: {

            username: {
                ho_ten_khai_sinh_nkt: true,
                required: true,
                minlength: 8,
                maxlength: 50,
            }

        },

        // Specify validation error messages
        messages: {
            username: {
                required: "Tên NKT không được để trống",
                minlength: "Tên NKT phải nhập ít nhất là 8 kí tự",
                maxlength: "Tên NKT phải nhập nhiều nhất là 50 kí tự",
            }
        }
    }
    $("#myForm1").multiStepForm({
        // defaultStep:0,
        beforeSubmit: function(form, submit) {
            console.log("called before submiting the form");
            console.log(form);
            console.log(submit);
        },
        validations: val,
    }).navigateTo(0);
});

// ----------------FORM 3 -------------------------
$(document).ready(function() {
    $.validator.addMethod('username', function(value, element, param) {
        var nameRegex = /^[a-zA-Z]+$/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');
    var val = {
        // Specify validation rules
        rules: {
            username: {
                ho_ten_khai_sinh_nkt: true,
                required: true,
                minlength: 8,
                maxlength: 50,
            }

        },
        // Specify validation error messages
        messages: {
            username: {
                required: "Tên NKT không được để trống",
                minlength: "Tên NKT phải nhập ít nhất là 8 kí tự",
                maxlength: "Tên NKT phải nhập nhiều nhất là 50 kí tự",
            }
        }
    }
    $("#myForm2").multiStepForm({
        // defaultStep:0,
        beforeSubmit: function(form, submit) {
            console.log("called before submiting the form");
            console.log(form);
            console.log(submit);
        },
        validations: val,
    }).navigateTo(0);
});
// ------------------- FORM 4 --------------------------
$(document).ready(function() {
    $.validator.addMethod('username', function(value, element, param) {
        var nameRegex = /^[a-zA-Z]+$/;
        return value.match(nameRegex);
    }, 'Chỉ được nhập a-z, A-Z kí tự cho phép');
    var val = {
        // Specify validation rules
        rules: {
            username: {
                ho_ten_khai_sinh_nkt: true,
                required: true,
                minlength: 8,
                maxlength: 50,
            }
        },
        // Specify validation error messages
        messages: {
            username: {
                required: "Tên NKT không được để trống",
                minlength: "Tên NKT phải nhập ít nhất là 8 kí tự",
                maxlength: "Tên NKT phải nhập nhiều nhất là 50 kí tự",
            }
        }
    }
    $("#myForm3").multiStepForm({
        // defaultStep:0,
        beforeSubmit: function(form, submit) {
            console.log("called before submiting the form");
            console.log(form);
            console.log(submit);
        },
        validations: val,
    }).navigateTo(0);
});