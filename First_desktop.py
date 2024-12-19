
import ipywidgets as widgets
from IPython.display import display

# ایجاد ویجت‌های انتخاب رمز ارز و مدل
crypto_dropdown = widgets.Dropdown(
    options=['Bitcoin', 'Ethereum', 'Litecoin'],
    value='Bitcoin',
    description='رمز ارز:',
)

model_dropdown = widgets.Dropdown(
    options=['مدل 1', 'مدل 2', 'مدل 3'],
    value='مدل 1',
    description='مدل:',
)

process_button = widgets.Button(description="پردازش")

# تابعی برای نمایش انتخاب‌ها و پردازش‌ها
def on_button_click(b):
    crypto_choice = crypto_dropdown.value
    model_choice = model_dropdown.value
    print(f"پردازش رمز ارز: {crypto_choice} با مدل: {model_choice}")

process_button.on_click(on_button_click)

# نمایش ویجت‌ها
display(crypto_dropdown, model_dropdown, process_button)
