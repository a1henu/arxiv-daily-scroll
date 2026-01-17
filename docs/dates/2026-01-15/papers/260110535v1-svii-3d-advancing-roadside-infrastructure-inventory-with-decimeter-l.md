---
layout: default
title: SVII-3D: Advancing Roadside Infrastructure Inventory with Decimeter-level 3D Localization and Comprehension from Sparse Street Imagery
---

# SVII-3D: Advancing Roadside Infrastructure Inventory with Decimeter-level 3D Localization and Comprehension from Sparse Street Imagery
**arXiv**：[2601.10535v1](https://arxiv.org/abs/2601.10535) · [PDF](https://arxiv.org/pdf/2601.10535.pdf)  
**作者**：Chong Liu, Luxuan Fu, Yang Jia, Zhen Dong, Bisheng Yang  

**一句话要点**：提出SVII-3D框架，通过稀疏街景图像实现分米级3D定位与细粒度状态理解，以推进路边基础设施数字化。

**关键词**：稀疏街景图像, 分米级3D定位, 视觉语言模型, 基础设施数字化, 智能维护

## 3 点简述
- 核心问题：稀疏图像在基础设施数字化中面临鲁棒性不足、定位不准确和状态理解缺失的挑战。
- 方法要点：融合LoRA微调检测与空间注意力匹配，结合几何引导精炼和视觉语言模型代理，实现精准定位与状态诊断。
- 实验或效果：实验显示SVII-3D显著提升识别精度并最小化定位误差，提供可扩展、经济高效的解决方案。

## 摘要（原文）

> The automated creation of digital twins and precise asset inventories is a critical task in smart city construction and facility lifecycle management. However, utilizing cost-effective sparse imagery remains challenging due to limited robustness, inaccurate localization, and a lack of fine-grained state understanding. To address these limitations, SVII-3D, a unified framework for holistic asset digitization, is proposed. First, LoRA fine-tuned open-set detection is fused with a spatial-attention matching network to robustly associate observations across sparse views. Second, a geometry-guided refinement mechanism is introduced to resolve structural errors, achieving precise decimeter-level 3D localization. Third, transcending static geometric mapping, a Vision-Language Model agent leveraging multi-modal prompting is incorporated to automatically diagnose fine-grained operational states. Experiments demonstrate that SVII-3D significantly improves identification accuracy and minimizes localization errors. Consequently, this framework offers a scalable, cost-effective solution for high-fidelity infrastructure digitization, effectively bridging the gap between sparse perception and automated intelligent maintenance.

