---
layout: default
title: On Regret Bounds of Thompson Sampling for Bayesian Optimization
---

# On Regret Bounds of Thompson Sampling for Bayesian Optimization
**arXiv**：[2603.09276v1](https://arxiv.org/abs/2603.09276) · [PDF](https://arxiv.org/pdf/2603.09276.pdf)  
**作者**：Shion Takeno, Shogo Iwazaki  

**一句话要点**：分析高斯过程汤普森采样的遗憾界，填补贝叶斯优化理论空白

**关键词**：贝叶斯优化, 汤普森采样, 高斯过程, 遗憾界分析, 理论分析

## 3 点简述
- 研究高斯过程汤普森采样在贝叶斯优化中的遗憾界，对比GP-UCB方法
- 证明多项遗憾界，包括下界、二阶矩上界、期望宽松遗憾界和改进累积遗憾界
- 提供有用引理，放宽改进遗憾界上界的必要条件

## 摘要（原文）

> We study a widely used Bayesian optimization method, Gaussian process Thompson sampling (GP-TS), under the assumption that the objective function is a sample path from a GP. Compared with the GP upper confidence bound (GP-UCB) with established high-probability and expected regret bounds, most analyses of GP-TS have been limited to expected regret. Moreover, whether the recent analyses of GP-UCB for the lenient regret and the improved cumulative regret upper bound can be applied to GP-TS remains unclear. To fill these gaps, this paper shows several regret bounds: (i) a regret lower bound for GP-TS, which implies that GP-TS suffers from a polynomial dependence on $1/δ$ with probability $δ$, (ii) an upper bound of the second moment of cumulative regret, which directly suggests an improved regret upper bound on $δ$, (iii) expected lenient regret upper bounds, and (iv) an improved cumulative regret upper bound on the time horizon $T$. Along the way, we provide several useful lemmas, including a relaxation of the necessary condition from recent analysis to obtain improved regret upper bounds on $T$.

