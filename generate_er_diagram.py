from PIL import Image, ImageDraw, ImageFont

width, height = 1100, 700
bg_color = (255, 255, 255)
box_color = (40, 116, 166)
text_color = (255, 255, 255)
line_color = (0, 0, 0)

img = Image.new('RGB', (width, height), bg_color)
draw = ImageDraw.Draw(img)
font_title = ImageFont.load_default()
font_body = ImageFont.load_default()

# Draw ML_MODEL box
ml_box = (80, 120, 520, 420)
draw.rectangle(ml_box, fill=box_color, outline=line_color, width=2)
draw.text((110, 130), 'ML_MODEL', fill=text_color, font=font_title)
attrs = [
    'model_id PK',
    'name',
    'version',
    'file_path',
    'feature_list',
    'created_at'
]
y = 170
for attr in attrs:
    draw.text((110, y), f'- {attr}', fill=text_color, font=font_body)
    y += 28

# Draw HDI_PREDICTION box
hd_box = (620, 120, 1040, 520)
draw.rectangle(hd_box, fill=(85, 139, 47), outline=line_color, width=2)
draw.text((650, 130), 'HDI_PREDICTION', fill=text_color, font=font_title)
attrs = [
    'prediction_id PK',
    'life_expectancy',
    'mean_years_schooling',
    'expected_years_schooling',
    'gni_per_capita',
    'predicted_hdi',
    'hdi_category',
    'predicted_at',
    'model_id FK'
]
y = 170
for attr in attrs:
    draw.text((650, y), f'- {attr}', fill=text_color, font=font_body)
    y += 28

# Draw relationship arrow
arrow_start = (520, 270)
arrow_end = (620, 270)
draw.line([arrow_start, arrow_end], fill=line_color, width=4)
# Arrow head
arrow_head = [(620, 270), (600, 260), (600, 280)]
draw.polygon(arrow_head, fill=line_color)

draw.text((340, 80), 'Entity Relationship Diagram', fill=(0,0,0), font=font_title)
img.save('ER_diagram.jpg', 'JPEG')
print('Saved ER_diagram.jpg')
