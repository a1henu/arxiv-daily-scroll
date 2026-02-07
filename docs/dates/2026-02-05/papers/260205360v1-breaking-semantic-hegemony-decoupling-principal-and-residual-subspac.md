---
layout: default
title: Breaking Semantic Hegemony: Decoupling Principal and Residual Subspaces for Generalized OOD Detection
---

# Breaking Semantic Hegemony: Decoupling Principal and Residual Subspaces for Generalized OOD Detection
**arXiv**：[2602.05360v1](https://arxiv.org/abs/2602.05360) · [PDF](https://arxiv.org/pdf/2602.05360.pdf)  
**作者**：Ningkang Peng, Xiaoqian Peng, Yuhao Zhang, Qianfeng Yu, Feng Xing, Peirong Ma, Xichen Yang, Yi Chen, Tingyu Lu, Yanhui Gu  

**一句话要点**：提出D-KNN框架以解决广义OOD检测中的语义霸权问题

**关键词**：广义OOD检测, 语义霸权, 几何解耦, 训练后方法, 神经网络崩溃, 双空间校准

## 3 点简述
- 核心问题：现有OOD检测模型存在简单性悖论，对语义细微样本敏感但对结构简单样本或噪声盲视。
- 方法要点：通过正交分解解耦主成分与残差子空间，引入双空间校准机制增强对弱残差信号的敏感性。
- 实验或效果：在CIFAR和ImageNet基准上实现新SOTA，显著降低FPR95并提升AUROC性能。

## 摘要（原文）

> While feature-based post-hoc methods have made significant strides in Out-of-Distribution (OOD) detection, we uncover a counter-intuitive Simplicity Paradox in existing state-of-the-art (SOTA) models: these models exhibit keen sensitivity in distinguishing semantically subtle OOD samples but suffer from severe Geometric Blindness when confronting structurally distinct yet semantically simple samples or high-frequency sensor noise. We attribute this phenomenon to Semantic Hegemony within the deep feature space and reveal its mathematical essence through the lens of Neural Collapse. Theoretical analysis demonstrates that the spectral concentration bias, induced by the high variance of the principal subspace, numerically masks the structural distribution shift signals that should be significant in the residual subspace. To address this issue, we propose D-KNN, a training-free, plug-and-play geometric decoupling framework. This method utilizes orthogonal decomposition to explicitly separate semantic components from structural residuals and introduces a dual-space calibration mechanism to reactivate the model's sensitivity to weak residual signals. Extensive experiments demonstrate that D-KNN effectively breaks Semantic Hegemony, establishing new SOTA performance on both CIFAR and ImageNet benchmarks. Notably, in resolving the Simplicity Paradox, it reduces the FPR95 from 31.3% to 2.3%; when addressing sensor failures such as Gaussian noise, it boosts the detection performance (AUROC) from a baseline of 79.7% to 94.9%.

