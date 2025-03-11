# Teko_DE_test

# Hướng Dẫn Chạy Code

## I. SQL

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
2. **Chạy file query.sql**

### II. Python Script - Trích Xuất Thông Tin Bảng Từ File SQL

### Mục đích
- Đọc file SQL có chứa nhiều câu lệnh.
- Trích xuất các bảng **input** (từ `FROM`, `JOIN`) và **output** (`CREATE TABLE`, `INSERT INTO`).
- Xuất kết quả ra file YAML.

### Yêu Cầu
- Python 3.x
- PostgreSQL đã được cài đặt và chạy trên máy.
- Thư viện Python: `pyyaml`, `psycopg2`, `sqlparse`.

### Hướng Dẫn Chạy

1. **Cài đặt thư viện**  
   ```bash
   pip install pyyaml psycopg2 sqlparse
   
2. **Tạo file input.sql**
   ```sql
   CREATE TABLE sales_data AS
   SELECT * FROM raw_data.transactions
   JOIN customer_info ON transactions.customer_id = customer_info.id;
3. **Chạy script python**
   ```python
   python parse_sql.py
4. **Kiểm tra kết quả trong file tables.yaml**
