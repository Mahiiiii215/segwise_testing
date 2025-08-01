from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.common.keys as Keys
import traceback
import time

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")
# options.add_argument("--headless")  # Uncomment if needed
driver = webdriver.Chrome(options=options)

try:
    print("🚀 Launching Segwise login page...")
    driver.get("https://auth.segwise.ai/en/login")
    wait = WebDriverWait(driver, 20)

    # Email input
    print("🔐 Waiting for email field...")
    email_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="email"]')))
    email_input.clear()
    email_input.send_keys("qa@segwise.ai")
    time.sleep(1)

    # Password input
    print("🔐 Waiting for password field...")
    password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
    assert password_input.is_enabled(), "❌ Password field is not enabled!"
    password_input.click()

    # Simulate typing password
    password = "segwise_test"
    print("⌨️ Typing password character by character...")
    for char in password:
        password_input.send_keys(char)
        time.sleep(0.1)
    time.sleep(2)
    driver.save_screenshot("after_typing_password_naturally.png")

    # Click login
    print("🔓 Clicking login button...")
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Log in with email')]")))
    login_button.click()
    print("✅ Login button clicked.")
    time.sleep(3)
    driver.save_screenshot("after_click_login.png")

    # Wait for URL to change
    try:
        print("⏳ Waiting for login redirect...")
        wait = WebDriverWait(driver, 40)
        wait.until(lambda d: d.current_url != "https://auth.segwise.ai/en/login")
        print("✅ URL changed to:", driver.current_url)
    except Exception:
        print("❌ Login did not redirect — still on login page.")
        driver.save_screenshot("login_timeout_or_stuck.png")
        raise

    # Navigate to dashboard (just in case redirect is delayed)
    print("📊 Navigating to dashboard page directly...")
    driver.get("https://ua.segwise.ai/qa_assignment/creatives")

    # Wait for dashboard charts
    print("📈 Waiting for dashboard content...")
    wait = WebDriverWait(driver, 40)
    wait.until(EC.presence_of_element_located((
        By.XPATH,
        "//div[contains(text(), 'Spend') or contains(text(), 'Top') or contains(text(), 'Advantage')]"
    )))

    print("✅ Test Passed: Dashboard content loaded.")
    driver.save_screenshot("dashboard_loaded.png")

    # Prevent browser from closing immediately so you can inspect
    input("📌 Press Enter to close the browser manually...")

except Exception as e:
    print("❌ Test Failed:")
    traceback.print_exc()
    driver.save_screenshot("general_error.png")
    print("📸 Screenshot saved: general_error.png")

    # Pause browser if it failed
    print("🛑 Holding browser open for inspection...")
    time.sleep(9999)

finally:
    driver.quit()








