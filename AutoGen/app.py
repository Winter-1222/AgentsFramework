import streamlit as st
import requests
from datetime import datetime

# 设置页面标题和图标
st.set_page_config(page_title="Bitcoin Price Tracker", page_icon="💰")

# 定义 API URL
API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_24hr_change=true"

# 获取比特币价格数据
def get_bitcoin_price():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching Bitcoin price: {e}")
        return None

# 主函数
def main():
    st.title("Bitcoin Price Tracker")
    st.write("Check the current Bitcoin price and its 24-hour change.")

    # 添加加载状态
    with st.spinner("Fetching Bitcoin price..."):
        data = get_bitcoin_price()

    if data:
        bitcoin_data = data['bitcoin']
        current_price = bitcoin_data['usd']
        price_change_24h = bitcoin_data['usd_24h_change']
        price_change_24h_abs = round(current_price * (price_change_24h / 100), 2)

        # 显示比特币价格
        st.header("Current Bitcoin Price (USD)")
        st.subheader(f"${current_price:.2f}")

        # 显示24小时价格变化
        st.header("24-Hour Price Change")
        if price_change_24h > 0:
            st.subheader(f"↑ {price_change_24h:.2f}% (${price_change_24h_abs:.2f})")
        else:
            st.subheader(f"↓ {abs(price_change_24h):.2f}% (${abs(price_change_24h_abs):.2f})")    

        # 刷新按钮
        if st.button("Refresh"):
            st.rerun()

if __name__ == "__main__":
    main()