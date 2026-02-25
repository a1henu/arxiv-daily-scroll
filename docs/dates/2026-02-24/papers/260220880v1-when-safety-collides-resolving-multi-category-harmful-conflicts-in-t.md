---
layout: default
title: When Safety Collides: Resolving Multi-Category Harmful Conflicts in Text-to-Image Diffusion via Adaptive Safety Guidance
---

# When Safety Collides: Resolving Multi-Category Harmful Conflicts in Text-to-Image Diffusion via Adaptive Safety Guidance
**arXiv**：[2602.20880v1](https://arxiv.org/abs/2602.20880) · [PDF](https://arxiv.org/pdf/2602.20880.pdf)  
**作者**：Yongli Xiang, Ziming Hong, Zhaoqing Wang, Xiangyu Zhao, Bo Han, Tongliang Liu  

**一句话要点**：提出冲突感知自适应安全引导以解决文本到图像扩散中多类别有害冲突问题

**关键词**：文本到图像扩散, 安全引导, 多类别冲突, 自适应框架, 训练免费方法

## 3 点简述
- 核心问题：现有安全引导方法在多有害类别间存在冲突，缓解一类可能加剧另一类。
- 方法要点：通过冲突感知类别识别和冲突解决引导应用，动态选择并应用类别对齐的安全方向。
- 实验或效果：在T2I安全基准上实现最先进性能，有害率降低高达15.4%。

## 摘要（原文）

> Text-to-Image (T2I) diffusion models have demonstrated significant advancements in generating high-quality images, while raising potential safety concerns regarding harmful content generation. Safety-guidance-based methods have been proposed to mitigate harmful outputs by steering generation away from harmful zones, where the zones are averaged across multiple harmful categories based on predefined keywords. However, these approaches fail to capture the complex interplay among different harm categories, leading to "harmful conflicts" where mitigating one type of harm may inadvertently amplify another, thus increasing overall harmful rate. To address this issue, we propose Conflict-aware Adaptive Safety Guidance (CASG), a training-free framework that dynamically identifies and applies the category-aligned safety direction during generation. CASG is composed of two components: (i) Conflict-aware Category Identification (CaCI), which identifies the harmful category most aligned with the model's evolving generative state, and (ii) Conflict-resolving Guidance Application (CrGA), which applies safety steering solely along the identified category to avoid multi-category interference. CASG can be applied to both latent-space and text-space safeguards. Experiments on T2I safety benchmarks demonstrate CASG's state-of-the-art performance, reducing the harmful rate by up to 15.4% compared to existing methods.

