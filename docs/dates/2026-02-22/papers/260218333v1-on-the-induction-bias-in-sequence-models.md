---
layout: default
title: On the "Induction Bias" in Sequence Models
---

# On the "Induction Bias" in Sequence Models
**arXiv**：[2602.18333v1](https://arxiv.org/abs/2602.18333) · [PDF](https://arxiv.org/pdf/2602.18333.pdf)  
**作者**：M. Reza Ebrahimi, Michaël Defferrard, Sunny Panchal, Roland Memisevic  

**一句话要点**：比较Transformer与RNN的数据效率与状态跟踪能力，揭示Transformer在分布内训练中的局限性

**关键词**：状态跟踪, 数据效率, Transformer, 循环神经网络, 长度泛化, 权重共享

## 3 点简述
- 核心问题：Transformer在状态跟踪任务中，即使训练与评估分布匹配，仍存在数据效率低和长度泛化差的问题
- 方法要点：通过大规模实验分析Transformer和RNN在不同监督机制下的数据需求与权重共享程度
- 实验或效果：Transformer需更多数据应对状态空间和序列长度增长，且跨长度权重共享无效，而RNN能有效共享学习

## 摘要（原文）

> Despite the remarkable practical success of transformer-based language models, recent work has raised concerns about their ability to perform state tracking. In particular, a growing body of literature has shown this limitation primarily through failures in out-of-distribution (OOD) generalization, such as length extrapolation. In this work, we shift attention to the in-distribution implications of these limitations. We conduct a large-scale experimental study of the data efficiency of transformers and recurrent neural networks (RNNs) across multiple supervision regimes. We find that the amount of training data required by transformers grows much more rapidly with state-space size and sequence length than for RNNs. Furthermore, we analyze the extent to which learned state-tracking mechanisms are shared across different sequence lengths. We show that transformers exhibit negligible or even detrimental weight sharing across lengths, indicating that they learn length-specific solutions in isolation. In contrast, recurrent models exhibit effective amortized learning by sharing weights across lengths, allowing data from one sequence length to improve performance on others. Together, these results demonstrate that state tracking remains a fundamental challenge for transformers, even when training and evaluation distributions match.

