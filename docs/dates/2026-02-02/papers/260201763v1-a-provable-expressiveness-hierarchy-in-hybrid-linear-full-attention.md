---
layout: default
title: A Provable Expressiveness Hierarchy in Hybrid Linear-Full Attention
---

# A Provable Expressiveness Hierarchy in Hybrid Linear-Full Attention
**arXiv**：[2602.01763v1](https://arxiv.org/abs/2602.01763) · [PDF](https://arxiv.org/pdf/2602.01763.pdf)  
**作者**：Xiaowei Ye, Xiaoyu He, Chao Liao, Chen Wu, Pinyan Lu  

**一句话要点**：提出理论证明混合注意力与全注意力的表达能力层次，以解决高效注意力机制表达力缺乏严格理论刻画的问题。

**关键词**：注意力机制, 表达能力理论, Transformer模型, 线性注意力, 混合注意力, 序列推理

## 3 点简述
- 核心问题：高效注意力机制（如线性、混合注意力）相对于全注意力的表达能力缺乏严格理论刻画。
- 方法要点：建立表达能力层次，证明在序列函数组合任务中，全注意力网络层数需求远少于混合网络。
- 实验或效果：提供首个可证明的混合注意力与全注意力分离，为理解不同注意力机制的能力和限制提供理论视角。

## 摘要（原文）

> Transformers serve as the foundation of most modern large language models. To mitigate the quadratic complexity of standard full attention, various efficient attention mechanisms, such as linear and hybrid attention, have been developed. A fundamental gap remains: their expressive power relative to full attention lacks a rigorous theoretical characterization. In this work, we theoretically characterize the performance differences among these attention mechanisms. Our theory applies to all linear attention variants that can be formulated as a recurrence, including Mamba, DeltaNet, etc. Specifically, we establish an expressiveness hierarchy: for the sequential function composition-a multi-step reasoning task that must occur within a model's forward pass, an ($L+1$)-layer full attention network is sufficient, whereas any hybrid network interleaving $L-1$ layers of full attention with a substantially larger number ($2^{3L^2}$) of linear attention layers cannot solve it. This result demonstrates a clear separation in expressive power between the two types of attention. Our work provides the first provable separation between hybrid attention and standard full attention, offering a theoretical perspective for understanding the fundamental capabilities and limitations of different attention mechanisms.

