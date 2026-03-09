---
layout: default
title: FontUse: A Data-Centric Approach to Style- and Use-Case-Conditioned In-Image Typography
---

# FontUse: A Data-Centric Approach to Style- and Use-Case-Conditioned In-Image Typography
**arXiv**：[2603.06038v1](https://arxiv.org/abs/2603.06038) · [PDF](https://arxiv.org/pdf/2603.06038.pdf)  
**作者**：Xia Xin, Yuki Endo, Yoshihiro Kanamori  

**一句话要点**：提出FontUse数据驱动方法，通过结构化标注训练图像生成模型，以解决文本到图像模型中排版控制不足的问题。

**关键词**：排版控制, 数据驱动方法, 图像生成, 多模态标注, 字体风格, 使用案例

## 3 点简述
- 核心问题：现有文本到图像模型在生成图像时难以精确控制排版样式，常忽略或弱化用户指定的字体风格和使用场景。
- 方法要点：构建大规模排版数据集FontUse，约70K图像，利用分割模型和多模态大语言模型自动标注字体风格、使用案例和文本区域。
- 实验或效果：通过微调现有生成器，无需架构修改，显著提升排版与提示的一致性，并引入基于Long-CLIP的评估指标验证效果。

## 摘要（原文）

> Recent text-to-image models can generate high-quality images from natural-language prompts, yet controlling typography remains challenging: requested typographic appearance is often ignored or only weakly followed. We address this limitation with a data-centric approach that trains image generation models using targeted supervision derived from a structured annotation pipeline specialized for typography. Our pipeline constructs a large-scale typography-focused dataset, FontUse, consisting of about 70K images annotated with user-friendly prompts, text-region locations, and OCR-recognized strings. The annotations are automatically produced using segmentation models and multimodal large language models (MLLMs). The prompts explicitly combine font styles (e.g., serif, script, elegant) and use cases (e.g., wedding invitations, coffee-shop menus), enabling intuitive specification even for novice users. Fine-tuning existing generators with these annotations allows them to consistently interpret style and use-case conditions as textual prompts without architectural modification. For evaluation, we introduce a Long-CLIP-based metric that measures alignment between generated typography and requested attributes. Experiments across diverse prompts and layouts show that models trained with our pipeline produce text renderings more consistent with prompts than competitive baselines. The source code for our annotation pipeline is available at https://github.com/xiaxinz/FontUSE.

