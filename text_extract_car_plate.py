import re


def extract_car_plates(raw_car_plates):

    raw_car_plates_join = "".join(raw_car_plates)

    filter_pattern = "[\{\}\[\]\/?.,;:|\)*~`!^\-_+<>@\#$%&\\\=\(\'\"]"

    filtered_text = re.sub(filter_pattern, '', raw_car_plates_join)

    car_plate_pattern = r"\d{2,3}[ㄱ-힣]\d{4}"

    match = re.findall(car_plate_pattern, filtered_text)

    return match
