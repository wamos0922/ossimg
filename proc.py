# ======================================================================
# File: ossimg/proc.py (Library Repository)
# 
# Contains 4 core editing features: Brightness, Saturation, Sharpness, and Shadows
# Also contains preset templates and the Manual Edit sequence function.
# ======================================================================
from PIL import Image, ImageEnhance
import math
from typing import Generator, Tuple, Union

# --- General Utility ---

def load_image(path: str) -> Image.Image:
    """Loads an image from a file path."""
    return Image.open(path)

# --- Feature Implementations ---

# 1. BRIGHTNESS (General Luminance Control)
def adjust_brightness(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjusts the overall brightness of the image.
    Factor 1.0 = original, > 1.0 = brighter, < 1.0 = darker.
    """
    if not isinstance(img, Image.Image):
        raise TypeError("Input must be a PIL Image object.")
    
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)

# 2. SATURATION (Color Intensity Control)
def adjust_saturation(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjusts the intensity of colors (saturation).
    
    Factor 1.0 = original, 0.0 = grayscale, > 1.0 = more vibrant colors.
    """
    if not isinstance(img, Image.Image):
        raise TypeError("Input must be a PIL Image object.")
        
    enhancer = ImageEnhance.Color(img)
    return enhancer.enhance(factor)




# 3. SHARPNESS (Detail/Edge Control)
def adjust_sharpness(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjusts the image sharpness.
    
    Factor 1.0 = original, > 1.0 = sharper, < 1.0 = blurrier.
    """
    if not isinstance(img, Image.Image):
        raise TypeError("Input must be a PIL Image object.")
        
    enhancer = ImageEnhance.Sharpness(img)
    return enhancer.enhance(factor)



# 4. SHADOWS (Tonal Control - Advanced Custom Curve)
def adjust_shadows(img: Image.Image, amount: float) -> Image.Image:
    """
    Lifts or darkens the shadow areas (darkest pixels) without affecting 
    the brightest areas significantly. Positive amount lifts shadows.
    """
    if not isinstance(img, Image.Image):
        raise TypeError("Input must be a PIL Image object.")
        
    img = img.convert("RGB")
    
    def shadow_curve(x):
        # Applies a gamma-like curve only to dark pixels (for shadows)
        x_norm = x / 255.0
        # Ensure the amount is clipped to prevent extreme gamma values
        gamma_exponent = max(-2.0, min(2.0, -amount))
        gamma = math.pow(2, gamma_exponent) 
        result_norm = math.pow(x_norm, gamma)
        return int(result_norm * 255)

    lut = [shadow_curve(i) for i in range(256)]
    
    # Apply the custom lookup table to all three RGB channels
    return img.point(lut * 3)



# --- TEMPLATE FUNCTIONS (Library Presets) ---

#goldenhourtemplate
def apply_golden_hour(img: Image.Image) -> Image.Image:
    """
    Applies a warm, soft 'Golden Hour' look.
    Uses Saturation to boost warm colors, Brightness for overall glow.
    """
    img = adjust_saturation(img, 1.30) 
    img = adjust_shadows(img, 0.30)
    img = adjust_brightness(img, 1.15)
    img = adjust_sharpness(img, 0.80)
    return img

def apply_gritty_contrast(img: Image.Image) -> Image.Image:
    """
    Applies an 'Urban Gritty Contrast' look.
    Low saturation and crushed shadows for high contrast.
    """
    img = adjust_sharpness(img, 2.50)
    img = adjust_brightness(img, 0.90)
    img = adjust_shadows(img, -0.20)
    img = adjust_saturation(img, 0.80) 
    return img
#pastelTemplate





# --- MANUAL EDIT SEQUENCE (New Library Function) ---


    
# Do not forget to keep the setup.py file in the outer ossimg directory!