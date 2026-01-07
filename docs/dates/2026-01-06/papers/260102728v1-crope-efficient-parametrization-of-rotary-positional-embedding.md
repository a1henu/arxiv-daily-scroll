---
layout: default
title: CRoPE: Efficient Parametrization of Rotary Positional Embedding
---

# CRoPE: Efficient Parametrization of Rotary Positional Embedding
**arXiv**：[2601.02728v1](https://arxiv.org/abs/2601.02728) · [PDF](https://arxiv.org/pdf/2601.02728.pdf)  
**作者**：Beicheng Lou, Zifei Xu  

**一句话要点**：提出CRoPE以优化旋转位置编码的参数效率，在Transformer模型中节省近50%注意力参数。

**关键词**：旋转位置编码, 参数效率, Transformer模型, 复线性变换, 注意力机制

## 3 点简述
- 核心问题：旋转位置编码的Q/K/V投影实现与复线性变换不等价，存在参数冗余。
- 方法要点：采用复线性变换作为更自然的参数化方式，减少注意力块内参数。
- 实验或效果：经验验证参数减少对模型性能影响可忽略，提升参数使用效率和表示空间解释性。

## 摘要（原文）

> Rotary positional embedding has become the state-of-the-art approach to encode position information in transformer-based models. While it is often succinctly expressed in complex linear algebra, we note that the actual implementation of $Q/K/V$-projections is not equivalent to a complex linear transformation. We argue that complex linear transformation is a more natural parametrization and saves near 50\% parameters within the attention block. We show empirically that removing such redundancy has negligible impact on the model performance both in sample and out of sample. Our modification achieves more efficient parameter usage, as well as a cleaner interpretation of the representation space.

