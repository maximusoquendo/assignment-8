# Module 8 Assignment: Data Lookup with Dictionaries & Basic Aggregation
# GlobalTech Solutions Customer Management System

# Print a header for the program
print("=" * 60)
print("GLOBALTECH SOLUTIONS - CUSTOMER MANAGEMENT SYSTEM")
print("=" * 60)

# TODO 1: Dictionary of services and hourly rates
# Key = service name, Value = hourly rate
services = {
    "Web Development": 150,
    "Data Analysis": 175,
    "Cybersecurity": 200,
    "Cloud Computing": 180,
    "IT Support": 90
}

# TODO 2: Individual customer dictionaries
# Each dictionary stores details about one customer
customer1 = {
    "company_name": "ABC Corp",
    "contact_person": "John Smith",
    "email": "john@abc.com",
    "phone": "111-222-3333"
}

customer2 = {
    "company_name": "TechNova",
    "contact_person": "Sara Lee",
    "email": "sara@technova.com",
    "phone": "222-333-4444"
}

customer3 = {
    "company_name": "DataWorks",
    "contact_person": "Mike Brown",
    "email": "mike@dataworks.com",
    "phone": "333-444-5555"
}

customer4 = {
    "company_name": "SecureIT",
    "contact_person": "Emma Davis",
    "email": "emma@secureit.com",
    "phone": "444-555-6666"
}

# TODO 3: Master dictionary of all customers
# Key = Customer ID, Value = customer dictionary
customers = {
    "C001": customer1,
    "C002": customer2,
    "C003": customer3,
    "C004": customer4
}

# TODO 4: Display all customers
print("\nAll Customers:")
print("-" * 60)

# Loop through dictionary using .items() to get key and value
for cid, info in customers.items():
    print(cid, info)

# TODO 5: Customer lookups
print("\n\nCustomer Lookups:")
print("-" * 60)

# Direct access using key
c002_info = customers["C002"]

# Access nested value (contact_person inside C003)
c003_contact = customers["C003"]["contact_person"]

# Safe lookup using .get() (prevents crash if key not found)
c999_info = customers.get("C999", "Customer not found")

print("C002 Info:", c002_info)
print("C003 Contact:", c003_contact)
print("C999 Lookup:", c999_info)

# TODO 6: Update customer data
# Modify existing value
customers["C001"]["phone"] = "999-888-7777"

# Add new field to dictionary
customers["C002"]["industry"] = "Technology"

print("\n\nUpdating Customer Information:")
print("-" * 60)

# Show updated customers
for cid in ["C001", "C002"]:
    print(cid, customers[cid])

# TODO 7: Create project data
# Each project is a dictionary
# Each customer ID maps to a list of their projects
projects = {
    "C001": [
        {"name": "Website Revamp", "service": "Web Development", "hours": 100, "budget": 15000},
        {"name": "Cloud Migration", "service": "Cloud Computing", "hours": 80, "budget": 14000}
    ],
    "C002": [
        {"name": "Security Audit", "service": "Cybersecurity", "hours": 60, "budget": 12000}
    ],
    "C003": [
        {"name": "Data Dashboard", "service": "Data Analysis", "hours": 90, "budget": 15750}
    ],
    "C004": []  # No projects yet
}

print("\n\nProject Information:")
print("-" * 60)

# Loop through all projects
for cid, plist in projects.items():
    print(cid, plist)

# TODO 8: Calculate project costs
print("\n\nProject Cost Calculations:")
print("-" * 60)

# Loop through projects and calculate cost = rate * hours
for cid, plist in projects.items():
    for proj in plist:
        rate = services[proj["service"]]  # get rate from services dict
        cost = rate * proj["hours"]
        print(proj["name"], "Cost:", cost)
        
# TODO 9: Customer statistics
print("\n\nCustomer Statistics:")
print("-" * 60)

# .keys() returns all dictionary keys
print("Customer IDs:", customers.keys())

# Extract company names from values
print("Companies:", [c["company_name"] for c in customers.values()])

# Count total customers
print("Total Customers:", len(customers))

# TODO 10: Count service usage
service_counts = {}

# Count how many times each service appears
for plist in projects.values():
    for proj in plist:
        svc = proj["service"]
        service_counts[svc] = service_counts.get(svc, 0) + 1

print("\n\nService Usage Analysis:")
print("-" * 60)
print(service_counts)

# TODO 11: Financial calculations
total_hours = 0
total_budget = 0
budgets = []

# Aggregate totals
for plist in projects.values():
    for proj in plist:
        total_hours += proj["hours"]
        total_budget += proj["budget"]
        budgets.append(proj["budget"])

# Calculate average, max, min
avg_budget = total_budget / len(budgets)
max_budget = max(budgets)
min_budget = min(budgets)

print("\n\nFinancial Summary:")
print("-" * 60)
print("Total Hours:", total_hours)
print("Total Budget:", total_budget)
print("Average Budget:", avg_budget)
print("Max Budget:", max_budget)
print("Min Budget:", min_budget)

# TODO 12: Customer summary report
print("\n\nCustomer Summary Report:")
print("-" * 60)

# Show summary per customer
for cid, cust in customers.items():
    plist = projects.get(cid, [])
    total_h = sum(p["hours"] for p in plist)
    total_b = sum(p["budget"] for p in plist)
    print(cid, cust["company_name"], "| Projects:", len(plist), "| Hours:", total_h, "| Budget:", total_b)

# TODO 13: Increase service rates by 10% using dictionary comprehension
adjusted_rates = {
    service: rate * 1.1
    for service, rate in services.items()
}

print("\n\nAdjusted Service Rates (10% increase):")
print("-" * 60)
print(adjusted_rates)

# TODO 14: Filter customers who have projects
active_customers = {
    cid: customers[cid]
    for cid in projects
    if len(projects[cid]) > 0
}

print("\n\nActive Customers (with projects):")
print("-" * 60)
print(active_customers)

# TODO 15: Total budget per customer
customer_budgets = {
    cid: sum(p["budget"] for p in plist)
    for cid, plist in projects.items()
}

print("\n\nCustomer Budget Totals:")
print("-" * 60)
print(customer_budgets)

# TODO 16: Categorize services into pricing tiers
service_tiers = {
    s: ("Premium" if r >= 200 else "Standard" if r >= 100 else "Basic")
    for s, r in services.items()
}

print("\n\nService Pricing Tiers:")
print("-" * 60)
print(service_tiers)

# TODO 17: Validation function
def validate_customer(customer_dict):
    # Required fields list
    required = ["company_name", "contact_person", "email", "phone"]

    # Check all fields exist using all()
    return all(field in customer_dict for field in required)

print("\n\nCustomer Validation:")
print("-" * 60)

# Test validation for each customer
for cid, cust in customers.items():
    print(cid, validate_customer(cust))

# TODO 18: Add project status and count them
status_counts = {"active": 0, "completed": 0, "pending": 0}

statuses = ["active", "completed", "pending"]
i = 0

# Assign statuses in a rotating way
for plist in projects.values():
    for proj in plist:
        proj["status"] = statuses[i % 3]
        status_counts[proj["status"]] += 1
        i += 1

print("\n\nProject Status Summary:")
print("-" * 60)
print(status_counts)

# TODO 19: Analyze budgets per customer
def analyze_customer_budgets(projects_dict):
    result = {}

    for cid, plist in projects_dict.items():
        total = sum(p["budget"] for p in plist)
        count = len(plist)
        avg = total / count if count > 0 else 0

        result[cid] = {
            "total": total,
            "average": avg,
            "count": count
        }

    return result

print("\n\nDetailed Budget Analysis:")
print("-" * 60)
print(analyze_customer_budgets(projects))

# TODO 20: Recommend services
def recommend_services(customer_id, customers, projects, services):
    # Services already used
    used = {p["service"] for p in projects.get(customer_id, [])}

    # Services not yet used
    unused = [s for s in services if s not in used]

    # Calculate average budget
    budgets = [p["budget"] for p in projects.get(customer_id, [])]
    avg_budget = sum(budgets) / len(budgets) if budgets else 0

    recommendations = []

    # Recommend services that fit budget
    for svc in unused:
        if services[svc] * 50 <= avg_budget:
            recommendations.append(svc)

    return recommendations

print("\n\nService Recommendations:")
print("-" * 60)

# Show recommendations for each customer
for cid in customers:
    print(cid, recommend_services(cid, customers, projects, services))