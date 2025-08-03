# ----------- FULL FILE: source_manager.py (ULTRA ELITE PRICE ENGINE) -----------
import os
import json
import time
import random

# Simulated APIs — in real build, use requests or aiohttp
from utils.sources.coingecko import get_price_from_coingecko
from utils.sources.binance import get_price_from_binance
from utils.sources.uniswap import get_price_from_uniswap
from utils.sources.chainlink import get_price_from_chainlink

SCORE_LOG = "logs/price_source_scores.json"
CACHE_FILE = "logs/prices/price_cache.json"

class SourceManager:
    def __init__(self):
        self.sources = [
            ("coingecko", get_price_from_coingecko),
            ("binance", get_price_from_binance),
            ("uniswap", get_price_from_uniswap),
            ("chainlink", get_price_from_chainlink),
        ]
        self.scores = {src[0]: 1.0 for src in self.sources}
        self.cache = {}
        self.load_cache()

    def load_cache(self):
        if os.path.exists(CACHE_FILE):
            with open(CACHE_FILE, "r") as f:
                self.cache = json.load(f)

    def save_cache(self):
        os.makedirs(os.path.dirname(CACHE_FILE), exist_ok=True)
        with open(CACHE_FILE, "w") as f:
            json.dump(self.cache, f, indent=2)

    def get_best_source(self):
        return sorted(self.sources, key=lambda s: -self.scores[s[0]])

    def get_price(self, token):
        if token in self.cache and time.time() - self.cache[token]["timestamp"] < 60:
            return self.cache[token]["price"]

        for name, fn in self.get_best_source():
            try:
                price = fn(token)
                if price:
                    self.cache[token] = {"price": price, "timestamp": time.time()}
                    self.scores[name] += 0.05  # reward
                    self.save_cache()
                    return price
            except:
                self.scores[name] -= 0.1  # penalty
                continue

        raise ValueError(f"❌ All sources failed for {token}")

    def run_test(self):
        print("📡 Testing SourceManager...")
        test_token = "ETH"
        try:
            price = self.get_price(test_token)
            print(f"✅ Best price for {test_token}: ${price:.2f}")
        except Exception as e:
            print(str(e))

if __name__ == "__main__":
    manager = SourceManager()
    manager.run_test()

def get_live_price(token):
    return SourceManager().get_price(token)
