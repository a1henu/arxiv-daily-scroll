---
layout: default
title: UM-Text: A Unified Multimodal Model for Image Understanding
---

# UM-Text: A Unified Multimodal Model for Image Understanding
**arXiv**：[2601.08321v1](https://arxiv.org/abs/2601.08321) · [PDF](https://arxiv.org/pdf/2601.08321.pdf)  
**作者**：Lichen Ma, Xiaolong Fu, Gaojing Zhou, Zipeng Guo, Ting Zhu, Yichun Liu, Yu Shi, Jason Li, Junshi Huang  

**一句话要点**：提出UM-Text统一多模态模型，通过自然语言指令实现图像理解和视觉文本编辑。

**关键词**：视觉文本编辑, 多模态模型, 自然语言指令, 风格一致性, 区域一致性损失, 大规模数据集

## 3 点简述
- 核心问题：视觉文本编辑需理解指令和参考图像，保持风格一致性，现有方法常忽略此点。
- 方法要点：引入视觉语言模型处理指令和图像，结合UM-Encoder自动配置条件嵌入，采用区域一致性损失和三阶段训练策略。
- 实验或效果：在多个公开基准测试中实现最先进性能，并贡献UM-DATA-200K大规模数据集。

## 摘要（原文）

> With the rapid advancement of image generation, visual text editing using natural language instructions has received increasing attention. The main challenge of this task is to fully understand the instruction and reference image, and thus generate visual text that is style-consistent with the image. Previous methods often involve complex steps of specifying the text content and attributes, such as font size, color, and layout, without considering the stylistic consistency with the reference image. To address this, we propose UM-Text, a unified multimodal model for context understanding and visual text editing by natural language instructions. Specifically, we introduce a Visual Language Model (VLM) to process the instruction and reference image, so that the text content and layout can be elaborately designed according to the context information. To generate an accurate and harmonious visual text image, we further propose the UM-Encoder to combine the embeddings of various condition information, where the combination is automatically configured by VLM according to the input instruction. During training, we propose a regional consistency loss to offer more effective supervision for glyph generation on both latent and RGB space, and design a tailored three-stage training strategy to further enhance model performance. In addition, we contribute the UM-DATA-200K, a large-scale visual text image dataset on diverse scenes for model training. Extensive qualitative and quantitative results on multiple public benchmarks demonstrate that our method achieves state-of-the-art performance.

