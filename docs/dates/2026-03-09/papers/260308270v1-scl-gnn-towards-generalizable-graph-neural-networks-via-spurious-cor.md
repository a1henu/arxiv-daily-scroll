---
layout: default
title: SCL-GNN: Towards Generalizable Graph Neural Networks via Spurious Correlation Learning
---

# SCL-GNN: Towards Generalizable Graph Neural Networks via Spurious Correlation Learning
**arXiv**：[2603.08270v1](https://arxiv.org/abs/2603.08270) · [PDF](https://arxiv.org/pdf/2603.08270.pdf)  
**作者**：Yuxiang Zhang, Enyan Dai  

**一句话要点**：提出SCL-GNN框架，通过虚假相关性学习提升图神经网络在IID和OOD图上的泛化能力。

**关键词**：图神经网络, 虚假相关性学习, 泛化能力, HSIC, 双层优化, 分布偏移

## 3 点简述
- 核心问题：图神经网络易受节点特征与标签间虚假相关性影响，泛化能力受限。
- 方法要点：利用HSIC量化相关性，结合双层优化策略，识别并缓解虚假相关性。
- 实验或效果：在真实和合成数据集上优于现有基线，展示出鲁棒性和泛化优势。

## 摘要（原文）

> Graph Neural Networks (GNNs) have demonstrated remarkable success across diverse tasks. However, their generalization capability is often hindered by spurious correlations between node features and labels in the graph. Our analysis reveals that GNNs tend to exploit imperceptible statistical correlations in training data, even when such correlations are unreliable for prediction. To address this challenge, we propose the Spurious Correlation Learning Graph Neural Network (SCL-GNN), a novel framework designed to enhance generalization on both Independent and Identically Distributed (IID) and Out-of-Distribution (OOD) graphs. SCL-GNN incorporates a principled spurious correlation learning mechanism, leveraging the Hilbert-Schmidt Independence Criterion (HSIC) to quantify correlations between node representations and class scores. This enables the model to identify and mitigate irrelevant but influential spurious correlations effectively. Additionally, we introduce an efficient bi-level optimization strategy to jointly optimize modules and GNN parameters, preventing overfitting. Extensive experiments on real-world and synthetic datasets demonstrate that SCL-GNN consistently outperforms state-of-the-art baselines under various distribution shifts, highlighting its robustness and generalization capabilities.

