
    # Danh sách để lưu các công việc
tasks = []

def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")

def delete_task(task_index):
    """Xóa một công việc khỏi danh sách theo chỉ số."""
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"Đã xóa công việc: '{removed}'")
    else:
        print("Chỉ số công việc không hợp lệ!")

# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học hỏi Git và GitHub")