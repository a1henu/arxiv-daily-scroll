---
layout: default
title: Holographic generative flows with AdS/CFT
---

# Holographic generative flows with AdS/CFT
**arXiv**：[2601.22033v1](https://arxiv.org/abs/2601.22033) · [PDF](https://arxiv.org/pdf/2601.22033.pdf)  
**作者**：Ehsan Mirafzali, Sanjit Shashi, Sanya Murdeshwar, Edgar Shaghoulian, Daniele Venturi, Razvan Marinescu  

**一句话要点**：提出基于AdS/CFT的全息生成流框架，以提升流匹配算法的收敛速度与质量。

**关键词**：全息生成流, AdS/CFT对应, 流匹配算法, 生成建模, 物理可解释性, 深度学习

## 3 点简述
- 核心问题：如何将量子引力全息原理应用于生成式机器学习，增强流匹配算法的物理可解释性。
- 方法要点：利用AdS中标量场的体-边界映射，表示数据从基分布到学习分布的流动过程。
- 实验或效果：在棋盘玩具数据集和MNIST上，模型比无物理的流匹配模型收敛更快、质量更高。

## 摘要（原文）

> We present a framework for generative machine learning that leverages the holographic principle of quantum gravity, or to be more precise its manifestation as the anti-de Sitter/conformal field theory (AdS/CFT) correspondence, with techniques for deep learning and transport theory. Our proposal is to represent the flow of data from a base distribution to some learned distribution using the bulk-to-boundary mapping of scalar fields in AdS. In the language of machine learning, we are representing and augmenting the flow-matching algorithm with AdS physics. Using a checkerboard toy dataset and MNIST, we find that our model achieves faster and higher quality convergence than comparable physics-free flow-matching models. Our method provides a physically interpretable version of flow matching. More broadly, it establishes the utility of AdS physics and geometry in the development of novel paradigms in generative modeling.

