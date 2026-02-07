---
layout: default
title: Orthogonal Self-Attention
---

# Orthogonal Self-Attention
**arXiv**：[2602.05996v1](https://arxiv.org/abs/2602.05996) · [PDF](https://arxiv.org/pdf/2602.05996.pdf)  
**作者**：Leo Zhang, James Martens  

**一句话要点**：提出正交自注意力以解决无跳跃连接Transformer中的不稳定问题

**关键词**：自注意力机制, Transformer架构, 正交矩阵, 秩塌缩, 雅可比矩阵条件数, 无跳跃连接训练

## 3 点简述
- 软最大自注意力在无跳跃连接架构中易导致秩塌缩和雅可比矩阵病态
- 通过映射斜对称矩阵至正交矩阵，设计正交自注意力机制
- 实现线性计算复杂度，并证明雅可比矩阵的良好条件性

## 摘要（原文）

> Softmax Self-Attention (SSA) is a key component of Transformer architectures. However, when utilised within skipless architectures, which aim to improve representation learning, recent work has highlighted the inherent instability of SSA due to inducing rank collapse and poorly-conditioned Jacobians. In this work, we design a novel attention mechanism: Orthogonal Self-Attention (OSA), which aims to bypass these issues with SSA, in order to allow for (non-causal) Transformers without skip connections and normalisation layers to be more easily trained. In particular, OSA parametrises the attention matrix to be orthogonal via mapping a skew-symmetric matrix, formed from query-key values, through the matrix exponential. We show that this can be practically implemented, by exploiting the low-rank structure of our query-key values, resulting in the computational complexity and memory cost of OSA scaling linearly with sequence length. Furthermore, we derive an initialisation scheme for which we prove ensures that the Jacobian of OSA is well-conditioned.

