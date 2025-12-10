---
layout: default
title: PaintFlow: A Unified Framework for Interactive Oil Paintings Editing and Generation
---

# PaintFlow: A Unified Framework for Interactive Oil Paintings Editing and Generation
**arXiv**：[2512.08534v1](https://arxiv.org/abs/2512.08534) · [PDF](https://arxiv.org/pdf/2512.08534.pdf)  
**作者**：Zhangli Hu, Ye Chen, Jiajun Yao, Bingbing Ni  

**一句话要点**：提出PaintFlow统一框架，通过多模态交互实现油画生成与编辑，解决风格一致性和语义控制难题。

**关键词**：油画生成, 交互编辑, 多模态框架, 风格迁移, 语义控制, 自监督学习

## 3 点简述
- 核心问题：油画数字生成与编辑因复杂笔触和风格化特性而受限，现有方法依赖训练数据分布且多针对真实照片。
- 方法要点：结合空间对齐与语义增强条件策略、基于SBR的自监督风格迁移管道，以及AdaIN特征融合，实现多模态交互控制。
- 实验或效果：系统支持参考图像、手绘草图和自然语言提示，保持统一油画风格，实验证明能精细编辑并保留艺术品质。

## 摘要（原文）

> Oil painting, as a high-level medium that blends human abstract thinking with artistic expression, poses substantial challenges for digital generation and editing due to its intricate brushstroke dynamics and stylized characteristics. Existing generation and editing techniques are often constrained by the distribution of training data and primarily focus on modifying real photographs. In this work, we introduce a unified multimodal framework for oil painting generation and editing. The proposed system allows users to incorporate reference images for precise semantic control, hand-drawn sketches for spatial structure alignment, and natural language prompts for high-level semantic guidance, while consistently maintaining a unified painting style across all outputs. Our method achieves interactive oil painting creation through three crucial technical advancements. First, we enhance the training stage with spatial alignment and semantic enhancement conditioning strategy, which map masks and sketches into spatial constraints, and encode contextual embedding from reference images and text into feature constraints, enabling object-level semantic alignment. Second, to overcome data scarcity, we propose a self-supervised style transfer pipeline based on Stroke-Based Rendering (SBR), which simulates the inpainting dynamics of oil painting restoration, converting real images into stylized oil paintings with preserved brushstroke textures to construct a large-scale paired training dataset. Finally, during inference, we integrate features using the AdaIN operator to ensure stylistic consistency. Extensive experiments demonstrate that our interactive system enables fine-grained editing while preserving the artistic qualities of oil paintings, achieving an unprecedented level of imagination realization in stylized oil paintings generation and editing.

