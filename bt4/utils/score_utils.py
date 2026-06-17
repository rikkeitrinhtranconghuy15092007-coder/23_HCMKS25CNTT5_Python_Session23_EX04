def normalize_student_names(records: list) -> None:
    """
    Chức năng 2: Chuẩn hóa chuỗi họ tên của toàn bộ sinh viên trong danh sách.
    Xử lý khoảng trắng thừa và viết hoa chữ cái đầu. Bẫy dữ liệu danh sách rỗng (Bẫy 1).
    """
    print("\n--- CHUẨN HÓA TÊN SINH VIÊN ---")
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    for student in records:
        raw_name = student.get("name", "")
        # Tách từ loại bỏ khoảng trắng thừa bất kể vị trí, viết hoa chữ cái đầu từng từ
        clean_name = " ".join(raw_name.split()).title()
        student["name"] = clean_name
        print(f"{student['student_id']}: {clean_name}")
        
    print(">> Đã chuẩn hóa toàn bộ tên sinh viên.")