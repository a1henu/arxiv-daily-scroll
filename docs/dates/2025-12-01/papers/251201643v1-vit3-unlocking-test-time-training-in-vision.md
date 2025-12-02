---
layout: default
title: ViT$^3$: Unlocking Test-Time Training in Vision
---

# ViT$^3$: Unlocking Test-Time Training in Vision
**arXiv**：[2512.01643v1](https://arxiv.org/abs/2512.01643) · [PDF](https://arxiv.org/pdf/2512.01643.pdf)  
**作者**：Dongchen Han, Yining Li, Tianyu Li, Zixuan Cao, Ziming Wang, Jun Song, Yu Cheng, Bo Zheng, Gao Huang  

**一句话要点**：提出ViT^3模型，通过系统研究测试时训练设计，实现视觉序列建模的线性复杂度与并行计算。

**关键词**：测试时训练, 视觉序列建模, 线性复杂度, 注意力机制, 在线学习, 视觉Transformer

## 3 点简述
- 核心问题：视觉测试时训练缺乏设计原则与实用指南，导致性能受限。
- 方法要点：将注意力操作重构为在线学习问题，构建紧凑内部模型，实现线性计算复杂度。
- 实验或效果：在图像分类、生成、检测和分割任务中，ViT^3匹配或超越先进线性模型，缩小与优化Transformer的差距。

## 摘要（原文）

> Test-Time Training (TTT) has recently emerged as a promising direction for efficient sequence modeling. TTT reformulates attention operation as an online learning problem, constructing a compact inner model from key-value pairs at test time. This reformulation opens a rich and flexible design space while achieving linear computational complexity. However, crafting a powerful visual TTT design remains challenging: fundamental choices for the inner module and inner training lack comprehensive understanding and practical guidelines. To bridge this critical gap, in this paper, we present a systematic empirical study of TTT designs for visual sequence modeling. From a series of experiments and analyses, we distill six practical insights that establish design principles for effective visual TTT and illuminate paths for future improvement. These findings culminate in the Vision Test-Time Training (ViT$^3$) model, a pure TTT architecture that achieves linear complexity and parallelizable computation. We evaluate ViT$^3$ across diverse visual tasks, including image classification, image generation, object detection, and semantic segmentation. Results show that ViT$^3$ consistently matches or outperforms advanced linear-complexity models (e.g., Mamba and linear attention variants) and effectively narrows the gap to highly optimized vision Transformers. We hope this study and the ViT$^3$ baseline can facilitate future work on visual TTT models. Code is available at https://github.com/LeapLabTHU/ViTTT.

