from phue import Bridge

from ip_address import bridge_ip_address

def get_bridge(bridge_ip_address):
    b = Bridge(bridge_ip_address)
    return b

def get_light_names(bridge_ip_address):
    b = Bridge(bridge_ip_address)
    light_name_list = b.get_light_objects('name')
    return light_name_list

def film_lights():
    lights = get_light_names(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = '10000'
        lights[light].saturation = 200
        lights[light].brightness = 75

def red_lights():
    lights = get_light_names(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = '1000'
        lights[light].saturation = 255

def green_lights():
    lights = get_light_names(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = '25000'
        lights[light].saturation = 255

def cyan_lights():
    lights = get_light_names(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = '40000'
        lights[light].saturation = 255

def purple_lights():
    lights = get_light_names(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = '50000'
        lights[light].saturation = 255

def pink_lights():
    lights = get_light_names(bridge_ip_address)
    for light in lights:
        lights[light].on = True
        lights[light].hue = '60000'
        lights[light].saturation = 255

def print_lights():
    lights = get_light_names(bridge_ip_address)
    for light in lights:
        print(light)

def set_brightness_half():
    lights = get_light_names(bridge_ip_address)
    for light in lights:
        lights[light].brightness = 127

def set_brightness_max():
    lights = get_light_names(bridge_ip_address)
    for light in lights:
        lights[light].brightness = 254

def get_schedules():
    b = get_bridge(bridge_ip_address)
    b.get_schedule()

def set_left_lamp():
    lights = get_light_names(bridge_ip_address)
    lights["Your lamp name here"].brightness = 127

def set_right_lamp():
    lights = get_light_names(bridge_ip_address)
    lights["Your lamp name here"].brightness = 127

def print_lamp_is_on():
    b = get_bridge(bridge_ip_address)
    print(b.get_light('Your lamp name here', 'on'))

def color_loop():
    lights = get_light_names(bridge_ip_address)
    for light in lights:
        lights[light].effect = 'colorloop'

def stop_color_loop():
    lights = get_light_names(bridge_ip_address)
    for light in lights:
        lights[light].effect = 'none'

# Fill in the function you want to run
if __name__ == '__main__':
   new_lights()