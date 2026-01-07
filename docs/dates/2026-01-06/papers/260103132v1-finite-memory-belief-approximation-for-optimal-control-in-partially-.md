---
layout: default
title: Finite Memory Belief Approximation for Optimal Control in Partially Observable Markov Decision Processes
---

# Finite Memory Belief Approximation for Optimal Control in Partially Observable Markov Decision Processes
**arXiv**：[2601.03132v1](https://arxiv.org/abs/2601.03132) · [PDF](https://arxiv.org/pdf/2601.03132.pdf)  
**作者**：Mintae Kim  

**一句话要点**：提出基于截断历史的有限记忆信念近似方法，以量化部分可观测马尔可夫决策过程中的控制性能损失。

**关键词**：部分可观测马尔可夫决策过程, 有限记忆信念近似, Wasserstein度量, 控制性能边界, 线性二次高斯系统, 信息损失量化

## 3 点简述
- 研究部分可观测随机最优控制中无限维信念状态不实用的问题。
- 利用Wasserstein度量建立信息损失与控制性能的直接理论关系。
- 在线性二次高斯系统中验证信念失配随记忆长度指数衰减，性能失配相应缩放。

## 摘要（原文）

> We study finite memory belief approximation for partially observable (PO) stochastic optimal control (SOC) problems. While belief states are sufficient for SOC in partially observable Markov decision processes (POMDPs), they are generally infinite-dimensional and impractical. We interpret truncated input-output (IO) histories as inducing a belief approximation and develop a metric-based theory that directly relates information loss to control performance. Using the Wasserstein metric, we derive policy-conditional performance bounds that quantify value degradation induced by finite memory along typical closed-loop trajectories. Our analysis proceeds via a fixed-policy comparison: we evaluate two cost functionals under the same closed-loop execution and isolate the effect of replacing the true belief by its finite memory approximation inside the belief-level cost. For linear quadratic Gaussian (LQG) systems, we provide closed-form belief mismatch evaluation and empirically validate the predicted mechanism, demonstrating that belief mismatch decays approximately exponentially with memory length and that the induced performance mismatch scales accordingly. Together, these results provide a metric-aware characterization of what finite memory belief approximation can and cannot achieve in PO settings.

