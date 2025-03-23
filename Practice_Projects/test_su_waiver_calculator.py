import time
import tkinter as tk
from tkinter import font as tkfont
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SU Payment Waiver Calculator")
        self.geometry("600x700")  # Increased window size for better layout

        # Define font
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight='bold')
        self.label_font = tkfont.Font(family='Arial', size=12)
        self.value_font = tkfont.Font(family='Arial', size=12, weight='bold')
        self.section_font = tkfont.Font(family='Helvetica', size=14, weight='bold')

        # Part 1: Input section
        self.input_frame = tk.LabelFrame(self, text="Login Details", font=self.section_font, padx=10, pady=10)
        self.input_frame.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        self.label_id = tk.Label(self.input_frame, text="ID:", font=self.label_font)
        self.label_id.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_id = tk.Entry(self.input_frame, font=self.label_font, relief="solid", bd=2)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.label_password = tk.Label(self.input_frame, text="Password:", font=self.label_font)
        self.label_password.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_password = tk.Entry(self.input_frame, show="*", font=self.label_font, relief="solid", bd=2)
        self.entry_password.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

        self.button_submit = tk.Button(self.input_frame, text="Submit", command=self.submit, font=self.label_font, bg="#4CAF50", fg="white", relief="solid", bd=2)
        self.button_submit.grid(row=2, column=0, columnspan=2, padx=10, pady=20, ipadx=10, ipady=5, sticky="ew")

        # Part 2: Output section
        self.output_frame = tk.LabelFrame(self, text="Calculation Results", font=self.section_font, padx=10, pady=10)
        self.output_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        self.label_your_name = tk.Label(self.output_frame, text="Your Name:", font=self.label_font)
        self.label_your_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.label_your_name_value = tk.Label(self.output_frame, text="", font=self.value_font, fg="#555")
        self.label_your_name_value.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.label_your_id = tk.Label(self.output_frame, text="Your ID:", font=self.label_font)
        self.label_your_id.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.label_your_id_value = tk.Label(self.output_frame, text="", font=self.value_font, fg="#555")
        self.label_your_id_value.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.label_total_package = tk.Label(self.output_frame, text="Total Package:", font=self.label_font)
        self.label_total_package.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.label_total_package_value = tk.Label(self.output_frame, text="", font=self.value_font, fg="#555")
        self.label_total_package_value.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.label_already_paid = tk.Label(self.output_frame, text="Already Paid to SU:", font=self.label_font)
        self.label_already_paid.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.label_already_paid_value = tk.Label(self.output_frame, text="", font=self.value_font, fg="#555")
        self.label_already_paid_value.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.label_dues = tk.Label(self.output_frame, text="Dues:", font=self.label_font)
        self.label_dues.grid(row=4, column=0, padx=10, pady=5, sticky="w")
        self.label_dues_value = tk.Label(self.output_frame, text="", font=self.value_font, fg="#555")
        self.label_dues_value.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.label_discount = tk.Label(self.output_frame, text="Discount Calculated:", font=self.label_font)
        self.label_discount.grid(row=5, column=0, padx=10, pady=5, sticky="w")
        self.label_discount_value = tk.Label(self.output_frame, text="", font=self.value_font, fg="#555")
        self.label_discount_value.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.label_after_discount = tk.Label(self.output_frame, text="After Discount Remaining:", font=self.label_font)
        self.label_after_discount.grid(row=6, column=0, padx=10, pady=5, sticky="w")
        self.label_after_discount_value = tk.Label(self.output_frame, text="", font=self.value_font, fg="#555")
        self.label_after_discount_value.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.label_already_paid_discount = tk.Label(self.output_frame, text="Already Paid for 10% Discount:", font=self.label_font)
        self.label_already_paid_discount.grid(row=7, column=0, padx=10, pady=5, sticky="w")
        self.label_already_paid_discount_value = tk.Label(self.output_frame, text="", font=self.value_font, fg="#555")
        self.label_already_paid_discount_value.grid(row=7, column=1, padx=10, pady=5, sticky="w")

        self.label_pay_now = tk.Label(self.output_frame, text="The Amount You Should Pay Now:", font=self.label_font)
        self.label_pay_now.grid(row=8, column=0, padx=10, pady=5, sticky="w")
        self.label_pay_now_value = tk.Label(self.output_frame, text="", font=self.value_font, fg="#555")
        self.label_pay_now_value.grid(row=8, column=1, padx=10, pady=5, sticky="w")

    def submit(self):
        id = self.entry_id.get()
        password = self.entry_password.get()

        # Selenium logic start here
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run in headless mode
        chrome_options.add_argument("--no-sandbox")  # Necessary for some environments
        chrome_options.add_argument("--disable-dev-shm-usage")  # Fix issues in some environments
        driver = webdriver.Chrome(options=chrome_options)
        # driver = webdriver.Chrome()

        # fetching URL
        url = "http://sue.su.edu.bd:5081/sonargaon_erp/home"
        driver.get(url)
        driver.find_element(By.XPATH, "//input[@id='email']").send_keys(id)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        driver.find_element(By.XPATH, "//input[@name='login']").click()
        time.sleep(5)
        fullname = driver.find_element(By.XPATH, "//span[@class='oe_topbar_name']").text
        print(fullname)

        # backend values for calculation
        name = fullname
        bill = int(driver.find_element(By.XPATH, '(//td[b[text()="Total bill generate"]]/span[@id="generate_amount"])[2]').text)
        waivers = 9069 + 1694 + 2012  # need to fetch acurately
        total_package = int(driver.find_element(By.XPATH, '//td[text()="Total Amount"]/following::td[15]').text.replace(',', '')) + bill
        already_paid_str = driver.find_element(By.XPATH, '//input[@id="get_taken_semester"]/following::td[1]').text
        already_paid = int(already_paid_str.replace(',', ''))
        already_paid_discount_str = driver.find_element(By.XPATH, '//input[@id="get_taken_semester"]/following::td[1]/preceding::td[11]/b').text
        already_paid_discount = int(already_paid_discount_str.replace(',', ''))
        dues = (total_package - already_paid) - waivers + already_paid_discount
        discount_fraction = 0.2 * total_package
        discount = round(discount_fraction)
        after_discount_remaining = total_package - discount
        pay_now = discount - already_paid_discount

        # Update labels with calculated values
        self.label_your_name_value.config(text=f"{name.upper()}")
        self.label_your_id_value.config(text=f"{id.upper()}")
        self.label_total_package_value.config(text=f"{total_package}")
        self.label_already_paid_value.config(text=f"{already_paid}")
        self.label_dues_value.config(text=f"{dues}")
        self.label_discount_value.config(text=f"{discount}")
        self.label_after_discount_value.config(text=f"{after_discount_remaining}")
        self.label_already_paid_discount_value.config(text=f"{already_paid_discount}")
        self.label_pay_now_value.config(text=f"{pay_now}")
        driver.quit()


if __name__ == "__main__":
    app = MyApp()
    app.mainloop()