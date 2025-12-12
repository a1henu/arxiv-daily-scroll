---
layout: default
title: HybridVFL: Disentangled Feature Learning for Edge-Enabled Vertical Federated Multimodal Classification
---

# HybridVFL: Disentangled Feature Learning for Edge-Enabled Vertical Federated Multimodal Classification
**arXiv**：[2512.10701v1](https://arxiv.org/abs/2512.10701) · [PDF](https://arxiv.org/pdf/2512.10701.pdf)  
**作者**：Mostafa Anoosha, Zeinab Dehghani, Kuniko Paxton, Koorosh Aslansefat, Dhavalkumar Thakker  

**一句话要点**：提出HybridVFL框架，通过特征解耦与跨模态Transformer解决边缘垂直联邦多模态分类中的特征融合瓶颈。

**关键词**：垂直联邦学习, 多模态分类, 特征解耦, 跨模态Transformer, 边缘AI, 隐私保护

## 3 点简述
- 核心问题：标准垂直联邦学习在边缘AI场景中因简单特征融合导致性能受限。
- 方法要点：采用客户端特征解耦与服务器端跨模态Transformer进行上下文感知融合。
- 实验或效果：在HAM10000皮肤病变数据集上显著优于基线，验证了高级融合机制的重要性。

## 摘要（原文）

> Vertical Federated Learning (VFL) offers a privacy-preserving paradigm for Edge AI scenarios like mobile health diagnostics, where sensitive multimodal data reside on distributed, resource-constrained devices. Yet, standard VFL systems often suffer performance limitations due to simplistic feature fusion. This paper introduces HybridVFL, a novel framework designed to overcome this bottleneck by employing client-side feature disentanglement paired with a server-side cross-modal transformer for context-aware fusion. Through systematic evaluation on the multimodal HAM10000 skin lesion dataset, we demonstrate that HybridVFL significantly outperforms standard federated baselines, validating the criticality of advanced fusion mechanisms in robust, privacy-preserving systems.

