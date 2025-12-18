---
layout: default
title: Graph Contextual Reinforcement Learning for Efficient Directed Controller Synthesis
---

# Graph Contextual Reinforcement Learning for Efficient Directed Controller Synthesis
**arXiv**：[2512.15295v1](https://arxiv.org/abs/2512.15295) · [PDF](https://arxiv.org/pdf/2512.15295.pdf)  
**作者**：Toshihide Ubukata, Enhong Mu, Takuto Yamauchi, Mingyue Zhang, Jialong Li, Kenji Tei  

**一句话要点**：提出GCRL方法，通过图神经网络增强强化学习，以提升控制器合成的效率。

**关键词**：控制器合成, 强化学习, 图神经网络, 探索策略, 形式化方法

## 3 点简述
- 控制器合成效率受限于探索策略，传统方法仅考虑有限当前特征。
- GCRL利用图神经网络编码LTS探索历史，捕获更广泛的非当前上下文信息。
- 在五个基准域中，GCRL在四个域表现出更优的学习效率和泛化能力。

## 摘要（原文）

> Controller synthesis is a formal method approach for automatically generating Labeled Transition System (LTS) controllers that satisfy specified properties. The efficiency of the synthesis process, however, is critically dependent on exploration policies. These policies often rely on fixed rules or strategies learned through reinforcement learning (RL) that consider only a limited set of current features. To address this limitation, this paper introduces GCRL, an approach that enhances RL-based methods by integrating Graph Neural Networks (GNNs). GCRL encodes the history of LTS exploration into a graph structure, allowing it to capture a broader, non-current-based context. In a comparative experiment against state-of-the-art methods, GCRL exhibited superior learning efficiency and generalization across four out of five benchmark domains, except one particular domain characterized by high symmetry and strictly local interactions.

