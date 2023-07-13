class AbstractController:
    def __init__(self, page):
        self.page = page

    def js(self, js_string):
        return self.page.evaluate(f"() => {js_string}")
    
    @staticmethod    
    def canvas_action_decorator(method):
        def wrapper(self, *args, **kwargs):
            
            try:
                AbstractController.small_timeout(self)
                print(f"Start JS injection {method.__name__}")
                method(self, *args, **kwargs)
                print('JS injection done')
                AbstractController.focus_canvas(self)
                AbstractController.tiny_timeout(self)
               
            except Exception as e:
                print(e)
                return AbstractController.canvas_action_decorator(method)(*args, **kwargs)
            
        return wrapper
    
    @staticmethod
    def focus_canvas(self):
        print('Start focusing')
        # self.page.locator(self.canvas_element).focus()
        self.page.locator(self.canvas_element).hover()
        # self.page.locator(self.canvas_element).click()
        print('Focusing done')
    
    @staticmethod
    def tiny_timeout(self):
        print("Waiting 500ms")
        self.page.wait_for_timeout(500)
    
    @staticmethod
    def small_timeout(self):
        print("Waiting 2s")
        self.page.wait_for_timeout(2000)
    
    @staticmethod
    def medium_timeout(self):
        print("Waiting 4s")
        self.page.wait_for_timeout(4000)
        
    @staticmethod
    def big_timeout(self):
        print("Waiting 8s")
        self.page.wait_for_timeout(8000)
