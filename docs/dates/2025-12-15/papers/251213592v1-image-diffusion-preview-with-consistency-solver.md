---
layout: default
title: Image Diffusion Preview with Consistency Solver
---

# Image Diffusion Preview with Consistency Solver
**arXiv**：[2512.13592v1](https://arxiv.org/abs/2512.13592) · [PDF](https://arxiv.org/pdf/2512.13592.pdf)  
**作者**：Fu-Yun Wang, Hao Zhou, Liangzhe Yuan, Sanghyun Woo, Boqing Gong, Bohyung Han, Ming-Hsuan Yang, Han Zhang, Yukun Zhu, Ting Liu, Long Zhao  

**一句话要点**：提出ConsistencySolver以加速图像扩散模型的预览生成，提升预览质量与一致性。

**关键词**：图像扩散模型, 预览生成, 一致性求解器, 强化学习优化, 交互加速

## 3 点简述
- 核心问题：图像扩散模型推理慢，影响交互体验，现有方法难以保证预览质量与最终输出的一致性。
- 方法要点：基于通用线性多步方法，设计轻量可训练高阶求解器，通过强化学习优化预览质量和一致性。
- 实验或效果：在低步数场景下显著提升生成质量和一致性，减少用户交互时间近50%，代码已开源。

## 摘要（原文）

> The slow inference process of image diffusion models significantly degrades interactive user experiences. To address this, we introduce Diffusion Preview, a novel paradigm employing rapid, low-step sampling to generate preliminary outputs for user evaluation, deferring full-step refinement until the preview is deemed satisfactory. Existing acceleration methods, including training-free solvers and post-training distillation, struggle to deliver high-quality previews or ensure consistency between previews and final outputs. We propose ConsistencySolver derived from general linear multistep methods, a lightweight, trainable high-order solver optimized via Reinforcement Learning, that enhances preview quality and consistency. Experimental results demonstrate that ConsistencySolver significantly improves generation quality and consistency in low-step scenarios, making it ideal for efficient preview-and-refine workflows. Notably, it achieves FID scores on-par with Multistep DPM-Solver using 47% fewer steps, while outperforming distillation baselines. Furthermore, user studies indicate our approach reduces overall user interaction time by nearly 50% while maintaining generation quality. Code is available at https://github.com/G-U-N/consolver.

