def process_payment_token(token):
    # Missing input validation - vulnerability
    payment_data = decode_token(token)  # Line 3: No validation before processing
    return process_payment(payment_data)

def decode_token(raw_token):
    # Accepts any token format without sanitization
    return {'amount': raw_token.split('_')[1]}  # Line 7: Unsafe parsing
