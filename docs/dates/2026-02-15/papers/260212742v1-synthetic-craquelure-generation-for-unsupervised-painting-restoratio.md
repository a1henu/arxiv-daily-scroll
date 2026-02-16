---
layout: default
title: Synthetic Craquelure Generation for Unsupervised Painting Restoration
---

# Synthetic Craquelure Generation for Unsupervised Painting Restoration
**arXiv**：[2602.12742v1](https://arxiv.org/abs/2602.12742) · [PDF](https://arxiv.org/pdf/2602.12742.pdf)  
**作者**：Jana Cuch-Guillén, Antonio Agudo, Raül Pérez-Gonzalo  

**一句话要点**：提出基于合成龟裂生成的无监督绘画修复框架，以解决标注稀缺下的精细龟裂恢复问题。

**关键词**：无监督绘画修复, 合成龟裂生成, 形态学检测, 低秩适应, 各向异性扩散修复

## 3 点简述
- 核心问题：文化遗产绘画修复中，缺乏像素级标注导致精细龟裂模式识别与恢复困难。
- 方法要点：使用贝塞尔轨迹合成真实龟裂，结合形态学检测器与基于LoRA的SegFormer细化模块，并注入空间先验。
- 实验或效果：在零样本设置下显著优于现有摄影修复模型，同时忠实保留原始画笔笔触。

## 摘要（原文）

> Cultural heritage preservation increasingly demands non-invasive digital methods for painting restoration, yet identifying and restoring fine craquelure patterns from complex brushstrokes remains challenging due to scarce pixel-level annotations. We propose a fully annotation-free framework driven by a domain-specific synthetic craquelure generator, which simulates realistic branching and tapered fissure geometry using Bézier trajectories. Our approach couples a classical morphological detector with a learning-based refinement module: a SegFormer backbone adapted via Low-Rank Adaptation (LoRA). Uniquely, we employ a detector-guided strategy, injecting the morphological map as an input spatial prior, while a masked hybrid loss and logit adjustment constrain the training to focus specifically on refining candidate crack regions. The refined masks subsequently guide an Anisotropic Diffusion inpainting stage to reconstruct missing content. Experimental results demonstrate that our pipeline significantly outperforms state-of-the-art photographic restoration models in zero-shot settings, while faithfully preserving the original paint brushwork.

