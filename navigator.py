from abstract import AbstractController as abst

class NavigatorController:

    @staticmethod
    def target_tab_click(self, tab_btn, element):
        tab_btn.click(force=True)
        abst.tiny_timeout(self)
        element.click(force=True)
        abst.tiny_timeout(self)
        
    @staticmethod
    def wheels_and_colors_click(method):
        def wrapper(self, *args, **kwargs):
            NavigatorController.target_tab_click(self, self.wheels_and_colors_btn, method(self, *args, **kwargs))
            
        return wrapper
        
    @staticmethod
    def interior_click(method):
        def wrapper(self, *args, **kwargs):
            NavigatorController.target_tab_click(self, self.interior_btn, method(self, *args, **kwargs))
            
        return wrapper

        
       