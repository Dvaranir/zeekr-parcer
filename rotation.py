from abstract import AbstractController as abst

class RotationController:
    
    def __init__(self, page, canvas_element, abstract):
        self.page = page
        self.canvas_element = canvas_element
        self.abstract = abstract
        self.rotations = [
            self.rotate_angle,
            self.rotate_up,
            self.rotate_profile,
            self.rotate_front,
            self.rotate_front_edge,
            self.rotate_back,
            self.rotate_back_edge,
            self.rotate_front_wheel,
            self.rotate_back_wheel,
        ]
        
    @abst.canvas_action_decorator
    def rotate(self, x, y, vector=None, partial=None):
        msg = f"Starting rotation: x={x} y={y}"
        print(msg)
        self.abstract.add_to_log(msg)
        target_y = "CameraHandle.camScript.targetRotY"
        target_x = "CameraHandle.camScript.targetRotX"
        
        camera_y = self.abstract.js(target_y)

        if camera_y:
            
            js_x = f"{target_x} = '{x}';"
            js_y = f"{target_y} = '{y}';"
            
            if partial:
                self.abstract.js(js_x)
                abst.focus_canvas(self)
                abst.tiny_timeout(self)
                self.abstract.js(js_y)
                abst.focus_canvas(self)
            else:
                js = js_x + js_y                
                self.abstract.js(js)
                
            if vector:
                abst.tiny_timeout(self)
                js = f"CameraHandle.camScript.targetViewPos = new pc.Vec3({vector});"
                self.abstract.js(js)
                
            new_camera_x = self.abstract.js(target_x)
            new_camera_y = self.abstract.js(target_y)
            
            if int(new_camera_x) != int(x) or int(new_camera_y) != int(y):
                self.rotate(x, y)
            
            msg = "Rotation done"
            print(msg)
            self.abstract.add_to_log(msg)
            
        else: self.rotate(x, y)
        
    def zoom(self, distance, speed=-1):
        abst.tiny_timeout(self)
        js = f"CameraHandle.camScript.zoomLerpSpeed = {speed};"
        self.abstract.js(js)
        abst.focus_canvas(self)
        abst.tiny_timeout(self)
        js = f"CameraHandle.camScript.distance = {distance};"
        self.abstract.js(js)
        abst.focus_canvas(self)
        abst.tiny_timeout(self)
        
    def init_zoom(self):
        self.zoom(12)
        
    def wheel_zoom(self):
        self.zoom(7)
        
    def rotate_front(self):
        self.rotate(0, -90)
        self.position = 'Front'
        
    def rotate_front_edge(self):
        self.rotate(-10, -90, partial=True)
        self.position = 'Front Inclined'
        
    def rotate_back(self):
        self.rotate(0, 90)
        self.position = 'Back'
        
    def rotate_back_edge(self):
        self.rotate(-10, 90, partial=True)
        self.position = 'Back Inclined'
        
    def rotate_profile(self):
        self.rotate(0, 0)
        self.position = 'Side'
        
    def rotate_up(self):
        self.rotate(-90, 180, partial=True)
        self.position = 'Roof'
        
    def rotate_front_wheel(self):
        self.wheel_zoom()
        self.rotate(0, 0, "-1.2, 1, 0")
        self.position = 'Front Wheel'
        
    def rotate_back_wheel(self):
        self.wheel_zoom()
        self.rotate(0, 0, "1.2, 1, 0")
        self.position = 'Back Wheel'
        
    def rotate_angle(self):
        self.position = 'Angle'
        return
