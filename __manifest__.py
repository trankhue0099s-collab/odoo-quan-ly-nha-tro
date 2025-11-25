{
    'name': "Hệ thống Quản lý Nhà trọ",
    'summary': "Phần mềm quản lý thuê phòng",
    'description': "Module giúp quản lý nhà trọ, điện nước",
    'author': "Ten Cua Ban",
    'category': 'Real Estate',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'sequence.xml',
        'data/cron.xml',
        'views/views.xml',
        'reports/hop_dong_report.xml',
    ],
    'application': True,
}