---
layout: default
title: Strategically Robust Multi-Agent Reinforcement Learning with Linear Function Approximation
---

# Strategically Robust Multi-Agent Reinforcement Learning with Linear Function Approximation
**arXiv**：[2603.09208v1](https://arxiv.org/abs/2603.09208) · [PDF](https://arxiv.org/pdf/2603.09208.pdf)  
**作者**：Jake Gonzales, Max Horwitz, Eric Mazumdar, Lillian J. Ratliff  

**一句话要点**：提出RQRE-OVI算法，用于大规模状态空间中的鲁棒多智能体强化学习均衡计算。

**关键词**：多智能体强化学习, 均衡计算, 风险敏感量化响应均衡, 线性函数近似, 鲁棒性分析, 样本复杂度

## 3 点简述
- 核心问题：一般和马尔可夫博弈中均衡计算效率低且对近似误差敏感，纳什均衡存在多重性和脆弱性。
- 方法要点：引入风险敏感量化响应均衡（RQRE），提供唯一平滑解，并设计乐观值迭代算法RQRE-OVI，支持线性函数近似。
- 实验或效果：理论分析显示样本复杂度与理性及风险参数相关，实证表明RQRE-OVI在自玩和跨玩中比纳什方法更鲁棒且性能竞争。

## 摘要（原文）

> Provably efficient and robust equilibrium computation in general-sum Markov games remains a core challenge in multi-agent reinforcement learning. Nash equilibrium is computationally intractable in general and brittle due to equilibrium multiplicity and sensitivity to approximation error. We study Risk-Sensitive Quantal Response Equilibrium (RQRE), which yields a unique, smooth solution under bounded rationality and risk sensitivity. We propose \texttt{RQRE-OVI}, an optimistic value iteration algorithm for computing RQRE with linear function approximation in large or continuous state spaces. Through finite-sample regret analysis, we establish convergence and explicitly characterize how sample complexity scales with rationality and risk-sensitivity parameters. The regret bounds reveal a quantitative tradeoff: increasing rationality tightens regret, while risk sensitivity induces regularization that enhances stability and robustness. This exposes a Pareto frontier between expected performance and robustness, with Nash recovered in the limit of perfect rationality and risk neutrality. We further show that the RQRE policy map is Lipschitz continuous in estimated payoffs, unlike Nash, and RQRE admits a distributionally robust optimization interpretation. Empirically, we demonstrate that \texttt{RQRE-OVI} achieves competitive performance under self-play while producing substantially more robust behavior under cross-play compared to Nash-based approaches. These results suggest \texttt{RQRE-OVI} offers a principled, scalable, and tunable path for equilibrium learning with improved robustness and generalization.

