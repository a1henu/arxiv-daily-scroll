---
layout: default
title: Transformers as Measure-Theoretic Associative Memory: A Statistical Perspective and Minimax Optimality
---

# Transformers as Measure-Theoretic Associative Memory: A Statistical Perspective and Minimax Optimality
**arXiv**：[2602.01863v1](https://arxiv.org/abs/2602.01863) · [PDF](https://arxiv.org/pdf/2602.01863.pdf)  
**作者**：Ryotaro Kawata, Taiji Suzuki  

**一句话要点**：提出基于测度论的Transformer模型，用于从任意长分布上下文中进行关联记忆检索，并证明其极小极大最优性。

**关键词**：测度论Transformer, 关联记忆, 极小极大最优性, 分布上下文, 内容寻址检索, 泛化保证

## 3 点简述
- 核心问题：将Transformer的关联记忆能力重新定义为概率测度层面的内容寻址检索，处理分布化上下文。
- 方法要点：使用浅层测度论Transformer结合MLP，在谱假设下学习召回-预测映射，通过经验风险最小化训练。
- 实验或效果：建立匹配的极小极大下界，证明收敛阶的锐利性，提供可证明泛化保证的设计与分析框架。

## 摘要（原文）

> Transformers excel through content-addressable retrieval and the ability to exploit contexts of, in principle, unbounded length. We recast associative memory at the level of probability measures, treating a context as a distribution over tokens and viewing attention as an integral operator on measures. Concretely, for mixture contexts $ν= I^{-1} \sum_{i=1}^I μ^{(i^*)}$ and a query $x_{\mathrm{q}}(i^*)$, the task decomposes into (i) recall of the relevant component $μ^{(i^*)}$ and (ii) prediction from $(μ_{i^*},x_\mathrm{q})$. We study learned softmax attention (not a frozen kernel) trained by empirical risk minimization and show that a shallow measure-theoretic Transformer composed with an MLP learns the recall-and-predict map under a spectral assumption on the input densities. We further establish a matching minimax lower bound with the same rate exponent (up to multiplicative constants), proving sharpness of the convergence order. The framework offers a principled recipe for designing and analyzing Transformers that recall from arbitrarily long, distributional contexts with provable generalization guarantees.

