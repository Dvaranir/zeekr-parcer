from abstract import AbstractController as abst

class RotationController:
    
    def __init__(self, page, canvas_element, abstract):
        self.page = page
        self.canvas_element = canvas_element
        self.abstract = abstract
        self.rotations = [
            self.rotate_profile,
            self.rotate_front,
            self.rotate_front_edge,
            self.rotate_back,
            self.rotate_back_edge,
            self.rotate_front_wheel,
            self.rotate_back_wheel,
            self.rotate_up,
            self.rotate_angle,
        ]
        
    def rotate_front(self):
        self.abstract.js('document.rotateFrontal()')
        self.position = 'Front'
        print(self.position)
        
    def rotate_front_edge(self):
        self.abstract.js('document.rotateFrontalAngle()')
        self.position = 'Front Inclined'
        print(self.position)
        
    def rotate_back(self):
        self.abstract.js('document.rotateBack()')
        self.position = 'Back'
        print(self.position)
        
    def rotate_back_edge(self):
        self.abstract.js('document.rotateBackAngle()')
        self.position = 'Back Inclined'
        print(self.position)
        
    def rotate_profile(self):
        self.abstract.js('document.rotateProfile()')
        self.position = 'Side'
        print(self.position)
        
    def rotate_up(self):
        self.abstract.js('document.rotateRoof()')
        self.position = 'Roof'
        print(self.position)
        
    def rotate_front_wheel(self):
        self.abstract.js('document.rotateFrontWheel()')
        self.position = 'Front Wheel'
        print(self.position)
        
    def rotate_back_wheel(self):
        self.abstract.js('document.rotateBackWheel()')
        self.position = 'Back Wheel'
        print(self.position)
        
    def rotate_angle(self):
        self.position = 'Angle'
        print(self.position)
        return
