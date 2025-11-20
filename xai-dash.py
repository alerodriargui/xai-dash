import streamlit as st
import matplotlib.pyplot as plt

# -------------------------------------------------
# Datos de ejemplo
# -------------------------------------------------
example = {
    "customer_id": "CUST_001",
    "monthly_charges": 75.0,          # relativamente alto
    "tenure": 3,                       # poco tiempo con la compañía
    "total_charges": 220.0,            # bajo, consistente con tenure
    "internet_service": "80 hours",    # consumo medio
    "contract": "Month-to-Month",      # contrato corto → más riesgo
    "payment_method": "Credit Card",
    "prediction": 0.78,                # 78% de riesgo de churn, coherente con perfil
    "positive": {
        "Month-to-Month Contract": 0.2,   
        "High Monthly Charges": 0.25,     
        "Support Tickets": 0.4
    },
    "negative": {
        "Tenure": -0.10,   # disminuye riesgo un poco
        "Late Payments": -0.08,
        "Premium Services": -0.05
    },
    "support_tickets_last_3mo": 5,
    "premium_services": 0,
    "late_payments": 0,
    "last_support_contact_days": 10,
    "num_products": 1
}


# -------------------------------------------------
# Layout principal
# -------------------------------------------------
st.set_page_config(page_title="XAI-Dashboard", layout="wide")
st.title("📊 XAI Dashboard – Customer Churn")

# Columnas principales
col1, col2 = st.columns([1, 1.5])

# -------------------------------------------------
# Panel izquierdo: info del cliente
# -------------------------------------------------
with col1:
    st.subheader("Customer Information")

    # Expander para compactar info
    with st.expander("Show customer details", expanded=True):
        left_cols = st.columns([1, 1])
        left_cols[0].markdown(f"<span style='font-size:18px'><b>Customer ID:</b> {example['customer_id']}</span>", unsafe_allow_html=True)
        left_cols[1].markdown(f"<span style='font-size:18px'><b>Monthly Charges:</b> {example['monthly_charges']} €</span>", unsafe_allow_html=True)

        left_cols = st.columns([1,1])
        left_cols[0].markdown(f"<span style='font-size:18px'><b>Tenure:</b> {example['tenure']} months</span>", unsafe_allow_html=True)
        left_cols[1].markdown(f"<span style='font-size:18px'><b>Total Charges:</b> {example['total_charges']} €</span>", unsafe_allow_html=True)

        left_cols = st.columns([1,1])
        left_cols[0].markdown(f"<span style='font-size:18px'><b>Avg. Monthly Usage:</b> {example['internet_service']}</span>", unsafe_allow_html=True)
        left_cols[1].markdown(f"<span style='font-size:18px'><b>Contract:</b> {example['contract']}</span>", unsafe_allow_html=True)

        left_cols = st.columns([1,1])
        left_cols[0].markdown(f"<span style='font-size:18px'><b>Payment Method:</b> {example['payment_method']}</span>", unsafe_allow_html=True)
        left_cols[1].markdown(f"<span style='font-size:18px'><b>Support Tickets:</b> {example['support_tickets_last_3mo']}</span>", unsafe_allow_html=True)

        left_cols = st.columns([1,1])
        left_cols[0].markdown(f"<span style='font-size:18px'><b>Premium Services:</b> {example['premium_services']}</span>", unsafe_allow_html=True)
        left_cols[1].markdown(f"<span style='font-size:18px'><b>Late Payments:</b> {example['late_payments']}</span>", unsafe_allow_html=True)

        left_cols = st.columns([1,1])
        left_cols[0].markdown(f"<span style='font-size:18px'><b>Last Support Contact:</b> {example['last_support_contact_days']} days ago</span>", unsafe_allow_html=True)
        left_cols[1].markdown(f"<span style='font-size:18px'><b>Number of Products:</b> {example['num_products']}</span>", unsafe_allow_html=True)

    st.subheader("Churn Risk")
    st.markdown(f"<h2 style='color:#b71c1c'>{int(example['prediction']*100)}%</h2>", unsafe_allow_html=True)

    st.markdown("<span style='font-size:18px'><b>Decision:</b> Should we offer a retention bonus?</span>", unsafe_allow_html=True)

    # Botones en la misma línea y más grandes
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        go = st.button("✅ GO", use_container_width=True)
    with btn_col2:
        no_go = st.button("❌ NO-GO", use_container_width=True)

    if go:
        st.success("Decision: GO")
    elif no_go:
        st.error("Decision: NO-GO")


# -------------------------------------------------
# Panel derecho: explicación
# -------------------------------------------------
with col2:
    with st.expander("Explain Prediction", expanded=False):
        labels = list(example['positive'].keys()) + list(example['negative'].keys())
        values = list(example['positive'].values()) + list(example['negative'].values())
        colors = ["green"]*len(example['positive']) + ["red"]*len(example['negative'])

        fig, ax = plt.subplots(figsize=(6,4))
        ax.barh(labels, values, color=colors)
        ax.set_xlabel("Impact")
        ax.set_ylabel("Factors")
        ax.set_title("Top Factors Influencing Prediction")
        plt.tight_layout()
        st.pyplot(fig)
