---
layout: default
title: A Lightweight Medical Image Classification Framework via Self-Supervised Contrastive Learning and Quantum-Enhanced Feature Modeling
---

# A Lightweight Medical Image Classification Framework via Self-Supervised Contrastive Learning and Quantum-Enhanced Feature Modeling
**arXiv**：[2601.16608v1](https://arxiv.org/abs/2601.16608) · [PDF](https://arxiv.org/pdf/2601.16608.pdf)  
**作者**：Jingsong Xia, Siqi Wang  

**一句话要点**：提出轻量级医学图像分类框架，结合自监督对比学习和量子增强特征建模以解决资源受限下的性能问题。

**关键词**：医学图像分类, 自监督对比学习, 量子增强特征建模, 轻量级框架, 资源受限AI

## 3 点简述
- 核心问题：医学图像分析面临标注稀缺、计算资源有限和模型泛化能力不足的挑战。
- 方法要点：使用MobileNetV2作为骨干网络，通过自监督对比学习预训练，并嵌入参数化量子电路进行特征增强。
- 实验或效果：在少量参数和低计算成本下，该方法在准确性、AUC和F1分数上优于无自监督或量子增强的基线模型。

## 摘要（原文）

> Intelligent medical image analysis is essential for clinical decision support but is often limited by scarce annotations, constrained computational resources, and suboptimal model generalization. To address these challenges, we propose a lightweight medical image classification framework that integrates self-supervised contrastive learning with quantum-enhanced feature modeling. MobileNetV2 is employed as a compact backbone and pretrained using a SimCLR-style self-supervised paradigm on unlabeled images. A lightweight parameterized quantum circuit (PQC) is embedded as a quantum feature enhancement module, forming a hybrid classical-quantum architecture, which is subsequently fine-tuned on limited labeled data. Experimental results demonstrate that, with only approximately 2-3 million parameters and low computational cost, the proposed method consistently outperforms classical baselines without self-supervised learning or quantum enhancement in terms of Accuracy, AUC, and F1-score. Feature visualization further indicates improved discriminability and representation stability. Overall, this work provides a practical and forward-looking solution for high-performance medical artificial intelligence under resource-constrained settings.

