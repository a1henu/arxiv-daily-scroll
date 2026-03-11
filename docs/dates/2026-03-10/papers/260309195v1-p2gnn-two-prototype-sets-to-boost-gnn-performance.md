---
layout: default
title: $P^2$GNN: Two Prototype Sets to boost GNN Performance
---

# $P^2$GNN: Two Prototype Sets to boost GNN Performance
**arXiv**：[2603.09195v1](https://arxiv.org/abs/2603.09195) · [PDF](https://arxiv.org/pdf/2603.09195.pdf)  
**作者**：Arihant Jain, Gundeep Arora, Anoop Saladi, Chaosheng Dong  

**一句话要点**：提出P²GNN原型增强方法以解决GNN的局部依赖和噪声邻域问题

**关键词**：图神经网络, 原型学习, 消息传递, 去噪增强, 全局上下文, 节点分类

## 3 点简述
- 核心问题：MP-GNN依赖局部上下文，缺乏全局信息，且假设强同质性，易受噪声邻域影响。
- 方法要点：利用原型集作为全局邻居和聚类对齐，增强消息传递，实现去噪和全局上下文丰富。
- 实验或效果：在18个数据集上验证，包括电商推荐和开源分类任务，性能优于生产模型并获最高平均排名。

## 摘要（原文）

> Message Passing Graph Neural Networks (MP-GNNs) have garnered attention for addressing various industry challenges, such as user recommendation and fraud detection. However, they face two major hurdles: (1) heavy reliance on local context, often lacking information about the global context or graph-level features, and (2) assumption of strong homophily among connected nodes, struggling with noisy local neighborhoods. To tackle these, we introduce $P^2$GNN, a plug-and-play technique leveraging prototypes to optimize message passing, enhancing the performance of the base GNN model. Our approach views the prototypes in two ways: (1) as universally accessible neighbors for all nodes, enriching global context, and (2) aligning messages to clustered prototypes, offering a denoising effect. We demonstrate the extensibility of our proposed method to all message-passing GNNs and conduct extensive experiments across 18 datasets, including proprietary e-commerce datasets and open-source datasets, on node recommendation and node classification tasks. Results show that $P^2$GNN outperforms production models in e-commerce and achieves the top average rank on open-source datasets, establishing it as a leading approach. Qualitative analysis supports the value of global context and noise mitigation in the local neighborhood in enhancing performance.

