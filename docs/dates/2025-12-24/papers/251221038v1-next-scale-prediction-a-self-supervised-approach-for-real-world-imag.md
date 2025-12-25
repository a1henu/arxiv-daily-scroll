---
layout: default
title: Next-Scale Prediction: A Self-Supervised Approach for Real-World Image Denoising
---

# Next-Scale Prediction: A Self-Supervised Approach for Real-World Image Denoising
**arXiv**：[2512.21038v1](https://arxiv.org/abs/2512.21038) · [PDF](https://arxiv.org/pdf/2512.21038.pdf)  
**作者**：Yiwen Shan, Haiyu Zhao, Peng Hu, Xi Peng, Yuanbiao Gou  

**一句话要点**：提出Next-Scale Prediction以解决自监督真实图像去噪中噪声去相关与细节保留的冲突

**关键词**：自监督去噪, 噪声去相关, 跨尺度预测, 盲点网络, 真实图像处理, 超分辨率

## 3 点简述
- 核心问题：自监督真实图像去噪中，噪声去相关与高频细节保留存在对抗性权衡
- 方法要点：通过跨尺度训练对，使用低分辨率去噪子图像预测高分辨率目标，解耦噪声去相关与细节保留
- 实验或效果：在真实世界基准测试中实现最先进的去噪性能，并自然支持噪声图像超分辨率

## 摘要（原文）

> Self-supervised real-world image denoising remains a fundamental challenge, arising from the antagonistic trade-off between decorrelating spatially structured noise and preserving high-frequency details. Existing blind-spot network (BSN) methods rely on pixel-shuffle downsampling (PD) to decorrelate noise, but aggressive downsampling fragments fine structures, while milder downsampling fails to remove correlated noise. To address this, we introduce Next-Scale Prediction (NSP), a novel self-supervised paradigm that decouples noise decorrelation from detail preservation. NSP constructs cross-scale training pairs, where BSN takes low-resolution, fully decorrelated sub-images as input to predict high-resolution targets that retain fine details. As a by-product, NSP naturally supports super-resolution of noisy images without retraining or modification. Extensive experiments demonstrate that NSP achieves state-of-the-art self-supervised denoising performance on real-world benchmarks, significantly alleviating the long-standing conflict between noise decorrelation and detail preservation.

