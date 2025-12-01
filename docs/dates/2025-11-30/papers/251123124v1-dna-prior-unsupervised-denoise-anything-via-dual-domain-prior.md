---
layout: default
title: DNA-Prior: Unsupervised Denoise Anything via Dual-Domain Prior
---

# DNA-Prior: Unsupervised Denoise Anything via Dual-Domain Prior
**arXiv**：[2511.23124v1](https://arxiv.org/abs/2511.23124) · [PDF](https://arxiv.org/pdf/2511.23124.pdf)  
**作者**：Yanqi Cheng, Chun-Wun Cheng, Jim Denholm, Thiago Lima, Javier A. Montoya-Zegarra, Richard Goodwin, Carola-Bibiane Schönlieb, Angelica I Aviles-Rivero  

**一句话要点**：提出DNA-Prior，一种无监督通用去噪框架，通过双域先验解决医学图像去噪问题。

**关键词**：无监督去噪, 医学图像处理, 双域先验, 优化框架, 噪声抑制

## 3 点简述
- 核心问题：医学图像去噪依赖标注数据或监督学习，在异构模态和有限真值数据下受限。
- 方法要点：结合隐式架构先验和显式谱-空间先验，形成双域优化问题，无需外部训练数据。
- 实验或效果：在多模态实验中，DNA-Prior在不同噪声条件下实现一致的噪声抑制和结构保持。

## 摘要（原文）

> Medical imaging pipelines critically rely on robust denoising to stabilise downstream tasks such as segmentation and reconstruction. However, many existing denoisers depend on large annotated datasets or supervised learning, which restricts their usability in clinical environments with heterogeneous modalities and limited ground-truth data. To address this limitation, we introduce DNA-Prior, a universal unsupervised denoising framework that reconstructs clean images directly from corrupted observations through a mathematically principled hybrid prior. DNA-Prior integrates (i) an implicit architectural prior, enforced through a deep network parameterisation, with (ii) an explicit spectral-spatial prior composed of a frequency-domain fidelity term and a spatial regularisation functional. This dual-domain formulation yields a well-structured optimisation problem that jointly preserves global frequency characteristics and local anatomical structure, without requiring any external training data or modality-specific tuning. Experiments across multiple modalities show that DNA achieves consistent noise suppression and structural preservation under diverse noise conditions.

