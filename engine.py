from playwright.sync_api import sync_playwright
from abstract import AbstractController
from rotation import RotationController
from spareparts import SparepartsController

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
        
        self.event_loop()
        
    def event_loop(self):
        with sync_playwright() as pw:
            self.start_session(pw)
            
            page = self.page
            canvas_element = self.canvas_element
            parts = self.parts
            rotations = self.rotations
            
            for rotation in rotations.rotations:     
                for i, o_color in enumerate(parts.outer_colors):
                    for j, i_color in enumerate(parts.inner_colors):
                        parts.change_inner_color(j)
                        
                        for wheel in parts.wheels:
                            parts.change_wheel(wheel)
                            parts.change_outer_color(i)
                            rotation()
                            final_path = self.image_path_constructor(rotations.position, o_color, i_color, wheel)
                            page.locator(canvas_element).screenshot(path=final_path, type='png')

            # browser.close()
        
        
    def start_session(self, pw):
        self.browser = pw.chromium.launch(headless=False,
                                        executable_path='D:\Programs\Development\PlaywrightBrowsers\chromium-1060\chrome-win\chrome.exe',
                                        args=self.chrome_args,
                                        timeout=0)
        self.page = self.browser.new_page()
        self.page.set_viewport_size({ 'width': 1920, 'height': 1080 })
        abstract = AbstractController(self.page)
        self.rotations = RotationController(self.page, self.canvas_element, abstract)
        self.parts = SparepartsController(self.page, abstract, self.canvas_element)
        
        print(f"Fetching {self.url}")
        self.page.goto(self.url, timeout=0)
        self.page.wait_for_load_state('networkidle', timeout=0)
        self.page.wait_for_selector(self.wait_selector, timeout=0)
        print(f"Selector {self.wait_selector} appeared")
        
        self.hide_waste_elements()    
        
        
    def hide_waste_elements(self):
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
            # self.page.evaluate(f"() => {{document.querySelector('{element}').remove()}}")
            self.page.evaluate(f"() => {{document.querySelector('{element}').style.opacity = '0';}}")
            print(f"Element {element} hidden")
            
        AbstractController.small_timeout(self)
        print("Removing done")
        
        
    def image_path_constructor(self, position, outer_color, inner_color, wheel_index):
        return f"screenshots/{position}/{outer_color}-outer/{inner_color}-inner/{wheel_index}-wheel.png"