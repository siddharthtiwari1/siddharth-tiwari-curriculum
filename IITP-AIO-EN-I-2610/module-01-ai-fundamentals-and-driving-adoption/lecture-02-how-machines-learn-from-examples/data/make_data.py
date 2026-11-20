"""Creates supplied practice files for Module 1. Run once: python make_data.py"""
import csv, random, os
random.seed(7)

# ---- 2.1 customers: 60 labelled + 10 held back ----
def make(n, start):
    rows = []
    for i in range(n):
        tenure = random.randint(1, 48)
        spend = random.choice([299, 499, 699, 999])
        tickets = random.randint(0, 6)
        score = (tickets >= 3) + (tenure <= 6) + (spend == 299) * 0.5 + random.choice([0, 0, 0.5])
        churned = "Yes" if score >= 1.5 else "No"
        rows.append([f"C{start+i:03d}", tenure, spend, tickets, churned])
    return rows
labelled = make(60, 1); held = make(10, 61)
with open("customers_labelled.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["customer_id","tenure_months","monthly_spend_rs","support_tickets_last_90d","churned"]); w.writerows(labelled)
with open("customers_heldback.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["customer_id","tenure_months","monthly_spend_rs","support_tickets_last_90d"]); w.writerows([r[:4] for r in held])
with open("customers_heldback_ANSWERS.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["customer_id","churned"]); w.writerows([[r[0], r[4]] for r in held])

# ---- 2.2 tickets: 60, 5 themes ----
themes = {
 "Billing": ["I was charged twice for my plan this month", "My invoice shows an amount I did not agree to", "Please refund the extra charge on my bill", "The discount on my renewal was not applied"],
 "Login": ["I cannot log in, the password reset email never arrives", "My account is locked after three attempts", "The one-time code is not reaching my phone", "I keep getting signed out of the app"],
 "Delivery": ["My order has not arrived after seven days", "The tracking page has shown the same status for a week", "The parcel was marked delivered but I did not get it", "I received the wrong item in my package"],
 "App bug": ["The app crashes when I open the settings page", "The search box freezes after I type two letters", "Photos will not upload and the screen goes blank", "The app shows a white screen after the latest update"],
 "Feature request": ["Please add a dark mode to the app", "It would help to export my history to a spreadsheet", "Can you add a way to schedule orders in advance", "I would like to share my list with family members"],
}
tickets = []
names = list(themes)
tid = 1
for rnd in range(12):
    for t in names:
        base = themes[t][rnd % 4]
        tickets.append([tid, base + ("." if rnd % 3 else " - please help."), t]); tid += 1
random.shuffle(tickets)
tickets = [[i+1, t[1], t[2]] for i, t in enumerate(tickets)]
with open("support_tickets.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["ticket_id","text"]); w.writerows([[t[0], t[1]] for t in tickets])
with open("support_tickets_ANSWERS.csv", "w", newline="") as f:
    w = csv.writer(f); w.writerow(["ticket_id","true_theme"]); w.writerows([[t[0], t[2]] for t in tickets])

# ---- 1.2 images: 3 classes ----
try:
    from PIL import Image, ImageDraw
    os.makedirs("shapes/train", exist_ok=True); os.makedirs("shapes/test", exist_ok=True)
    def draw(kind, seed):
        r = random.Random(seed)
        im = Image.new("RGB", (160, 160), (r.randint(220,255),)*3); d = ImageDraw.Draw(im)
        col = tuple(r.randint(20,200) for _ in range(3)); cx, cy, s = r.randint(60,100), r.randint(60,100), r.randint(25,45)
        if kind == "circle": d.ellipse([cx-s, cy-s, cx+s, cy+s], fill=col)
        elif kind == "square": d.rectangle([cx-s, cy-s, cx+s, cy+s], fill=col)
        else: d.polygon([(cx, cy-s), (cx-s, cy+s), (cx+s, cy+s)], fill=col)
        return im
    n = 0
    for kind in ["circle","square","triangle"]:
        os.makedirs(f"shapes/train/{kind}", exist_ok=True); os.makedirs(f"shapes/test/{kind}", exist_ok=True)
        for i in range(20): draw(kind, 1000+n).save(f"shapes/train/{kind}/{kind}_{i+1:02d}.png"); n += 1
        for i in range(6): draw(kind, 5000+n).save(f"shapes/test/{kind}/{kind}_test_{i+1:02d}.png"); n += 1
except ImportError:
    print("Pillow not installed: skipped shapes/")
print("done")
