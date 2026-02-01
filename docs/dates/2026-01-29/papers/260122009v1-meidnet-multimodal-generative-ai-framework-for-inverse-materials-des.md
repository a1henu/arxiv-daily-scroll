---
layout: default
title: MEIDNet: Multimodal generative AI framework for inverse materials design
---

# MEIDNet: Multimodal generative AI framework for inverse materials design
**arXiv**：[2601.22009v1](https://arxiv.org/abs/2601.22009) · [PDF](https://arxiv.org/pdf/2601.22009.pdf)  
**作者**：Anand Babu, Rogério Almeida Gouvêa, Pierre Vandergheynst, Gian-Marco Rignanese  

**一句话要点**：提出MEIDNet多模态生成式AI框架，通过对比学习和等变图神经网络加速材料逆向设计。

**关键词**：材料逆向设计, 多模态学习, 等变图神经网络, 生成式AI, 对比学习, 钙钛矿材料

## 3 点简述
- 核心问题：材料逆向设计需高效探索化学结构空间以满足预设性能目标。
- 方法要点：结合多模态学习和生成式逆向设计，使用等变图神经网络编码结构信息。
- 实验或效果：在钙钛矿材料生成中实现13.6%的稳定、独特、新颖率，学习效率提升约60倍。

## 摘要（原文）

> In this work, we present Multimodal Equivariant Inverse Design Network (MEIDNet), a framework that jointly learns structural information and materials properties through contrastive learning, while encoding structures via an equivariant graph neural network (EGNN). By combining generative inverse design with multimodal learning, our approach accelerates the exploration of chemical-structural space and facilitates the discovery of materials that satisfy predefined property targets. MEIDNet exhibits strong latent-space alignment with cosine similarity 0.96 by fusion of three modalities through cross-modal learning. Through implementation of curriculum learning strategies, MEIDNet achieves ~60 times higher learning efficiency than conventional training techniques. The potential of our multimodal approach is demonstrated by generating low-bandgap perovskite structures at a stable, unique, and novel (SUN) rate of 13.6 %, which are further validated by ab initio methods. Our inverse design framework demonstrates both scalability and adaptability, paving the way for the universal learning of chemical space across diverse modalities.

