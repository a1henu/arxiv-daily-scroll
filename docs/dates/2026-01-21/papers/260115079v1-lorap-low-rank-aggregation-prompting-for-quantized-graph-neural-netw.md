---
layout: default
title: LoRAP: Low-Rank Aggregation Prompting for Quantized Graph Neural Networks Training
---

# LoRAP: Low-Rank Aggregation Prompting for Quantized Graph Neural Networks Training
**arXiv**：[2601.15079v1](https://arxiv.org/abs/2601.15079) · [PDF](https://arxiv.org/pdf/2601.15079.pdf)  
**作者**：Chenyu Liu, Haige Li, Luca Rossi  

**一句话要点**：提出低秩聚合提示方法以提升量化图神经网络的训练性能

**关键词**：图神经网络, 量化训练, 提示学习, 低秩聚合, 图数据, 资源受限环境

## 3 点简述
- 核心问题：量化图神经网络中，仅提示节点特征无法优化聚合结果，影响性能
- 方法要点：引入低秩聚合提示，向聚合特征注入轻量级、输入相关的提示以优化量化聚合
- 实验或效果：在9个图数据集和4个QAT框架上评估，LoRAP一致提升低比特量化GNN性能，计算开销小

## 摘要（原文）

> Graph Neural Networks (GNNs) are neural networks that aim to process graph data, capturing the relationships and interactions between nodes using the message-passing mechanism. GNN quantization has emerged as a promising approach for reducing model size and accelerating inference in resource-constrained environments. Compared to quantization in LLMs, quantizing graph features is more emphasized in GNNs. Inspired by the above, we propose to leverage prompt learning, which manipulates the input data, to improve the performance of quantization-aware training (QAT) for GNNs. To mitigate the issue that prompting the node features alone can only make part of the quantized aggregation result optimal, we introduce Low-Rank Aggregation Prompting (LoRAP), which injects lightweight, input-dependent prompts into each aggregated feature to optimize the results of quantized aggregations. Extensive evaluations on 4 leading QAT frameworks over 9 graph datasets demonstrate that LoRAP consistently enhances the performance of low-bit quantized GNNs while introducing a minimal computational overhead.

