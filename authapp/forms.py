from django import forms
from django.forms import ModelForm,ValidationError
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Nhập tên đăng nhập'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Nhập mật khẩu'}))

class RegistrationForm(forms.Form):
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'firstname', 'placeholder': 'Nhập họ'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'lastname', 'placeholder': 'Nhập tên'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'email', 'name': 'email', 'placeholder': 'Nhập Email'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'text', 'name': 'username', 'placeholder': 'Nhập tên đăng nhâp'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'password', 'placeholder': 'Nhập mật khẩu'}))
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'type': 'password', 'name': 'confirm-password', 'placeholder': 'Nhập xác nhận mật khẩu'}))



class RegisterForm(forms.ModelForm):
    class Meta:
        model = information_NKT
        fields = '__all__' 

    ngay_sinh_nkt = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%m/%d/%Y', )
    )
    ngay_cap_nhat = forms.DateField(
        widget=forms.DateInput(format='%m/%d/%Y', attrs={'class': 'datepicker'}),
        input_formats=('%m/%d/%Y', )
    )

    so_dinh_danh = forms.CharField(widget=forms.TextInput(attrs={ 'type': 'text',  'placeholder': ''}))


class UpdateForm(forms.ModelForm):
    class Meta:
        model = information_NKT
        fields = '__all__'
class KhuyetTatForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KhuyetTatForm, self).__init__(*args, **kwargs)
        # Making location required
        self.fields['bai_nao'].required = False
        self.fields['liet_tu_chi'].required = False
        self.fields['ban_chan_khoe'].required = False
        self.fields['liet_nua_nguoi'].required = False
        self.fields['cut_chi'].required = False
        self.fields['cot_song'].required = False
        self.fields['ton_thuong_tuy'].required = False
        self.fields['thoai_hoa'].required = False
        self.fields['trat_khop'].required = False
        self.fields['nhuoc_co'].required = False
        self.fields['vandong_khac'].required = False
        self.fields['mu_mau'].required = False
        self.fields['quang_ga'].required = False
        self.fields['can_thi'].required = False
        self.fields['mu_2_mat'].required = False
        self.fields['mu_1_mat'].required = False
        self.fields['mat_thi_truong'].required = False
        self.fields['vien_thi'].required = False
        self.fields['lac_mat'].required = False
        self.fields['nhin_khac'].required = False
        self.fields['noi'].required = False
        self.fields['nghe'].required = False
        self.fields['cham'].required = False
        self.fields['down'].required = False
        self.fields['tu_ky'].required = False
        self.fields['tam_than'].required = False
        self.fields['nhan_thuc_khac'].required = False
        self.fields['dong_kinh'].required = False
        self.fields['bong'].required = False
        self.fields['tim'].required = False
        self.fields['ho_hap'].required = False
        self.fields['cam_giac'].required = False
        self.fields['kt_khac'].required = False
        self.fields['namkhuyettat'].required = False
        self.fields['tinhtrangkt'].required = False
        self.fields['nguyennhanbs_khac'].required = False
        self.fields['nguyennhanmp_khac'].required = False
        self.fields['kt_khac'].required = False
        self.fields['nguyennhankt'].required = False
        self.fields['mucdokt'].required = False
        self.fields['lydochuaxacdinhkt'].required = False
        self.fields['so_dinh_danh'].required = True
    class Meta:
        model = KhuyetTat
        fields = '__all__'
class NhuCauForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NhuCauForm, self).__init__(*args, **kwargs)
        self.fields['nc_kt_tuyentren'].required = False
        self.fields['nc_kb_tuyentren'].required = False
        self.fields['nc_capchiphi'].required = False
        self.fields['nc_capbhyt'].required = False
        self.fields['nc_taphoiphuc_bbhyt'].required = False
        self.fields['nc_taphoiphuc'].required = False
        self.fields['nc_dungcuphcn'].required = False
        self.fields['nc_phauthuatchinhinh'].required = False
        self.fields['nc_chuongtrinhphathien'].required = False
        self.fields['nc_khac'].required = False
        self.fields['nc_trocap_tx'].required = False
        self.fields['nc_trocap_dx'].required = False
        self.fields['nc_nhao'].required = False
        self.fields['nc_daotaonghe'].required = False
        self.fields['nc_tudoanh'].required = False
        self.fields['nc_vayvon'].required = False
        self.fields['nc_tg_tcxh'].required = False
        self.fields['nc_xs_tt'].required = False
        self.fields['nc_suachuanha'].required = False
        self.fields['nc_vieclam'].required = False
        self.fields['nc_caithiendieukiensong'].required = False
        self.fields['nc_phuhuynhtg'].required = False
        self.fields['nc_tg_hdxh'].required = False
        self.fields['nc_miencuocbus'].required = False
        self.fields['nv_xh_khac'].required = False
        self.fields['nc_duocdihoc'].required = False
        self.fields['nc_hotrohocphi'].required = False
        self.fields['nc_hocphudao'].required = False
        self.fields['nc_dungcuhoctap'].required = False
        self.fields['nc_gd_khac'].required = False
        self.fields['so_dinh_danh'].required = True
    class Meta:
        model = NhuCau
        fields = "__all__"
class NhuCauDaNhanForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NhuCauDaNhanForm, self).__init__(*args, **kwargs)
        self.fields['ncdn_kt_tuyentren'].required = False
        self.fields['ncdn_kb_tuyentren'].required = False
        self.fields['ncdn_capchiphi'].required = False
        self.fields['ncdn_capbhyt'].required = False
        self.fields['ncdn_taphoiphuc_bbhyt'].required = False
        self.fields['ncdn_taphoiphuc'].required = False
        self.fields['ncdn_dungcuphcn'].required = False
        self.fields['ncdn_phauthuatchinhinh'].required = False
        self.fields['ncdn_chuongtrinhphathien'].required = False
        self.fields['ncdn_khac'].required = False
        self.fields['ncdn_trocap_tx'].required = False
        self.fields['ncdn_trocap_dx'].required = False
        self.fields['ncdn_nhao'].required = False
        self.fields['ncdn_daotaonghe'].required = False
        self.fields['ncdn_tudoanh'].required = False
        self.fields['ncdn_vayvon'].required = False
        self.fields['ncdn_tg_tcxh'].required = False
        self.fields['ncdn_xs_tt'].required = False
        self.fields['ncdn_suachuanha'].required = False
        self.fields['ncdn_vieclam'].required = False
        self.fields['ncdn_caithiendieukiensong'].required = False
        self.fields['ncdn_phuhuynhtg'].required = False
        self.fields['ncdn_tg_hdxh'].required = False
        self.fields['ncdn_miencuocbus'].required = False
        self.fields['nv_xh_khac'].required = False
        self.fields['ncdn_duocdihoc'].required = False
        self.fields['ncdn_hotrohocphi'].required = False
        self.fields['ncdn_hocphudao'].required = False
        self.fields['ncdn_dungcuhoctap'].required = False
        self.fields['ncdn_gd_khac'].required = False
        self.fields['so_dinh_danh'].required = True
        self.fields['ncdn_ngaynhan'].required = False
        self.fields['ncdn_cuthehotro'].required = False
        self.fields['ncdn_nguonhotro'].required = False
        self.fields['ncdn_cuthenguonhotro'].required = False
    class Meta:
        model = NhuCauDaNhan
        fields = "__all__"
        required = False