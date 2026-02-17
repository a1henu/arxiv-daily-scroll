---
layout: default
title: Prototype Instance-semantic Disentanglement with Low-rank Regularized Subspace Clustering for WSIs Explainable Recognition
---

# Prototype Instance-semantic Disentanglement with Low-rank Regularized Subspace Clustering for WSIs Explainable Recognition
**arXiv**：[2602.14501v1](https://arxiv.org/abs/2602.14501) · [PDF](https://arxiv.org/pdf/2602.14501.pdf)  
**作者**：Chentao Li, Pan Huang  

**一句话要点**：提出PID-LRSC框架以解决全切片图像中实例-语义纠缠问题，提升可解释识别性能。

**关键词**：全切片图像识别, 实例-语义解耦, 低秩子空间聚类, 增强对比学习, 病理诊断可解释性, 多实例学习

## 3 点简述
- 核心问题：肿瘤与非肿瘤实例比例失衡及肿瘤与癌前组织高度相似导致实例-语义纠缠，影响模型表示与可解释性。
- 方法要点：采用低秩正则化子空间聚类处理实例纠缠，增强对比学习设计原型实例语义解耦解决语义纠缠。
- 实验或效果：在多中心病理数据集上验证，PID-LRSC优于其他SOTA方法，增强辅助诊断可靠性。

## 摘要（原文）

> The tumor region plays a key role in pathological diagnosis. Tumor tissues are highly similar to precancerous lesions and non tumor instances often greatly exceed tumor instances in whole slide images (WSIs). These issues cause instance-semantic entanglement in multi-instance learning frameworks, degrading both model representation capability and interpretability. To address this, we propose an end-to-end prototype instance semantic disentanglement framework with low-rank regularized subspace clustering, PID-LRSC, in two aspects. First, we use secondary instance subspace learning to construct low-rank regularized subspace clustering (LRSC), addressing instance entanglement caused by an excessive proportion of non tumor instances. Second, we employ enhanced contrastive learning to design prototype instance semantic disentanglement (PID), resolving semantic entanglement caused by the high similarity between tumor and precancerous tissues. We conduct extensive experiments on multicentre pathology datasets, implying that PID-LRSC outperforms other SOTA methods. Overall, PID-LRSC provides clearer instance semantics during decision-making and significantly enhances the reliability of auxiliary diagnostic outcomes.

