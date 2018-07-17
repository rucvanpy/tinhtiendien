from django import forms

class TinhTienDienForm(forms.Form):
    cong_suat = forms.IntegerField(label='Công suất(W)',
                                    widget=forms.TextInput(attrs={'class': 'f-text', 'id' : 'cong_suat', 'placeholder': 'VD: 900'}))
    gia_dien = forms.IntegerField(label='Giá điện cho mỗi  kW/h(đ)', help_text='Để trống để lấy giá lũy tiến của EVN', required=False,
                                    widget=forms.TextInput(attrs={'class': 'f-text', 'id' : 'gia_dien', 'placeholder': 'VD:1500'}))
    thoi_gian = forms.IntegerField(label='Thời gian sử dụng mỗi ngày (tiếng)',
                                    widget=forms.TextInput(attrs={'class': 'f-text', 'id': 'thoi_gian', 'placeholder': 'VD: 8'}))
