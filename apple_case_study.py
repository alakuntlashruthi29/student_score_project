# Case Study Analysis of Apple Inc.

apple = {
    "Business Model": [
        "Premium Pricing",
        "Product Ecosystem",
        "Innovation"
    ],

    "Marketing Techniques": [
        "Strong Branding",
        "Digital Marketing",
        "Customer Experience"
    ],

    "Reasons for Success": [
        "High Product Quality",
        "Customer Loyalty",
        "Continuous Innovation"
    ],

    "Lessons Learned": [
        "Focus on User Experience",
        "Maintain Brand Value",
        "Invest in Innovation"
    ]
}

print("\nCASE STUDY ANALYSIS: APPLE INC.\n")

for category, items in apple.items():

    print(category + ":")

    for item in items:
        print("-", item)

    print()