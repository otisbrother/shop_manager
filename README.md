# Simple Shop Manager

Quản lý cửa hàng đơn giản bằng Python (OOP + JSON + CLI)

## Mô tả
- Ứng dụng quản lý sản phẩm cho cửa hàng nhỏ, sử dụng Python.
- Lưu trữ dữ liệu sản phẩm bằng file JSON.
- Giao diện dòng lệnh (CLI) dễ sử dụng.

## Tính năng
- Thêm sản phẩm (Create)
- Hiển thị danh sách sản phẩm (Read)
- Cập nhật thông tin sản phẩm (Update)
- Xoá sản phẩm (Delete)
- Lưu dữ liệu vào file `data/products.json`

## Cấu trúc thư mục
```
shop_manager/
├── models/
│   └── product.py
├── services/
│   └── product_service.py
├── data/
│   └── products.json
├── main.py
├── requirements.txt
└── README.md
```

## Hướng dẫn sử dụng
1. Cài Python 3.x
2. Mở terminal/cmd, di chuyển vào thư mục `shop_manager`
3. Chạy chương trình:
   ```bash
   python main.py
   ```
4. Làm theo hướng dẫn trên màn hình để thêm, xem, sửa, xoá sản phẩm.

## Ghi chú
- Dữ liệu sản phẩm sẽ được lưu tự động vào file `data/products.json`.
- Không cần cài thêm thư viện ngoài.

---
Tác giả: Nguyễn Huy Tỏa
