---
layout: default
title: Closing the Gap on the Sample Complexity of 1-Identification
---

# Closing the Gap on the Sample Complexity of 1-Identification
**arXiv**：[2601.15620v1](https://arxiv.org/abs/2601.15620) · [PDF](https://arxiv.org/pdf/2601.15620.pdf)  
**作者**：Zitian Li, Wang Chi Cheung  

**一句话要点**：提出新算法与下界分析以解决多臂老虎机中1-识别问题的样本复杂度差距

**关键词**：多臂老虎机, 纯探索, 样本复杂度, 1-识别, 下界分析, 算法设计

## 3 点简述
- 核心问题：在纯探索多臂老虎机中，以高概率识别是否存在均值不低于阈值的合格臂
- 方法要点：通过优化公式推导新下界，并设计算法实现紧上界，差距为对数多项式因子
- 实验或效果：补充了多合格臂情况下的期望总拉动次数分析，解决了历史文献中的开放问题

## 摘要（原文）

> 1-identification is a fundamental multi-armed bandit formulation on pure exploration. An agent aims to determine whether there exists a qualified arm whose mean reward is not less than a known threshold $μ_0$, or to output \textsf{None} if it believes such an arm does not exist. The agent needs to guarantee its output is correct with probability at least $1-δ$, while making expected total pulling times $\mathbb{E}τ$ as small as possible. We work on 1-identification with two main contributions. (1) We utilize an optimization formulation to derive a new lower bound of $\mathbb{E}τ$, when there is at least one qualified arm. (2) We design a new algorithm, deriving tight upper bounds whose gap to lower bounds are up to a polynomial of logarithm factor across all problem instance. Our result complements the analysis of $\mathbb{E}τ$ when there are multiple qualified arms, which is an open problem left by history literature.

