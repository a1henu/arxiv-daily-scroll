---
layout: default
title: Nonparametric Teaching of Attention Learners
---

# Nonparametric Teaching of Attention Learners
**arXiv**：[2602.20461v1](https://arxiv.org/abs/2602.20461) · [PDF](https://arxiv.org/pdf/2602.20461.pdf)  
**作者**：Chen Zhang, Jianghui Wang, Bingyang Cheng, Zhongtao Chen, Wendong XU, Cong Wang, Marco Canini, Francesco Orabona, Yik Chung WU, Ngai Wong  

**一句话要点**：提出非参数化注意力教学范式以加速注意力学习器训练

**关键词**：注意力机制, 非参数化教学, 训练加速, 示例选择, 梯度下降

## 3 点简述
- 核心问题：注意力学习器训练成本高，需提升效率
- 方法要点：通过非参数化教学视角，选择示例子集优化训练
- 实验或效果：在LLM和ViT上减少训练时间，保持或提升准确性

## 摘要（原文）

> Attention learners, neural networks built on the attention mechanism, e.g., transformers, excel at learning the implicit relationships that relate sequences to their corresponding properties, e.g., mapping a given sequence of tokens to the probability of the next token. However, the learning process tends to be costly. To address this, we present a novel paradigm named Attention Neural Teaching (AtteNT) that reinterprets the learning process through a nonparametric teaching perspective. Specifically, the latter provides a theoretical framework for teaching mappings that are implicitly defined (i.e., nonparametric) via example selection. Such an implicit mapping is embodied through a dense set of sequence-property pairs, with the AtteNT teacher selecting a subset to accelerate convergence in attention learner training. By analytically investigating the role of attention on parameter-based gradient descent during training, and recasting the evolution of attention learners, shaped by parameter updates, through functional gradient descent in nonparametric teaching, we show for the first time that teaching attention learners is consistent with teaching importance-adaptive nonparametric learners. These new findings readily commit AtteNT to enhancing learning efficiency of attention learners. Specifically, we observe training time reductions of 13.01% for LLMs and 20.58% for ViTs, spanning both fine-tuning and training-from-scratch regimes. Crucially, these gains are achieved without compromising accuracy; in fact, performance is consistently preserved and often enhanced across a diverse set of downstream tasks.

