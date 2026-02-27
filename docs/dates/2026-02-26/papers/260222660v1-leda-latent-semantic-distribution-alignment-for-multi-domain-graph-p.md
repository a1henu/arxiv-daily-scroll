---
layout: default
title: LEDA: Latent Semantic Distribution Alignment for Multi-domain Graph Pre-training
---

# LEDA: Latent Semantic Distribution Alignment for Multi-domain Graph Pre-training
**arXiv**：[2602.22660v1](https://arxiv.org/abs/2602.22660) · [PDF](https://arxiv.org/pdf/2602.22660.pdf)  
**作者**：Lianze Shan, Jitao Zhao, Dongxiao He, Siqi Liu, Jiaxu Cui, Weixiong Zhang  

**一句话要点**：提出LEDA模型以解决多领域图预训练中的语义对齐和训练指导不足问题。

**关键词**：图预训练, 多领域学习, 语义对齐, 变分推断, 跨领域迁移

## 3 点简述
- 核心问题：现有方法因数据对齐简单和训练指导有限，难以从通用图中学习有效知识。
- 方法要点：引入维度投影单元和变分语义推断模块，对齐多领域特征到共享语义空间。
- 实验或效果：在广泛图数据和下游任务中表现优异，尤其在少样本跨领域设置中显著超越基线。

## 摘要（原文）

> Recent advances in generic large models, such as GPT and DeepSeek, have motivated the introduction of universality to graph pre-training, aiming to learn rich and generalizable knowledge across diverse domains using graph representations to improve performance in various downstream applications. However, most existing methods face challenges in learning effective knowledge from generic graphs, primarily due to simplistic data alignment and limited training guidance. The issue of simplistic data alignment arises from the use of a straightforward unification for highly diverse graph data, which fails to align semantics and misleads pre-training models. The problem with limited training guidance lies in the arbitrary application of in-domain pre-training paradigms to cross-domain scenarios. While it is effective in enhancing discriminative representation in one data space, it struggles to capture effective knowledge from many graphs. To address these challenges, we propose a novel Latent sEmantic Distribution Alignment (LEDA) model for universal graph pre-training. Specifically, we first introduce a dimension projection unit to adaptively align diverse domain features into a shared semantic space with minimal information loss. Furthermore, we design a variational semantic inference module to obtain the shared latent distribution. The distribution is then adopted to guide the domain projection, aligning it with shared semantics across domains and ensuring cross-domain semantic learning. LEDA exhibits strong performance across a broad range of graphs and downstream tasks. Remarkably, in few-shot cross-domain settings, it significantly outperforms in-domain baselines and advanced universal pre-training models.

