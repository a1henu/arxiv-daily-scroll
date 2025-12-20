---
layout: default
title: FOD-Diff: 3D Multi-Channel Patch Diffusion Model for Fiber Orientation Distribution
---

# FOD-Diff: 3D Multi-Channel Patch Diffusion Model for Fiber Orientation Distribution
**arXiv**：[2512.16075v1](https://arxiv.org/abs/2512.16075) · [PDF](https://arxiv.org/pdf/2512.16075.pdf)  
**作者**：Hao Tang, Hanyu Liu, Alessandro Perelli, Xi Chen, Chao Li  

**一句话要点**：提出3D多通道补丁扩散模型以从低角分辨率扩散MRI预测高角分辨率纤维取向分布

**关键词**：扩散模型, 纤维取向分布, 扩散MRI, 球谐系数, 3D补丁学习, 脑解剖先验

## 3 点简述
- 核心问题：从单壳低角分辨率扩散MRI估计纤维取向分布精度有限，而多壳高角分辨率方法扫描时间长。
- 方法要点：设计FOD补丁适配器引入脑解剖先验，并采用SH注意力模块学习球谐系数复杂相关性。
- 实验或效果：实验结果显示该方法在高角分辨率纤维取向分布预测中性能最佳，优于其他先进方法。

## 摘要（原文）

> Diffusion MRI (dMRI) is a critical non-invasive technique to estimate fiber orientation distribution (FOD) for characterizing white matter integrity. Estimating FOD from single-shell low angular resolution dMRI (LAR-FOD) is limited by accuracy, whereas estimating FOD from multi-shell high angular resolution dMRI (HAR-FOD) requires a long scanning time, which limits its applicability. Diffusion models have shown promise in estimating HAR-FOD based on LAR-FOD. However, using diffusion models to efficiently generate HAR-FOD is challenging due to the large number of spherical harmonic (SH) coefficients in FOD. Here, we propose a 3D multi-channel patch diffusion model to predict HAR-FOD from LAR-FOD. We design the FOD-patch adapter by introducing the prior brain anatomy for more efficient patch-based learning. Furthermore, we introduce a voxel-level conditional coordinating module to enhance the global understanding of the model. We design the SH attention module to effectively learn the complex correlations of the SH coefficients. Our experimental results show that our method achieves the best performance in HAR-FOD prediction and outperforms other state-of-the-art methods.

