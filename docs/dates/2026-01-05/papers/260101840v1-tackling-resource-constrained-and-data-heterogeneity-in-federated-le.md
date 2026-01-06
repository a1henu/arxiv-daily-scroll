---
layout: default
title: Tackling Resource-Constrained and Data-Heterogeneity in Federated Learning with Double-Weight Sparse Pack
---

# Tackling Resource-Constrained and Data-Heterogeneity in Federated Learning with Double-Weight Sparse Pack
**arXiv**：[2601.01840v1](https://arxiv.org/abs/2601.01840) · [PDF](https://arxiv.org/pdf/2601.01840.pdf)  
**作者**：Qiantao Yang, Liquan Chen, Mingfu Xue, Songze Li  

**一句话要点**：提出FedCSPACK方法，通过余弦稀疏参数打包和双权重聚合解决联邦学习中资源受限和数据异构问题。

**关键词**：联邦学习, 数据异构, 资源受限, 参数稀疏化, 加权聚合, 模型性能优化

## 3 点简述
- 核心问题：现有联邦学习方法在数据异构下模型性能下降，且忽视客户端通信带宽和计算能力不足。
- 方法要点：基于余弦相似性打包参数并选择贡献最大的包共享，结合掩码矩阵和双权重聚合机制提升效率与鲁棒性。
- 实验或效果：在四个数据集上对比十种方法，FedCSPACK在保持高模型精度的同时有效提升通信和计算效率。

## 摘要（原文）

> Federated learning has drawn widespread interest from researchers, yet the data heterogeneity across edge clients remains a key challenge, often degrading model performance. Existing methods enhance model compatibility with data heterogeneity by splitting models and knowledge distillation. However, they neglect the insufficient communication bandwidth and computing power on the client, failing to strike an effective balance between addressing data heterogeneity and accommodating limited client resources. To tackle this limitation, we propose a personalized federated learning method based on cosine sparsification parameter packing and dual-weighted aggregation (FedCSPACK), which effectively leverages the limited client resources and reduces the impact of data heterogeneity on model performance. In FedCSPACK, the client packages model parameters and selects the most contributing parameter packages for sharing based on cosine similarity, effectively reducing bandwidth requirements. The client then generates a mask matrix anchored to the shared parameter package to improve the alignment and aggregation efficiency of sparse updates on the server. Furthermore, directional and distribution distance weights are embedded in the mask to implement a weighted-guided aggregation mechanism, enhancing the robustness and generalization performance of the global model. Extensive experiments across four datasets using ten state-of-the-art methods demonstrate that FedCSPACK effectively improves communication and computational efficiency while maintaining high model accuracy.

