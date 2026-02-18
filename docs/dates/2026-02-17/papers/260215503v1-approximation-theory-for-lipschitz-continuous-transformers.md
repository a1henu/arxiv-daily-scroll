---
layout: default
title: Approximation Theory for Lipschitz Continuous Transformers
---

# Approximation Theory for Lipschitz Continuous Transformers
**arXiv**：[2602.15503v1](https://arxiv.org/abs/2602.15503) · [PDF](https://arxiv.org/pdf/2602.15503.pdf)  
**作者**：Takashi Furuya, Davide Murari, Carola-Bibiane Schönlieb  

**一句话要点**：提出梯度下降型上下文Transformer以解决Lipschitz连续Transformer的近似理论保证问题

**关键词**：Lipschitz连续Transformer, 近似理论, 梯度下降型Transformer, 测度论形式化, 通用近似定理, 稳定性与鲁棒性

## 3 点简述
- 核心问题：Lipschitz连续Transformer缺乏近似理论保证，影响安全敏感部署的稳定性与鲁棒性
- 方法要点：通过负梯度流的显式欧拉步实现MLP和注意力块，构建Lipschitz连续Transformer
- 实验或效果：证明在Lipschitz约束函数空间中的通用近似定理，基于测度论形式化，近似保证独立于令牌数量

## 摘要（原文）

> Stability and robustness are critical for deploying Transformers in safety-sensitive settings. A principled way to enforce such behavior is to constrain the model's Lipschitz constant. However, approximation-theoretic guarantees for architectures that explicitly preserve Lipschitz continuity have yet to be established. In this work, we bridge this gap by introducing a class of gradient-descent-type in-context Transformers that are Lipschitz-continuous by construction. We realize both MLP and attention blocks as explicit Euler steps of negative gradient flows, ensuring inherent stability without sacrificing expressivity. We prove a universal approximation theorem for this class within a Lipschitz-constrained function space. Crucially, our analysis adopts a measure-theoretic formalism, interpreting Transformers as operators on probability measures, to yield approximation guarantees independent of token count. These results provide a rigorous theoretical foundation for the design of robust, Lipschitz continuous Transformer architectures.

