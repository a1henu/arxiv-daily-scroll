---
layout: default
title: SENDAI: A Hierarchical Sparse-measurement, EfficieNt Data AssImilation Framework
---

# SENDAI: A Hierarchical Sparse-measurement, EfficieNt Data AssImilation Framework
**arXiv**：[2601.21664v1](https://arxiv.org/abs/2601.21664) · [PDF](https://arxiv.org/pdf/2601.21664.pdf)  
**作者**：Xingyue Zhang, Yuxuan Bao, Mars Liyao Gao, J. Nathan Kutz  

**一句话要点**：提出SENDAI框架，通过结合模拟先验与学习校正，从超稀疏观测重建时空场。

**关键词**：稀疏测量重建, 数据同化, 时空场重建, 卫星遥感, 分布偏移

## 3 点简述
- 核心问题：数据丰富训练与观测稀疏部署间的分布偏移、异质结构和多尺度动态挑战。
- 方法要点：分层框架结合模拟先验与学习校正，实现高效数据同化。
- 实验或效果：在卫星遥感中，优于基线方法，提升SSIM达185%，保留诊断相关结构。

## 摘要（原文）

> Bridging the gap between data-rich training regimes and observation-sparse deployment conditions remains a central challenge in spatiotemporal field reconstruction, particularly when target domains exhibit distributional shifts, heterogeneous structure, and multi-scale dynamics absent from available training data. We present SENDAI, a hierarchical Sparse-measurement, EfficieNt Data AssImilation Framework that reconstructs full spatial states from hyper sparse sensor observations by combining simulation-derived priors with learned discrepancy corrections. We demonstrate the performance on satellite remote sensing, reconstructing MODIS (Moderate Resolution Imaging Spectroradiometer) derived vegetation index fields across six globally distributed sites. Using seasonal periods as a proxy for domain shift, the framework consistently outperforms established baselines that require substantially denser observations -- SENDAI achieves a maximum SSIM improvement of 185% over traditional baselines and a 36% improvement over recent high-frequency-based methods. These gains are particularly pronounced for landscapes with sharp boundaries and sub-seasonal dynamics; more importantly, the framework effectively preserves diagnostically relevant structures -- such as field topologies, land cover discontinuities, and spatial gradients. By yielding corrections that are more structurally and spectrally separable, the reconstructed fields are better suited for downstream inference of indirectly observed variables. The results therefore highlight a lightweight and operationally viable framework for sparse-measurement reconstruction that is applicable to physically grounded inference, resource-limited deployment, and real-time monitor and control.

