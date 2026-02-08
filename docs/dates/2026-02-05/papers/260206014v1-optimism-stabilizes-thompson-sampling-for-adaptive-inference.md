---
layout: default
title: Optimism Stabilizes Thompson Sampling for Adaptive Inference
---

# Optimism Stabilizes Thompson Sampling for Adaptive Inference
**arXiv**：[2602.06014v1](https://arxiv.org/abs/2602.06014) · [PDF](https://arxiv.org/pdf/2602.06014.pdf)  
**作者**：Shunxing Yan, Han Zhong  

**一句话要点**：证明乐观机制稳定汤普森采样以实现多臂老虎机中的渐近有效推断

**关键词**：汤普森采样, 多臂老虎机, 自适应推断, 乐观机制, 渐近稳定性, 高斯老虎机

## 3 点简述
- 核心问题：汤普森采样在自适应数据收集下，臂特定样本量随机且与奖励耦合，导致经典渐近推断失效。
- 方法要点：通过方差膨胀或显式均值奖励的乐观修改，确保每个臂的拉动次数集中在确定性尺度上。
- 实验或效果：在K臂高斯老虎机中，包括多臂最优的挑战性场景，实现稳定性，仅带来轻微额外遗憾成本。

## 摘要（原文）

> Thompson sampling (TS) is widely used for stochastic multi-armed bandits, yet its inferential properties under adaptive data collection are subtle. Classical asymptotic theory for sample means can fail because arm-specific sample sizes are random and coupled with the rewards through the action-selection rule. We study this phenomenon in the $K$-armed Gaussian bandit and identify \emph{optimism} as a key mechanism for restoring \emph{stability}, a sufficient condition for valid asymptotic inference requiring each arm's pull count to concentrate around a deterministic scale. First, we prove that variance-inflated TS \citep{halder2025stable} is stable for any $K \ge 2$, including the challenging regime where multiple arms are optimal. This resolves the open question raised by \citet{halder2025stable} through extending their results from the two-armed setting to the general $K$-armed setting. Second, we analyze an alternative optimistic modification that keeps the posterior variance unchanged but adds an explicit mean bonus to posterior mean, and establish the same stability conclusion. In summary, suitably implemented optimism stabilizes Thompson sampling and enables asymptotically valid inference in multi-armed bandits, while incurring only a mild additional regret cost.

