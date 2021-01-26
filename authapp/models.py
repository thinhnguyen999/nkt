from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#-----PHÂN QUYỀN USER SỬ DỤNG -----------
class Permission(models.Model):
    user_rel = models.ForeignKey(User,on_delete=models.CASCADE)
    can_view = models.BooleanField(default=True)
    can_add = models.BooleanField(default=True)
    can_edit = models.BooleanField(default=True)
    can_delete = models.BooleanField(default=True)
    can_report = models.BooleanField(default=True)
    can_manage_user = models.BooleanField(default=True)

    def __str__(self):
        return self.user_rel.username


#----- THÔNG TIN NGƯỜI KHUYẾT TẬT ------
class information_NKT(models.Model):
    ho_ten_khai_sinh_nkt = models.CharField(max_length=50,null=True, default="Nguyen Van A")
    noi_dk_khai_sinh = models.CharField(max_length=100, null=True, default="Tinh Ben Tre")
    que_quan = models.CharField(max_length=100, null=True, default="Tinh Ben Tre")
    dia_chi_thuong_tru = models.CharField(max_length=100, null=True, default="Nguyen Van A")
    so_tt_nkt = models.CharField(max_length=15,null=True,default="1111111111")
    # so_tt_nkt = models.CharField(max_length=15,null=True,unique=True,error_messages={'unique':'Số thứ tự đã tồn tại'})
    ngay_sinh_nkt = models.DateField(null=True,blank=True)
    so_dinh_danh = models.CharField(max_length=20,unique=True, error_messages={'unique':'Số định danh đã tồn tại'},default="333333333333")
    so_hieu_giay_xac_nhan = models.CharField(max_length=12,unique=True,error_messages={'unique':'Số hiệu đã tồn tại'},default="111111111111")
    list_gioi_tinh = [
        ('Nam','Nam'),
        ('Nữ','Nữ'),
        ('Khác','Khác'),
    ]
    gioi_tinh = models.CharField(choices=list_gioi_tinh, max_length=20, default=1)

    so_cmnd = models.CharField(max_length=10, null=True, blank=True,unique=True,error_messages={'unique':'Số CMND đã tồn tại'},default="1111111111")
    quoc_tich = models.CharField(max_length=20, null=True, default="Viet Nam")
    list_dan_toc= [
        ('Kinh', 'Kinh'),
        ('Tày', 'Tày'),
        ('Thái', 'Thái'),
        ('Hoa', 'Hoa'),
    ]
    dan_toc= models.CharField( choices=list_dan_toc, max_length=200, default=1)
    list_ton_giao = [
        ('Thiên chúa', 'Thiên Chúa '),
        ('Phật giáo', 'Phật Giáo'),
        ('Không tôn giáo', 'Không tôn giáo'),
        ('Khác', 'Khác'),
    ] 
    ton_giao = models.CharField( choices=list_ton_giao, max_length=100, default=1)
    list_nhom_mau = [
        ('Nhóm máu O', 'Nhóm máu O'),
        ('Nhóm máu A', 'Nhóm máu A'),
        ('Nhóm máu B', 'Nhóm máu B'),
        ('Nhóm máu AB', 'Nhóm máu AB'),
    ]
    nhom_mau= models.CharField( choices=list_nhom_mau, max_length=200, default=1)
    list_trinh_do = [
        ('Không đi học/ Mù chữ', 'Không đi học/ Mù chữ'),
        ('Biết đọc, biết viết', 'Biết đọc, biết viết'),
        ('Tiểu học', 'Tiểu học'),
        ('THCS', 'THCS'),
        ('THPT', 'THPT'),
        ('Sơ cấp/ Trung học', 'Sơ cấp/ Trung học'),
        ('Cao đẳng/ Đại học', 'Cao đẳng/ Đại học'),
        ('Trên đại học', 'Trên đại học'),
        ('Khác', 'Khác'),
    ]
    trinh_do = models.CharField( choices=list_trinh_do, max_length=200, default=1)
    list_chuyen_mon =[
        ('Chưa qua đào tạo', 'Chưa qua đào tạo'),
        ('Trung học', 'Trung học'),
        ('Cao đẳng/ Đại học', 'Cao đẳng/ Đại học'),
        ('Trên đại học', 'Trên đại học'),
        ('Khác', 'Khác'),
    ]
    chuyen_mon = models.CharField(choices=list_chuyen_mon, max_length=100, default=1)
    list_nghe_nghiep =[
        ('Còn nhỏ', 'Còn nhỏ'),
        ('Nội trợ', 'Nội trợ'),
        ('Nông nghiệp', 'Nông nghiệp'),
        ('Trên đại học', 'Trên đại học'),
        ('Khác', 'Khác'),
    ]
    nghe_nghiep = models.CharField(choices=list_nghe_nghiep, max_length=100, default=1)
    list_nan_nhan_da_cam = [
        ('Có','Có'),
        ('Không','Không'),
        ('Khác', 'Khác'),
    ]
    nan_nhan_da_cam = models.CharField(choices=list_nan_nhan_da_cam, max_length=100,default=1)
    list_hon_nhan =[
        ('Chưa kết hôn', 'Chưa kết hôn'),
        ('Đã kết hôn', 'Đã kết hôn'),
        ('Ly hôn', 'Ly hôn'),
        ('Góa', 'Góa'),
        ('Khác', 'Khác'),
    ]
    hon_nhan = models.CharField(choices=list_hon_nhan, max_length=100,default=1)
    tong_so_con = models.CharField(max_length=10, null=True,default=1)
    so_con_duoi_16 = models.CharField(max_length=2, null=True,default=1)
    #----- THÔNG TIN LIÊN LẠC NKT -----
    dia_chi = models.CharField(max_length=100,null=True,blank=True, default="Tỉnh Bến Tre")
    so_dt_lh = models.CharField(max_length=11,null=True,unique=True,error_messages={'unique':'Số điện thoại đã tồn tại'}, default="1234556562")
    ngay_cap_nhat = models.DateField(null=True)
    nguoi_cap_nhat = models.CharField(max_length=100,null=True, default="Nguyen Vn b")
    ho_ten_nguoi_ql = models.CharField(max_length=50,null=True, default="Nguyen Vn b Vn")
    don_vi_cong_tac = models.CharField(max_length=50,null=True, default="đá  sda dđ")
    linh_vuc = models.CharField(max_length=100,null=True, default="sd adsa ")

    #----- THÔNG TIN HỘ GIA ĐÌNH -----
    ho_ten_chu_ho = models.CharField(max_length=30, null=True, default="Tỉnh Bến Tre")
    so_cmnd_chu_ho = models.CharField(max_length=12, null=True, default="566565645")
    ma_so_dinh_danh_chu_ho = models.CharField(max_length=15, null=True, default="566565645246")
    quoc_tich_chu_ho = models.CharField(max_length=15, null=True, default="Viet Name")

    list_quan_he_nkt = [
        ('Bố', 'Bố'),
        ('Mẹ', 'Mẹ'),
        ('Ông', 'Ông'),
        ('Bà', 'Bà'),
        ('Cô', 'Cô'),
        ('Dì', 'Dì'),
        ('Chú', 'Chú'),
        ('Bác', 'Bác'),
        ('Anh', 'Anh'),
        ('Chị', 'Chị'),
        ('Em', 'Em'),
        ('Chồng', 'Chồng'),
        ('Vợ', 'Vợ'),
        ('Con', 'Con'),
        ('Cháu', 'Cháu'),
        ('Người khuyết tật', 'Người khuyết tật'),
        ('Khác', 'Khác'),
    ]
    quan_he_voi_nkt = models.CharField(max_length=20,choices=list_quan_he_nkt, default=1)
    sdt_lien_lac_ho_gia_dinh = models.CharField(max_length=11, null=True, default="1234567890")
    #----- THÔNG TIN NGƯỜI THÂN ĐẠI DIỆN -----
    ho_ten_nguoi_dai_dien = models.CharField(max_length=30, null=True, default="Transsss Csss")
    sdt_nguoi_dai_dien = models.CharField(max_length=11, null=True, default="1234567890")
    so_cmnd_nguoi_dai_dien = models.CharField(max_length=30, null=True, default="123456789")
    ma_so_dinh_danh_nguoi_dai_dien = models.CharField(max_length=30, null=True, default="123456789101")
    quoc_tich_nguoi_dai_dien = models.CharField(max_length=20, null=True, default="Viet Nam")
    list_ndd_quan_he_nkt = [
        ('Bố', 'Bố'),
        ('Mẹ', 'Mẹ'),
        ('Ông', 'Ông'),
        ('Bà', 'Bà'),
        ('Cô', 'Cô'),
        ('Dì', 'Dì'),
        ('Chú', 'Chú'),
        ('Bác', 'Bác'),
        ('Anh', 'Anh'),
        ('Chị', 'Chị'),
        ('Em', 'Em'),
        ('Chồng', 'Chồng'),
        ('Vợ', 'Vợ'),
        ('Con', 'Con'),
        ('Cháu', 'Cháu'),
        ('Người khuyết tật', 'Người khuyết tật'),
        ('Khác', 'Khác'),
    ]
    ndd_quan_he_voi_nkt = models.CharField(max_length=20,choices=list_ndd_quan_he_nkt, default=1)
    #----- THÔNG TIN NGƯỜI CHĂM SÓC -----
    ho_ten_nguoi_cham_soc = models.CharField(max_length=20, null=True, default="Tran Van B")
    so_cmnd_nguoi_cham_soc = models.CharField(max_length=15, null=True, default="123456789")
    ma_so_dinh_danh_nguoi_cham_soc = models.CharField(max_length=20, null=True, default="123456789101")
    quoc_tich_nguoi_cham_soc = models.CharField(max_length=20, null=True, default="Viet Nam")
    so_dt_nguoi_cham_soc = models.CharField(max_length=11, null=True, default="0123456789")
    list_ncs_quan_he_nkt = [
        ('Bố', 'Bố'),
        ('Mẹ', 'Mẹ'),
        ('Ông', 'Ông'),
        ('Bà', 'Bà'),
        ('Cô', 'Cô'),
        ('Dì', 'Dì'),
        ('Chú', 'Chú'),
        ('Bác', 'Bác'),
        ('Anh', 'Anh'),
        ('Chị', 'Chị'),
        ('Em', 'Em'),
        ('Chồng', 'Chồng'),
        ('Vợ', 'Vợ'),
        ('Con', 'Con'),
        ('Cháu', 'Cháu'),
        ('Người khuyết tật', 'Người khuyết tật'),
        ('Khác', 'Khác'),
    ]
    ncs_quan_he_voi_nkt = models.CharField(max_length=20,choices=list_ncs_quan_he_nkt, default=1)

class KhuyetTat(models.Model):
    bai_nao = models.CharField(max_length=100,null=True, default="")
    liet_tu_chi = models.CharField(max_length=100,null=True, default="")
    ban_chan_khoe = models.CharField(max_length=100,null=True, default="")
    liet_nua_nguoi = models.CharField(max_length=100,null=True, default="")
    cut_chi = models.CharField(max_length=100,null=True, default="")
    cot_song = models.CharField(max_length=100,null=True, default="")
    ton_thuong_tuy = models.CharField(max_length=100,null=True, default="")
    thoai_hoa = models.CharField(max_length=100,null=True, default="")
    trat_khop = models.CharField(max_length=100,null=True, default="")
    nhuoc_co = models.CharField(max_length=100,null=True, default="")
    vandong_khac = models.CharField(max_length=100,null=True, default="")
    mu_mau = models.CharField(max_length=100,null=True, default="")
    quang_ga = models.CharField(max_length=100,null=True, default="")
    can_thi = models.CharField(max_length=100,null=True, default="")
    mu_2_mat = models.CharField(max_length=100,null=True, default="")
    mu_1_mat = models.CharField(max_length=100,null=True, default="")
    mat_thi_truong = models.CharField(max_length=100,null=True, default="")
    vien_thi = models.CharField(max_length=100,null=True, default="")
    lac_mat = models.CharField(max_length=100,null=True, default="")
    nhin_khac = models.CharField(max_length=100,null=True, default="")
    noi = models.CharField(max_length=100,null=True, default="")
    nghe = models.CharField(max_length=100,null=True, default="")
    cham = models.CharField(max_length=100,null=True, default="")
    down = models.CharField(max_length=100,null=True, default="")
    tu_ky = models.CharField(max_length=100,null=True, default="")
    tam_than = models.CharField(max_length=100,null=True, default="")
    nhan_thuc_khac = models.CharField(max_length=100,null=True, default="")
    dong_kinh = models.CharField(max_length=100,null=True, default="")
    bong = models.CharField(max_length=100,null=True, default="")
    tim = models.CharField(max_length=100,null=True, default="")
    ho_hap = models.CharField(max_length=100,null=True, default="")
    cam_giac = models.CharField(max_length=100,null=True, default="")
    kt_khac = models.CharField(max_length=100,null=True, default="")
    namkhuyettat = models.CharField(max_length=100,null=True, default="")
    tinhtrangkt = models.CharField(max_length=100,null=True, default="")
    nguyennhanbs_khac = models.CharField(max_length=100,null=True, default="")
    nguyennhanmp_khac = models.CharField(max_length=100,null=True, default="")
    kt_khac = models.CharField(max_length=100,null=True, default="")
    nguyennhankt =  models.CharField(max_length=100,null=True, default="")
    mucdokt =  models.CharField(max_length=100,null=True, default="")
    lydochuaxacdinhkt =  models.CharField(max_length=100,null=True, default="")
    so_dinh_danh = models.CharField(max_length=20,unique=True,error_messages={'unique':'Số định danh đã tồn tại'},default="333333333333")
class NhuCau(models.Model):
    nc_kt_tuyentren = models.CharField(max_length=100,null=True, default="")
    nc_kb_tuyentren = models.CharField(max_length=100,null=True, default="")
    nc_capchiphi = models.CharField(max_length=100,null=True, default="")
    nc_capbhyt = models.CharField(max_length=100,null=True, default="")
    nc_taphoiphuc_bbhyt = models.CharField(max_length=100,null=True, default="")
    nc_taphoiphuc = models.CharField(max_length=100,null=True, default="")
    nc_dungcuphcn = models.CharField(max_length=100,null=True, default="")
    nc_phauthuatchinhinh = models.CharField(max_length=100,null=True, default="")
    nc_chuongtrinhphathien = models.CharField(max_length=100,null=True, default="")
    nc_khac = models.CharField(max_length=100,null=True, default="")
    nc_trocap_tx = models.CharField(max_length=100,null=True, default="")
    nc_trocap_dx = models.CharField(max_length=100,null=True, default="")
    nc_nhao = models.CharField(max_length=100,null=True, default="")
    nc_daotaonghe = models.CharField(max_length=100,null=True, default="")
    nc_tudoanh = models.CharField(max_length=100,null=True, default="")
    nc_vayvon = models.CharField(max_length=100,null=True, default="")
    nc_tg_tcxh = models.CharField(max_length=100,null=True, default="")
    nc_xs_tt = models.CharField(max_length=100,null=True, default="")
    nc_suachuanha = models.CharField(max_length=100,null=True, default="")
    nc_vieclam = models.CharField(max_length=100,null=True, default="")
    nc_caithiendieukiensong = models.CharField(max_length=100,null=True, default="")
    nc_phuhuynhtg = models.CharField(max_length=100,null=True, default="")
    nc_tg_hdxh = models.CharField(max_length=100,null=True, default="")
    nc_miencuocbus = models.CharField(max_length=100,null=True, default="")
    nv_xh_khac = models.CharField(max_length=100,null=True, default="")
    nc_duocdihoc = models.CharField(max_length=100,null=True, default="")
    nc_hotrohocphi = models.CharField(max_length=100,null=True, default="")
    nc_hocphudao = models.CharField(max_length=100,null=True, default="")
    nc_dungcuhoctap = models.CharField(max_length=100,null=True, default="")
    nc_gd_khac = models.CharField(max_length=100,null=True, default="")
    so_dinh_danh = models.CharField(max_length=20,unique=True,error_messages={'unique':'Số định danh đã tồn tại'},default="333333333333")


class NhuCauDaNhan(models.Model):
    ncdn_ngaynhan = models.CharField(max_length=100,null=True, default="")
    ncdn_cuthehotro = models.CharField(max_length=100,null=True, default="")
    ncdn_nguonhotro = models.CharField(max_length=100,null=True, default="")
    ncdn_cuthenguonhotro = models.CharField(max_length=100,null=True, default="")
    ncdn_kt_tuyentren = models.CharField(max_length=100,null=True, default="")
    ncdn_kb_tuyentren = models.CharField(max_length=100,null=True, default="")
    ncdn_capchiphi = models.CharField(max_length=100,null=True, default="")
    ncdn_capbhyt = models.CharField(max_length=100,null=True, default="")
    ncdn_taphoiphuc_bbhyt = models.CharField(max_length=100,null=True, default="")
    ncdn_taphoiphuc = models.CharField(max_length=100,null=True, default="")
    ncdn_dungcuphcn = models.CharField(max_length=100,null=True, default="")
    ncdn_phauthuatchinhinh = models.CharField(max_length=100,null=True, default="")
    ncdn_chuongtrinhphathien = models.CharField(max_length=100,null=True, default="")
    ncdn_khac = models.CharField(max_length=100,null=True, default="")
    ncdn_trocap_tx = models.CharField(max_length=100,null=True, default="")
    ncdn_trocap_dx = models.CharField(max_length=100,null=True, default="")
    ncdn_nhao = models.CharField(max_length=100,null=True, default="")
    ncdn_daotaonghe = models.CharField(max_length=100,null=True, default="")
    ncdn_tudoanh = models.CharField(max_length=100,null=True, default="")
    ncdn_vayvon = models.CharField(max_length=100,null=True, default="")
    ncdn_tg_tcxh = models.CharField(max_length=100,null=True, default="")
    ncdn_xs_tt = models.CharField(max_length=100,null=True, default="")
    ncdn_suachuanha = models.CharField(max_length=100,null=True, default="")
    ncdn_vieclam = models.CharField(max_length=100,null=True, default="")
    ncdn_caithiendieukiensong = models.CharField(max_length=100,null=True, default="")
    ncdn_phuhuynhtg = models.CharField(max_length=100,null=True, default="")
    ncdn_tg_hdxh = models.CharField(max_length=100,null=True, default="")
    ncdn_miencuocbus = models.CharField(max_length=100,null=True, default="")
    nv_xh_khac = models.CharField(max_length=100,null=True, default="")
    ncdn_duocdihoc = models.CharField(max_length=100,null=True, default="")
    ncdn_hotrohocphi = models.CharField(max_length=100,null=True, default="")
    ncdn_hocphudao = models.CharField(max_length=100,null=True, default="")
    ncdn_dungcuhoctap = models.CharField(max_length=100,null=True, default="")
    ncdn_gd_khac = models.CharField(max_length=100,null=True, default="")
    so_dinh_danh = models.CharField(max_length=20,unique=True,error_messages={'unique':'Số định danh đã tồn tại'},default="333333333333")

class TinhThanh(models.Model):
    id = models.CharField(max_length=3,null=False, primary_key  = True)
    ten =  models.CharField(max_length=50,null=False)
    loai =  models.CharField(max_length=20,null=False)

class QuanHuyen(models.Model):
    id = models.CharField(max_length=3,null=False, primary_key  = True)
    ten =  models.CharField(max_length=50,null=False)
    loai =  models.CharField(max_length=20,null=False)
    id_tinh =  models.CharField(max_length=3,null=False)

class PhuongXa(models.Model):
    id = models.CharField(max_length=3,null=False, primary_key  = True)
    ten =  models.CharField(max_length=50,null=False)
    loai =  models.CharField(max_length=20,null=False)
    id_quanhuyen =  models.CharField(max_length=3,null=False)