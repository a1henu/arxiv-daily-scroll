---
layout: default
title: Frequentist Regret Analysis of Gaussian Process Thompson Sampling via Fractional Posteriors
---

# Frequentist Regret Analysis of Gaussian Process Thompson Sampling via Fractional Posteriors
**arXiv**：[2602.14472v1](https://arxiv.org/abs/2602.14472) · [PDF](https://arxiv.org/pdf/2602.14472.pdf)  
**作者**：Somjit Roy, Prateek Jaiswal, Anirban Bhattacharya, Debdeep Pati, Bani K. Mallick  

**一句话要点**：提出基于分数后验的高斯过程汤普森采样，用于连续动作空间决策，提供无离散化的频繁遗憾分析框架。

**关键词**：高斯过程汤普森采样, 频繁遗憾分析, 分数后验, 连续动作空间, 核方法, 决策理论

## 3 点简述
- 研究高斯过程汤普森采样在连续动作空间中的频繁遗憾分析，避免依赖先验工作中的域离散化。
- 将现有分析中的方差膨胀解释为基于分数后验的汤普森采样，推导出与信息增益和后验收缩率相关的核无关遗憾界。
- 在特定高斯过程先验条件下控制后验收缩率，为平方指数、Matérn和有理二次核提供统一遗憾界。

## 摘要（原文）

> We study Gaussian Process Thompson Sampling (GP-TS) for sequential decision-making over compact, continuous action spaces and provide a frequentist regret analysis based on fractional Gaussian process posteriors, without relying on domain discretization as in prior work. We show that the variance inflation commonly assumed in existing analyses of GP-TS can be interpreted as Thompson Sampling with respect to a fractional posterior with tempering parameter $α\in (0,1)$. We derive a kernel-agnostic regret bound expressed in terms of the information gain parameter $γ_t$ and the posterior contraction rate $ε_t$, and identify conditions on the Gaussian process prior under which $ε_t$ can be controlled. As special cases of our general bound, we recover regret of order $\tilde{\mathcal{O}}(T^{\frac{1}{2}})$ for the squared exponential kernel, $\tilde{\mathcal{O}}(T^{\frac{2ν+3d}{2(2ν+d)}} )$ for the Matérn-$ν$ kernel, and a bound of order $\tilde{\mathcal{O}}(T^{\frac{2ν+3d}{2(2ν+d)}})$ for the rational quadratic kernel. Overall, our analysis provides a unified and discretization-free regret framework for GP-TS that applies broadly across kernel classes.

