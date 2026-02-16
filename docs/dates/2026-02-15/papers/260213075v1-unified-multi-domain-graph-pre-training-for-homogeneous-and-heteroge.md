---
layout: default
title: Unified Multi-Domain Graph Pre-training for Homogeneous and Heterogeneous Graphs via Domain-Specific Expert Encoding
---

# Unified Multi-Domain Graph Pre-training for Homogeneous and Heterogeneous Graphs via Domain-Specific Expert Encoding
**arXiv**：[2602.13075v1](https://arxiv.org/abs/2602.13075) · [PDF](https://arxiv.org/pdf/2602.13075.pdf)  
**作者**：Chundong Liang, Yongqi Huang, Dongxiao He, Peiyuan Li, Yawen Li, Di Jin, Weixiong Zhang  

**一句话要点**：提出GPH²方法，通过领域特定专家编码实现同质与异质图的统一预训练，以应对混合图场景中的分布偏移问题。

**关键词**：图预训练, 同质图, 异质图, 专家编码, 多领域学习, 分布偏移

## 3 点简述
- 核心问题：现有图预训练方法多针对同质或异质图设计，难以统一建模混合图类型，且上游预训练与下游部署间存在分布偏移。
- 方法要点：采用统一多视图图构建编码混合图，引入领域特定专家编码捕获单图知识，并设计任务导向专家融合策略自适应整合专家。
- 实验或效果：在混合图上实验表明，GPH²能稳定跨图类型和领域迁移，显著优于现有图预训练方法。

## 摘要（原文）

> Graph pre-training has achieved remarkable success in recent years, delivering transferable representations for downstream adaptation. However, most existing methods are designed for either homogeneous or heterogeneous graphs, thereby hindering unified graph modeling across diverse graph types. This separation contradicts real-world applications, where mixed homogeneous and heterogeneous graphs are ubiquitous, and distribution shifts between upstream pre-training and downstream deployment are common. In this paper, we empirically demonstrate that a balanced mixture of homogeneous and heterogeneous graph pre-training benefits downstream tasks and propose a unified multi-domain \textbf{G}raph \textbf{P}re-training method across \textbf{H}omogeneous and \textbf{H}eterogeneous graphs ($\mathbf{GPH^{2}}$). To address the lack of a unified encoder for homogeneous and heterogeneous graphs, we propose a Unified Multi-View Graph Construction that simultaneously encodes both without explicit graph-type-specific designs. To cope with the increased cross-domain distribution discrepancies arising from mixed graphs, we introduce domain-specific expert encoding. Each expert is independently pre-trained on a single graph to capture domain-specific knowledge, thereby shielding the pre-training encoder from the adverse effects of cross-domain discrepancies. For downstream tasks, we further design a Task-oriented Expert Fusion Strategy that adaptively integrates multiple experts based on their discriminative strengths. Extensive experiments on mixed graphs demonstrate that $\text{GPH}^{2}$ enables stable transfer across graph types and domains, significantly outperforming existing graph pre-training methods.

