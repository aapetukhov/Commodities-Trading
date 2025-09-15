from decimal import Decimal

def calculate_sigma_zone(self, last_window_values: list[float], sigma_low: int, sigma_high: int):
    N = Decimal(len(last_window_values))
    weights = [Decimal(i + 1) for i in range(len(last_window_values))]
    total_weight = sum(weights)
    wma_sum = Decimal('0.0')
    for price, weight in zip(last_window_values, weights):
        price_decimal = Decimal(str(price))
        wma_sum += price_decimal * weight
    wma = wma_sum / total_weight
    sma_sum = sum(Decimal(str(price)) for price in last_window_values)
    sma = sma_sum / N
    A = Decimal('4.0') * sma - Decimal('3.0') * wma
    B = Decimal('3.0') * wma - Decimal('2.0') * sma
    m = (A - B / (N - Decimal('1.0')))
    SSE = sum((Decimal(str(price)) - B - m * Decimal(N - Decimal(i))) ** Decimal('2') for i, price in enumerate(last_window_values))
    rmse = (SSE / (N - Decimal('1.0'))) ** Decimal('0.5')
    center = B
    low_sigma = Decimal(str(sigma_low))
    high_sigma = Decimal(str(sigma_high))
    upper_band_low_sigma = float(center + rmse * low_sigma)
    lower_band_low_sigma = float(center - rmse * low_sigma)
    upper_band_high_sigma = float(center + rmse * high_sigma)
    lower_band_high_sigma = float(center - rmse * high_sigma)
    return float(center), float(rmse), float(upper_band_low_sigma), float(lower_band_low_sigma), float(upper_band_high_sigma), float(lower_band_high_sigma)