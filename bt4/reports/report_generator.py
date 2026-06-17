from datetime import datetime
import colorama as col

# Sử dụng import chỉ định rõ hàm từ package utils nội bộ (Kiểu import 2)
from utils.score_utils import calculate_average, classify_student

# Khởi tạo thư viện colorama tự động reset màu sau mỗi dòng in
col.init(autoreset=True)

def display_student_scores(records: list) -> None:
    """
    Chức năng 1: Hiển thị danh sách điểm số kèm điểm trung bình và xếp loại.
    Bẫy dữ liệu danh sách rỗng (Bẫy 1).
    """
    print("\n--- DANH SÁCH ĐIỂM SINH VIÊN ---")
    if not records:
        print("Hệ thống chưa có dữ liệu sinh viên.")
        return

    for index, student in enumerate(records, start=1):
        scores = student.get("scores", [])
        avg_score = calculate_average(scores)
        classification = classify_student(avg_score)
        
        # Định dạng canh lề chuỗi tên để hiển thị ngay ngắn trên terminal
        padded_name = f"{student['name']:<15}"
        print(f"{index}. [{student['student_id']}] {padded_name} | Điểm: {scores} | ĐTB: {avg_score:.2f} - {classification}")
    print("-" * 33)


def export_learning_report(records: list) -> None:
    """
    Chức năng 4: Phân tích số liệu và xuất tệp tin văn bản learning_report.txt.
    Sử dụng thư viện ngoại colorama để thông báo thành công có màu sắc trực quan.
    """
    print("\n--- XUẤT BÁO CÁO HỌC TẬP ---")
    if not records:
        # Sử dụng mã màu đỏ của Colorama để in cảnh báo lỗi dữ liệu rỗng
        print(col.Fore.RED + "Hệ thống chưa có dữ liệu sinh viên.")
        return

    total_students = len(records)
    pass_count = 0
    improve_count = 0

    for student in records:
        avg = calculate_average(student.get("scores", []))
        if avg >= 5.0:
            pass_count += 1
        else:
            improve_count += 1

    print(f"Tổng số sinh viên: {total_students}")
    print(f"Số sinh viên đạt yêu cầu: {pass_count}")
    print(f"Số sinh viên cần cải thiện: {improve_count}")

    # Thực hiện tác vụ I/O ghi tệp tin vật lý xuống đĩa cứng
    filename = "learning_report.txt"
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write("=========================================\n")
        file.write("        BÁO CÁO KẾT QUẢ HỌC TẬP         \n")
        file.write(f"Thời gian khởi tạo: {current_time}\n")
        file.write("=========================================\n")
        file.write(f"Tổng số sinh viên phân tích: {total_students}\n")
        file.write(f"Số sinh viên đạt yêu cầu (ĐTB >= 5.0): {pass_count}\n")
        file.write(f"Số sinh viên cần cải thiện (ĐTB < 5.0): {improve_count}\n")
        file.write("-----------------------------------------\n")
        file.write("Trạng thái hệ thống: Hoàn tất trích xuất dữ liệu.\n")

    # In thông báo chữ màu XANH LÁ (Fore.GREEN) khẳng định tác vụ hoàn thành
    print(col.Fore.GREEN + f">> Đã xuất báo cáo ra file {filename}")