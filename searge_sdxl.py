"""

Custom nodes for SDXL in ComfyUI

MIT License

Copyright (c) 2023 Searge

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

"""


from .modules.prompt_text_input import SeargeTextInputV2
from .modules.prompt_adapter import SeargePromptAdapterV2
from .modules.image_adapter import SeargeImageAdapterV2
from .modules.controlnet_adapter import SeargeControlnetAdapterV2

from .modules.ui_separator import SeargeSeparator
from .modules.ui_preview_image import SeargePreviewImage

from .modules.ui_model_selector import SeargeModelSelector
from .modules.ui_upscale_models import SeargeUpscaleModels
from .modules.ui_loras import SeargeLoras
from .modules.ui_controlnet_models import SeargeControlnetModels

from .modules.ui_generation_parameters import SeargeGenerationParameters
from .modules.ui_conditioning_parameters import SeargeConditioningParameters
from .modules.ui_advanced_parameters import SeargeAdvancedParameters
from .modules.ui_image_saving import SeargeImageSaving
from .modules.ui_operating_mode import SeargeOperatingMode
from .modules.ui_img2img_inpaint import SeargeImage2ImageAndInpainting
from .modules.ui_custom_prompt_mode import SeargeCustomPromptMode
from .modules.ui_prompt_styles import SeargePromptStyles
from .modules.ui_high_resolution import SeargeHighResolution
from .modules.ui_condition_mixing import SeargeConditionMixing

from .modules.magic_box import SeargeMagicBox
from .modules.mb_pipeline_start import SeargePipelineStart
from .modules.mb_pipeline_terminator import SeargePipelineTerminator

from .modules.after_vae_decode import SeargeCustomAfterVaeDecode
from .modules.after_upscaling import SeargeCustomAfterUpscaling

from .modules.debug_printer import SeargeDebugPrinter

# from .modules.sdxl_sampler import SeargeSDXLSamplerV4
# from .modules.sdxl_sampler_input import SeargeSDXLSamplerV4Inputs
# from .modules.sdxl_sampler_output import SeargeSDXLSamplerV4Outputs

# from .modules.prompt_adapter_output import SeargePromptAdapterV2Output

# ====================================================================================================
# Register nodes in ComfyUI
# ====================================================================================================

SEARGE_CLASS_MAPPINGS = {
    "SeargeTextInputV2": SeargeTextInputV2,
    "SeargePromptAdapterV2": SeargePromptAdapterV2,
    "SeargeImageAdapterV2": SeargeImageAdapterV2,
    "SeargeControlnetAdapterV2": SeargeControlnetAdapterV2,
    "SeargeSeparator": SeargeSeparator,
    "SeargePreviewImage": SeargePreviewImage,
    "SeargeAdvancedParameters": SeargeAdvancedParameters,
    "SeargeConditioningParameters": SeargeConditioningParameters,
    "SeargeConditionMixing": SeargeConditionMixing,
    "SeargeControlnetModels": SeargeControlnetModels,
    "SeargeCustomPromptMode": SeargeCustomPromptMode,
    "SeargeGenerationParameters": SeargeGenerationParameters,
    "SeargeHighResolution": SeargeHighResolution,
    "SeargeImage2ImageAndInpainting": SeargeImage2ImageAndInpainting,
    "SeargeImageSaving": SeargeImageSaving,
    "SeargeLoras": SeargeLoras,
    "SeargeModelSelector": SeargeModelSelector,
    "SeargeOperatingMode": SeargeOperatingMode,
    "SeargePromptStyles": SeargePromptStyles,
    "SeargeUpscaleModels": SeargeUpscaleModels,
    "SeargeMagicBox": SeargeMagicBox,
    "SeargePipelineStart": SeargePipelineStart,
    "SeargePipelineTerminator": SeargePipelineTerminator,
    "SeargeCustomAfterVaeDecode": SeargeCustomAfterVaeDecode,
    "SeargeCustomAfterUpscaling": SeargeCustomAfterUpscaling,
    "SeargeDebugPrinter": SeargeDebugPrinter,
}

# SEARGE_CLASS_MAPPINGS = SEARGE_CLASS_MAPPINGS | {
#     f"SeargeSDXLSamplerV4": SeargeSDXLSamplerV4,
#     f"SeargeSDXLSamplerV4Inputs": SeargeSDXLSamplerV4Inputs,
#     f"SeargeSDXLSamplerV4Outputs": SeargeSDXLSamplerV4Outputs,
#
#     f"SeargePromptAdapterV2Output": SeargePromptAdapterV2Output,
# }

# ====================================================================================================
# Human readable names for the nodes
# ====================================================================================================

SEARGE_DISPLAY_NAME_MAPPINGS = {
    "SeargeTextInputV2": "Text Input v2",
    "SeargePromptAdapterV2": "Prompt Adapter v2",
    "SeargeImageAdapterV2": "Image Adapter v2",
    "SeargeControlnetAdapterV2": "Controlnet Adapter v2",
    "SeargeSeparator": "Separator",
    "SeargePreviewImage": "SeargePreviewImage",
    "SeargeAdvancedParameters": "Advanced Parameters v2",
    "SeargeConditioningParameters": "Conditioning Parameters v2",
    "SeargeConditionMixing": "Condition Mixing v2",
    "SeargeControlnetModels": "Controlnet Models Selector v2",
    "SeargeCustomPromptMode": "Custom Prompt Mode v2",
    "SeargeGenerationParameters": "Generation Parameters v2",
    "SeargeHighResolution": "High Resolution v2",
    "SeargeImage2ImageAndInpainting": "Image to Image and Inpainting v2",
    "SeargeImageSaving": "Image Saving v2",
    "SeargeLoras": "Lora Selector v2",
    "SeargeModelSelector": "Model Selector v2",
    "SeargeOperatingMode": "Operating Mode v2",
    "SeargePromptStyles": "Prompt Styles v2",
    "SeargeUpscaleModels": "Upscale Models Selector v2",
    "SeargeMagicBox": "Searge's Magic Box for SDXL",
    "SeargePipelineStart": "Magic Box Pipeline Start",
    "SeargePipelineTerminator": "Magic Box Pipeline Terminator",
    "SeargeCustomAfterVaeDecode": "After VAE Decode",
    "SeargeCustomAfterUpscaling": "After Upscaling",
    "SeargeDebugPrinter": "Debug Printer",
}

# SEARGE_DISPLAY_NAME_MAPPINGS = SEARGE_DISPLAY_NAME_MAPPINGS | {
#     f"SeargeSDXLSamplerV4": "SDXL Sampler v4",
#     f"SeargeSDXLSamplerV4Inputs": "SDXL Sampler v4 Inputs",
#     f"SeargeSDXLSamplerV4Outputs": "SDXL Sampler v4 Outputs",
#
#     f"SeargePromptAdapterV2Output": "Prompt Adapter v2 Output",
# }
