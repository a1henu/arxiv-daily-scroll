---
layout: default
title: GNN-MoE: Context-Aware Patch Routing using GNNs for Parameter-Efficient Domain Generalization
---

# GNN-MoE: Context-Aware Patch Routing using GNNs for Parameter-Efficient Domain Generalization
**arXiv**：[2511.04008v1](https://arxiv.org/abs/2511.04008) · [PDF](https://arxiv.org/pdf/2511.04008.pdf)  
**作者**：Mahmoud Soliman, Omar Abdelaziz, Ahmed Radwan, Anand, Mohamed Shehata  

**一句话要点**：提出GNN-MoE以解决领域泛化中参数高效适应问题

**关键词**：领域泛化, 参数高效微调, 图神经网络, 专家混合, 视觉Transformer

## 3 点简述
- 核心问题：领域泛化中预训练ViT高效适应困难，标准微调成本高且泛化差。
- 方法要点：使用GNN路由器和MoE框架，基于图结构动态分配图像块到专家。
- 实验或效果：在DG基准上实现先进性能，参数效率高。

## 摘要（原文）

> Domain generalization (DG) seeks robust Vision Transformer (ViT) performance
> on unseen domains. Efficiently adapting pretrained ViTs for DG is challenging;
> standard fine-tuning is costly and can impair generalization. We propose
> GNN-MoE, enhancing Parameter-Efficient Fine-Tuning (PEFT) for DG with a
> Mixture-of-Experts (MoE) framework using efficient Kronecker adapters. Instead
> of token-based routing, a novel Graph Neural Network (GNN) router (GCN, GAT,
> SAGE) operates on inter-patch graphs to dynamically assign patches to
> specialized experts. This context-aware GNN routing leverages inter-patch
> relationships for better adaptation to domain shifts. GNN-MoE achieves
> state-of-the-art or competitive DG benchmark performance with high parameter
> efficiency, highlighting the utility of graph-based contextual routing for
> robust, lightweight DG.

