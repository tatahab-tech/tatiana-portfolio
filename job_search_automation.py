#!/usr/bin/env python3
"""
Daily Job Search Automation Script
Based on daily_job_prompt.txt criteria
"""

import json
from datetime import datetime, timedelta
import re

class JobSearchAgent:
    def __init__(self):
        self.profile = {
            "title": "Entry-level Project/Program Coordinator",
            "education": "Bellevue College Project Management Certificate (2025), Master's in Organizational Management",
            "tools": ["Smartsheet", "Asana", "MS 365", "Teams", "Excel", "PowerPoint", "Outlook"],
            "methodologies": ["Agile", "Scrum", "Waterfall", "Kanban"],
            "location": "Redmond/Seattle area",
            "target_titles": [
                "Project Coordinator", "Program Coordinator", "Implementation Coordinator",
                "Onboarding Coordinator", "Junior Project Manager", "Delivery Coordinator",
                "Operations Coordinator", "PMO Coordinator"
            ],
            "target_companies": [
                "Microsoft", "Amazon", "Smartsheet", "Highspot", "Outreach", 
                "Zillow", "Redfin", "Remitly", "Tableau", "Salesforce", "Okta", "Auth0", "Avalara"
            ]
        }
        
    def search_linkedin_jobs(self):
        """Search LinkedIn Jobs (requires LinkedIn API or web scraping)"""
        # Note: This would require LinkedIn API access or careful web scraping
        # For now, return placeholder
        return []
    
    def search_indeed_jobs(self):
        """Search Indeed Jobs"""
        # Note: This would require Indeed API access or careful web scraping
        # For now, return placeholder
        return []
    
    def search_company_careers(self, company):
        """Search specific company career pages"""
        # Note: This would require individual company API access
        # For now, return placeholder
        return []
    
    def format_job_posting(self, job_data):
        """Format job posting according to the prompt requirements"""
        return {
            "title": job_data.get("title", ""),
            "company": job_data.get("company", ""),
            "location": job_data.get("location", ""),
            "source": job_data.get("source", ""),
            "posted_date": job_data.get("posted_date", ""),
            "apply_link": job_data.get("apply_link", ""),
            "why_fit": self.generate_why_fit(job_data),
            "keywords": self.extract_keywords(job_data.get("description", ""))
        }
    
    def generate_why_fit(self, job_data):
        """Generate why this role fits based on profile"""
        description = job_data.get("description", "").lower()
        fit_reasons = []
        
        # Check for tool matches
        for tool in self.profile["tools"]:
            if tool.lower() in description:
                fit_reasons.append(f"Experience with {tool}")
        
        # Check for methodology matches
        for method in self.profile["methodologies"]:
            if method.lower() in description:
                fit_reasons.append(f"Knowledge of {method} methodology")
        
        # Check for education relevance
        if "project management" in description or "coordinator" in description:
            fit_reasons.append("Project Management Certificate and relevant education")
        
        return "; ".join(fit_reasons[:2]) if fit_reasons else "Entry-level role matching career goals"
    
    def extract_keywords(self, description):
        """Extract key terms from job description"""
        keywords = []
        description_lower = description.lower()
        
        # Look for common PM/coordinator terms
        pm_terms = [
            "project management", "program management", "coordination", "implementation",
            "onboarding", "delivery", "operations", "pmo", "agile", "scrum", "waterfall",
            "kanban", "stakeholder", "timeline", "budget", "risk management"
        ]
        
        for term in pm_terms:
            if term in description_lower:
                keywords.append(term)
        
        return ", ".join(keywords[:5])
    
    def generate_daily_report(self, jobs):
        """Generate the daily report in the specified format"""
        today = datetime.now().strftime("%B %d, %Y")
        
        report = f"DAILY IT/STARTUP PM ROLES — {today}\n\n"
        report += "Top matches (max 12):\n"
        
        if not jobs:
            report += "No new roles today\n\n"
            report += "Most recent 3 from the past week:\n"
            # This would be populated with recent jobs from previous searches
            report += "1) [Previous search results would go here]\n"
        else:
            for i, job in enumerate(jobs[:12], 1):
                report += f"{i}) {job['title']} — {job['company']} — {job['location']} — {job['source']}\n"
                report += f"   - Posted: {job['posted_date']}\n"
                report += f"   - Apply: {job['apply_link']}\n"
                report += f"   - Why fit: {job['why_fit']}\n"
                report += f"   - Keywords to mirror: {job['keywords']}\n\n"
        
        # Quick actions
        report += "Quick actions:\n"
        report += "- 3 tailored resume bullet suggestions:\n"
        report += "  • Coordinated cross-functional projects using Agile methodology and Smartsheet\n"
        report += "  • Managed stakeholder communications and project timelines in MS Teams\n"
        report += "  • Implemented process improvements using data analysis in Excel\n\n"
        
        report += "- 1-paragraph reusable cover note:\n"
        report += "As an entry-level Project Coordinator with a Project Management Certificate from Bellevue College and experience with Smartsheet, Asana, and MS 365, I am excited to contribute to your team's success. My background in Agile/Scrum methodologies and strong organizational skills make me well-suited for coordinating cross-functional projects and ensuring timely delivery.\n\n"
        
        # Trend notes
        report += "Trend notes:\n"
        report += "• Agile/Scrum methodologies frequently mentioned\n"
        report += "• Smartsheet and MS 365 tools commonly required\n"
        report += "• Remote/hybrid work options increasing\n"
        report += "• Entry-level roles often require 1-2 years experience\n"
        report += "• Strong communication skills emphasized\n\n"
        
        # Next steps
        report += "Next steps for tomorrow:\n"
        report += "• Check LinkedIn Jobs for new postings\n"
        report += "• Review company career pages for direct applications\n"
        report += "• Update resume with trending keywords from today's search\n"
        
        return report
    
    def run_daily_search(self):
        """Run the complete daily job search"""
        print("Starting daily job search...")
        
        # In a real implementation, these would make actual API calls
        jobs = []
        
        # For demonstration, create a sample job
        sample_job = {
            "title": "Project Coordinator",
            "company": "Sample Tech Company",
            "location": "Seattle, WA",
            "source": "LinkedIn",
            "posted_date": "December 19, 2024",
            "apply_link": "https://example.com/apply",
            "description": "We are looking for an entry-level Project Coordinator with experience in Agile methodology and Smartsheet..."
        }
        
        jobs.append(self.format_job_posting(sample_job))
        
        report = self.generate_daily_report(jobs)
        return report

def main():
    agent = JobSearchAgent()
    report = agent.run_daily_search()
    print(report)
    
    # Save report to file
    with open('/Users/tatiana/Desktop/cursor tutorial/daily_job_report.txt', 'w') as f:
        f.write(report)
    
    print("\nReport saved to daily_job_report.txt")

if __name__ == "__main__":
    main()
