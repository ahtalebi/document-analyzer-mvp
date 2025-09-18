import streamlit as st
import asyncio
import os
from document_processor import process_uploaded_file
from agents import analyze_document

# Load environment variables from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # dotenv not installed, skip

def configure_page():
    """Configure Streamlit page"""
    st.set_page_config(
        page_title="Smart Document Analyzer",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded"
    )

def setup_sidebar():
    """Setup sidebar with instructions"""
    with st.sidebar:
        # Instructions
        st.subheader("📋 How to Use")
        st.markdown("""
        1. Upload a document or paste text
        2. Click 'Analyze Document'
        3. View AI-powered insights
        """)
        
        st.markdown("---")
        st.markdown("**Supported formats:**")
        st.markdown("• PDF files")
        st.markdown("• Images (PNG, JPG)")
        st.markdown("• Text files")
        st.markdown("• Direct text input")
        
        st.markdown("---")
        st.markdown("**Sample Documents to Try:**")
        st.markdown("• Business emails")
        st.markdown("• Contracts or agreements")
        st.markdown("• News articles")
        st.markdown("• Reports or summaries")
        
        # Check if API key is available from environment
        api_key_available = bool(os.getenv("OPENAI_API_KEY"))
        if api_key_available:
            st.success("✅ AI Analysis Ready!")
        else:
            st.error("❌ AI Analysis Unavailable")
        
        return api_key_available

def render_upload_section():
    """Render file upload section"""
    st.header("📁 Upload Document")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose a file",
        type=['pdf', 'txt', 'png', 'jpg', 'jpeg'],
        help="Upload PDF, text, or image files"
    )
    
    # Text input alternative
    st.markdown("**Or paste text directly:**")
    direct_text = st.text_area(
        "Paste your document text here",
        height=200,
        placeholder="Paste any text you want analyzed...",
        help="You can paste emails, articles, contracts, etc."
    )
    
    return uploaded_file, direct_text

def render_analysis_results(analysis):
    """Render analysis results in organized format"""
    if not analysis:
        return
    
    st.success("🎉 Analysis Complete!")
    
    # Header with document type
    st.subheader(f"📋 {analysis.document_type}")
    st.markdown(f"**Main Topic:** {analysis.main_topic}")
    
    # Create tabs for better organization
    tab1, tab2, tab3 = st.tabs(["📝 Summary & Insights", "📊 Metrics", "⚠️ Risks & Actions"])
    
    with tab1:
        # Summary
        st.markdown("### 📝 Summary")
        st.info(analysis.summary)
        
        # Key points
        st.markdown("### 🎯 Key Points")
        for i, point in enumerate(analysis.key_points, 1):
            st.markdown(f"**{i}.** {point}")
    
    with tab2:
        # Metrics in columns
        col1, col2 = st.columns(2)
        
        with col1:
            sentiment_color = {
                "positive": "green",
                "negative": "red", 
                "neutral": "blue"
            }.get(analysis.sentiment.lower(), "gray")
            
            st.markdown(f"### 😊 Sentiment")
            st.markdown(f"<h2 style='color: {sentiment_color}'>{analysis.sentiment.title()}</h2>", 
                       unsafe_allow_html=True)
        
        with col2:
            urgency_color = "red" if analysis.urgency_level >= 7 else "orange" if analysis.urgency_level >= 4 else "green"
            st.markdown(f"### 🚨 Urgency Level")
            st.markdown(f"<h2 style='color: {urgency_color}'>{analysis.urgency_level}/10</h2>", 
                       unsafe_allow_html=True)
    
    with tab3:
        # Action items
        if analysis.action_items:
            st.markdown("### ✅ Action Items")
            for i, item in enumerate(analysis.action_items, 1):
                st.markdown(f"**{i}.** {item}")
        else:
            st.info("No specific action items identified.")
        
        st.markdown("---")
        
        # Risks
        if analysis.potential_risks:
            st.markdown("### ⚠️ Potential Risks")
            for i, risk in enumerate(analysis.potential_risks, 1):
                st.warning(f"**{i}.** {risk}")
        else:
            st.success("No significant risks identified.")

def main():
    """Main application function"""
    configure_page()
    
    # Header
    st.title("📄 Smart Document Analyzer")
    st.markdown("**Powered by Pydantic AI** - Upload any document and get AI-powered insights!")
    
    # Setup sidebar and get API key status
    api_key_configured = setup_sidebar()
    
    # Main content layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file, direct_text = render_upload_section()
        
        # Analyze button
        analyze_button = st.button(
            "🔍 Analyze Document", 
            type="primary",
            use_container_width=True
        )
    
    with col2:
        st.header("📊 Analysis Results")
        
        if analyze_button:
            if not api_key_configured:
                st.error("🚨 AI Analysis is currently unavailable. Please check back later.")
                return
            
            # Get text content
            text_content = ""
            
            if uploaded_file:
                with st.spinner("📄 Extracting text from file..."):
                    text_content = process_uploaded_file(uploaded_file)
            elif direct_text.strip():
                text_content = direct_text.strip()
            
            if text_content and len(text_content.strip()) > 10:
                with st.spinner("🤖 Analyzing document with AI..."):
                    try:
                        # Run async analysis
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                        
                        analysis = loop.run_until_complete(analyze_document(text_content))
                        render_analysis_results(analysis)
                        
                    except Exception as e:
                        st.error(f"❌ Error during analysis: {str(e)}")
                    finally:
                        loop.close()
            else:
                st.warning("⚠️ Please upload a file or paste some text to analyze (minimum 10 characters)")
    
    # Footer
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center'>"
        "Built with <a href='https://github.com/pydantic/pydantic-ai'>Pydantic AI</a> • "
        "Deploy on <a href='https://streamlit.io/cloud'>Streamlit Cloud</a> for free!"
        "</div>", 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
