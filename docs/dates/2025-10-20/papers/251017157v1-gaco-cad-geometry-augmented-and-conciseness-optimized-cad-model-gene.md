---
layout: default
title: GACO-CAD: Geometry-Augmented and Conciseness-Optimized CAD Model Generation from Single Image
---

# GACO-CAD: Geometry-Augmented and Conciseness-Optimized CAD Model Generation from Single Image
**arXiv**：[2510.17157v1](https://arxiv.org/abs/2510.17157) · [PDF](https://arxiv.org/pdf/2510.17157.pdf)  
**作者**：Yinghui Wang, Xinyu Zhang, Peng Du  

**一句话要点**：提出GACO-CAD框架，通过几何增强与简洁优化从单图像生成可编辑CAD模型

**关键词**：CAD模型生成, 单视图重建, 几何增强, 强化学习, 多模态大语言模型, 建模简洁性

## 3 点简述
- 核心问题：多模态大语言模型从2D图像推断3D几何时空间推理能力不足
- 方法要点：两阶段后训练，结合深度与法线图作为几何先验，并引入组长度奖励优化建模序列
- 实验或效果：在DeepCAD和Fusion360数据集上实现SOTA，提升代码有效性、几何精度和建模简洁性

## 摘要（原文）

> Generating editable, parametric CAD models from a single image holds great
> potential to lower the barriers of industrial concept design. However, current
> multi-modal large language models (MLLMs) still struggle with accurately
> inferring 3D geometry from 2D images due to limited spatial reasoning
> capabilities. We address this limitation by introducing GACO-CAD, a novel
> two-stage post-training framework. It is designed to achieve a joint objective:
> simultaneously improving the geometric accuracy of the generated CAD models and
> encouraging the use of more concise modeling procedures. First, during
> supervised fine-tuning, we leverage depth and surface normal maps as dense
> geometric priors, combining them with the RGB image to form a multi-channel
> input. In the context of single-view reconstruction, these priors provide
> complementary spatial cues that help the MLLM more reliably recover 3D geometry
> from 2D observations. Second, during reinforcement learning, we introduce a
> group length reward that, while preserving high geometric fidelity, promotes
> the generation of more compact and less redundant parametric modeling
> sequences. A simple dynamic weighting strategy is adopted to stabilize
> training. Experiments on the DeepCAD and Fusion360 datasets show that GACO-CAD
> achieves state-of-the-art performance under the same MLLM backbone,
> consistently outperforming existing methods in terms of code validity,
> geometric accuracy, and modeling conciseness.

