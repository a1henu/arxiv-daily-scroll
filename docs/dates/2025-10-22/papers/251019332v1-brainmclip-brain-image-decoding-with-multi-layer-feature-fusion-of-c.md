---
layout: default
title: BrainMCLIP: Brain Image Decoding with Multi-Layer feature Fusion of CLIP
---

# BrainMCLIP: Brain Image Decoding with Multi-Layer feature Fusion of CLIP
**arXiv**：[2510.19332v1](https://arxiv.org/abs/2510.19332) · [PDF](https://arxiv.org/pdf/2510.19332.pdf)  
**作者**：Tian Xia, Zihan Ma, Xinlong Wang, Qing Liu, Xiaowei He, Tianming Liu, Yudan Ren  

**一句话要点**：提出BrainMCLIP以高效解码fMRI脑图像，融合CLIP多层特征并避免VAE路径。

**关键词**：脑图像解码, CLIP特征融合, 功能层次对齐, 参数高效模型, fMRI信号处理

## 3 点简述
- 核心问题：现有方法忽略CLIP中间层信息，且与大脑功能层次不符，依赖参数密集的VAE。
- 方法要点：基于视觉系统功能层次，对齐fMRI信号与CLIP多层特征，引入跨重建策略和多粒度损失。
- 实验或效果：在高级语义指标上媲美或超越SOTA，参数减少71.7%，无需VAE路径。

## 摘要（原文）

> Decoding images from fMRI often involves mapping brain activity to CLIP's
> final semantic layer. To capture finer visual details, many approaches add a
> parameter-intensive VAE-based pipeline. However, these approaches overlook rich
> object information within CLIP's intermediate layers and contradicts the
> brain's functionally hierarchical. We introduce BrainMCLIP, which pioneers a
> parameter-efficient, multi-layer fusion approach guided by human visual
> system's functional hierarchy, eliminating the need for such a separate VAE
> pathway. BrainMCLIP aligns fMRI signals from functionally distinct visual areas
> (low-/high-level) to corresponding intermediate and final CLIP layers,
> respecting functional hierarchy. We further introduce a Cross-Reconstruction
> strategy and a novel multi-granularity loss. Results show BrainMCLIP achieves
> highly competitive performance, particularly excelling on high-level semantic
> metrics where it matches or surpasses SOTA(state-of-the-art) methods, including
> those using VAE pipelines. Crucially, it achieves this with substantially fewer
> parameters, demonstrating a reduction of
> 71.7\%(Table.\ref{tab:compare_clip_vae}) compared to top VAE-based SOTA
> methods, by avoiding the VAE pathway. By leveraging intermediate CLIP features,
> it effectively captures visual details often missed by CLIP-only approaches,
> striking a compelling balance between semantic accuracy and detail fidelity
> without requiring a separate VAE pipeline.

