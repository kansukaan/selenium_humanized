import random
import time
import numpy as np
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class HumanLikeActions:
    def __init__(self, driver, profile_manager, profile_name="Profile1"):
        self.driver = driver
        self.action_chains = ActionChains(driver)
        self.profile = profile_manager.get_profile(profile_name)
        if not self.profile:
            raise ValueError(f"Profil bulunamadı: {profile_name}. Mevcut profiller: {profile_manager.list_profiles()}")
    def human_delay(self, min_seconds=None, max_seconds=None):
        if min_seconds is None:
            min_seconds = self.profile['move_speed_min']
        if max_seconds is None:
            max_seconds = self.profile['move_speed_max']
        delay = random.uniform(min_seconds, max_seconds)
        time.sleep(delay)
        return delay
    def human_type(self, element, text):
        self.human_click(element)
        for char in text:
            element.send_keys(char)
            self.human_delay(self.profile['typing_speed_min'], self.profile['typing_speed_max'])
            if random.random() < self.profile['error_rate']:
                element.send_keys(Keys.BACK_SPACE)
                self.human_delay(0.1, 0.5)
                element.send_keys(char)
                self.human_delay(0.1, 0.3)
    def human_move_to_element(self, element):
        try:
            location = element.location_once_scrolled_into_view
            size = element.size
            element_center_x = location['x'] + size['width'] / 2
            element_center_y = location['y'] + size['height'] / 2
            self._human_curve_movement(element_center_x, element_center_y)
            self._hover_jitter(element_center_x, element_center_y)
        except Exception as e:
            print(f"Elemente hareket ederken hata oluştu: {e}")
            self.action_chains.move_to_element(element).perform()
    def human_click(self, element):
        self.human_move_to_element(element)
        self.human_delay(0.1, 0.8)
        offset_x = random.randint(-self.profile['jitter_intensity'], self.profile['jitter_intensity'])
        offset_y = random.randint(-self.profile['jitter_intensity'], self.profile['jitter_intensity'])
        self.action_chains.move_by_offset(offset_x, offset_y).perform()
        self.human_delay(0.05, 0.2)
        self.action_chains.click().perform()
        self.human_delay(0.1, 0.5)
        self.action_chains.move_by_offset(-offset_x//2, -offset_y//2).perform()
    def human_scroll(self, scroll_amount=None):
        if scroll_amount is None:
            scroll_amount = random.randint(200, 800)
        # Profile göre scroll adımları
        if self.profile['scroll_speed'] == 'fast':
            steps = random.randint(2, 5)
        elif self.profile['scroll_speed'] == 'slow':
            steps = random.randint(8, 15)
        else:  # medium
            steps = random.randint(5, 10)
        step_size = scroll_amount / steps
        for _ in range(steps):
            current_step = step_size * random.uniform(0.8, 1.2)
            self.driver.execute_script(f"window.scrollBy(0, {current_step});")
            self.human_delay(0.05, 0.3)
    def _human_curve_movement(self, target_x, target_y):
        current_x, current_y = 0, 0
        control_points = self._generate_control_points(current_x, current_y, target_x, target_y)
        steps = random.randint(20, 40)
        for t in np.linspace(0, 1, steps):
            x = (1-t)**3 * control_points[0][0] + 3*(1-t)**2*t * control_points[1][0] + 3*(1-t)*t**2 * control_points[2][0] + t**3 * control_points[3][0]
            y = (1-t)**3 * control_points[0][1] + 3*(1-t)**2*t * control_points[1][1] + 3*(1-t)*t**2 * control_points[2][1] + t**3 * control_points[3][1] 
            self.action_chains.move_by_offset(x - current_x, y - current_y).perform()
            current_x, current_y = x, y
            self.human_delay(0.01, 0.05)
    def _generate_control_points(self, start_x, start_y, end_x, end_y):
        cp1_x = start_x + (end_x - start_x) * random.uniform(0.2, 0.4)
        cp1_y = start_y + (end_y - start_y) * random.uniform(0.1, 0.3)
        cp2_x = start_x + (end_x - start_x) * random.uniform(0.6, 0.8)
        cp2_y = start_y + (end_y - start_y) * random.uniform(0.7, 0.9)
        max_deviation = min(abs(end_x - start_x), abs(end_y - start_y)) * 0.3
        cp1_x += random.uniform(-max_deviation, max_deviation)
        cp1_y += random.uniform(-max_deviation, max_deviation)
        cp2_x += random.uniform(-max_deviation, max_deviation)
        cp2_y += random.uniform(-max_deviation, max_deviation)
        return [(start_x, start_y), (cp1_x, cp1_y), (cp2_x, cp2_y), (end_x, end_y)]
    def _hover_jitter(self, x, y):
        jitter_count = random.randint(1, self.profile['jitter_intensity'])
        for _ in range(jitter_count):
            offset_x = random.randint(-self.profile['jitter_intensity'], self.profile['jitter_intensity'])
            offset_y = random.randint(-self.profile['jitter_intensity'], self.profile['jitter_intensity'])
            self.action_chains.move_by_offset(offset_x, offset_y).perform()
            self.human_delay(0.02, 0.1)
        self.action_chains.move_to_element_with_offset(self.driver.find_element(By.TAG_NAME, 'body'), x, y).perform()