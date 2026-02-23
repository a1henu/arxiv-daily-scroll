---
layout: default
title: Tighter Regret Lower Bound for Gaussian Process Bandits with Squared Exponential Kernel in Hypersphere
---

# Tighter Regret Lower Bound for Gaussian Process Bandits with Squared Exponential Kernel in Hypersphere
**arXiv**：[2602.17940v1](https://arxiv.org/abs/2602.17940) · [PDF](https://arxiv.org/pdf/2602.17940.pdf)  
**作者**：Shogo Iwazaki  

**一句话要点**：针对超球面输入域的高斯过程赌博机，提出更紧的遗憾下界以部分解决维度依赖对数因子差距问题。

**关键词**：高斯过程赌博机, 平方指数核, 遗憾下界, 超球面输入域, 维度依赖对数因子, 最大信息增益

## 3 点简述
- 研究高斯过程赌博机在频率论设置下的算法无关最坏情况遗憾下界，聚焦平方指数核函数。
- 在超球面输入域下，证明累积遗憾下界为Ω(√T(ln T)^d(ln ln T)^{-d})，简单遗憾下界为Ω(ε^{-2}(ln 1/ε)^d(ln ln 1/ε)^{-d})。
- 提供平方指数核最大信息增益的改进上界O((ln T)^{d+1}(ln ln T)^{-d})，确保现有最佳算法在维度无关对数因子下的最优性。

## 摘要（原文）

> We study an algorithm-independent, worst-case lower bound for the Gaussian process (GP) bandit problem in the frequentist setting, where the reward function is fixed and has a bounded norm in the known reproducing kernel Hilbert space (RKHS). Specifically, we focus on the squared exponential (SE) kernel, one of the most widely used kernel functions in GP bandits. One of the remaining open questions for this problem is the gap in the \emph{dimension-dependent} logarithmic factors between upper and lower bounds. This paper partially resolves this open question under a hyperspherical input domain. We show that any algorithm suffers $Ω(\sqrt{T (\ln T)^{d} (\ln \ln T)^{-d}})$ cumulative regret, where $T$ and $d$ represent the total number of steps and the dimension of the hyperspherical domain, respectively. Regarding the simple regret, we show that any algorithm requires $Ω(ε^{-2}(\ln \frac{1}ε)^d (\ln \ln \frac{1}ε)^{-d})$ time steps to find an $ε$-optimal point. We also provide the improved $O((\ln T)^{d+1}(\ln \ln T)^{-d})$ upper bound on the maximum information gain for the SE kernel. Our results guarantee the optimality of the existing best algorithm up to \emph{dimension-independent} logarithmic factors under a hyperspherical input domain.

