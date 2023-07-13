from abstract import AbstractController as abst

class RotationController:
    
    def __init__(self, page, canvas_element, abstract):
        self.page = page
        self.canvas_element = canvas_element
        self.abstract = abstract
        self.rotations = [
            self.rotate_front,
            self.rotate_front_edge,
            self.rotate_back,
            self.rotate_back_edge,
            self.rotate_profile,
            self.rotate_up,
            self.rotate_front_wheel,
            self.rotate_back_wheel,
        ]
        
    @abst.canvas_action_decorator
    def rotate(self, x, y, vector=None):
        print(f"Starting basic rotation: x={x} y={y}")
        target_y = "CameraHandle.camScript.targetRotY"
        target_x = "CameraHandle.camScript.targetRotX"
        
        camera_y = self.abstract.js(target_y)

        if camera_y:
            js = f"{target_x} = {x}; {target_y} = {y};"
            
            if vector:
                js += f"CameraHandle.camScript.targetViewPos = new pc.Vec3({vector});"  
                
            self.abstract.js(js)
            
            new_camera_x = self.abstract.js(target_x)
            new_camera_y = self.abstract.js(target_y)
            
            if new_camera_x != x or new_camera_y != y:
                self.rotate(x, y)
                
            print("Rotation done")
            
        else: self.rotate(x, y)
        
    def zoom(self, distance, speed=-1):
        js = f"CameraHandle.camScript.zoomLerpSpeed = {speed}; CameraHandle.camScript.distance = {distance};"
        self.abstract.js(js)
        
    def init_zoom(self):
        self.zoom(12)
        
    def wheel_zoom(self):
        self.zoom(7)
        
    def rotate_front(self):
        self.rotate(0, -90)
        self.position = 'Front'
        
    def rotate_front_edge(self):
        self.rotate(-10, -90)
        self.position = 'Front Inclined'
        
    def rotate_back(self):
        self.rotate(0, 90)
        self.position = 'Back'
        
    def rotate_back_edge(self):
        self.rotate(-10, 90)
        self.position = 'Back Inclined'
        
    def rotate_profile(self):
        self.rotate(0, 0)
        self.position = 'Side'
        
    def rotate_up(self):
        self.rotate(-90, 180)
        self.position = 'Roof'
        
    def rotate_front_wheel(self):
        self.wheel_zoom()
        self.rotate(0, 0, "-1.2, 1, 0")
        self.position = 'Front Wheel'
        
    def rotate_back_wheel(self):
        self.wheel_zoom()
        self.rotate(0, 0, "1.2, 1, 0")
        self.position = 'Back Wheel'

        
    
        
        
    # def init_zoom(self):
        