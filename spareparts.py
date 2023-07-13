# from abstract import AbstractController as abst
from navigator import NavigatorController as nvgt

class SparepartsController:
    
    def __init__(self, page, abstract, canvas_element):
        self.page = page
        self.abstract = abstract
        
        self.canvas_element = canvas_element
        self.outer_colors = ["parisBeige", "athensWhite", "californiaPink", "berlinGrey", "hangzhouGreen", "sydneyBlue",];
        self.inner_colors = ["roseViolet", "blueWhite", "grayBlack", "blueGreen"]
        self.wheels = [0, 1, 2, 3]
                
        self.interior_btn = self.page.locator('.column-tabbar .column-tabbar-item').nth(2)
        self.wheels_and_colors_btn = self.page.locator('.column-tabbar .column-tabbar-item').nth(1)
        
        self.first_tab = self.page.locator('.componentsone-secondary-item').nth(0).locator('.componentsone-last')
        self.second_tab = self.page.locator('.componentsone-secondary-item').nth(1).locator('.componentsone-last')
      
    @nvgt.wheels_and_colors_click
    def change_outer_color(self, index):
        return self.first_tab.locator('.componentsone-last-item').nth(index)
    
    @nvgt.interior_click
    def change_inner_color(self, index):
        return self.first_tab.locator('.componentsone-last-item').nth(index)
      
    @nvgt.wheels_and_colors_click
    def change_wheel(self, index):
        return self.second_tab.locator('.componentsone-last-item').nth(index)
      
    
    
    
    # @abst.canvas_action_decorator
    # def ew_fire(self, target, value):
    #     js = f"EW.fire('{target}', {value});"
    #     print(f"EW firing {js}")
    #     self.abstract.js(js)
        
    # @abst.canvas_action_decorator
    # def change_outer_color(self, index):
    #     self.ew_fire('outerChange', index)

    # @abst.canvas_action_decorator
    # def change_inner_color(self, index):
    #     self.ew_fire('innerChange', index)        

    # @abst.canvas_action_decorator
    # def change_wheel(self, index):
    #     self.ew_fire('wheelChange', index)        
        
    