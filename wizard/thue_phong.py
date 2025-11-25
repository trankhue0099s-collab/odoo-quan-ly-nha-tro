from odoo import models, fields, api

class ThuePhongWizard(models.TransientModel):
    _name = 'quan_ly_nha_tro.thue_phong.wizard'
    _description = 'Cửa sổ thuê phòng nhanh'

    phong_tro_id = fields.Many2one('quan_ly_nha_tro.phong_tro', string="Phòng muốn thuê", readonly=True)
    khach_thue_id = fields.Many2one('quan_ly_nha_tro.khach_thue', string="Khách thuê", required=True)
    ngay_bat_dau = fields.Date(string="Ngày bắt đầu", default=fields.Date.today)

    def action_tao_hop_dong(self):
        # Tạo hợp đồng mới
        self.env['quan_ly_nha_tro.hop_dong'].create({
            'khach_thue_id': self.khach_thue_id.id,
            'phong_tro_id': self.phong_tro_id.id,
            'ngay_bat_dau': self.ngay_bat_dau,
            'trang_thai': 'dang_thue',
            'gia_thue': self.phong_tro_id.gia_thue
        })
        # Đổi trạng thái phòng
        self.phong_tro_id.tinh_trang = 'dang_thue'
        # Đóng cửa sổ lại
        return {'type': 'ir.actions.act_window_close'}