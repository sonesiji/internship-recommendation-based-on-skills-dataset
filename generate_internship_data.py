import pandas as pd
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Define fields
internship_titles = ["Data Science Intern", "Marketing Intern", "Software Engineer Intern", "Graphic Design Intern", "Finance Intern"]
companies = ["TechCorp", "MarketInc", "DevSolutions", "CreativeArts", "FinAnalytics"]
locations = ["New York, NY", "San Francisco, CA", "Remote", "Los Angeles, CA", "Chicago, IL"]
skills_list = [
    ["Python", "Machine Learning", "SQL"],
    ["Digital Marketing", "SEO", "Content Writing"],
    ["Java", "React", "Node.js"],
    ["Adobe Photoshop", "Illustrator", "InDesign"],
    ["Excel", "Financial Modeling", "Analysis"]
]
eligibility_majors = [
    "Computer Science, Graduating 2025",
    "Marketing, Business Majors",
    "Computer Science, Graduating 2024",
    "Design, Fine Arts Majors",
    "Finance, Economics Majors"
]
descriptions = [
    "Work on data analysis projects, create machine learning models",
    "Assist in creating marketing campaigns and SEO strategies",
    "Develop and maintain web applications",
    "Create visual content for various media",
    "Assist in financial analysis and reporting"
]

# Generate dataset
data = []

for i in range(1000):
    idx = random.randint(0, 4)
    data.append([
        i + 1,
        internship_titles[idx],
        companies[idx],
        locations[idx],
        ", ".join(skills_list[idx]),
        random.randint(2, 6),  # Duration
        random.randint(1000, 2000),  # Stipend
        fake.date_between(start_date='today', end_date='+60d'),  # Application Deadline
        eligibility_majors[idx],
        descriptions[idx]
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "Internship ID", "Internship Title", "Company Name", "Location",
    "Skills Required", "Duration (Months)", "Stipend (USD/Month)",
    "Application Deadline", "Eligibility", "Internship Description"
])

# Save to CSV
df.to_csv("internship_recommendations.csv", index=False)
