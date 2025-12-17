---
layout: default
title: CLNet: Cross-View Correspondence Makes a Stronger Geo-Localizationer
---

# CLNet: Cross-View Correspondence Makes a Stronger Geo-Localizationer
**arXiv**：[2512.14560v1](https://arxiv.org/abs/2512.14560) · [PDF](https://arxiv.org/pdf/2512.14560.pdf)  
**作者**：Xianwei Cao, Dou Quan, Shuang Wang, Ning Huyan, Wei Wang, Yunan Li, Licheng Jiao  

**一句话要点**：提出CLNet框架，通过显式跨视图对应解决图像检索式地理定位问题

**关键词**：跨视图地理定位, 图像检索, 特征对齐, 神经对应图, 特征重校准

## 3 点简述
- 核心问题：现有方法依赖全局表示或隐式对齐，难以建模跨视图的显式空间对应关系
- 方法要点：CLNet包含神经对应图、非线性嵌入转换器和全局特征重校准三个互补模块
- 实验或效果：在CVUSA等四个基准测试中达到最优性能，提升可解释性和泛化能力

## 摘要（原文）

> Image retrieval-based cross-view geo-localization (IRCVGL) aims to match images captured from significantly different viewpoints, such as satellite and street-level images. Existing methods predominantly rely on learning robust global representations or implicit feature alignment, which often fail to model explicit spatial correspondences crucial for accurate localization. In this work, we propose a novel correspondence-aware feature refinement framework, termed CLNet, that explicitly bridges the semantic and geometric gaps between different views. CLNet decomposes the view alignment process into three learnable and complementary modules: a Neural Correspondence Map (NCM) that spatially aligns cross-view features via latent correspondence fields; a Nonlinear Embedding Converter (NEC) that remaps features across perspectives using an MLP-based transformation; and a Global Feature Recalibration (GFR) module that reweights informative feature channels guided by learned spatial cues. The proposed CLNet can jointly capture both high-level semantics and fine-grained alignments. Extensive experiments on four public benchmarks, CVUSA, CVACT, VIGOR, and University-1652, demonstrate that our proposed CLNet achieves state-of-the-art performance while offering better interpretability and generalizability.

