from odoo import models, fields, api, _
import logging

# Khai báo Logger để in thông báo ra màn hình đen cho dễ theo dõi
_logger = logging.getLogger(__name__)

# 1. PHÒNG TRỌ
class PhongTro(models.Model):
    _name = 'quan_ly_nha_tro.phong_tro'
    _description = 'Thông tin phòng trọ'

    name = fields.Char(string="Tên Phòng", required=True)
    gia_thue = fields.Float(string="Giá Thuê/Tháng", required=True)
    dien_tich = fields.Float(string="Diện Tích (m2)")
    mo_ta = fields.Text(string="Mô tả thêm")
    
    tinh_trang = fields.Selection([
        ('trong', 'Phòng Trống'),
        ('dang_thue', 'Đang Thuê'),
    ], string="Tình Trạng", default='trong')
    
    hop_dong_ids = fields.One2many('quan_ly_nha_tro.hop_dong', 'phong_tro_id', string="Danh Sách Hợp Đồng")

# 2. KHÁCH THUÊ
class KhachThue(models.Model):
    _name = 'quan_ly_nha_tro.khach_thue'
    _description = 'Hồ sơ khách thuê'

    name = fields.Char(string="Họ Tên", required=True)
    cmnd = fields.Char(string="CCCD")
    sdt = fields.Char(string="SĐT")
    gioi_tinh = fields.Selection([('nam', 'Nam'), ('nu', 'Nữ')], string="Giới tính")
    image = fields.Binary(string="Ảnh đại diện")
    
    hop_dong_ids = fields.One2many('quan_ly_nha_tro.hop_dong', 'khach_thue_id', string="Danh sách Hợp đồng")
    hop_dong_count = fields.Integer(string="Số lượng HĐ", compute='_compute_hop_dong_count')

    @api.depends('hop_dong_ids')
    def _compute_hop_dong_count(self):
        for r in self:
            r.hop_dong_count = len(r.hop_dong_ids)

    def action_view_hop_dong(self):
        return {
            'name': 'Hợp đồng của khách',
            'type': 'ir.actions.act_window',
            'res_model': 'quan_ly_nha_tro.hop_dong',
            'view_mode': 'tree,form',
            'domain': [('khach_thue_id', '=', self.id)],
            'context': {'default_khach_thue_id': self.id}
        }

# 3. HỢP ĐỒNG (CÓ HÀM ROBOT)
class HopDong(models.Model):
    _name = 'quan_ly_nha_tro.hop_dong'
    _description = 'Quản lý hợp đồng'

    name = fields.Char(string="Mã Hợp Đồng", required=True, copy=False, readonly=True, 
                       default=lambda self: self.env['ir.sequence'].next_by_code('quan_ly_nha_tro.hop_dong') or _('New'))
    
    khach_thue_id = fields.Many2one('quan_ly_nha_tro.khach_thue', string="Khách Thuê", required=True)
    phong_tro_id = fields.Many2one('quan_ly_nha_tro.phong_tro', string="Phòng Trọ", required=True)
    
    ngay_bat_dau = fields.Date(string="Ngày Bắt Đầu", default=fields.Date.today)
    ngay_ket_thuc = fields.Date(string="Ngày Kết Thúc")
    gia_thue = fields.Integer(string="Giá Thuê Chốt")
    
    trang_thai = fields.Selection([
        ('moi', 'Mới'), 
        ('dang_thue', 'Đang thuê'), 
        ('da_ket_thuc', 'Đã kết thúc')
    ], string="Trạng thái", default='moi')

    @api.onchange('phong_tro_id')
    def _onchange_phong_tro(self):
        if self.phong_tro_id:
            self.gia_thue = self.phong_tro_id.gia_thue

    # --- ĐÂY LÀ HÀM ROBOT ---
    @api.model
    def action_quet_hop_dong_het_han(self):
        _logger.info("========== ROBOT BẮT ĐẦU LÀM VIỆC ==========")
        today = fields.Date.today()
        
        # 1. Tìm các hợp đồng 'đang thuê' mà 'hết hạn'
        hop_dong_het_han = self.search([
            ('trang_thai', '=', 'dang_thue'),
            ('ngay_ket_thuc', '<', today)
        ])
        
        # 2. Xử lý từng hợp đồng
        for hd in hop_dong_het_han:
            # Đóng hợp đồng
            hd.trang_thai = 'da_ket_thuc'
            
            # Trả phòng về trống
            if hd.phong_tro_id:
                hd.phong_tro_id.tinh_trang = 'trong'
            
            _logger.info(f"ROBOT: Đã đóng hợp đồng {hd.name} và trả phòng {hd.phong_tro_id.name}")

# 4. HÓA ĐƠN
class HoaDon(models.Model):
    _name = 'quan_ly_nha_tro.hoa_don'
    _description = 'Hóa đơn tiền điện nước'

    name = fields.Char(string="Mã Hóa Đơn", default="Hóa đơn mới")
    hop_dong_id = fields.Many2one('quan_ly_nha_tro.hop_dong', string="Hợp Đồng", required=True)
    thang = fields.Selection([('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12')], string="Tháng")
    
    dien_cu = fields.Integer(string="Điện cũ")
    dien_moi = fields.Integer(string="Điện mới")
    nuoc_cu = fields.Integer(string="Nước cũ")
    nuoc_moi = fields.Integer(string="Nước mới")
    
    tong_tien = fields.Integer(compute='_tinh_tong', store=True)
    state = fields.Selection([('draft', 'Nháp'), ('confirm', 'Đã xác nhận'), ('paid', 'Đã thanh toán')], default='draft')

    @api.depends('dien_cu', 'dien_moi', 'nuoc_cu', 'nuoc_moi', 'hop_dong_id')
    def _tinh_tong(self):
        for r in self:
            tien_nha = r.hop_dong_id.gia_thue if r.hop_dong_id else 0
            tien_dien = (r.dien_moi - r.dien_cu) * 3500
            tien_nuoc = (r.nuoc_moi - r.nuoc_cu) * 10000
            r.tong_tien = tien_dien + tien_nuoc + tien_nha

    def action_confirm(self):
        for r in self: r.state = 'confirm'
    def action_done(self):
        for r in self: r.state = 'paid'
    def action_draft(self):
        for r in self: r.state = 'draft'