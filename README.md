# 🏠 HỆ THỐNG QUẢN LÝ NHÀ TRỌ (ODOO 17)

## 📌 Giới thiệu
Đây là Module Odoo giúp giải quyết bài toán quản lý thuê phòng trọ, căn hộ dịch vụ. Hệ thống giúp chủ nhà trọ tự động hóa quy trình tính tiền, quản lý hợp đồng và theo dõi doanh thu.

## 🚀 Tính năng nổi bật

### 1. Quản lý Phòng & Hiện trạng (Kanban View)
- Giao diện thẻ bài trực quan: **Xanh (Trống)** - **Đỏ (Đang thuê)**.
- Theo dõi giá thuê, diện tích, thiết bị từng phòng.

### 2. Tự động hóa Hợp đồng (Smart Automation)
- **Robot (Cron Job):** Tự động quét các hợp đồng hết hạn mỗi ngày để đóng hợp đồng và trả phòng về trạng thái trống.
- **Smart Button:** Tra cứu nhanh lịch sử thuê phòng của từng khách hàng.
- **In ấn:** Xuất Hợp đồng thuê nhà ra file PDF chuẩn mẫu quy định.

### 3. Tính tiền Điện Nước tự động
- Chỉ cần nhập chỉ số Điện/Nước (Mới - Cũ).
- Hệ thống tự động nhân giá và cộng tiền phòng để ra Tổng hóa đơn.

### 4. Báo cáo & Thống kê
- **Biểu đồ (Graph View):** So sánh doanh thu theo từng tháng.
- **Bộ lọc thông minh:** Lọc nhanh các hóa đơn chưa thanh toán, các phòng đang trống.

## 🛠 Công nghệ sử dụng
- **Core:** Python, Odoo 17 Framework.
- **Database:** PostgreSQL.
- **Interface:** XML, QWeb Reports.
- **Version Control:** Git & GitHub.

---
*Developed by Tran Hoang Anh Khue*