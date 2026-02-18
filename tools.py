# =============================================================
# tools.py — Registry semua tools
#
# Cara tambah tool baru:
#   1. Buat handler function di bawah
#   2. Daftarkan ke tools_registry
#   3. Buat file templates/tools/<id>.html
# =============================================================


# ── HANDLERS ─────────────────────────────────────────────────

def handle_calculator(data):
    """Kalkulator dasar: +  -  *  /"""
    try:
        num1 = float(data.get('num1', 0))
        num2 = float(data.get('num2', 0))
        op   = data.get('operator', '+')

        if   op == '+': result = num1 + num2
        elif op == '-': result = num1 - num2
        elif op == '*': result = num1 * num2
        elif op == '/':
            if num2 == 0:
                return {'success': False, 'error': 'Tidak bisa dibagi dengan 0!'}
            result = num1 / num2
        else:
            return {'success': False, 'error': 'Operator tidak valid'}

        # Tampilkan sebagai integer kalau tidak ada desimal
        out = str(int(result)) if result == int(result) else str(round(result, 10))
        return {'success': True, 'result': out}

    except (ValueError, TypeError) as e:
        return {'success': False, 'error': f'Input tidak valid: {e}'}


# ── REGISTRY ─────────────────────────────────────────────────

tools_registry = {

    # ── Math ──────────────────────────────────────────────────
    'calculator': {
        'name'       : '🧮 Kalkulator',
        'category'   : 'Math',
        'description': 'Operasi matematika dasar',
        'handler'    : handle_calculator,
    },

    # Tambah tool berikutnya di sini ↓
    # 'bmi': {
    #     'name'       : '⚖️ BMI Calculator',
    #     'category'   : 'Health',
    #     'description': 'Hitung Body Mass Index',
    #     'handler'    : handle_bmi,
    # },

}
