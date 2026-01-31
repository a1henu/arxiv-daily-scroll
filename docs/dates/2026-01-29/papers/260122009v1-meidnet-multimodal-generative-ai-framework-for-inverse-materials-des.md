---
layout: default
title: MEIDNet: Multimodal generative AI framework for inverse materials design
---

# MEIDNet: Multimodal generative AI framework for inverse materials design
**arXiv**：[2601.22009v1](https://arxiv.org/abs/2601.22009) · [PDF](https://arxiv.org/pdf/2601.22009.pdf)  
**作者**：Anand Babu, Rogério Almeida Gouvêa, Pierre Vandergheynst, Gian-Marco Rignanese  

**一句话要点**：提出MEIDNet多模态生成AI框架，通过对比学习和等变图神经网络加速材料逆向设计。

**关键词**：材料逆向设计, 多模态学习, 等变图神经网络, 对比学习, 生成模型, 钙钛矿结构

## 3 点简述
- 核心问题：材料逆向设计中需同时学习结构和属性，以高效探索化学结构空间。
- 方法要点：结合生成逆向设计与多模态学习，使用等变图神经网络编码结构，通过跨模态学习对齐潜在空间。
- 实验或效果：学习效率提升约60倍，生成低带隙钙钛矿结构的SUN率达13.6%，并通过第一性原理验证。

## 摘要（原文）

> In this work, we present Multimodal Equivariant Inverse Design Network (MEIDNet), a framework that jointly learns structural information and materials properties through contrastive learning, while encoding structures via an equivariant graph neural network (EGNN). By combining generative inverse design with multimodal learning, our approach accelerates the exploration of chemical-structural space and facilitates the discovery of materials that satisfy predefined property targets. MEIDNet exhibits strong latent-space alignment with cosine similarity 0.96 by fusion of three modalities through cross-modal learning. Through implementation of curriculum learning strategies, MEIDNet achieves ~60 times higher learning efficiency than conventional training techniques. The potential of our multimodal approach is demonstrated by generating low-bandgap perovskite structures at a stable, unique, and novel (SUN) rate of 13.6 %, which are further validated by ab initio methods. Our inverse design framework demonstrates both scalability and adaptability, paving the way for the universal learning of chemical space across diverse modalities.

