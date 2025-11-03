import streamlit as st
import numpy as np
from scipy.stats import norm

def black_scholes_call_warrant(S0, K, T, r, sigma, conversion_ratio=1.0):
    """
    Price a European call covered warrant using Black-Scholes model, accounting for conversion ratio.
    
    Parameters:
    - S0: Current price of the underlying asset (e.g., HPG stock price)
    - K: Strike price of the warrant
    - T: Time to maturity in years
    - r: Risk-free interest rate (annualized)
    - sigma: Annualized volatility of the underlying asset
    - conversion_ratio: Number of warrants needed to buy 1 share (default 1.0 for 1:1)
    
    Returns:
    - Warrant price
    """
    call_price = 0

    # Avoid FloatDivisionError
    if S0 and K != 0:  
        # Adjust for conversion ratio
        S0_adjusted = S0 / conversion_ratio
        K_adjusted = K / conversion_ratio
    
        # Black-Scholes formula
        d1 = (np.log(S0_adjusted / K_adjusted) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        call_price = S0_adjusted * norm.cdf(d1) - K_adjusted * np.exp(-r * T) * norm.cdf(d2)
    
        return call_price
    return call_price

st.markdown("""
    <style>
    
    [data-testid="stAppViewContainer"] {
        background-color: #f0f2f6;
        color: black; 
    }

    div[data-testid="stHorizontalBlock"] {
        background-color: white;
        border-radius: 8px;
        padding: 10px 15px;
        display: flex;
        flex-direction: row;
        flex-wrap: nowrap;
        align-items: center;
    }
    
    div[data-testid="stHorizontalBlock"] > div:first-child {
        flex: 1 1 auto;
        min-width: 120px;
    }
    
    div[data-testid="stHorizontalBlock"] > div:last-child {
        flex: 0 1 auto;
        min-width: 150px;
        max-width: 250px;
    }
    
    .stNumberInput {
        width: 100%;
    }
    
    .stNumberInput input {
        border: none ;
        border-radius: 0 ;
        padding: 8px 12px;
        background-color: white;
        color: black;
        font-size: 15px;
        width: 100%;
    }
    
    .stNumberInput input:focus {
        outline: none ;
    }
    
    /* Hide +/- buttons */
    .stNumberInput button {
        display: none ;
    }
    
    /* Result container */
    .result-container {
        background-color: white;
        border-radius: 8px;
        padding: 25px;
        text-align: center;
    }
    
    .result-value {
        font-size: 28px;
        font-weight: 700;
    }
    
    /* Mobile */
    @media (max-width: 640px) {
        div[data-testid="stHorizontalBlock"] {
            padding: 10px 15px;
        }
        
        div[data-testid="stHorizontalBlock"] > div:first-child {
            min-width: 100px;
            font-size: 13px;
        }
        
        div[data-testid="stHorizontalBlock"] > div:last-child {
            min-width: 100px;
            max-width: 180px;
        }
        
        .stNumberInput input {
            padding: 4px 6px;
            font-size: 13px;
        }
        
        .stNumberInput button {
            padding: 4px 6px;
            font-size: 13px;
        }

        .result-container {
            background-color: white;
            border-radius: 6px;
            padding: 8px;
            text-align: center;
        }
    
        .result-value {
            font-size: 18px;
            font-weight: 600;
        }
    }
    
    </style>
""", unsafe_allow_html=True)

# UI
st.markdown("## Black-Scholes Calculator") 

# S0
with st.container():
    col1, col2 = st.columns([2.5, 1.5])
    with col1:
        st.markdown("**Current Stock Price (VND)**")
    with col2:
        S0 = st.number_input("S0", min_value=0.0, value=None, step=100.0, format="%.2f", placeholder="Please enter content", label_visibility="collapsed")

# K
with st.container():
    col1, col2 = st.columns([2.5, 1.5])
    with col1:
        st.markdown("**Exercise Price (VND)**")
    with col2:
        K = st.number_input("K", min_value=0.0, value=None, step=100.0, format="%.2f", placeholder="Please enter content", label_visibility="collapsed")

# T
with st.container():
    col1, col2 = st.columns([2.5, 1.5])
    with col1:
        st.markdown("**Maturity date (days)**")
    with col2:
        maturity_days = st.number_input("maturity", min_value=1, value=None, step=1, format="%d", placeholder="Please enter content", label_visibility="collapsed")

# R
with st.container():
    col1, col2 = st.columns([2.5, 1.5])
    with col1:
        st.markdown("**Risk-free interest rate (%)**")
    with col2:
        r_input = st.number_input("r", min_value=0.0, value=None, max_value=100.0, step=0.1, format="%.2f", placeholder="Please enter content", label_visibility="collapsed")
        r = r_input / 100 if r_input is not None else 0.0

# sigma
with st.container():
    col1, col2 = st.columns([2.5, 1.5])
    with col1:
        st.markdown("**Volatility (%)**")
    with col2:
        sigma_input = st.number_input("sigma", min_value=0.0, value=None, max_value=200.0, step=1.0, format="%.2f", placeholder="Please enter content", label_visibility="collapsed")
        sigma = sigma_input / 100 if sigma_input is not None else 0.0

# conversion_ratio
with st.container():
    col1, col2 = st.columns([2.5, 1.5])
    with col1:
        st.markdown("**Conversion ratio (n:1)**")
    with col2:
        conversion_ratio = st.number_input("ratio", min_value=0.1, value=None, step=0.1, format="%g", placeholder="Please enter content", label_visibility="collapsed")
        
# Convert days to years & Calculate warrant price
T = maturity_days / 365 if maturity_days else 0
price = black_scholes_call_warrant(S0 if S0 else 0, K if K else 0, T, r, sigma, conversion_ratio if conversion_ratio else 1.0)

# Display result
st.markdown(f"""
    <div class="result-container">
        <div class="result-label">Covered Warrant (Call) Price</div>
        <div class="result-value">{price:,.2f} VND</div>
    </div>
""", unsafe_allow_html=True)

# Terminal testing
print(f"Covered Warrant (Call) Price: {price:.2f} VND")

# # Assumptions (based on your HPG data sample):
# S0 =  25500.00  # Current HPG close price 
# K = 23000  # Strike price
# T = 324/365       # 324 days to expiration
# r = 0.065      # Risk-free rate 
# sigma = 0.5  # Volatility
# conversion_ratio = 2.0  

# # return Delta of the warrant

# price = black_scholes_call_warrant(S0, K, T, r, sigma, conversion_ratio)
# print(f"Covered Warrant (Call) Price: {price:.2f} VND")