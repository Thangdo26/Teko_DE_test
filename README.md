                                                                                                                                                   # Teko_DE_test
# Đoạn script này sẽ tạo (hoặc ghi đè) file readme.md với nội dung hướng dẫn

readme_content = """
# Hướng Dẫn Chạy Code

## 1. SQL

### Mục đích
Chạy các truy vấn SQL để lấy giao dịch đầu tiên của mỗi khách hàng từ bảng `Transactions`.

### Yêu Cầu
- Một hệ quản trị CSDL (VD: MySQL, PostgreSQL, SQL Server, …).
- Công cụ quản trị SQL (SQL client hoặc command line).

### Các Bước Thực Hiện
1. **Tạo bảng và chèn dữ liệu mẫu**  
   Sử dụng file SQL dưới đây để tạo bảng và chèn dữ liệu mẫu:
   ```sql
   CREATE TABLE Transactions (
       TransactionID INT,
       CustomerID INT,
       TransactionAmount DECIMAL(10,2),
       TransactionDate DATE
   );

   INSERT INTO Transactions (TransactionID, CustomerID, TransactionAmount, TransactionDate)
   VALUES
   (1, 100, 50.00, '2023-01-01'),
   (2, 100, 70.00, '2023-01-05'),
   (3, 101, 20.00, '2023-01-03'),
   (4, 102, 100.00, '2023-01-05'),
   (5, 102, 150.00, '2023-01-04');
