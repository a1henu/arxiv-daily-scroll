---
layout: default
title: Scalable Heterogeneous Graph Learning via Heterogeneous-aware Orthogonal Prototype Experts
---

# Scalable Heterogeneous Graph Learning via Heterogeneous-aware Orthogonal Prototype Experts
**arXiv**：[2601.05537v1](https://arxiv.org/abs/2601.05537) · [PDF](https://arxiv.org/pdf/2601.05537.pdf)  
**作者**：Wei Zhou, Hong Huang, Ruize Shi, Bang Liu  

**一句话要点**：提出HOPE框架以解决异质图学习中的线性投影瓶颈问题

**关键词**：异质图神经网络, 混合专家模型, 长尾分布, 原型学习, 正交化, 图学习

## 3 点简述
- 核心问题：异质图神经网络解码阶段使用单一线性头导致语义丢失和长尾节点欠服务
- 方法要点：基于可学习原型的路由分配实例，结合专家正交化提升多样性和防止崩溃
- 实验或效果：在四个真实数据集上验证了HOPE对多种SOTA HGNN骨干的稳定提升效果

## 摘要（原文）

> Heterogeneous Graph Neural Networks(HGNNs) have advanced mainly through better encoders, yet their decoding/projection stage still relies on a single shared linear head, assuming it can map rich node embeddings to labels. We call this the Linear Projection Bottleneck: in heterogeneous graphs, contextual diversity and long-tail shifts make a global head miss fine semantics, overfit hub nodes, and underserve tail nodes. While Mixture-of-Experts(MoE) could help, naively applying it clashes with structural imbalance and risks expert collapse. We propose a Heterogeneous-aware Orthogonal Prototype Experts framework named HOPE, a plug-and-play replacement for the standard prediction head. HOPE uses learnable prototype-based routing to assign instances to experts by similarity, letting expert usage follow the natural long-tail distribution, and adds expert orthogonalization to encourage diversity and prevent collapse. Experiments on four real datasets show consistent gains across SOTA HGNN backbones with minimal overhead.

