# from abstract import AbstractController as abst
from navigator import NavigatorController as nvgt

class SparepartsController:
    
    def __init__(self, page, abstract, canvas_element):
        self.page = page
        self.abstract = abstract
        
        self.canvas_element = canvas_element
        self.outer_colors = ["orange", "white", "platinum", "black", "ocean", "blue"];
        self.inner_colors = [1, 2, 3, 4, 5]
        self.wheels = [1, 2, 3, 4, 5]
        self.roofs = [1, 2]
                
        self.interior_btn = self.page.locator('.column-tabbar .column-tabbar-item').nth(2)
        self.wheels_and_colors_btn = self.page.locator('.column-tabbar .column-tabbar-item').nth(1)
        
        self.first_tab = self.page.locator('.componentsone-secondary-item').nth(0).locator('.componentsone-last')
        self.second_tab = self.page.locator('.componentsone-secondary-item').nth(1).locator('.componentsone-last')
        self.third_tab = self.page.locator('.componentsone-secondary-item').nth(2).locator('.componentsone-last')
      
    @nvgt.wheels_and_colors_click
    def change_outer_color(self, index):
        self.abstract.add_to_log("Changing outer color")
        return self.first_tab.locator('.componentsone-last-item').nth(index)
    
    @nvgt.interior_click
    def change_inner_color(self, index):
        self.abstract.add_to_log("Changing interior color")
        return self.first_tab.locator('.componentsone-last-item').nth(index)
      
    @nvgt.wheels_and_colors_click
    def change_roof(self, index):
        self.abstract.add_to_log("Changing wheel")
        return self.second_tab.locator('.componentsone-last-item').nth(index)
      
    @nvgt.wheels_and_colors_click
    def change_wheel(self, index):
        self.abstract.add_to_log("Changing wheel")
        return self.third_tab.locator('.componentsone-last-item').nth(index)
      
        
    