"""Task 10 - Simple Fact Verification (weather facts)"""

facts = ["raining", "foggy", "cloudy"]

fact = input("Enter a weather fact: ").lower()

if fact in facts:
    print("Fact is TRUE")
else:
    print("Fact is FALSE")
