---
layout: default
title: Optimism Stabilizes Thompson Sampling for Adaptive Inference
---

# Optimism Stabilizes Thompson Sampling for Adaptive Inference
**arXiv**：[2602.06014v1](https://arxiv.org/abs/2602.06014) · [PDF](https://arxiv.org/pdf/2602.06014.pdf)  
**作者**：Shunxing Yan, Han Zhong  

**一句话要点**：提出乐观化方法以稳定汤普森采样，实现多臂赌博机中的渐近有效推断

**关键词**：汤普森采样, 多臂赌博机, 自适应推断, 乐观化方法, 渐近稳定性, 高斯赌博机

## 3 点简述
- 核心问题：汤普森采样在自适应数据收集下，样本量随机且与奖励耦合，导致经典渐近推断失效
- 方法要点：通过方差膨胀或均值奖励的乐观化修改，确保各臂拉动次数稳定集中
- 实验或效果：证明乐观化方法在K臂高斯赌博机中稳定，支持渐近有效推断，仅带来轻微遗憾成本

## 摘要（原文）

> Thompson sampling (TS) is widely used for stochastic multi-armed bandits, yet its inferential properties under adaptive data collection are subtle. Classical asymptotic theory for sample means can fail because arm-specific sample sizes are random and coupled with the rewards through the action-selection rule. We study this phenomenon in the $K$-armed Gaussian bandit and identify \emph{optimism} as a key mechanism for restoring \emph{stability}, a sufficient condition for valid asymptotic inference requiring each arm's pull count to concentrate around a deterministic scale. First, we prove that variance-inflated TS \citep{halder2025stable} is stable for any $K \ge 2$, including the challenging regime where multiple arms are optimal. This resolves the open question raised by \citet{halder2025stable} through extending their results from the two-armed setting to the general $K$-armed setting. Second, we analyze an alternative optimistic modification that keeps the posterior variance unchanged but adds an explicit mean bonus to posterior mean, and establish the same stability conclusion. In summary, suitably implemented optimism stabilizes Thompson sampling and enables asymptotically valid inference in multi-armed bandits, while incurring only a mild additional regret cost.

