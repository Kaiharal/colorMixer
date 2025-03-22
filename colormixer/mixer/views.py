from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    mixed_color = ""
    
    if request.method == "POST":
        color1 = request.POST.get("color1")
        color2 = request.POST.get("color2")
        
        if is_valid_hex(color1) and is_valid_hex(color2):
            mixed_color = mix_colors(color1, color2)
        else:
            mixed_color = "Invalid hex codes. Please use a valid color code (e.g., #FF5733)."
    
    return render(request, "index.html", {"mixed_color": mixed_color})

def is_valid_hex(color):
    if color and color.startswith("#") and len(color) == 7:
        try:
            int(color[1:], 16)
            return True
        except ValueError:
            return False
    return False

# thank you ChatGPT for helping me get a quick way to mix color codes!

def mix_colors(color1, color2):
    rgb1 = hex_to_rgb(color1)
    rgb2 = hex_to_rgb(color2)
    
    mixed_rgb = [(a + b) // 2 for a, b in zip(rgb1, rgb2)]
    
    return rgb_to_hex(mixed_rgb)

def hex_to_rgb(hex):
    return [int(hex[i:i+2], 16) for i in range(1, 7, 2)]

def rgb_to_hex(rgb):
    return f"#{''.join([f'{x:02x}' for x in rgb])}"
