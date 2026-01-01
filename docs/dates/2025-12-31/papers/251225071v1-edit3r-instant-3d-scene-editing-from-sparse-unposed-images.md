---
layout: default
title: Edit3r: Instant 3D Scene Editing from Sparse Unposed Images
---

# Edit3r: Instant 3D Scene Editing from Sparse Unposed Images
**arXiv**：[2512.25071v1](https://arxiv.org/abs/2512.25071) · [PDF](https://arxiv.org/pdf/2512.25071.pdf)  
**作者**：Jiageng Liu, Weijie Lyu, Xueting Li, Yejie Guo, Ming-Hsuan Yang  

**一句话要点**：提出Edit3r前馈框架，从稀疏无位姿图像中单次重建并编辑3D场景

**关键词**：3D场景编辑, 前馈框架, 无位姿图像, 跨视角一致性, 实时编辑

## 3 点简述
- 核心问题：缺乏多视角一致的编辑图像监督，阻碍3D编辑模型训练
- 方法要点：采用SAM2重着色策略生成跨视角一致监督，结合非对称输入融合不同观测
- 实验或效果：在DL3DV-Edit-Bench上实现语义对齐和3D一致性提升，推理速度快

## 摘要（原文）

> We present Edit3r, a feed-forward framework that reconstructs and edits 3D scenes in a single pass from unposed, view-inconsistent, instruction-edited images. Unlike prior methods requiring per-scene optimization, Edit3r directly predicts instruction-aligned 3D edits, enabling fast and photorealistic rendering without optimization or pose estimation. A key challenge in training such a model lies in the absence of multi-view consistent edited images for supervision. We address this with (i) a SAM2-based recoloring strategy that generates reliable, cross-view-consistent supervision, and (ii) an asymmetric input strategy that pairs a recolored reference view with raw auxiliary views, encouraging the network to fuse and align disparate observations. At inference, our model effectively handles images edited by 2D methods such as InstructPix2Pix, despite not being exposed to such edits during training. For large-scale quantitative evaluation, we introduce DL3DV-Edit-Bench, a benchmark built on the DL3DV test split, featuring 20 diverse scenes, 4 edit types and 100 edits in total. Comprehensive quantitative and qualitative results show that Edit3r achieves superior semantic alignment and enhanced 3D consistency compared to recent baselines, while operating at significantly higher inference speed, making it promising for real-time 3D editing applications.

