"""
SUB HEADERS
TODO: change to en
"""
factory_medical_supplies = [
    # 口罩
    ('普通医用口罩', 'YY/T 0969-2013'),
    ('医用外科口罩', 'YY 0469-2010'),
    ('医用防护口罩 | N95口罩', 'GB 19083-2010, 建议3M 1860/1870/9123,防飞沫血液体液款'),
    # 面罩
    ('防冲击眼罩/护目镜/防护眼镜', 'GB 19083-2010, 建议3M 1860/1870/9123,防飞沫血液体液款'),
    ('防护面罩', 'GB 19083-2010, 建议3M 1860/1870/9123,防飞沫血液体液款'),
    ('防护帽/医用帽/圆帽', 'GB 19083-2010, 建议3M 1860/1870/9123,防飞沫血液体液款'),
    # 衣物
    ('隔离衣', ''),
    ('防护服', 'GB 19082-2003'),
    ('手术衣', ''),
    # 手套
    ('乳胶手套', '灭菌，GB 10213-2006'),
    # 鞋
    ('长筒胶鞋/防污染靴', ),
    ('防污染鞋套', ),
    ('防污染靴套', ),
    # 消毒耗材
    ('84消毒液', ),
    ('过氧乙酸', ),
    ('75%酒精', ),
    ('手部皮肤消毒液', ),
    ('活力碘', ),
    # 其它耗材
    ('床罩', ),
    ('医用面罩式雾化器', ),
    ('测体温设备', ),
    ('空气消毒设备', ),
    ('医用紫外线消毒车', )
]

"""
CSV HEADERS
"""
DONATION_HEADERS = [
    'donate_sorce',
    'donate_way',
    'donate_link',
    'donate_account_info',
    'donate_cur_status',
    'donate_audit_status',
    'donate_audit_person'
]
FACTORY_HEADERS = [
    'factory_prov',
    'factory_name',
    factory_medical_supplies,
    'factory_qualification',
    'factory_addr',
    'factory_contact',
    'factory_note',
    'factory_link',
    'factory_audit_status',
    'factory_reviewer'
]
CLINIC_HEADERS = [
    'clinic_unit',
    'clinic_contact',
    'clinic_note'
]
HOTEL_HEADERS = [
    'hotel_name',
    'hotel_prov',
    'hotel_addr',
    'hotel_room_num',
    'hotel_acceptable_num',
    'hotel_supplier',
    'hotel_concat_person',
    'hotel_concat_phone',
    'hotel_note',
    'hotel_link',
    'hotel_audit_status',
    'hotel_audit_person'
]
LOGISTICS_HEADERS = [
    'logistics_name',
    'logistics_area',
    'logistics_power',
    'logistics_link',
    'logistics_contact'
]
NEWS_HEADERS = [
    'news_title',
    'news_summary',
    'news_time',
    'news_link'
]
HOSPITAL_HEADERS = [
    'hospital_prov',
    'hospital_name',
    factory_medical_supplies,
    'hospital_link',
    'hospital_addr',
    'hospital_contact',
    'hospital_note',
    'hospital_audit_status',
    'hospital_audit_person'
]
