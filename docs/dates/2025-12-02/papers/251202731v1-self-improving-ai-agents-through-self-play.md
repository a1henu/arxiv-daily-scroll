---
layout: default
title: Self-Improving AI Agents through Self-Play
---

# Self-Improving AI Agents through Self-Play
**arXiv**：[2512.02731v1](https://arxiv.org/abs/2512.02731) · [PDF](https://arxiv.org/pdf/2512.02731.pdf)  
**作者**：Przemyslaw Chojecki  

**一句话要点**：提出基于生成-验证-更新算子的自改进AI代理框架，统一自博弈与自校正方法。

**关键词**：自改进AI代理, 生成-验证-更新算子, 方差不等式, 自博弈, 自校正, 合成数据引导

## 3 点简述
- 核心问题：如何形式化AI代理的自改进过程，确保其稳定性和有效性。
- 方法要点：引入参数化流和自改进系数，推导方差不等式作为稳定性条件。
- 实验或效果：将框架应用于语言自博弈、自校正和合成数据引导，统一多种架构。

## 摘要（原文）

> We extend the moduli-theoretic framework of psychometric batteries to the domain of dynamical systems. While previous work established the AAI capability score as a static functional on the space of agent representations, this paper formalizes the agent as a flow $ν_r$ parameterized by computational resource $r$, governed by a recursive Generator-Verifier-Updater (GVU) operator. We prove that this operator generates a vector field on the parameter manifold $Θ$, and we identify the coefficient of self-improvement $κ$ as the Lie derivative of the capability functional along this flow.
>   The central contribution of this work is the derivation of the Variance Inequality, a spectral condition that is sufficient (under mild regularity) for the stability of self-improvement. We show that a sufficient condition for $κ> 0$ is that, up to curvature and step-size effects, the combined noise of generation and verification must be small enough.
>   We then apply this formalism to unify the recent literature on Language Self-Play (LSP), Self-Correction, and Synthetic Data bootstrapping. We demonstrate that architectures such as STaR, SPIN, Reflexion, GANs and AlphaZero are specific topological realizations of the GVU operator that satisfy the Variance Inequality through filtration, adversarial discrimination, or grounding in formal systems.

