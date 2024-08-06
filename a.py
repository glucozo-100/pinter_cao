from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

# Cấu hình Selenium và khởi tạo trình duyệt
chrome_options = Options()
chrome_options.add_argument("--headless")  # chạy trình duyệt ở chế độ headless
chrome_driver_path = r"D:\Crawl_Anime\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # thay thế bằng đường dẫn tới chromedriver của bạn
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


url = "https://www.pinterest.com/pin/1970393581618266/"
driver.get(url)


try:
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "tBJ.dyH.iFc.sAJ.X8m.zDA.IZT.H2s"))
    )
except:
    print("Element not found")
    driver.quit()


page_source = driver.page_source
soup = BeautifulSoup(page_source, "html.parser")


reactions_div = soup.find("div", {"class": "tBJ dyH iFc sAJ X8m zDA IZT H2s"})
print(reactions_div) # chỗ này đáng nhẽ phải in ra như sau: <div class="tBJ dyH iFc sAJ X8m zDA IZT H2s">102</div>
#nhưng anh chạy cái ảnh nào nó cũng chỉ in ra <div class="tBJ dyH iFc sAJ X8m zDA IZT H2s">Image search</div>

# if reactions_div:
#     reactions = reactions_div.text.strip()
#     print("Reactions:", reactions)
# else:
#     print("reactions_div not found")

# driver.quit()