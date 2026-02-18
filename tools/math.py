# =============================================================
# tools/math.py — Semua tools kategori Math
# =============================================================

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

        out = str(int(result)) if result == int(result) else str(round(result, 10))
        return {'success': True, 'result': out}

    except (ValueError, TypeError) as e:
        return {'success': False, 'error': f'Input tidak valid: {e}'}


# Tambah handler math berikutnya di sini ↓
# def handle_bmi(data): ...


# =============================================================
registry = {

    'calculator': {
        'name'       : '🧮 Kalkulator',
        'category'   : 'Math',
        'description': 'Operasi matematika dasar',
        'handler'    : handle_calculator,
    },

    # 'bmi': {
    #     'name'       : '⚖️ BMI Calculator',
    #     'category'   : 'Math',
    #     'description': 'Hitung Body Mass Index',
    #     'handler'    : handle_bmi,
    # },

      }
