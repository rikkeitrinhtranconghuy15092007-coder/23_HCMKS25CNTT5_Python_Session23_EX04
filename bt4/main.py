# Nạp tập dữ liệu thô ban đầu từ module data
from data.students import student_records

# Nạp các hàm xử lý từ các module thuộc các package khác nhau
from utils.random_utils import generate_assignment_code
from utils.string_utils import normalize_student_names
import reports.report_generator as report

def main():
    while True:
        print("\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====")
        print("1. Xem danh sách sinh viên và điểm trung bình")
        print("2. Chuẩn hóa tên sinh viên")
        print("3. Sinh mã bài tập ngẫu nhiên")
        print("4. Xuất báo cáo học tập")
        print("5. Thoát chương trình")
        print("====================================================")
        
        user_input = input("Chọn chức năng (1-5): ").strip()
        
        # Bẫy 4 — Ngăn chặn ký tự lạ hoặc chữ cái (ValueError) gây sập chương trình chính
        try:
            choice = int(user_input)
        except ValueError:
            print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")
            continue
            
        if choice == 1:
            report.display_student_scores(student_records)
        elif choice == 2:
            normalize_student_names(student_records)
        elif choice == 3:
            code = generate_assignment_code()
            print("\n--- SINH MÃ BÀI TẬP ---")
            print(f"Mã bài tập của bạn là: {code}")
        elif choice == 4:
            report.export_learning_report(student_records)
        elif choice == 5:
            print("Cảm ơn bạn đã sử dụng hệ thống!")
            break
        else:
            print("Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.")

if __name__ == "__main__":
    main()