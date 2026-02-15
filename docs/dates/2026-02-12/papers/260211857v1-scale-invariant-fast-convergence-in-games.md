---
layout: default
title: Scale-Invariant Fast Convergence in Games
---

# Scale-Invariant Fast Convergence in Games
**arXiv**：[2602.11857v1](https://arxiv.org/abs/2602.11857) · [PDF](https://arxiv.org/pdf/2602.11857.pdf)  
**作者**：Taira Tsuchiya, Haipeng Luo, Shinji Ito  

**一句话要点**：提出尺度不变快速收敛学习动态，以解决博弈中无需先验效用尺度的快速收敛问题。

**关键词**：博弈论学习, 尺度不变性, 快速收敛, 遗憾界分析, 自适应学习率, 相关均衡

## 3 点简述
- 核心问题：博弈中尺度不变性重要，但现有快速收敛方法需先验效用尺度信息。
- 方法要点：基于乐观跟随正则化领导者，结合自适应学习率和停止时间分析，实现尺度自由和尺度不变。
- 实验或效果：在零和博弈中外部遗憾界为Õ(A_diff)，在一般和博弈中交换遗憾界为O(U_max log T)。

## 摘要（原文）

> Scale-invariance in games has recently emerged as a widely valued desirable property. Yet, almost all fast convergence guarantees in learning in games require prior knowledge of the utility scale. To address this, we develop learning dynamics that achieve fast convergence while being both scale-free, requiring no prior information about utilities, and scale-invariant, remaining unchanged under positive rescaling of utilities. For two-player zero-sum games, we obtain scale-free and scale-invariant dynamics with external regret bounded by $\tilde{O}(A_{\mathrm{diff}})$, where $A_{\mathrm{diff}}$ is the payoff range, which implies an $\tilde{O}(A_{\mathrm{diff}} / T)$ convergence rate to Nash equilibrium after $T$ rounds. For multiplayer general-sum games with $n$ players and $m$ actions, we obtain scale-free and scale-invariant dynamics with swap regret bounded by $O(U_{\mathrm{max}} \log T)$, where $U_{\mathrm{max}}$ is the range of the utilities, ignoring the dependence on the number of players and actions. This yields an $O(U_{\mathrm{max}} \log T / T)$ convergence rate to correlated equilibrium. Our learning dynamics are based on optimistic follow-the-regularized-leader with an adaptive learning rate that incorporates the squared path length of the opponents' gradient vectors, together with a new stopping-time analysis that exploits negative terms in regret bounds without scale-dependent tuning. For general-sum games, scale-free learning is enabled also by a technique called doubling clipping, which clips observed gradients based on past observations.

