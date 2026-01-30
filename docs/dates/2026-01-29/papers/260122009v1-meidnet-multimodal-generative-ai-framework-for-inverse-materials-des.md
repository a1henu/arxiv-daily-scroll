---
layout: default
title: MEIDNet: Multimodal generative AI framework for inverse materials design
---

# MEIDNet: Multimodal generative AI framework for inverse materials design
**arXiv**：[2601.22009v1](https://arxiv.org/abs/2601.22009) · [PDF](https://arxiv.org/pdf/2601.22009.pdf)  
**作者**：Anand Babu, Rogério Almeida Gouvêa, Pierre Vandergheynst, Gian-Marco Rignanese  

**一句话要点**：提出MEIDNet多模态生成式AI框架，通过逆设计加速材料发现以满足预设性能目标。

**关键词**：多模态学习, 生成式逆设计, 等变图神经网络, 材料发现, 对比学习, 钙钛矿结构

## 3 点简述
- 核心问题：传统材料设计方法探索化学结构空间效率低，难以快速发现满足特定性能的材料。
- 方法要点：结合对比学习和等变图神经网络，通过多模态学习对齐结构信息与材料性能，实现生成式逆设计。
- 实验或效果：在钙钛矿材料生成中，达到13.6%的稳定、独特、新颖率，学习效率比传统方法提高约60倍。

## 摘要（原文）

> In this work, we present Multimodal Equivariant Inverse Design Network (MEIDNet), a framework that jointly learns structural information and materials properties through contrastive learning, while encoding structures via an equivariant graph neural network (EGNN). By combining generative inverse design with multimodal learning, our approach accelerates the exploration of chemical-structural space and facilitates the discovery of materials that satisfy predefined property targets. MEIDNet exhibits strong latent-space alignment with cosine similarity 0.96 by fusion of three modalities through cross-modal learning. Through implementation of curriculum learning strategies, MEIDNet achieves ~60 times higher learning efficiency than conventional training techniques. The potential of our multimodal approach is demonstrated by generating low-bandgap perovskite structures at a stable, unique, and novel (SUN) rate of 13.6 %, which are further validated by ab initio methods. Our inverse design framework demonstrates both scalability and adaptability, paving the way for the universal learning of chemical space across diverse modalities.

