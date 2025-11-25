---
layout: default
title: Unsupervised Multi-View Visual Anomaly Detection via Progressive Homography-Guided Alignment
---

# Unsupervised Multi-View Visual Anomaly Detection via Progressive Homography-Guided Alignment
**arXiv**：[2511.18766v1](https://arxiv.org/abs/2511.18766) · [PDF](https://arxiv.org/pdf/2511.18766.pdf)  
**作者**：Xintao Chen, Xiaohao Xu, Bozhong Zheng, Yun Liu, Yingna Wu  

**一句话要点**：提出VSAD框架以解决多视角图像中异常检测的视角变化问题

**关键词**：多视角异常检测, 同形变换对齐, 扩散模型, 特征一致性, 无监督学习

## 3 点简述
- 核心问题：多视角图像中视角变化导致良性外观变化与真实缺陷难以区分
- 方法要点：使用同形变换对齐多视角特征，结合扩散模型进行渐进式对齐
- 实验或效果：在RealIAD和MANTA数据集上实现新SOTA，显著降低误报率

## 摘要（原文）

> Unsupervised visual anomaly detection from multi-view images presents a significant challenge: distinguishing genuine defects from benign appearance variations caused by viewpoint changes. Existing methods, often designed for single-view inputs, treat multiple views as a disconnected set of images, leading to inconsistent feature representations and a high false-positive rate. To address this, we introduce ViewSense-AD (VSAD), a novel framework that learns viewpoint-invariant representations by explicitly modeling geometric consistency across views. At its core is our Multi-View Alignment Module (MVAM), which leverages homography to project and align corresponding feature regions between neighboring views. We integrate MVAM into a View-Align Latent Diffusion Model (VALDM), enabling progressive and multi-stage alignment during the denoising process. This allows the model to build a coherent and holistic understanding of the object's surface from coarse to fine scales. Furthermore, a lightweight Fusion Refiner Module (FRM) enhances the global consistency of the aligned features, suppressing noise and improving discriminative power. Anomaly detection is performed by comparing multi-level features from the diffusion model against a learned memory bank of normal prototypes. Extensive experiments on the challenging RealIAD and MANTA datasets demonstrate that VSAD sets a new state-of-the-art, significantly outperforming existing methods in pixel, view, and sample-level visual anomaly proving its robustness to large viewpoint shifts and complex textures.

