import os
from pydantic_ai import Agent
from models import DocumentInsight

# Clear proxy settings to avoid conflicts
for proxy_var in ['http_proxy', 'https_proxy', 'HTTP_PROXY', 'HTTPS_PROXY', 'all_proxy', 'ALL_PROXY']:
    if proxy_var in os.environ:
        del os.environ[proxy_var]

def create_agent():
    """Create AI agent - called only when API key is available"""
    return Agent(
        'openai:gpt-4o-mini',  # Using mini for cost efficiency
        output_type=DocumentInsight,
        instructions="""
        You are an expert document analyzer. Analyze the provided document text and extract:
        1. Document type and main topic
        2. Key insights and important points
        3. Sentiment and urgency level
        4. Actionable items
        5. Potential risks or concerns
        
        Be thorough but concise. Focus on practical, actionable insights.
        """
    )

async def analyze_document(text_content: str) -> DocumentInsight:
    """Analyze document using Pydantic AI"""
    # Create agent fresh each time to ensure API key is loaded
    agent = create_agent()
    result = await agent.run(f"Please analyze this document:\n\n{text_content}")
    return result.output
