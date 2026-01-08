---
layout: default
title: CroBIM-U: Uncertainty-Driven Referring Remote Sensing Image Segmentation
---

# CroBIM-U: Uncertainty-Driven Referring Remote Sensing Image Segmentation
**arXiv**：[2601.03490v1](https://arxiv.org/abs/2601.03490) · [PDF](https://arxiv.org/pdf/2601.03490.pdf)  
**作者**：Yuzhe Sun, Zhe Dong, Haochen Jiang, Tianzhu Liu, Yanfeng Gu  

**一句话要点**：提出不确定性引导框架以提升遥感图像指代分割的鲁棒性和几何保真度

**关键词**：遥感图像分割, 指代分割, 不确定性建模, 跨模态对齐, 自适应融合, 局部细化

## 3 点简述
- 核心问题：遥感图像指代分割中跨模态对齐存在空间非均匀性，导致现有方法在清晰区域引入噪声，在混淆区域解歧不足。
- 方法要点：引入指代不确定性评分器预测空间模糊分布，并基于此设计不确定性门控融合和局部细化模块，实现自适应推理。
- 实验或效果：作为即插即用方案，在复杂遥感场景中显著提升鲁棒性和几何保真度，不改变骨干架构。

## 摘要（原文）

> Referring remote sensing image segmentation aims to localize specific targets described by natural language within complex overhead imagery. However, due to extreme scale variations, dense similar distractors, and intricate boundary structures, the reliability of cross-modal alignment exhibits significant \textbf{spatial non-uniformity}. Existing methods typically employ uniform fusion and refinement strategies across the entire image, which often introduces unnecessary linguistic perturbations in visually clear regions while failing to provide sufficient disambiguation in confused areas. To address this, we propose an \textbf{uncertainty-guided framework} that explicitly leverages a pixel-wise \textbf{referring uncertainty map} as a spatial prior to orchestrate adaptive inference. Specifically, we introduce a plug-and-play \textbf{Referring Uncertainty Scorer (RUS)}, which is trained via an online error-consistency supervision strategy to interpretably predict the spatial distribution of referential ambiguity. Building on this prior, we design two plug-and-play modules: 1) \textbf{Uncertainty-Gated Fusion (UGF)}, which dynamically modulates language injection strength to enhance constraints in high-uncertainty regions while suppressing noise in low-uncertainty ones; and 2) \textbf{Uncertainty-Driven Local Refinement (UDLR)}, which utilizes uncertainty-derived soft masks to focus refinement on error-prone boundaries and fine details. Extensive experiments demonstrate that our method functions as a unified, plug-and-play solution that significantly improves robustness and geometric fidelity in complex remote sensing scenes without altering the backbone architecture.

