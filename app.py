import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📈 Math Visualization App")

st.write("Select a function to visualize:")

# Dropdown to select mathematical function
option = st.selectbox("Choose a function:", ["Sine Wave", "Cosine Wave", "Quadratic Function"])

# Generate x values
x = np.linspace(-10, 10, 400)
fig, ax = plt.subplots()

# Plot based on selection
if option == "Sine Wave":
    ax.plot(x, np.sin(x), label="sin(x)", color='blue')
elif option == "Cosine Wave":
    ax.plot(x, np.cos(x), label="cos(x)", color='red')
elif option == "Quadratic Function":
    ax.plot(x, x**2, label="x²", color='green')

ax.legend()
ax.grid()
st.pyplot(fig)
