from playwright.sync_api import sync_playwright
from rotation import RotationController

class PlaywrightController:
    
    def __init__(self):
        self.chrome_args = [
            '--use-angle=vulkan',
            '--enable-gpu',
            '--no-sandbox',
            '--ignore-gpu-blocklist',
        ]

        self.canvas_element = '#application-canvas'
        self.url = "https://www.zeekrlife.com/toReserve?modelInfoId=3"
        self.wait_selector = '.reserve-main-tips'
        
    def event_loop(self):
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, executable_path='D:\Programs\Development\PlaywrightBrowsers\chromium-1060\chrome-win\chrome.exe', args=chrome_args, timeout=0)
            self.page = browser.new_page()
            self.page.set_viewport_size({ 'width': 1920, 'height': 1080 })
            self.rotation_controller = RotationController(self.page, self.canvas_element)
            
            print(f"Fetching {self.url}")
            self.page.goto(self.url, timeout=0)

            self.page.wait_for_load_state('networkidle', timeout=0)
            self.page.wait_for_selector(self.wait_selector, timeout=0)
            print(f"Selector {self.wait_selector} appeared")

            self.remove_waste_elements()
            self.page.locator(self.canvas_element).focus()
            self.rotation_controller.rotate_front()
            self.page.locator(self.canvas_element).screenshot(path='canvas.png', type='png')

            # self.page.wait_for_timeout(5000)
            self.page.screenshot(path="Test.png", type='png')
            self.page.wait_for_timeout(20000)
            # browser.close()
        
    def remove_waste_elements(self):
        print(f"Removing waste elements")
        wasteElementsClasses = [
            '.reserve-main-tabbar', 
            '.reserve-main-tips', 
            '.othercomponents-top',
            '.reserve-main-changecar-box',
            '.footertoast',
        ]
        
        for element in wasteElementsClasses:
            self.page.wait_for_selector(f"{element}")
            self.page.evaluate(f"() => {{document.querySelector('{element}').remove()}}")
            print(f"Element {element} removed")
            
        self.rotation_controller.smallTimeOut()
        print("Removing done")