---
layout: default
title: SHARE: A Fully Unsupervised Framework for Single Hyperspectral Image Restoration
---

# SHARE: A Fully Unsupervised Framework for Single Hyperspectral Image Restoration
**arXiv**：[2601.13987v1](https://arxiv.org/abs/2601.13987) · [PDF](https://arxiv.org/pdf/2601.13987.pdf)  
**作者**：Jiangwei Xie, Zhang Wen, Mike Davies, Dongdong Chen  

**一句话要点**：提出SHARE框架，通过几何等变性和低秩建模实现无监督高光谱图像修复

**关键词**：高光谱图像修复, 无监督学习, 几何等变性, 低秩建模, 动态自适应注意力

## 3 点简述
- 核心问题：高光谱图像修复依赖标注数据，限制实际应用。
- 方法要点：结合几何等变性自监督和动态自适应光谱注意力模块。
- 实验或效果：在修复和超分辨率任务中优于无监督方法，接近监督方法性能。

## 摘要（原文）

> Hyperspectral image (HSI) restoration is a fundamental challenge in computational imaging and computer vision. It involves ill-posed inverse problems, such as inpainting and super-resolution. Although deep learning methods have transformed the field through data-driven learning, their effectiveness hinges on access to meticulously curated ground-truth datasets. This fundamentally restricts their applicability in real-world scenarios where such data is unavailable. This paper presents SHARE (Single Hyperspectral Image Restoration with Equivariance), a fully unsupervised framework that unifies geometric equivariance principles with low-rank spectral modelling to eliminate the need for ground truth. SHARE's core concept is to exploit the intrinsic invariance of hyperspectral structures under differentiable geometric transformations (e.g. rotations and scaling) to derive self-supervision signals through equivariance consistency constraints. Our novel Dynamic Adaptive Spectral Attention (DASA) module further enhances this paradigm shift by explicitly encoding the global low-rank property of HSI and adaptively refining local spectral-spatial correlations through learnable attention mechanisms. Extensive experiments on HSI inpainting and super-resolution tasks demonstrate the effectiveness of SHARE. Our method outperforms many state-of-the-art unsupervised approaches and achieves performance comparable to that of supervised methods. We hope that our approach will shed new light on HSI restoration and broader scientific imaging scenarios. The code will be released at https://github.com/xuwayyy/SHARE.

