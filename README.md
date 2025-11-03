# Black-Scholes Covered Warrant Calculator

A Streamlit web application for calculating European call covered warrant prices using the Black-Scholes model.

## Features

- Clean, modern UI matching the provided design
- Black-Scholes pricing model with conversion ratio support
- Pre-configured with test values for demonstration

## Hardcoded Test Values

The application currently runs with the following hardcoded values:

- **Current Stock Price (S0)**: 25,500 VND
- **Exercise Price (K)**: 23,000 VND
- **Maturity Date**: 324 days
- **Risk-free Interest Rate (r)**: 6.5%
- **Volatility (σ)**: 50%
- **Conversion Ratio**: 2.0 (2:1)

## Installation

1. Make sure you have Python 3.8 or higher installed

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

To run the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## How It Works

The Black-Scholes model calculates the theoretical price of a European call option. This implementation adjusts for conversion ratios, which is important for covered warrants where multiple warrants may be needed to purchase one share.

### Formula

The Black-Scholes formula for a call option:

```
C = S₀ * N(d₁) - K * e^(-rT) * N(d₂)

where:
d₁ = [ln(S₀/K) + (r + σ²/2)T] / (σ√T)
d₂ = d₁ - σ√T
```

With conversion ratio adjustment:

- S₀_adjusted = S₀ / conversion_ratio
- K_adjusted = K / conversion_ratio

## Project Structure

```
black-scholes-calculator/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Dependencies

- **streamlit**: Web application framework
- **numpy**: Numerical computing
- **scipy**: Scientific computing (for statistical distributions)

## License

This project is for educational and testing purposes.
