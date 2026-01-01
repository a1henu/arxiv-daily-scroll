---
layout: default
title: Self-Supervised Neural Architecture Search for Multimodal Deep Neural Networks
---

# Self-Supervised Neural Architecture Search for Multimodal Deep Neural Networks
**arXiv**：[2512.24793v1](https://arxiv.org/abs/2512.24793) · [PDF](https://arxiv.org/pdf/2512.24793.pdf)  
**作者**：Shota Suzuki, Satoshi Ono  

**一句话要点**：提出自监督学习方法以解决多模态深度神经网络架构搜索中依赖大量标注数据的问题。

**关键词**：自监督学习, 神经架构搜索, 多模态深度神经网络, 特征融合, 无标注数据

## 3 点简述
- 核心问题：多模态深度神经网络架构搜索需大量标注数据，成本高且不切实际。
- 方法要点：采用自监督学习全面应用于架构搜索和模型预训练过程，减少对标注数据的依赖。
- 实验或效果：实验证明该方法能从无标注训练数据中成功设计出有效的神经网络架构。

## 摘要（原文）

> Neural architecture search (NAS), which automates the architectural design process of deep neural networks (DNN), has attracted increasing attention. Multimodal DNNs that necessitate feature fusion from multiple modalities benefit from NAS due to their structural complexity; however, constructing an architecture for multimodal DNNs through NAS requires a substantial amount of labeled training data. Thus, this paper proposes a self-supervised learning (SSL) method for architecture search of multimodal DNNs. The proposed method applies SSL comprehensively for both the architecture search and model pretraining processes. Experimental results demonstrated that the proposed method successfully designed architectures for DNNs from unlabeled training data.

