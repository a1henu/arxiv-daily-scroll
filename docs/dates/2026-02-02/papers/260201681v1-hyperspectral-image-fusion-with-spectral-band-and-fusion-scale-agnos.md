---
layout: default
title: Hyperspectral Image Fusion with Spectral-Band and Fusion-Scale Agnosticism
---

# Hyperspectral Image Fusion with Spectral-Band and Fusion-Scale Agnosticism
**arXiv**：[2602.01681v1](https://arxiv.org/abs/2602.01681) · [PDF](https://arxiv.org/pdf/2602.01681.pdf)  
**作者**：Yu-Jie Liang, Zihan Cao, Liang-Jian Deng, Yang Yang, Malu Zhang  

**一句话要点**：提出SSA框架，通过Matryoshka Kernel和隐式神经表示实现多光谱/高光谱图像融合的谱带与尺度无关性。

**关键词**：高光谱图像融合, 谱带无关性, 尺度无关性, 隐式神经表示, Matryoshka Kernel, 传感器泛化

## 3 点简述
- 当前多光谱/高光谱图像融合模型受限于固定谱带和空间尺度，难以跨传感器泛化。
- 引入Matryoshka Kernel适应任意谱带，结合隐式神经表示实现任意空间分辨率重建。
- 实验表明单一模型在未见传感器和尺度上取得先进性能，支持高光谱基础模型发展。

## 摘要（原文）

> Current deep learning models for Multispectral and Hyperspectral Image Fusion (MS/HS fusion) are typically designed for fixed spectral bands and spatial scales, which limits their transferability across diverse sensors. To address this, we propose SSA, a universal framework for MS/HS fusion with spectral-band and fusion-scale agnosticism. Specifically, we introduce Matryoshka Kernel (MK), a novel operator that enables a single model to adapt to arbitrary numbers of spectral channels. Meanwhile, we build SSA upon an Implicit Neural Representation (INR) backbone that models the HS signal as a continuous function, enabling reconstruction at arbitrary spatial resolutions. Together, these two forms of agnosticism enable a single MS/HS fusion model that generalizes effectively to unseen sensors and spatial scales. Extensive experiments demonstrate that our single model achieves state-of-the-art performance while generalizing well to unseen sensors and scales, paving the way toward future HS foundation models.

