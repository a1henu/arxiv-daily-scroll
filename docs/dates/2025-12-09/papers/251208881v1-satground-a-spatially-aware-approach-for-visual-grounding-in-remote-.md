---
layout: default
title: SATGround: A Spatially-Aware Approach for Visual Grounding in Remote Sensing
---

# SATGround: A Spatially-Aware Approach for Visual Grounding in Remote Sensing
**arXiv**：[2512.08881v1](https://arxiv.org/abs/2512.08881) · [PDF](https://arxiv.org/pdf/2512.08881.pdf)  
**作者**：Aysim Toker, Andreea-Maria Oncescu, Roy Miles, Ismail Elezi, Jiankang Deng  

**一句话要点**：提出SATGround方法，通过结构化定位机制增强遥感图像中的视觉定位能力。

**关键词**：视觉语言模型, 遥感图像, 视觉定位, 结构化定位, 控制令牌, 联合推理

## 3 点简述
- 核心问题：遥感图像中视觉语言模型的视觉定位精度不足，需提升复杂场景下的对象定位能力。
- 方法要点：微调预训练视觉语言模型，结合专用定位模块和特殊控制令牌，实现语言与空间信息的联合推理。
- 实验或效果：在多个遥感基准测试中显著提升性能，视觉定位任务相对改进24.8%，优于现有方法。

## 摘要（原文）

> Vision-language models (VLMs) are emerging as powerful generalist tools for remote sensing, capable of integrating information across diverse tasks and enabling flexible, instruction-based interactions via a chat interface. In this work, we enhance VLM-based visual grounding in satellite imagery by proposing a novel structured localization mechanism. Our approach involves finetuning a pretrained VLM on a diverse set of instruction-following tasks, while interfacing a dedicated grounding module through specialized control tokens for localization. This method facilitates joint reasoning over both language and spatial information, significantly enhancing the model's ability to precisely localize objects in complex satellite scenes. We evaluate our framework on several remote sensing benchmarks, consistently improving the state-of-the-art, including a 24.8% relative improvement over previous methods on visual grounding. Our results highlight the benefits of integrating structured spatial reasoning into VLMs, paving the way for more reliable real-world satellite data analysis.

