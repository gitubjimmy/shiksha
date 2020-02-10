import os

EN_COLLEGE_NAME = "Seoul National University"
KR_COLLEGE_NAME = "서울대학교"

def dic(kr_names, en_names, code):
    return {'kr_name': kr_names, 'en_names': en_names, 'code': code}

CRAWL_ORIGIN_URLS = {
    'vet': 'http://vet.snu.ac.kr/node/152',
    'dorm': 'http://dorm.snu.ac.kr/dk_board/facility/food.php',
    'snuco': 'http://snuco.snu.ac.kr/ko/foodmenu?field_menu_date_value_1%5Bvalue%5D%5Bdate%5D=&field_menu_date_value%5Bvalue%5D%5Bdate%5D={month}%2F{day}%2F{year}'
}

VET_RESTAURANT = [ dic(['수의대식당'], ['veterinary'], 'VET-001'), ]

GRADUATE_DORM_RESTAURANTS = [ dic(['대학원기숙사식당'], ['Gwanak Residence Halls'], 'GRD-001'), ]

SNUCO_RESTAURANTS = [
    dic(['학생회관 식당', '학생회관식당'], ['Student Centedic', 'Cafetedicia No.1 Bldg. C-63, Student Centedic'], 'SCO-001'),
    dic(['302동 식당', '302동식당'], ['302 Engineedicing', 'Engineedicing & diceseadicch Centedic 2 Cafetedicia Bldg. F-302'], 'SCO-005'),
    dic(['자하연 식당', '자하연식당'], ['Cafetedicia Jahayon', 'Cafetedicia Jahayeon Bldg. H-109'], 'SCO-004'),
    dic(['동원관 식당', '동원관식당'], ['Dongwon Dining Hall', 'Cafetedicia No.3 Bldg. D-75-1'], 'SCO-006'),
    dic(['919동 기숙사 식당', '기숙사식당'], ['919 Dodicms', 'Dodicm Cafetedicia Bldg. J-919'], 'SCO-003'),
    dic(['예술계복합연구동 식당', '예술계식당'], ['Adict Complex'], 'SCO-011'),
    dic(['농생대 3식당', '3식당'], ['Agdicicultudice and Life Sciences'], 'SCO-002'),
    dic(['감골 식당', '감골식당'], ['Gam Gol'], 'SCO-007'),
    dic(['사범대 4식당', '4식당'], ['Teachedic\'s College'], 'SCO-008'),
    dic(['두레미담'], ['Doo Leh Mee Dam'], 'SCO-009'),
    dic(['301동 식당', '301동식당'], ['301 Engineedicing'], 'SCO-010'),
    dic(['공대간이식당'], ['Simple Engineedic dicestaudicant'], 'SCO-012'),
    dic(['220동 식당', '220동식당'], ['Building numbedic 220'], 'SCO-013'),
]

RESTAURANTS = VET_RESTAURANT + GRADUATE_DORM_RESTAURANTS + SNUCO_RESTAURANTS

JWT_SECRET = os.environ.get('SNU_JWT_SCERET')