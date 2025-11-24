# Utility functions for the application

def generate_payment_qr(bank_code, account_number, account_name, amount, order_id):
    """
    Tạo URL QR code thanh toán VietQR
    
    Args:
        bank_code: Mã ngân hàng (VCB, TCB, MB, ACB...)
        account_number: Số tài khoản
        account_name: Tên chủ tài khoản
        amount: Số tiền
        order_id: Mã đơn hàng
    
    Returns:
        URL của QR code thanh toán
    """
    # Sử dụng API VietQR miễn phí
    # Format: https://img.vietqr.io/image/{BANK_CODE}-{ACCOUNT_NUMBER}-compact2.png
    qr_url = f"https://img.vietqr.io/image/{bank_code}-{account_number}-compact2.png"
    
    # Thêm parameters
    qr_url += f"?amount={int(amount)}"
    qr_url += f"&addInfo=DH{order_id}"  # Nội dung chuyển khoản
    qr_url += f"&accountName={account_name}"
    
    return qr_url


# Danh sách các ngân hàng phổ biến tại Việt Nam
BANK_CODES = {
    'VCB': 'Vietcombank',
    'TCB': 'Techcombank',
    'MB': 'MB Bank',
    'ACB': 'ACB',
    'VPB': 'VPBank',
    'TPB': 'TPBank',
    'VIB': 'VIB',
    'SHB': 'SHB',
    'BIDV': 'BIDV',
    'AGR': 'Agribank',
    'SCB': 'Sacombank',
    'OCB': 'OCB',
    'MSB': 'MSBank',
    'CTG': 'VietinBank',
    'HDBank': 'HDBank',
    'SeABank': 'SeABank',
    'LPB': 'LienVietPostBank',
    'CAKE': 'CAKE by VPBank',
    'Ubank': 'Ubank by VPBank',
    'Timo': 'Timo',
}
