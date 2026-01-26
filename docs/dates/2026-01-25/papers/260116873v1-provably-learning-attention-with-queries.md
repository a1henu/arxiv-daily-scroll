---
layout: default
title: Provably Learning Attention with Queries
---

# Provably Learning Attention with Queries
**arXiv**：[2601.16873v1](https://arxiv.org/abs/2601.16873) · [PDF](https://arxiv.org/pdf/2601.16873.pdf)  
**作者**：Satwik Bhattamishra, Kulin Shah, Michael Hahn, Varun Kanade  

**一句话要点**：提出基于查询的算法，在单头注意力模型中可证明学习参数，并分析多头注意力的不可识别性。

**关键词**：注意力机制学习, 查询复杂度, 参数识别, Transformer模型, 压缩感知, 黑盒优化

## 3 点简述
- 研究黑盒访问下Transformer序列模型的学习问题，聚焦单头软注意力回归器。
- 针对单头注意力，提供精确学习算法，查询复杂度为O(d²)或O(rd)，并扩展到噪声鲁棒性。
- 证明多头注意力参数在值查询下一般不可识别，需额外结构假设才能保证学习。

## 摘要（原文）

> We study the problem of learning Transformer-based sequence models with black-box access to their outputs. In this setting, a learner may adaptively query the oracle with any sequence of vectors and observe the corresponding real-valued output. We begin with the simplest case, a single-head softmax-attention regressor. We show that for a model with width $d$, there is an elementary algorithm to learn the parameters of single-head attention exactly with $O(d^2)$ queries. Further, we show that if there exists an algorithm to learn ReLU feedforward networks (FFNs), then the single-head algorithm can be easily adapted to learn one-layer Transformers with single-head attention. Next, motivated by the regime where the head dimension $r \ll d$, we provide a randomised algorithm that learns single-head attention-based models with $O(rd)$ queries via compressed sensing arguments. We also study robustness to noisy oracle access, proving that under mild norm and margin conditions, the parameters can be estimated to $\varepsilon$ accuracy with a polynomial number of queries even when outputs are only provided up to additive tolerance. Finally, we show that multi-head attention parameters are not identifiable from value queries in general -- distinct parameterisations can induce the same input-output map. Hence, guarantees analogous to the single-head setting are impossible without additional structural assumptions.

