---
layout: default
title: RAD: Retrieval-Augmented Monocular Metric Depth Estimation for Underrepresented Classes
---

# RAD: Retrieval-Augmented Monocular Metric Depth Estimation for Underrepresented Classes
**arXiv**：[2602.09532v1](https://arxiv.org/abs/2602.09532) · [PDF](https://arxiv.org/pdf/2602.09532.pdf)  
**作者**：Michael Baltaxe, Dan Levi, Sagie Benaim  

**一句话要点**：提出RAD检索增强框架，通过检索邻居作为几何代理，解决单目度量深度估计中少数类准确性问题。

**关键词**：单目度量深度估计, 检索增强学习, 几何信息融合, 少数类性能提升, 不确定性感知检索

## 3 点简述
- 核心问题：单目度量深度估计在复杂场景中少数类深度估计不准确。
- 方法要点：使用不确定性感知检索机制，结合双流网络和匹配交叉注意力模块融合输入与检索上下文。
- 实验或效果：在NYU Depth v2、KITTI和Cityscapes数据集上，显著提升少数类性能，相对绝对误差分别降低29.2%、13.3%和7.2%。

## 摘要（原文）

> Monocular Metric Depth Estimation (MMDE) is essential for physically intelligent systems, yet accurate depth estimation for underrepresented classes in complex scenes remains a persistent challenge. To address this, we propose RAD, a retrieval-augmented framework that approximates the benefits of multi-view stereo by utilizing retrieved neighbors as structural geometric proxies. Our method first employs an uncertainty-aware retrieval mechanism to identify low-confidence regions in the input and retrieve RGB-D context samples containing semantically similar content. We then process both the input and retrieved context via a dual-stream network and fuse them using a matched cross-attention module, which transfers geometric information only at reliable point correspondences. Evaluations on NYU Depth v2, KITTI, and Cityscapes demonstrate that RAD significantly outperforms state-of-the-art baselines on underrepresented classes, reducing relative absolute error by 29.2% on NYU Depth v2, 13.3% on KITTI, and 7.2% on Cityscapes, while maintaining competitive performance on standard in-domain benchmarks.

