---
layout: default
title: Semantic Class Distribution Learning for Debiasing Semi-Supervised Medical Image Segmentation
---

# Semantic Class Distribution Learning for Debiasing Semi-Supervised Medical Image Segmentation
**arXiv**：[2603.05202v1](https://arxiv.org/abs/2603.05202) · [PDF](https://arxiv.org/pdf/2603.05202.pdf)  
**作者**：Yingxue Su, Yiheng Zhong, Keying Zhu, Zimu Zhang, Zhuoru Zhang, Yifang Wang, Yuxin Zhang, Jingxin Liu  

**一句话要点**：提出语义类别分布学习框架以解决半监督医学图像分割中的类别不平衡问题

**关键词**：医学图像分割, 半监督学习, 类别不平衡, 特征分布学习, 去偏方法

## 3 点简述
- 核心问题：医学图像分割中类别不平衡导致少数结构特征被主导类别淹没，影响分割性能。
- 方法要点：通过类别分布双向对齐和语义锚点约束，学习结构化类别条件特征分布以缓解监督和表示偏差。
- 实验或效果：在Synapse和AMOS数据集上显著提升整体和类别级分割指标，尤其在少数类别上表现突出。

## 摘要（原文）

> Medical image segmentation is critical for computer-aided diagnosis. However, dense pixel-level annotation is time-consuming and expensive, and medical datasets often exhibit severe class imbalance. Such imbalance causes minority structures to be overwhelmed by dominant classes in feature representations, hindering the learning of discriminative features and making reliable segmentation particularly challenging. To address this, we propose the Semantic Class Distribution Learning (SCDL) framework, a plug-and-play module that mitigates supervision and representation biases by learning structured class-conditional feature distributions. SCDL integrates Class Distribution Bidirectional Alignment (CDBA) to align embeddings with learnable class proxies and leverages Semantic Anchor Constraints (SAC) to guide proxies using labeled data. Experiments on the Synapse and AMOS datasets demonstrate that SCDL significantly improves segmentation performance across both overall and class-level metrics, with particularly strong gains on minority classes, achieving state-of-the-art results. Our code is released at https://github.com/Zyh55555/SCDL.

