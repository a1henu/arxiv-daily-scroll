---
layout: default
title: LoGoColor: Local-Global 3D Colorization for 360° Scenes
---

# LoGoColor: Local-Global 3D Colorization for 360° Scenes
**arXiv**：[2512.09278v1](https://arxiv.org/abs/2512.09278) · [PDF](https://arxiv.org/pdf/2512.09278.pdf)  
**作者**：Yeonjin Chang, Juhwan Cho, Seunghyeon Seo, Wonsik Shin, Nojun Kwak  

**一句话要点**：提出LoGoColor以解决360°场景3D着色中颜色多样性与多视图一致性问题

**关键词**：3D着色, 多视图一致性, 颜色多样性, 360°场景, 局部-全局方法, 多视图扩散模型

## 3 点简述
- 核心问题：现有3D着色方法因蒸馏2D图像模型导致颜色平均化，在复杂360°场景中产生单调结果
- 方法要点：采用局部-全局方法，分区处理场景并使用微调多视图扩散模型确保子场景内和子场景间一致性
- 实验或效果：在复杂360°场景上实现更一致和合理的3D着色，并通过新颜色多样性指数验证颜色多样性

## 摘要（原文）

> Single-channel 3D reconstruction is widely used in fields such as robotics and medical imaging. While this line of work excels at reconstructing 3D geometry, the outputs are not colored 3D models, thus 3D colorization is required for visualization. Recent 3D colorization studies address this problem by distilling 2D image colorization models. However, these approaches suffer from an inherent inconsistency of 2D image models. This results in colors being averaged during training, leading to monotonous and oversimplified results, particularly in complex 360° scenes. In contrast, we aim to preserve color diversity by generating a new set of consistently colorized training views, thereby bypassing the averaging process. Nevertheless, eliminating the averaging process introduces a new challenge: ensuring strict multi-view consistency across these colorized views. To achieve this, we propose LoGoColor, a pipeline designed to preserve color diversity by eliminating this guidance-averaging process with a `Local-Global' approach: we partition the scene into subscenes and explicitly tackle both inter-subscene and intra-subscene consistency using a fine-tuned multi-view diffusion model. We demonstrate that our method achieves quantitatively and qualitatively more consistent and plausible 3D colorization on complex 360° scenes than existing methods, and validate its superior color diversity using a novel Color Diversity Index.

