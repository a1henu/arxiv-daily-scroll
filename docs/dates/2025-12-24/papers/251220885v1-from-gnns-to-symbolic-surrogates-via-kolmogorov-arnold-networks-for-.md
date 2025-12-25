---
layout: default
title: From GNNs to Symbolic Surrogates via Kolmogorov-Arnold Networks for Delay Prediction
---

# From GNNs to Symbolic Surrogates via Kolmogorov-Arnold Networks for Delay Prediction
**arXiv**：[2512.20885v1](https://arxiv.org/abs/2512.20885) · [PDF](https://arxiv.org/pdf/2512.20885.pdf)  
**作者**：Sami Marouani, Kamal Singh, Baptiste Jeudy, Amaury Habrard  

**一句话要点**：提出FlowKANet与符号代理模型，用于通信网络流延迟预测，提升效率与透明度。

**关键词**：流延迟预测, 图神经网络, Kolmogorov-Arnold网络, 符号代理模型, 注意力机制, 模型蒸馏

## 3 点简述
- 核心问题：准确预测通信网络流延迟，以优化网络管理。
- 方法要点：结合GNN与KAN层，并蒸馏为符号模型，减少参数并保持性能。
- 实验或效果：KAN层在效率与准确性间提供良好权衡，符号模型支持轻量部署和透明性。

## 摘要（原文）

> Accurate prediction of flow delay is essential for optimizing and managing modern communication networks. We investigate three levels of modeling for this task. First, we implement a heterogeneous GNN with attention-based message passing, establishing a strong neural baseline. Second, we propose FlowKANet in which Kolmogorov-Arnold Networks replace standard MLP layers, reducing trainable parameters while maintaining competitive predictive performance. FlowKANet integrates KAMP-Attn (Kolmogorov-Arnold Message Passing with Attention), embedding KAN operators directly into message-passing and attention computation. Finally, we distill the model into symbolic surrogate models using block-wise regression, producing closed-form equations that eliminate trainable weights while preserving graph-structured dependencies. The results show that KAN layers provide a favorable trade-off between efficiency and accuracy and that symbolic surrogates emphasize the potential for lightweight deployment and enhanced transparency.

