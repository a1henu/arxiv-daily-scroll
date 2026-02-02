---
layout: default
title: Stochastic Linear Bandits with Parameter Noise
---

# Stochastic Linear Bandits with Parameter Noise
**arXiv**：[2601.23164v1](https://arxiv.org/abs/2601.23164) · [PDF](https://arxiv.org/pdf/2601.23164.pdf)  
**作者**：Daniel Ezer, Alon Peled-Cohen, Yishay Mansour  

**一句话要点**：提出参数噪声模型下的随机线性赌博机，分析其遗憾界并设计简单算法实现最优性能。

**关键词**：随机线性赌博机, 参数噪声模型, 遗憾分析, 探索-利用算法, 动作集优化

## 3 点简述
- 研究随机线性赌博机中参数噪声模型，奖励由动作与随机参数的内积生成。
- 证明遗憾上界为O~(√(dT log(K/δ) σ²_max))，下界为Ω~(d√(T σ²_max))，在log(K)≈d时紧致。
- 针对ℓ_p单位球动作集，展示最优遗憾界O~(√(dT σ²_q))，可用简单探索-利用算法实现。

## 摘要（原文）

> We study the stochastic linear bandits with parameter noise model, in which the reward of action $a$ is $a^\top θ$ where $θ$ is sampled i.i.d. We show a regret upper bound of $\widetilde{O} (\sqrt{d T \log (K/δ) σ^2_{\max})}$ for a horizon $T$, general action set of size $K$ of dimension $d$, and where $σ^2_{\max}$ is the maximal variance of the reward for any action. We further provide a lower bound of $\widetildeΩ (d \sqrt{T σ^2_{\max}})$ which is tight (up to logarithmic factors) whenever $\log (K) \approx d$. For more specific action sets, $\ell_p$ unit balls with $p \leq 2$ and dual norm $q$, we show that the minimax regret is $\widetildeΘ (\sqrt{dT σ^2_q)}$, where $σ^2_q$ is a variance-dependent quantity that is always at most $4$. This is in contrast to the minimax regret attainable for such sets in the classic additive noise model, where the regret is of order $d \sqrt{T}$. Surprisingly, we show that this optimal (up to logarithmic factors) regret bound is attainable using a very simple explore-exploit algorithm.

