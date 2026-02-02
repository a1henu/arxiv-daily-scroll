---
layout: default
title: Disentangling multispecific antibody function with graph neural networks
---

# Disentangling multispecific antibody function with graph neural networks
**arXiv**：[2601.23212v1](https://arxiv.org/abs/2601.23212) · [PDF](https://arxiv.org/pdf/2601.23212.pdf)  
**作者**：Joshua Southern, Changpeng Lu, Santrupti Nerli, Samuel D. Stanton, Andrew M. Watkins, Franziska Seeger, Frédéric A. Dreyer  

**一句话要点**：提出基于图神经网络的框架，以解耦多特异性抗体的功能复杂性，加速治疗设计。

**关键词**：多特异性抗体, 图神经网络, 功能预测, 合成数据生成, 迁移学习, 治疗优化

## 3 点简述
- 核心问题：多特异性抗体功能预测受限于拓扑结构复杂性和实验数据稀缺。
- 方法要点：生成合成功能景观并设计图神经网络编码拓扑约束，区分序列相似但结构不同的配置。
- 实验或效果：模型在合成数据上训练后能复现复杂功能，通过迁移学习在生物数据中实现高预测精度，优化疗效与毒性平衡。

## 摘要（原文）

> Multispecific antibodies offer transformative therapeutic potential by engaging multiple epitopes simultaneously, yet their efficacy is an emergent property governed by complex molecular architectures. Rational design is often bottlenecked by the inability to predict how subtle changes in domain topology influence functional outcomes, a challenge exacerbated by the scarcity of comprehensive experimental data. Here, we introduce a computational framework to address part of this gap. First, we present a generative method for creating large-scale, realistic synthetic functional landscapes that capture non-linear interactions where biological activity depends on domain connectivity. Second, we propose a graph neural network architecture that explicitly encodes these topological constraints, distinguishing between format configurations that appear identical to sequence-only models. We demonstrate that this model, trained on synthetic landscapes, recapitulates complex functional properties and, via transfer learning, has the potential to achieve high predictive accuracy on limited biological datasets. We showcase the model's utility by optimizing trade-offs between efficacy and toxicity in trispecific T-cell engagers and retrieving optimal common light chains. This work provides a robust benchmarking environment for disentangling the combinatorial complexity of multispecifics, accelerating the design of next-generation therapeutics.

