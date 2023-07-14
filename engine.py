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
        self.url = "https://www.zeekrlife.com/toReserve?modelInfoId=2"
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
                        for z, bumper in enumerate(parts.bumpers):
                            parts.change_bumper(z)
                            for k, wheel in enumerate(parts.wheels):
                                parts.change_wheel(k)
                                parts.change_outer_color(i)
                                rotation()
                                final_path = self.image_path_constructor(rotations.position, o_color, i_color, bumper, wheel)
                                page.locator(canvas_element).screenshot(path=final_path, type='png')
                                AbstractController.tiny_timeout(self)
                                self.abstract.add_to_log(f"{final_path} saved")

    def start_session(self, pw):
        self.browser = pw.chromium.launch(headless=False,
                                        executable_path='D:\Programs\Development\PlaywrightBrowsers\chromium-1060\chrome-win\chrome.exe',
                                        args=self.chrome_args,
                                        timeout=0)
        self.page = self.browser.new_page()
        self.page.set_viewport_size({ 'width': 1920, 'height': 1080 })
        self.abstract = AbstractController(self.page)
        self.rotations = RotationController(self.page, self.canvas_element, self.abstract)
        self.parts = SparepartsController(self.page, self.abstract, self.canvas_element)
        
        print(f"Fetching {self.url}")
        self.page.goto(self.url, timeout=0)
        self.page.wait_for_load_state('networkidle', timeout=0)
        self.page.wait_for_selector(self.wait_selector, timeout=0)
        print(f"Selector {self.wait_selector} appeared")
        AbstractController.enormous_timeout(self)
        
        self.hide_waste_elements()   
        self.lets_rock() 
                
        
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
        
    def lets_rock(self):
        js = '''
            const head = document.head || document.getElementsByTagName('head')[0];
            const style = document.createElement('style');
            const css = `
            .pricedetail{
                background-color: #131116 !important;
                opacity: 1 !important;
                z-index: 1 !important;
                pointer-events: none !important;
            }
            
            .pricedetail{
                padding-left: 0 !important;
                width: 100% !important;
                background-color: #131116 !important;
                display: flex !important;
                align-items: center !important;
                flex-direction: column !important;
                justify-content: center !important;
                height: 100% !important;
            }
            
            .pricedetail p{
                color: #97CC04 !important;
                font-size: 23px !important;
                font-weight: 700 !important;
                width: 80%;
                margin-left: auto !important;
                margin-right: auto !important;
                text-align: center: !important;
            }
            
            .pricedetail div img{
                width: 100% !important;
            }
            
            .componentsone{
                opacity: 0 !important;
            }
            `;
            style.appendChild(document.createTextNode(css));
            head.appendChild(style);
            const pricedetail_box = document.querySelector('.pricedetail')
            const pricedetail_box_children = pricedetail_box.querySelectorAll('*')
            pricedetail_box_children.forEach(element => element.remove())
            document.querySelector('.selectorfix').remove()
            
            const logo_container = document.createElement('div');
            const logo_image = document.createElement('img');
            logo_image.setAttribute('src', 'https://avatars.githubusercontent.com/u/87989392?s=400&u=863071ff228b33bbf75383915f31f34f98aa7bfd&v=4')
            logo_container.appendChild(logo_image);
            pricedetail_box.appendChild(logo_container);
            
            const title_command = document.createElement('p')
            title_command.textContent = "Здесь я браузером коммандую!"
            pricedetail_box.appendChild(title_command);
            
            const jay_container = document.createElement('div');
            const jay_image = document.createElement('img');
            jay_image.setAttribute('src', 'https://bigpicture.ru/wp-content/uploads/2018/11/bob1-800x420.jpg')
            jay_container.appendChild(jay_image);
            pricedetail_box.appendChild(jay_container);
            
            const log = document.createElement('p')
            log.setAttribute('id', 'log')
            log.textContent = "Лог"
            pricedetail_box.appendChild(log);
        '''
        
        self.page.evaluate(f"() => {{{js}}}")
        
        
    def image_path_constructor(self, position, outer_color, inner_color, bumper_index, wheel_index):
        return f"screenshots/{position}/{outer_color}-outer/{inner_color}-inner/{bumper_index}-bumper/{wheel_index}-wheel.png"