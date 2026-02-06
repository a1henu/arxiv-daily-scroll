---
layout: default
title: SpectraKAN: Conditioning Spectral Operators
---

# SpectraKAN: Conditioning Spectral Operators
**arXiv**：[2602.05187v1](https://arxiv.org/abs/2602.05187) · [PDF](https://arxiv.org/pdf/2602.05187.pdf)  
**作者**：Chun-Wun Cheng, Carola-Bibiane Schönlieb, Angelica I. Aviles-Rivero  

**一句话要点**：提出SpectraKAN以解决谱神经算子在处理多尺度、状态依赖偏微分方程时的静态核限制问题。

**关键词**：谱神经算子, 偏微分方程求解, 输入条件化, 多尺度傅里叶调制, 时空预测

## 3 点简述
- 现有谱算子如FNO使用静态傅里叶核，难以捕捉系统全局状态驱动的多尺度、各向异性动力学。
- SpectraKAN通过从时空历史提取全局表示，并利用单查询交叉注意力调制多尺度傅里叶主干，实现输入条件化谱卷积。
- 在多样PDE基准测试中，SpectraKAN达到最先进性能，RMSE降低高达49%，尤其在时空预测任务上表现突出。

## 摘要（原文）

> Spectral neural operators, particularly Fourier Neural Operators (FNO), are a powerful framework for learning solution operators of partial differential equations (PDEs) due to their efficient global mixing in the frequency domain. However, existing spectral operators rely on static Fourier kernels applied uniformly across inputs, limiting their ability to capture multi-scale, regime-dependent, and anisotropic dynamics governed by the global state of the system. We introduce SpectraKAN, a neural operator that conditions the spectral operator on the input itself, turning static spectral convolution into an input-conditioned integral operator. This is achieved by extracting a compact global representation from spatio-temporal history and using it to modulate a multi-scale Fourier trunk via single-query cross-attention, enabling the operator to adapt its behaviour while retaining the efficiency of spectral mixing. We provide theoretical justification showing that this modulation converges to a resolution-independent continuous operator under mesh refinement and KAN gives smooth, Lipschitz-controlled global modulation. Across diverse PDE benchmarks, SpectraKAN achieves state-of-the-art performance, reducing RMSE by up to 49% over strong baselines, with particularly large gains on challenging spatio-temporal prediction tasks.

