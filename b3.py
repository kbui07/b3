raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print("===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")
    choice = input("Nhập lựa chọn (1-4): ").strip()

    match choice:
        case "1":
            print(raw_data)

        case "2":
            employees = raw_data.split("|")
            print("BÁO CÁO NHÂN SỰ")
            for employee in employees:
                data = employee.split(";")
                employee_id = data[0].strip().upper()
                full_name = data[1].strip().title()
                phone = data[2].strip().replace("-", "")
                department = data[3].strip().upper()

                if phone.isdigit():
                    phone = "******" + phone[-4:]
                else:
                    phone = "Invalid Format"
                print("ID:", employee_id, "| Họ tên:", full_name, "| Điện thoại:", phone, "| Phòng ban:", department)

        case "3":
            search_id = input("Nhập mã nhân viên: ").strip().upper()
            employees = raw_data.split("|")
            found = False
            for employee in employees:
                data = employee.split(";")
                employee_id = data[0].strip().upper()
                if employee_id == search_id:
                    full_name = data[1].strip().title()
                    phone = data[2].strip().replace("-", "")
                    department = data[3].strip().upper()

                    if phone.isdigit():
                        phone = "******" + phone[-4:]
                    else:
                        phone = "Invalid Format"

                    print("ID:", employee_id)
                    print("Họ tên:", full_name)
                    print("Điện thoại:", phone)
                    print("Phòng ban:", department)
                    found = True
                    break
            if not found:
                print("Không tìm thấy nhân viên")

        case "4":
            print("Thoát chương trình")
            break

        case _:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại!")