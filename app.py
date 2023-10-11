from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def option1():
    if request.method == 'POST':
        phone_price = float(request.form['phone_price'])
        insurance_cost = float(request.form['insurance_cost'])
        down_payment = float(request.form['down_payment'])
        promotion_value = float(request.form['promotion_value'])

        accessory_option1_cost = 200  # Option 1 accessories cost
        accessory_option2_cost = 100  # Option 2 accessories cost

        # Calculate monthly payment for each option
        full_phone_price = phone_price - promotion_value
        monthly_phone_cost = (full_phone_price - down_payment) / 24
        monthly_insurance_cost = insurance_cost

        monthly_accessory_cost_option1 = accessory_option1_cost / 12
        monthly_accessory_cost_option2 = accessory_option2_cost / 12

        sales_tax_amount_option3 = phone_price * 0.06  # 6% sales tax
        sales_tax_amount_option2 = (phone_price + accessory_option2_cost) * 0.06
        sales_tax_amount_option1 = (phone_price + accessory_option1_cost) * 0.06

        amount_due_today_option1 = down_payment + sales_tax_amount_option1 + 35  # Upgrade fee
        amount_due_today_option2 = down_payment + sales_tax_amount_option2 + 35
        amount_due_today_option3 = down_payment + sales_tax_amount_option3 + 35

        monthly_payment_option1 = (monthly_phone_cost + monthly_accessory_cost_option1 + monthly_insurance_cost)
        monthly_payment_option2 = (monthly_phone_cost + monthly_accessory_cost_option2 + monthly_insurance_cost)
        monthly_payment_option3 = (phone_price / 24)

        # Define custom option names
        option1_name = "Phone+(200)+Insurance"
        option2_name = "Phone+(100)+P360"
        option3_name = "Phone BareBone"

        return render_template('result.html',
                               monthly_payment_option1=monthly_payment_option1,
                               monthly_payment_option2=monthly_payment_option2,
                               monthly_payment_option3=monthly_payment_option3,
                               amount_due_today_option1=amount_due_today_option1,
                               amount_due_today_option2=amount_due_today_option2,
                               amount_due_today_option3=amount_due_today_option3,
                               option1_name=option1_name,
                               option2_name=option2_name,
                               option3_name=option3_name)
    return render_template('input_form.html')
