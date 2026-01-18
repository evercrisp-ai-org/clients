#!/usr/bin/env python3
"""
Test script to verify the Capable Wealth template system works.
Generates a sample 3-page report PDF.
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.config import load_brand_config
from src.template_parser import TemplateParser
from src.renderers.pdf_renderer import PDFRenderer

def main():
    print("=" * 60)
    print("Capable Wealth Template System - Test Render")
    print("=" * 60)
    
    # Step 1: Load brand config
    print("\n1. Loading brand configuration...")
    try:
        config = load_brand_config()
        print(f"   ✓ Brand: {config.brand_name}")
        print(f"   ✓ Version: {config.version}")
        print(f"   ✓ Primary color: {config.colors['primary'].hex}")
        print(f"   ✓ Heading font: {config.typography['heading'].family}")
    except Exception as e:
        print(f"   ✗ Error loading config: {e}")
        return
    
    # Step 2: Initialize parser
    print("\n2. Initializing template parser...")
    try:
        parser = TemplateParser(brand_config=config)
        print("   ✓ Parser initialized")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return
    
    # Step 3: Load templates
    print("\n3. Loading and filling templates...")
    templates = []
    
    # Cover page
    try:
        cover = parser.load_template("templates/lead_magnets/report/cover_dark.json")
        cover_filled = parser.fill_variables(cover, {
            "title": "Hidden Tax Strategies",
            "subtitle": "for Orthopedic Surgeons",
            "date": "January 2026"
        })
        templates.append(cover_filled)
        print("   ✓ Cover page loaded")
    except Exception as e:
        print(f"   ✗ Cover page error: {e}")
    
    # Key findings page
    try:
        findings = parser.load_template("templates/lead_magnets/report/quote_key_findings.json")
        findings_filled = parser.fill_variables(findings, {
            "quote_text": "78% of surgeons underestimate tax impact",
            "findings_header": "Key Findings",
            "findings": [
                {"label": "Tax Planning", "summary": "reduces liability by 40%"},
                {"label": "Asset Protection", "summary": "shields 70% of wealth"},
                {"label": "Succession Timing", "summary": "optimal 5-7 year window"}
            ],
            "article_name": "Tax Strategies Report",
            "page_number": 2
        })
        templates.append(findings_filled)
        print("   ✓ Key findings page loaded")
    except Exception as e:
        print(f"   ✗ Key findings error: {e}")
    
    # Chart page
    try:
        chart = parser.load_template("templates/lead_magnets/report/chart_line.json")
        chart_filled = parser.fill_variables(chart, {
            "section_header": "Practice Value Over Time",
            "section_subheader": "How planning affects outcomes",
            "exhibit_number": 1,
            "chart_title": "Net Proceeds by Planning Window",
            "chart_data": {
                "labels": ["No Plan", "1 Year", "3 Years", "5 Years"],
                "series": [{"name": "Net %", "values": [58, 67, 78, 88]}]
            },
            "footnote": "Based on 127 practice transitions",
            "citation": "Source: Capable Wealth, 2024",
            "article_name": "Tax Strategies Report",
            "page_number": 3
        })
        templates.append(chart_filled)
        print("   ✓ Chart page loaded")
    except Exception as e:
        print(f"   ✗ Chart page error: {e}")
    
    if not templates:
        print("\n✗ No templates loaded successfully. Cannot render.")
        return
    
    # Step 4: Render PDF
    print(f"\n4. Rendering {len(templates)} pages to PDF...")
    try:
        renderer = PDFRenderer(brand_config=config)
        output_path = "outputs/drafts/test_report.pdf"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        result = renderer.render_document(templates, output_path)
        print(f"   ✓ PDF saved to: {result}")
    except Exception as e:
        print(f"   ✗ Render error: {e}")
        import traceback
        traceback.print_exc()
        return
    
    print("\n" + "=" * 60)
    print("TEST COMPLETE!")
    print(f"Open the PDF at: {os.path.abspath(output_path)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
