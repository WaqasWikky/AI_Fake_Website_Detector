import streamlit as st
import joblib
import pandas as pd
from src.url_features import extract_features

# ==============================
# Configuration
# ==============================
MODEL_PATH = "models/xgb_phish.pkl"

# ✅ Full feature list from training phase
TRAINING_FEATURES = [
    'length_url', 'length_hostname', 'ip', 'nb_dots', 'nb_hyphens', 'nb_at', 'nb_qm', 'nb_and', 'nb_or',
    'nb_eq', 'nb_underscore', 'nb_tilde', 'nb_percent', 'nb_slash', 'nb_star', 'nb_colon', 'nb_comma',
    'nb_semicolumn', 'nb_dollar', 'nb_space', 'nb_www', 'nb_com', 'nb_dslash', 'http_in_path', 'https_token',
    'ratio_digits_url', 'ratio_digits_host', 'punycode', 'port', 'tld_in_path', 'tld_in_subdomain',
    'abnormal_subdomain', 'nb_subdomains', 'prefix_suffix', 'random_domain', 'shortening_service',
    'path_extension', 'nb_redirection', 'nb_external_redirection', 'length_words_raw', 'char_repeat',
    'shortest_words_raw', 'shortest_word_host', 'shortest_word_path', 'longest_words_raw', 'longest_word_host',
    'longest_word_path', 'avg_words_raw', 'avg_word_host', 'avg_word_path', 'phish_hints', 'domain_in_brand',
    'brand_in_subdomain', 'brand_in_path', 'suspecious_tld', 'statistical_report', 'nb_hyperlinks',
    'ratio_intHyperlinks', 'ratio_extHyperlinks', 'ratio_nullHyperlinks', 'nb_extCSS', 'ratio_intRedirection',
    'ratio_extRedirection', 'ratio_intErrors', 'ratio_extErrors', 'login_form', 'external_favicon',
    'links_in_tags', 'submit_email', 'ratio_intMedia', 'ratio_extMedia', 'sfh', 'iframe', 'popup_window',
    'safe_anchor', 'onmouseover', 'right_clic', 'empty_title', 'domain_in_title', 'domain_with_copyright',
    'whois_registered_domain', 'domain_registration_length', 'domain_age', 'web_traffic', 'dns_record',
    'google_index', 'page_rank'
]

# ==============================
# Load model
# ==============================
@st.cache_resource
def load_model():
    try:
        model = joblib.load(MODEL_PATH)
        st.success("✅ Model loaded successfully!")
        return model
    except Exception as e:
        st.error(f"❌ Failed to load model: {e}")
        return None

model = load_model()

# ==============================
# Streamlit UI
# ==============================
st.set_page_config(page_title="AI Fake Website Detector", page_icon="🕵️‍♂️", layout="centered")
st.title("🕵️‍♂️ AI Fake Website Detector")
st.markdown("### Detect phishing or fake websites using AI & URL feature analysis")
st.divider()

# ==============================
# User Input
# ==============================
url_input = st.text_input("🔗 Enter Website URL:", placeholder="https://example.com")

if st.button("🔍 Detect"):
    if not url_input.strip():
        st.warning("⚠️ Please enter a URL first.")
    else:
        with st.spinner("Extracting features..."):
            features_dict = extract_features(url_input)

            if not features_dict:
                st.error("⚠️ Failed to extract features. Please check the URL.")
            else:
                df_features = pd.DataFrame([features_dict])

                # ✅ Align features safely with the model
                for col in TRAINING_FEATURES:
                    if col not in df_features.columns:
                        df_features[col] = 0
                df_features = df_features[TRAINING_FEATURES]

                with st.spinner("Analyzing with AI model..."):
                    try:
                        prediction = model.predict(df_features)[0]
                        proba = model.predict_proba(df_features)[0][prediction]
                    except Exception as e:
                        st.error(f"Model prediction failed: {e}")
                        st.stop()

                # ✅ Display result
                if prediction == 1:
                    st.error(f"🚨 **Phishing/Fake Website Detected!** (Confidence: {proba*100:.2f}%)")
                else:
                    st.success(f"✅ **Legitimate Website** (Confidence: {proba*100:.2f}%)")

st.divider()
st.caption("Developed by **Waqas** — Cybersecurity + AI Project")
