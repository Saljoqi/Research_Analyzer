import streamlit as st
from main import run_research_assistant

st.set_page_config(
    page_title="AI Research Hub",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    /* Global App Background Gradient */
    .stApp {
        background: linear-gradient(180deg, #020617 0%, #0f172a 100%);
        color: #f1f5f9;
    }

    /* Sidebar Glassmorphism */
    [data-testid="stSidebar"] {
        background-color: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(12px);
        border-right: 1px solid rgba(0, 212, 255, 0.2);
    }

    /* Title and Header Color Fix */
    h1, h2, h3, .stMarkdown p {
        color: #f1f5f9 !important;
    }

    /* Fancy Card Styling for Results (Summary & Answer) */
    div.stSuccess, div.stInfo, div.stAlert {
        background-color: #1e293b !important;
        border: 1px solid #00d4ff !important;
        border-radius: 15px !important;
        box-shadow: 0 4px 15px rgba(0, 212, 255, 0.2);
        color: #f1f5f9 !important;
        padding: 20px !important;
    }

    /* Button Styling & Hover Animation */
    .stButton>button {
        background: linear-gradient(90deg, #00d4ff 0%, #0081ff 100%);
        color: white !important;
        border: none;
        border-radius: 12px;
        font-weight: 600;
        height: 3em;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 4px 10px rgba(0, 212, 255, 0.3);
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0, 212, 255, 0.5);
    }

    /* Source Container Borders */
    [data-testid="stVerticalBlock"] > div > div > div[data-testid="stContainer"] {
        background-color: rgba(15, 23, 42, 0.8);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 15px;
        transition: all 0.3s;
    }
    
    [data-testid="stVerticalBlock"] > div > div > div[data-testid="stContainer"]:hover {
        border-color: #00d4ff;
        background-color: #1e293b;
    }
    
    /* Horizontal Rule Color */
    hr {
        border-color: rgba(0, 212, 255, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🔬 AI Research Analyzer")
st.caption("Empowered by Llama3 & arXiv - Precision Research at your fingertips")
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=80)
    st.header("Search Parameters")
    
    topic = st.text_input(
        "Research Topic", 
        value="LoRA fine-tuning efficiency",
        help="General area of research (e.g., Quantum Computing, LLMs)"
    )
    
    question = st.text_area(
        "Specific Question", 
        value="How much VRAM does LoRA save compared to full fine-tuning?",
        help="What specific detail are you looking for?"
    )
    
    analyze_btn = st.button("🚀 Start Deep Research", type="primary", use_container_width=True)

if analyze_btn:
    try:
        # Professional status updates
        with st.status("🔍 Analyzing the 'Needle in the Haystack'...", expanded=True) as status:
            st.write("📡 Connecting to arXiv API...")
            
            # This calls the function you modified in main.py
            summary, answer, sources = run_research_assistant(topic, question)
            
            status.update(label="Analysis Complete!", state="complete", expanded=False)

        # Main Layout for Results
        col1, col2 = st.columns([1, 1], gap="medium")

        with col1:
            st.subheader("📝 Executive Summary")
            st.success(summary)

        with col2:
            st.subheader("💡 Detailed Answer")
            st.info(answer)

        # --- SOURCES SECTION ---
        st.divider()
        st.subheader("🔗 Verified Source Proof")
        
        # Display sources as clickable cards in a 3-column grid
        if sources:
            source_cols = st.columns(3)
            for i, src in enumerate(sources):
                with source_cols[i % 3]:
                    with st.container(border=True):
                        st.markdown(f"**{src['title']}**")
                        st.caption(f"📄 Found on Page {src['page']}")
                        st.link_button("View Original PDF", src['url'], use_container_width=True)
        else:
            st.warning("No specific source links were extracted for this answer.")

    except Exception as e:
        st.error(f"An error occurred during analysis: {e}")

else:
    st.info("👋 Welcome! Enter a topic and question in the sidebar to begin your research.")
    st.markdown("""
    <div style="text-align: center; opacity: 0.5; margin-top: 100px;">
        <p>Built for Deep Scholarly Analysis</p>
    </div>
    """, unsafe_allow_html=True)