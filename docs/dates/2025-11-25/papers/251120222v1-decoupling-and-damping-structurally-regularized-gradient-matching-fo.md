---
layout: default
title: Decoupling and Damping: Structurally-Regularized Gradient Matching for Multimodal Graph Condensation
---

# Decoupling and Damping: Structurally-Regularized Gradient Matching for Multimodal Graph Condensation
**arXiv**：[2511.20222v1](https://arxiv.org/abs/2511.20222) · [PDF](https://arxiv.org/pdf/2511.20222.pdf)  
**作者**：Lian Shen, Zhendan Chen, Yinhui jiang, Meijia Song, Ziming Su, Juan Liu, Xiangrong Liu  

**一句话要点**：提出结构正则化梯度匹配以解决多模态图压缩中的梯度冲突和噪声放大问题

**关键词**：多模态图压缩, 梯度匹配, 结构正则化, 图神经网络, 梯度解耦, Dirichlet能量

## 3 点简述
- 多模态图压缩中梯度冲突和结构噪声放大导致GNN训练失败
- 采用梯度解耦和结构阻尼正则化优化梯度匹配过程
- 实验显示SR-GM提升精度、加速收敛并增强跨架构泛化

## 摘要（原文）

> In critical web applications such as e-commerce and recommendation systems, multimodal graphs integrating rich visual and textual attributes are increasingly central, yet their large scale introduces substantial computational burdens for training Graph Neural Networks (GNNs). While Graph Condensation (GC) offers a promising solution by synthesizing smaller datasets, existing methods falter in the multimodal setting. We identify a dual challenge causing this failure: (1) conflicting gradients arising from semantic misalignments between modalities, and (2) the GNN's message-passing architecture pathologically amplifying this gradient noise across the graph structure. To address this, we propose Structurally-Regularized Gradient Matching (SR-GM), a novel condensation framework tailored for multimodal graphs. SR-GM introduces two synergistic components: first, a gradient decoupling mechanism that resolves inter-modality conflicts at their source via orthogonal projection; and second, a structural damping regularizer that acts directly on the gradient field. By leveraging the graph's Dirichlet energy, this regularizer transforms the topology from a noise amplifier into a stabilizing force during optimization. Extensive experiments demonstrate that SR-GM significantly improves accuracy and accelerates convergence compared to baseline methods. Ablation studies confirm that addressing both gradient conflict and structural amplification in tandem is essential for achieving superior performance. Moreover, the condensed multimodal graphs exhibit strong cross-architecture generalization and promise to accelerate applications like Neural Architecture Search. This research provides a scalable methodology for multimodal graph-based learning in resource-constrained environments.

