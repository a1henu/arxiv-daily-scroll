---
layout: default
title: MAD-OOD: A Deep Learning Cluster-Driven Framework for an Out-of-Distribution Malware Detection and Classification
---

# MAD-OOD: A Deep Learning Cluster-Driven Framework for an Out-of-Distribution Malware Detection and Classification
**arXiv**：[2512.17594v1](https://arxiv.org/abs/2512.17594) · [PDF](https://arxiv.org/pdf/2512.17594.pdf)  
**作者**：Tosin Ige, Christopher Kiekintveld, Aritran Piplai, Asif Rahman, Olukunle Kolade, Sasidhar Kunapuli  

**一句话要点**：提出MAD-OOD框架以解决恶意软件分类中的分布外检测挑战

**关键词**：恶意软件检测, 分布外检测, 高斯判别分析, 聚类驱动, 深度神经网络, 网络安全

## 3 点简述
- 核心问题：恶意软件家族内变异导致分布外检测困难，现有方法性能下降。
- 方法要点：两阶段聚类驱动框架，使用高斯判别分析建模嵌入，结合深度网络提升分类。
- 实验或效果：在基准数据集上显著优于现有方法，AUC达0.911，适用于实际网络安全环境。

## 摘要（原文）

> Out of distribution (OOD) detection remains a critical challenge in malware classification due to the substantial intra family variability introduced by polymorphic and metamorphic malware variants. Most existing deep learning based malware detectors rely on closed world assumptions and fail to adequately model this intra class variation, resulting in degraded performance when confronted with previously unseen malware families. This paper presents MADOOD, a novel two stage, cluster driven deep learning framework for robust OOD malware detection and classification. In the first stage, malware family embeddings are modeled using class conditional spherical decision boundaries derived from Gaussian Discriminant Analysis (GDA), enabling statistically grounded separation of indistribution and OOD samples without requiring OOD data during training. Z score based distance analysis across multiple class centroids is employed to reliably identify anomalous samples in the latent space. In the second stage, a deep neural network integrates cluster based predictions, refined embeddings, and supervised classifier outputs to enhance final classification accuracy. Extensive evaluations on benchmark malware datasets comprising 25 known families and multiple novel OOD variants demonstrate that MADOOD significantly outperforms state of the art OOD detection methods, achieving an AUC of up to 0.911 on unseen malware families. The proposed framework provides a scalable, interpretable, and statistically principled solution for real world malware detection and anomaly identification in evolving cybersecurity environments.

