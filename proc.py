# ======================================================================
# File: ossimg/proc.py (Library Repository)
# 
# Contains 4 core editing features: Brightness, Saturation, Sharpness, and Shadows
# Also contains preset templates and the Manual Edit sequence function.
# ======================================================================


# --- General Utility ---



# --- Feature Implementations ---

# 1. BRIGHTNESS (General Luminance Control)



# 2. SATURATION (Color Intensity Control)




# 3. SHARPNESS (Detail/Edge Control)




# 4. SHADOWS (Tonal Control - Advanced Custom Curve)




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

#grittytemplate
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
def apply_pastel_matte(img: Image.Image) -> Image.Image:
    """
    Applies a 'Soft Pastel Matte' look.
    Over-brightness and aggressive shadow lift for the matte look.
    """
    img = adjust_saturation(img, 1.10)
    img = adjust_shadows(img, 0.70)
    img = adjust_brightness(img, 1.20)
    img = adjust_sharpness(img, 0.90)
    return img




# --- MANUAL EDIT SEQUENCE (New Library Function) ---
def process_manual_edits(
    img: Image.Image, 
    saturation_factor: float, 
    shadows_amount: float, 
    brightness_factor: float, 
    sharpness_factor: float
) -> Generator[Tuple[str, Image.Image], None, None]:
    """
    Applies the four manual edits sequentially and yields the image 
    after each step, plus the name of the feature just applied.
    
    The generator yields: (feature_name, image_object)
    """
    current_img = img.copy()

    # 1. SATURATION
    current_img = adjust_saturation(current_img, saturation_factor)
    yield ("saturation", current_img)

    # 2. SHADOWS
    current_img = adjust_shadows(current_img, shadows_amount)
    yield ("shadows", current_img)

    # 3. BRIGHTNESS
    current_img = adjust_brightness(current_img, brightness_factor)
    yield ("brightness", current_img)

    # 4. SHARPNESS
    current_img = adjust_sharpness(current_img, sharpness_factor)
    yield ("sharpness", current_img)

    
# Do not forget to keep the setup.py file in the outer ossimg directory!