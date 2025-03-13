def cs_standardize(feature):
    return f'math_division(math_subtraction({feature}, horizontal_mu({feature})), horizontal_mu({feature}))'

def standardize(feature, n):
    return f'math_division(math_subtraction({feature}, rolling_mu({feature},{n})), rolling_mu({feature},{n}))'

def add(f1, f2):
    return f'math_addition({f1},{f2})'

def sub(f1, f2):
    return f'math_subtraction({f1},{f2})'

def mul(f1, f2):
    return f'math_multiplication({f1},{f2})'

def div(f1, f2):
    return f'math_division({f1},{f2})'

def rev(f1):
    return f'math_multiply_negative_one({f1})'

def rank(f1):
    return f'horizontal_order({f1})'

def ts_rank(f1, n):
    return f'rolling_order({f1},{n})'

def zscore(f1):
    return f'horizontal_standard_score({f1})'

def ts_zscore(f1, n):
    return f'rolling_standard_zscore({f1},{n})'

def kurtosis(f1):
    return f'horizontal_kurtosis({f1})'

def ts_kurtosis(f1, n):
    return f'rolling_kurtosis({f1},{n})'

def skewness(f1):
    return f'horizontal_skewness({f1})'

def ts_skewness(f1, n):
    return f'rolling_skewness({f1},{n})'

def ts_cokurtosis(f1, f2, n):
    return f'rolling_cokurtosis({f1}, {f2}, {n})'

def ts_coskewness(f1, f2, n):
    return f'rolling_coskewness({f1}, {f2}, {n})'

def pct_change(f1,n):
    return f'rolling_pct_change({f1},{n})'

def pct_change_mean(f1,n):
    return f'rolling_pct_change_mu({f1},{n})'

def clip(f1,lower_bound=0.01,upper_bound=0.99):
    return f'math_clip_extremes({f1}, lower_bound={lower_bound}, upper_bound = {upper_bound})'

def ts_correlation(f1, f2, m):
    return f'rolling_correlation({f1}, {f2}, {m})'
 