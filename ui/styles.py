"""CSS Styles Module"""
from config.theme import PROFESSIONAL_COLORS, FONT_FAMILY


def get_custom_css():
    """Return custom CSS styles"""
    return f"""
        /* Import Professional Font */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Custom CSS for enhanced styling */
        .dashboard-header {{
            background: linear-gradient(135deg, {PROFESSIONAL_COLORS['primary']} 0%, {PROFESSIONAL_COLORS['secondary']} 100%);
            color: white;
            padding: 30px;
            border-radius: 15px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            font-family: {FONT_FAMILY};
        }}
        
        .dashboard-header h1 {{
            margin-bottom: 10px;
            font-size: 2.5rem;
            font-weight: 700;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}
        
        .dashboard-header p {{
            font-size: 1.2rem;
            opacity: 0.9;
        }}
        
        .card {{
            border: none;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.1);
            margin-bottom: 25px;
            overflow: hidden;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            font-family: {FONT_FAMILY};
        }}
        
        .card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        }}
        
        .card-header {{
            background: linear-gradient(135deg, {PROFESSIONAL_COLORS['secondary']} 0%, {PROFESSIONAL_COLORS['primary']} 100%);
            color: white;
            font-weight: 600;
            font-size: 1.1rem;
            padding: 20px;
            border: none;
        }}
        
        .card-body {{
            padding: 25px;
        }}
        
        .nav-tabs {{
            border-bottom: 3px solid {PROFESSIONAL_COLORS['neutral2']};
            margin-bottom: 25px;
        }}
        
        .nav-tabs .nav-link {{
            border: none;
            border-radius: 10px 10px 0 0;
            color: {PROFESSIONAL_COLORS['neutral1']};
            font-weight: 600;
            padding: 15px 25px;
            margin-right: 5px;
            transition: all 0.3s ease;
            font-family: {FONT_FAMILY};
        }}
        
        .nav-tabs .nav-link:hover {{
            background: linear-gradient(135deg, {PROFESSIONAL_COLORS['background']} 0%, {PROFESSIONAL_COLORS['neutral2']} 100%);
            color: {PROFESSIONAL_COLORS['primary']};
            transform: translateY(-2px);
        }}
        
        .nav-tabs .nav-link.active {{
            background: linear-gradient(135deg, {PROFESSIONAL_COLORS['primary']} 0%, {PROFESSIONAL_COLORS['secondary']} 100%);
            color: white;
            border: none;
        }}
        
        .metric-card {{
            background: white;
            padding: 25px;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 20px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            border-left: 5px solid {PROFESSIONAL_COLORS['accent1']};
            transition: all 0.3s ease;
            font-family: {FONT_FAMILY};
        }}
        
        .metric-card:hover {{
            transform: translateY(-3px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.12);
        }}
        
        .metric-value {{
            font-size: 2rem;
            font-weight: 700;
            color: {PROFESSIONAL_COLORS['primary']};
            margin-bottom: 5px;
        }}
        
        .metric-label {{
            color: {PROFESSIONAL_COLORS['neutral1']};
            font-size: 0.9rem;
            font-weight: 500;
        }}
        
        .plot-container {{
            background: white;
            border-radius: 15px;
            padding: 20px;
            min-height: 550px;
        }}
        
        .error-message {{
            background: #f8d7da;
            color: #721c24;
            padding: 15px;
            border-radius: 10px;
            margin: 20px;
            border-left: 5px solid {PROFESSIONAL_COLORS['accent3']};
            font-family: {FONT_FAMILY};
        }}
        
        .stats-container {{
            background: {PROFESSIONAL_COLORS['background']};
            border-radius: 15px;
            padding: 25px;
            font-family: 'Courier New', monospace;
            border-left: 5px solid {PROFESSIONAL_COLORS['success']};
        }}
        
        .table {{
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            font-family: {FONT_FAMILY};
        }}
        
        .table thead th {{
            background: linear-gradient(135deg, {PROFESSIONAL_COLORS['primary']} 0%, {PROFESSIONAL_COLORS['neutral1']} 100%);
            color: white;
            border: none;
            font-weight: 600;
        }}
        
        .table tbody tr:hover {{
            background: rgba({PROFESSIONAL_COLORS['accent1'][1:3]}, {PROFESSIONAL_COLORS['accent1'][3:5]}, {PROFESSIONAL_COLORS['accent1'][5:7]}, 0.1);
        }}
        
        /* About Page Styling */
        .about-section {{
            background: white;
            border-radius: 15px;
            padding: 30px;
            margin-bottom: 25px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            border-left: 5px solid {PROFESSIONAL_COLORS['accent1']};
        }}
        
        .about-section h3 {{
            color: {PROFESSIONAL_COLORS['secondary']};
            margin-bottom: 20px;
            font-weight: 600;
            font-family: {FONT_FAMILY};
        }}
        
        .about-section h4 {{
            color: {PROFESSIONAL_COLORS['secondary']};
            margin-top: 25px;
            margin-bottom: 15px;
            font-weight: 500;
            font-family: {FONT_FAMILY};
        }}
        
        .about-section ul {{
            margin-left: 20px;
            line-height: 1.8;
        }}
        
        .about-section li {{
            margin-bottom: 8px;
        }}
        
        .about-section p {{
            font-family: {FONT_FAMILY};
            line-height: 1.6;
        }}
        
        .highlight-box {{
            background: linear-gradient(135deg, {PROFESSIONAL_COLORS['background']} 0%, #e9ecef 100%);
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            border-left: 4px solid {PROFESSIONAL_COLORS['accent2']};
        }}
        
        /* Markdown content styling */
        .markdown-content {{
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            font-family: {FONT_FAMILY};
            line-height: 1.6;
        }}
        
        .markdown-content h1, .markdown-content h2, .markdown-content h3, .markdown-content h4 {{
            color: {PROFESSIONAL_COLORS['secondary']};
            margin-top: 1.5em;
            margin-bottom: 0.8em;
            font-family: {FONT_FAMILY};
        }}
        
        .markdown-content h1 {{
            border-bottom: 3px solid {PROFESSIONAL_COLORS['accent1']};
            padding-bottom: 10px;
        }}
        
        .markdown-content h2 {{
            border-bottom: 2px solid {PROFESSIONAL_COLORS['neutral2']};
            padding-bottom: 8px;
        }}
        
        .markdown-content ul, .markdown-content ol {{
            margin-left: 25px;
            margin-bottom: 1em;
        }}
        
        .markdown-content li {{
            margin-bottom: 0.5em;
        }}
        
        .markdown-content strong {{
            color: {PROFESSIONAL_COLORS['accent3']};
        }}
        
        .markdown-content blockquote {{
            background: {PROFESSIONAL_COLORS['background']};
            border-left: 4px solid {PROFESSIONAL_COLORS['accent2']};
            margin: 1em 0;
            padding: 15px 20px;
            border-radius: 5px;
        }}
        """
