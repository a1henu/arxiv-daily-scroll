---
layout: default
title: Towards Generalized Multimodal Homography Estimation
---

# Towards Generalized Multimodal Homography Estimation
**arXiv**：[2603.03956v1](https://arxiv.org/abs/2603.03956) · [PDF](https://arxiv.org/pdf/2603.03956.pdf)  
**作者**：Jinkun You, Jiaxin Cheng, Jie Zhang, Yicong Zhou  

**一句话要点**：提出合成训练数据与网络设计以提升跨模态单应性估计泛化能力

**关键词**：单应性估计, 跨模态泛化, 数据合成, 特征解耦, 网络设计

## 3 点简述
- 核心问题：现有单应性估计方法在未见模态上性能显著下降，泛化能力不足。
- 方法要点：从单张图像合成多样纹理与颜色的未对齐图像对，并设计网络利用跨尺度信息与解耦颜色特征。
- 实验或效果：广泛实验验证合成数据提升泛化性能，网络设计提高估计准确性。

## 摘要（原文）

> Supervised and unsupervised homography estimation methods depend on image pairs tailored to specific modalities to achieve high accuracy. However, their performance deteriorates substantially when applied to unseen modalities. To address this issue, we propose a training data synthesis method that generates unaligned image pairs with ground-truth offsets from a single input image. Our approach renders the image pairs with diverse textures and colors while preserving their structural information. These synthetic data empower the trained model to achieve greater robustness and improved generalization across various domains. Additionally, we design a network to fully leverage cross-scale information and decouple color information from feature representations, thus improving estimation accuracy. Extensive experiments show that our training data synthesis method improves generalization performance. The results also confirm the effectiveness of the proposed network.

