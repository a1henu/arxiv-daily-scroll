---
layout: default
title: HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control
---

# HopFormer: Sparse Graph Transformers with Explicit Receptive Field Control
**arXiv**：[2602.02268v1](https://arxiv.org/abs/2602.02268) · [PDF](https://arxiv.org/pdf/2602.02268.pdf)  
**作者**：Sanggeon Yun, Raheeb Hassan, Ryozo Masukawa, Sungheon Jeong, Mohsen Imani  

**一句话要点**：提出HopFormer，通过头特定n跳掩码稀疏注意力注入图结构，无需位置编码或架构修改。

**关键词**：图Transformer, 稀疏注意力, 感受野控制, 小世界图, 图神经网络

## 3 点简述
- 核心问题：图Transformer依赖位置编码和密集全局注意力，可能不必要且计算成本高。
- 方法要点：使用头特定n跳掩码稀疏注意力，实现显式感受野控制和线性计算缩放。
- 实验或效果：在节点和图级基准测试中表现竞争或更优，揭示小世界属性影响注意力需求。

## 摘要（原文）

> Graph Transformers typically rely on explicit positional or structural encodings and dense global attention to incorporate graph topology. In this work, we show that neither is essential. We introduce HopFormer, a graph Transformer that injects structure exclusively through head-specific n-hop masked sparse attention, without the use of positional encodings or architectural modifications. This design provides explicit and interpretable control over receptive fields while enabling genuinely sparse attention whose computational cost scales linearly with mask sparsity. Through extensive experiments on both node-level and graph-level benchmarks, we demonstrate that our approach achieves competitive or superior performance across diverse graph structures. Our results further reveal that dense global attention is often unnecessary: on graphs with strong small-world properties, localized attention yields more stable and consistently high performance, while on graphs with weaker small-world effects, global attention offers diminishing returns. Together, these findings challenge prevailing assumptions in graph Transformer design and highlight sparsity-controlled attention as a principled and efficient alternative.

