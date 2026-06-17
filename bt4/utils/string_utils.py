def calculate_average(scores: list) -> None:
    """
    Tính toán điểm trung bình từ danh sách điểm.
    Bẫy lỗi dữ liệu không phải số (Bẫy 3) và danh sách rỗng (Bẫy 2).
    """
    if not scores:
        return 0.0
        
    valid_scores = []
    for score in scores:
        if isinstance(score, (int, float)):
            valid_scores.append(score)
            
    if not valid_scores:
        return 0.0
        
    return sum(valid_scores) / len(valid_scores)


def classify_student(average: float) -> str:
    """
    Phân loại học lực sinh viên dựa trên điểm số trung bình.
    """
    if average >= 8.0:
        return "Giỏi"
    elif average >= 6.5:
        return "Khá"
    elif average >= 5.0:
        return "Trung bình"
    else:
        return "Yếu"