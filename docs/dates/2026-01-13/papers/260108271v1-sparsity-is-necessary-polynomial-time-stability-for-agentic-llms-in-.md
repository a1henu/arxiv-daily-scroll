---
layout: default
title: Sparsity Is Necessary: Polynomial-Time Stability for Agentic LLMs in Large Action Spaces
---

# Sparsity Is Necessary: Polynomial-Time Stability for Agentic LLMs in Large Action Spaces
**arXiv**：[2601.08271v1](https://arxiv.org/abs/2601.08271) · [PDF](https://arxiv.org/pdf/2601.08271.pdf)  
**作者**：Angshul Majumdar  

**一句话要点**：提出稀疏代理控制框架，以多项式时间稳定性解决大动作空间中工具增强LLM的决策问题。

**关键词**：稀疏代理控制, 大动作空间, 工具增强LLM, 策略学习, 压缩感知, 样本复杂度

## 3 点简述
- 核心问题：工具增强LLM在大离散动作空间中面临稀疏相关动作的序列决策挑战，传统方法不稳定。
- 方法要点：基于凸代理和ell_{1,2}正则化，建立压缩感知式理论，实现样本效率高的策略学习和工具支持恢复。
- 实验或效果：理论证明稀疏策略类仅需k log M样本，而密集类需Ω(M)样本，解释提示控制的不稳定性。

## 摘要（原文）

> Tool-augmented LLM systems expose a control regime that learning theory has largely ignored: sequential decision-making with a massive discrete action universe (tools, APIs, documents) in which only a small, unknown subset is relevant for any fixed task distribution. We formalize this setting as Sparse Agentic Control (SAC), where policies admit block-sparse representations over M >> 1 actions and rewards depend on sparse main effects and (optionally) sparse synergies. We study ell_{1,2}-regularized policy learning through a convex surrogate and establish sharp, compressed-sensing-style results: (i) estimation and value suboptimality scale as k (log M / T)^{1/2} under a Policy-RSC condition; (ii) exact tool-support recovery holds via primal-dual witness arguments when T > k log M under incoherence and beta-min; and (iii) any dense policy class requires Omega(M) samples, explaining the instability of prompt-only controllers. We further show that under partial observability, LLMs matter only through a belief/representation error epsilon_b, yielding an additive O(epsilon_b) degradation while preserving logarithmic dependence on M. Extensions cover tuning-free, online, robust, group-sparse, and interaction-aware SAC.

