---
layout: default
title: Temporal-Aware Heterogeneous Graph Reasoning with Multi-View Fusion for Temporal Question Answering
---

# Temporal-Aware Heterogeneous Graph Reasoning with Multi-View Fusion for Temporal Question Answering
**arXiv**：[2602.19569v1](https://arxiv.org/abs/2602.19569) · [PDF](https://arxiv.org/pdf/2602.19569.pdf)  
**作者**：Wuzhenghong Wen, Bowen Zhou, Jinwen Huang, Xianjie Wu, Yuwei Sun, Su Pan, Liang Li, Jianting Liu  

**一句话要点**：提出基于时间感知异构图推理与多视图融合的框架，以提升时序知识图谱问答性能。

**关键词**：时序知识图谱问答, 异构图推理, 多视图融合, 时间感知编码, 多跳推理, 注意力机制

## 3 点简述
- 核心问题：现有方法在时序约束融入、多跳推理和图-语言融合方面存在不足。
- 方法要点：结合约束感知问题表示、时间感知图神经网络和多视图注意力机制。
- 实验或效果：在多个基准测试中优于基线，验证了方法的有效性。

## 摘要（原文）

> Question Answering over Temporal Knowledge Graphs (TKGQA) has attracted growing interest for handling time-sensitive queries. However, existing methods still struggle with: 1) weak incorporation of temporal constraints in question representation, causing biased reasoning; 2) limited ability to perform explicit multi-hop reasoning; and 3) suboptimal fusion of language and graph representations. We propose a novel framework with temporal-aware question encoding, multi-hop graph reasoning, and multi-view heterogeneous information fusion. Specifically, our approach introduces: 1) a constraint-aware question representation that combines semantic cues from language models with temporal entity dynamics; 2) a temporal-aware graph neural network for explicit multi-hop reasoning via time-aware message passing; and 3) a multi-view attention mechanism for more effective fusion of question context and temporal graph knowledge. Experiments on multiple TKGQA benchmarks demonstrate consistent improvements over multiple baselines.

