---
layout: default
title: Automatic regularization parameter choice for tomography using a double model approach
---

# Automatic regularization parameter choice for tomography using a double model approach
**arXiv**：[2602.08528v1](https://arxiv.org/abs/2602.08528) · [PDF](https://arxiv.org/pdf/2602.08528.pdf)  
**作者**：Chuyang Wu, Samuli Siltanen  

**一句话要点**：提出基于双模型方法的自动正则化参数选择，以解决X射线断层扫描中的图像重建问题。

**关键词**：X射线断层扫描, 图像重建, 正则化参数选择, 双模型方法, 反馈控制算法, 病态逆问题

## 3 点简述
- 核心问题：X射线断层扫描图像重建是病态逆问题，正则化参数选择对平衡数据保真度和先验信息至关重要。
- 方法要点：使用两个不同计算离散化模型，通过反馈控制算法动态调整正则化强度，驱动迭代重建。
- 实验或效果：在真实断层扫描数据上验证了方法的有效性，实现自动参数选择。

## 摘要（原文）

> Image reconstruction in X-ray tomography is an ill-posed inverse problem, particularly with limited available data. Regularization is thus essential, but its effectiveness hinges on the choice of a regularization parameter that balances data fidelity against a priori information. We present a novel method for automatic parameter selection based on the use of two distinct computational discretizations of the same problem. A feedback control algorithm dynamically adjusts the regularization strength, driving an iterative reconstruction toward the smallest parameter that yields sufficient similarity between reconstructions on the two grids. The effectiveness of the proposed approach is demonstrated using real tomographic data.

