---
layout: default
title: Quantile Transfer for Reliable Operating Point Selection in Visual Place Recognition
---

# Quantile Transfer for Reliable Operating Point Selection in Visual Place Recognition
**arXiv**：[2602.04401v1](https://arxiv.org/abs/2602.04401) · [PDF](https://arxiv.org/pdf/2602.04401.pdf)  
**作者**：Dhyey Manish Rajani, Michael Milford, Tobias Fischer  

**一句话要点**：提出分位数转移方法以解决视觉地点识别中操作点选择的环境适应性问题

**关键词**：视觉地点识别, 操作点选择, 分位数归一化, 阈值转移, 环境适应性, 召回率优化

## 3 点简述
- 核心问题：视觉地点识别中手动调优阈值在环境变化时性能下降
- 方法要点：使用校准遍历和分位数归一化自动选择阈值以最大化召回率
- 实验或效果：在多个数据集上优于现有方法，高精度下召回率提升达25%

## 摘要（原文）

> Visual Place Recognition (VPR) is a key component for localisation in GNSS-denied environments, but its performance critically depends on selecting an image matching threshold (operating point) that balances precision and recall. Thresholds are typically hand-tuned offline for a specific environment and fixed during deployment, leading to degraded performance under environmental change. We propose a method that, given a user-defined precision requirement, automatically selects the operating point of a VPR system to maximise recall. The method uses a small calibration traversal with known correspondences and transfers thresholds to deployment via quantile normalisation of similarity score distributions. This quantile transfer ensures that thresholds remain stable across calibration sizes and query subsets, making the method robust to sampling variability. Experiments with multiple state-of-the-art VPR techniques and datasets show that the proposed approach consistently outperforms the state-of-the-art, delivering up to 25% higher recall in high-precision operating regimes. The method eliminates manual tuning by adapting to new environments and generalising across operating conditions. Our code will be released upon acceptance.

