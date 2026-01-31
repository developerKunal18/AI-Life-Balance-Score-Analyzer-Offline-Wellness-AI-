print("🧠 AI Life Balance Score Analyzer \n")

work_hours = float(input("Work hours today: "))
sleep_hours = float(input("Sleep hours today: "))
exercise_minutes = int(input("Exercise minutes today: "))
learning_hours = float(input("Learning hours today: "))
stress = int(input("Stress level (1–5): "))

score = 0

# Work balance
if work_hours <= 8:
    score += 20
else:
    score += max(0, 20 - (work_hours - 8) * 2)

# Sleep
if 7 <= sleep_hours <= 9:
    score += 25
else:
    score += max(0, 25 - abs(8 - sleep_hours) * 4)

# Exercise
score += min(15, exercise_minutes / 4)

# Learning
score += min(15, learning_hours * 3)

# Stress
score += (6 - stress) * 5

print("\n📊 LIFE BALANCE REPORT")
print(f"Life Balance Score: {score:.1f} / 100")

print("\n🧭 AI Assessment")

if score >= 80:
    print("🌟 Excellent life balance! Keep it up.")
elif score >= 60:
    print("🙂 Balanced, but can improve.")
elif score >= 40:
    print("⚠️ Imbalanced. Adjust priorities.")
else:
    print("🚨 Critical imbalance! Immediate changes needed.")

print("\n🧭 AI Suggestions")
if sleep_hours < 7:
    print("• Increase sleep duration")
if exercise_minutes < 30:
    print("• Add physical activity")
if work_hours > 9:
    print("• Reduce overworking")
if stress >= 4:
    print("• Practice stress management")
if learning_hours == 0:
    print("• Spend time learning something new")
