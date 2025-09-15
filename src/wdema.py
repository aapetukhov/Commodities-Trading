def _calculate_wdema(self, prices: list[float]) -> float:
        """Calculate Weighted Double Exponential Moving Average на основе минутных цен"""
        if not prices:
            return 0.0
        
        n = len(prices)
        alpha = 2.0 / (n + 1)
        
        # First EMA
        ema1 = prices[0]
        for price in prices[1:]:
            ema1 = alpha * price + (1 - alpha) * ema1
        
        # Second EMA (EMA of EMA)
        ema2 = ema1
        ema1_values = [prices[0]]
        temp_ema1 = prices[0]
        for price in prices[1:]:
            temp_ema1 = alpha * price + (1 - alpha) * temp_ema1
            ema1_values.append(temp_ema1)
        
        ema2 = ema1_values[0]
        for ema1_val in ema1_values[1:]:
            ema2 = alpha * ema1_val + (1 - alpha) * ema2
        
        # WDEMA = 2 * EMA1 - EMA2
        wdema = 2 * ema1 - ema2
        return wdema