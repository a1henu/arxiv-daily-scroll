---
layout: default
title: AutoRegressive Generation with B-rep Holistic Token Sequence Representation
---

# AutoRegressive Generation with B-rep Holistic Token Sequence Representation
**arXiv**：[2601.16771v1](https://arxiv.org/abs/2601.16771) · [PDF](https://arxiv.org/pdf/2601.16771.pdf)  
**作者**：Jiahao Li, Yunpeng Bai, Yongkang Dai, Hao Guo, Hongping Gan, Yilei Shi  

**一句话要点**：提出BrepARG，将B-rep编码为整体令牌序列，实现基于序列的自回归生成。

**关键词**：B-rep表示, 令牌序列编码, 自回归生成, Transformer架构, 几何拓扑融合

## 3 点简述
- 核心问题：现有B-rep表示方法依赖图结构，阻碍序列生成框架如Transformer的应用。
- 方法要点：将B-rep几何和拓扑编码为几何、位置和面索引令牌，构建层次化整体序列。
- 实验或效果：基于Transformer的自回归模型实现SOTA性能，验证序列表示的可行性。

## 摘要（原文）

> Previous representation and generation approaches for the B-rep relied on graph-based representations that disentangle geometric and topological features through decoupled computational pipelines, thereby precluding the application of sequence-based generative frameworks, such as transformer architectures that have demonstrated remarkable performance. In this paper, we propose BrepARG, the first attempt to encode B-rep's geometry and topology into a holistic token sequence representation, enabling sequence-based B-rep generation with an autoregressive architecture. Specifically, BrepARG encodes B-rep into 3 types of tokens: geometry and position tokens representing geometric features, and face index tokens representing topology. Then the holistic token sequence is constructed hierarchically, starting with constructing the geometry blocks (i.e., faces and edges) using the above tokens, followed by geometry block sequencing. Finally, we assemble the holistic sequence representation for the entire B-rep. We also construct a transformer-based autoregressive model that learns the distribution over holistic token sequences via next-token prediction, using a multi-layer decoder-only architecture with causal masking. Experiments demonstrate that BrepARG achieves state-of-the-art (SOTA) performance. BrepARG validates the feasibility of representing B-rep as holistic token sequences, opening new directions for B-rep generation.

