---
layout: default
title: UTDesign: A Unified Framework for Stylized Text Editing and Generation in Graphic Design Images
---

# UTDesign: A Unified Framework for Stylized Text Editing and Generation in Graphic Design Images
**arXiv**：[2512.20479v1](https://arxiv.org/abs/2512.20479) · [PDF](https://arxiv.org/pdf/2512.20479.pdf)  
**作者**：Yiming Zhao, Yuanpeng Gao, Yuxuan Luo, Jiwei Duan, Shisong Lin, Longfei Xiong, Zhouhui Lian  

**一句话要点**：提出UTDesign统一框架，用于图形设计图像中的高精度风格化文本编辑与条件生成，支持中英文脚本。

**关键词**：风格化文本编辑, 条件文本生成, 图形设计图像, DiT模型, 多模态编码, 文本到设计

## 3 点简述
- 核心问题：扩散模型在图形设计中的文本渲染性能有限，尤其对小字体和非拉丁脚本如中文。
- 方法要点：基于DiT训练文本风格迁移模型生成透明RGBA文本前景，并扩展为多模态条件编码的生成框架。
- 实验或效果：在开源方法中达到风格一致性和文本准确性的先进水平，优于未知商业方法。

## 摘要（原文）

> AI-assisted graphic design has emerged as a powerful tool for automating the creation and editing of design elements such as posters, banners, and advertisements. While diffusion-based text-to-image models have demonstrated strong capabilities in visual content generation, their text rendering performance, particularly for small-scale typography and non-Latin scripts, remains limited. In this paper, we propose UTDesign, a unified framework for high-precision stylized text editing and conditional text generation in design images, supporting both English and Chinese scripts. Our framework introduces a novel DiT-based text style transfer model trained from scratch on a synthetic dataset, capable of generating transparent RGBA text foregrounds that preserve the style of reference glyphs. We further extend this model into a conditional text generation framework by training a multi-modal condition encoder on a curated dataset with detailed text annotations, enabling accurate, style-consistent text synthesis conditioned on background images, prompts, and layout specifications. Finally, we integrate our approach into a fully automated text-to-design (T2D) pipeline by incorporating pre-trained text-to-image (T2I) models and an MLLM-based layout planner. Extensive experiments demonstrate that UTDesign achieves state-of-the-art performance among open-source methods in terms of stylistic consistency and text accuracy, and also exhibits unique advantages compared to proprietary commercial approaches. Code and data for this paper are available at https://github.com/ZYM-PKU/UTDesign.

