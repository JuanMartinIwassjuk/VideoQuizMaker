import json

class Animation:
    def __init__(self, time="", duration="", easing="", type="", direction="", split="", scope="", fade="", start_scale="", distance="", x_anchor="", y_anchor="", end_angle="", start_angle="", transition="", background_effect="", reversed=""):
        self.time = time
        self.duration = duration
        self.easing = easing
        self.type = type
        self.direction = direction
        self.split = split
        self.scope = scope
        self.fade = fade
        self.start_scale = start_scale
        self.distance = distance
        self.x_anchor = x_anchor
        self.y_anchor = y_anchor
        self.end_angle = end_angle
        self.start_angle = start_angle
        self.transition = transition
        self.background_effect = background_effect
        self.reversed = reversed

class Audio:
    def __init__(self, name, track, time, duration, dynamic, source, volume, audio_fade_out):
        self.type = "audio"
        self.name = name
        self.track = track
        self.time = time
        self.duration = duration
        self.dynamic = dynamic
        self.source = source
        self.volume = volume
        self.audio_fade_out = audio_fade_out

class Image:
    def __init__(self, source, track, duration, clip, animations=[], type="image",x="", y="",border_radius="", width="", height="", time=0):
        self.type = type
        self.source = source
        self.track = track
        self.duration = duration
        self.clip = clip
        self.animations = [Animation(**anim) for anim in animations] if animations else []
        self.time = time

        if (y != ""):
            self.y = y
            self.width = width
            self.height = height
        if (x != ""):
            self.x = x
        if (border_radius != ""):
            self.border_radius = border_radius

class Element:
    def __init__(self, type, track, animations=[], y="", x="", width="", height="", x_alignment="", y_alignment="", text="", font_family="", font_weight="600", font_size_maximum="", fill_color="", stroke_color="", stroke_width="", background_color="", z_index="", time="", duration="", font_size=""):
        self.type = type
        self.track = track
        self.animations = [Animation(**anim) for anim in animations] if animations else []
        self.y = y
        self.x = "50%"
        self.width = "90.48%"
        self.height = "15.12%"
        self.x_alignment = "50%"
        self.y_alignment = "5%"
        self.text = text
        self.font_family = "Montserrat"
        self.font_weight = font_weight
        self.font_size_maximum = "6 vmin"
        self.fill_color = fill_color
        self.stroke_width = "1.5 vmin"
        self.background_color = background_color
        self.stroke_color = stroke_color

        if time != "":
            self.time = time
            self.duration = duration
            self.z_index = z_index
            self.font_size = font_size
class Composition:
    def __init__(self, name, track, duration, elements=[]):
        self.name = name
        self.type = "composition"
        self.track = track
        self.duration = duration
        self.elements = [Element(**elem) for elem in elements]
        self.animations = []

class Source:
    def __init__(self, output_format, width, height, duration, elements=[]):
        self.output_format = output_format
        self.width = width
        self.height = height
        self.duration = duration
        self.elements = [Element(**elem) for elem in elements]

class Video:
    def __init__(self, source):
        self.source = source
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)