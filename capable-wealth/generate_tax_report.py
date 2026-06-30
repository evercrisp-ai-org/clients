#!/usr/bin/env python3
"""
Generate Tax Strategies Report

This script generates the full branded PDF report from the tax strategies
content JSON file using the Capable Wealth template system.

Usage:
    python generate_tax_report.py
    
Output:
    outputs/final/tax_strategies_report.pdf
"""

import sys
import os
import json
from pathlib import Path

# Add src to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.config import load_brand_config
from src.template_parser import TemplateParser
from src.renderers.pdf_renderer import PDFRenderer


def load_report_content(content_path: str) -> dict:
    """Load the report content JSON file."""
    with open(content_path, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    print("=" * 70)
    print("Capable Wealth - Tax Strategies Report Generator")
    print("=" * 70)
    
    # Paths
    project_root = Path(__file__).parent
    content_path = project_root / "examples" / "tax_strategies_report.json"
    templates_dir = project_root / "pdf-page-templates" / "lead_magnets" / "report"
    output_path = project_root / "outputs" / "drafts" / "tax_strategies_report_V6.pdf"
    
    # Step 1: Load brand configuration
    print("\n1. Loading brand configuration...")
    try:
        config = load_brand_config()
        print(f"   ✓ Brand: {config.brand_name}")
        print(f"   ✓ Primary color: {config.colors['primary'].hex}")
        print(f"   ✓ Heading font: {config.typography['heading'].family}")
    except Exception as e:
        print(f"   ✗ Error loading config: {e}")
        return 1
    
    # Step 2: Load report content
    print("\n2. Loading report content...")
    try:
        content = load_report_content(content_path)
        metadata = content.get("report_metadata", {})
        pages = content.get("pages", [])
        print(f"   ✓ Report: {metadata.get('title', 'Untitled')}")
        print(f"   ✓ Pages to generate: {len(pages)}")
    except FileNotFoundError:
        print(f"   ✗ Content file not found: {content_path}")
        return 1
    except json.JSONDecodeError as e:
        print(f"   ✗ Invalid JSON: {e}")
        return 1
    
    # Step 3: Initialize parser
    print("\n3. Initializing template parser...")
    try:
        parser = TemplateParser(brand_config=config, project_root=project_root)
        print("   ✓ Parser initialized")
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return 1
    
    # Step 4: Load and fill templates
    print("\n4. Loading and filling templates...")
    templates = []
    errors = []
    
    for i, page in enumerate(pages):
        template_name = page.get("template", "")
        page_content = page.get("content", {})
        page_num = i + 1
        
        # Add article_name and page_number if not present
        if "article_name" not in page_content:
            page_content["article_name"] = metadata.get("article_name", "Report")
        if "page_number" not in page_content:
            page_content["page_number"] = page_num
        
        template_path = templates_dir / f"{template_name}.json"
        
        try:
            # Load template
            template = parser.load_template(template_path)
            
            # Fill variables
            filled = parser.fill_variables(template, page_content)
            templates.append(filled)
            
            print(f"   ✓ Page {page_num}: {template_name}")
            
        except FileNotFoundError:
            error_msg = f"Template not found: {template_name}.json"
            errors.append((page_num, error_msg))
            print(f"   ✗ Page {page_num}: {error_msg}")
            
        except ValueError as e:
            error_msg = f"Missing variables: {e}"
            errors.append((page_num, error_msg))
            print(f"   ✗ Page {page_num}: {error_msg}")
            
        except Exception as e:
            error_msg = f"Error: {e}"
            errors.append((page_num, error_msg))
            print(f"   ✗ Page {page_num}: {error_msg}")
    
    if not templates:
        print("\n✗ No templates loaded successfully. Cannot render.")
        return 1
    
    print(f"\n   Summary: {len(templates)} pages loaded, {len(errors)} errors")
    
    # Step 5: Render PDF
    print(f"\n5. Rendering {len(templates)} pages to PDF...")
    try:
        renderer = PDFRenderer(brand_config=config, project_root=project_root)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        result = renderer.render_document(templates, output_path)
        print(f"   ✓ PDF saved to: {result}")
    except Exception as e:
        print(f"   ✗ Render error: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    # Done
    print("\n" + "=" * 70)
    print("GENERATION COMPLETE!")
    print(f"Report: {metadata.get('title', 'Report')}")
    print(f"Pages: {len(templates)}")
    print(f"Output: {output_path.absolute()}")
    print("=" * 70)
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
