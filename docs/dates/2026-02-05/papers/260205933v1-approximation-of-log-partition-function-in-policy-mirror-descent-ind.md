---
layout: default
title: Approximation of Log-Partition Function in Policy Mirror Descent Induces Implicit Regularization for LLM Post-Training
---

# Approximation of Log-Partition Function in Policy Mirror Descent Induces Implicit Regularization for LLM Post-Training
**arXiv**：[2602.05933v1](https://arxiv.org/abs/2602.05933) · [PDF](https://arxiv.org/pdf/2602.05933.pdf)  
**作者**：Zhenghao Xu, Qin Lu, Changlong Yu, Tuo Zhao  

**一句话要点**：提出PMD-mean算法，通过近似对数配分函数解决大语言模型后训练中策略镜像下降的有限样本挑战。

**关键词**：策略镜像下降, 大语言模型后训练, 对数配分函数近似, 自适应正则化, 强化学习算法

## 3 点简述
- 核心问题：策略镜像下降在LLM后训练中需估计对数配分函数，但动作空间大且样本有限导致困难。
- 方法要点：PMD-mean用采样策略的平均奖励近似对数配分项，在策略对数空间进行回归，引入自适应混合KL-χ²正则化。
- 实验或效果：在数学推理任务上，PMD-mean提升性能、稳定性和时间效率，增强对有限样本误差的鲁棒性。

## 摘要（原文）

> Policy mirror descent (PMD) provides a principled framework for reinforcement learning (RL) by iteratively solving KL-regularized policy improvement subproblems. While this approach has been adopted in training advanced LLMs such as Kimi K1.5/K2, the ideal closed-form PMD updates require reliable partition function estimation, a significant challenge when working with limited rollouts in the vast action spaces of LLMs. We investigate a practical algorithm, termed PMD-mean, that approximates the log-partition term with the mean reward under the sampling policy and performs regression in log-policy space. Specifically, we characterize the population solution of PMD-mean and demonstrate that it implicitly optimizes mirror descent subproblems with an adaptive mixed KL--$χ^2$ regularizer. This additional $χ^2$ regularization constrains large probability changes, producing more conservative updates when expected rewards are low and enhancing robustness against finite-sample estimation errors. Experiments on math reasoning tasks show that PMD-mean achieves superior performance with improved stability and time efficiency. These findings deepen our understanding of PMD-mean and illuminate pathways toward principled improvements in RL algorithms for LLMs. Code is available at https://github.com/horizon-rl/OpenKimi.

