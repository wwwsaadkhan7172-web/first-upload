# ═══════════════════════════════════════════════════
# PESHAWAR ELECTRONICS — SMART BILLING SYSTEM
# ═══════════════════════════════════════════════════

print("╔" + "═"*48 + "╗")
print("║" + "     PESHAWAR ELECTRONICS — BILLING     ".center(48) + "║")
print("╚" + "═"*48 + "╝")

# Customer info
naam = input("Customer naam: ")
phone = input("Phone number: ")
is_member = input("Member card hai? (haan/nahi): ").lower() == "haan"
payment_type = input("Payment method (cash/card/installment): ").lower()

# Item
item = input("\nItem naam: ")
price = float(input(f"'{item}' ki price (Rs.): "))

# ── Discount Logic ──
discount_percent = 0
discount_reason = "Koi discount nahi"

if is_member and price >= 10000:
    discount_percent = 15
    discount_reason = "Member + 10K+ purchase"
elif is_member:
    discount_percent = 10
    discount_reason = "Member discount"
elif price >= 50000:
    discount_percent = 12
    discount_reason = "Bulk purchase discount"
elif price >= 20000:
    discount_percent = 8
    discount_reason = "Large purchase discount"
elif payment_type == "cash":
    discount_percent = 5
    discount_reason = "Cash payment discount"

# ── Payment Type Logic ──
if payment_type == "installment":
    months = int(input("Kitne months mein? (6/12/24): "))
    if months == 6:
        markup = 5
    elif months == 12:
        markup = 10
    else:
        markup = 18
    price_with_markup = price * (1 + markup/100)
else:
    price_with_markup = price
    markup = 0

# ── Calculations ──
discount_amount = price * (discount_percent / 100)
after_discount = price - discount_amount
if payment_type == "installment":
    final = price_with_markup
    monthly = final / months
else:
    final = after_discount
    monthly = 0

gst = final * 0.17
grand_total = final + gst

# ── Print Bill ──
print(f"\n{'═'*50}")
print(f"{'BILL RECEIPT':^50}")
print(f"{'─'*50}")
print(f"Customer  : {naam.title()}")
print(f"Phone     : {phone}")
print(f"Member    : {'✅ Haan' if is_member else '❌ Nahi'}")
print(f"{'─'*50}")
print(f"Item      : {item}")
print(f"MRP       : Rs. {price:>12,.2f}")

if discount_percent > 0:
    print(f"Discount  : {discount_percent}% ({discount_reason})")
    print(f"           -Rs. {discount_amount:>10,.2f}")

if payment_type == "installment":
    print(f"Markup    : {markup}% ({months} months)")
    print(f"           +Rs. {price_with_markup - price:>10,.2f}")

print(f"GST (17%) : +Rs. {gst:>10,.2f}")
print(f"{'─'*50}")
print(f"TOTAL     : Rs. {grand_total:>12,.2f}")

if payment_type == "installment":
    print(f"Monthly   : Rs. {(grand_total/months):>12,.2f} x {months} months")

print(f"{'═'*50}")
print("Shukriya! Phir Tashreef Laein! 🙏")