---
layout: default
title: Position-Aware Sequential Attention for Accurate Next Item Recommendations
---

# Position-Aware Sequential Attention for Accurate Next Item Recommendations
**arXiv**：[2602.21052v1](https://arxiv.org/abs/2602.21052) · [PDF](https://arxiv.org/pdf/2602.21052.pdf)  
**作者**：Timur Nabiev, Evgeny Frolov  

**一句话要点**：提出位置感知顺序注意力机制，以改进序列自注意力模型中的位置信息处理，提升下一项推荐准确性。

**关键词**：序列推荐, 自注意力机制, 位置嵌入, 核方法, 下一项预测

## 3 点简述
- 核心问题：传统加性位置嵌入在序列自注意力中导致位置信息与语义纠缠，传播弱，限制顺序模式捕获。
- 方法要点：引入可学习位置核，在位置空间独立操作，直接调制注意力权重，实现解耦的多尺度顺序建模。
- 实验或效果：在标准下一项预测基准测试中，位置核注意力机制持续优于强基线模型。

## 摘要（原文）

> Sequential self-attention models usually rely on additive positional embeddings, which inject positional information into item representations at the input. In the absence of positional signals, the attention block is permutation-equivariant over sequence positions and thus has no intrinsic notion of temporal order beyond causal masking. We argue that additive positional embeddings make the attention mechanism only superficially sensitive to sequence order: positional information is entangled with item embedding semantics, propagates weakly in deep architectures, and limits the ability to capture rich sequential patterns. To address these limitations, we introduce a kernelized self-attention mechanism, where a learnable positional kernel operates purely in the position space, disentangled from semantic similarity, and directly modulates attention weights. When applied per attention block, this kernel enables adaptive multi-scale sequential modeling. Experiments on standard next-item prediction benchmarks show that our positional kernel attention consistently improves over strong competing baselines.

