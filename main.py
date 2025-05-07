from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from human_actions import ProfileManager, HumanLikeActions

def main():   
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    profile_manager = ProfileManager("profil.txt") 
    try:  
        human_actions = HumanLikeActions(driver, profile_manager, "Profile3")    
        driver.get("https://www.google.com")  
        search_box = driver.find_element(By.NAME, "q") 
        human_actions.human_type(search_box, "selenium insan benzeri hareketler")  
        search_button = driver.find_element(By.NAME, "btnK")
        human_actions.human_click(search_button)
        human_actions.human_scroll(500)
        
    except Exception as e:
        print(f"Hata oluştu: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()