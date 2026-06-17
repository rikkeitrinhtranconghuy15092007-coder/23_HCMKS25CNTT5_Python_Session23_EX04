import random
import string

def generate_assignment_code():
    """
    Chức năng 3: Sinh ngẫu nhiên mã bài tập theo cấu trúc PY-[4 ký tự chữ hoa/số]
    Sử dụng thư viện chuẩn random và string của Python.
    """
    # Tạo pool chứa chữ cái viết hoa và chữ số từ 0-9
    character_pool = string.ascii_uppercase + string.digits
    # Chọn ngẫu nhiên 4 phần tử có lặp lại
    random_chars = random.choices(character_pool, k=4)
    suffix_code = "".join(random_chars)
    return f"PY-{suffix_code}"