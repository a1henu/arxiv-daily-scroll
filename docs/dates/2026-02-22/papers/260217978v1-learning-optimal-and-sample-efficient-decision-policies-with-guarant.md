---
layout: default
title: Learning Optimal and Sample-Efficient Decision Policies with Guarantees
---

# Learning Optimal and Sample-Efficient Decision Policies with Guarantees
**arXiv**：[2602.17978v1](https://arxiv.org/abs/2602.17978) · [PDF](https://arxiv.org/pdf/2602.17978.pdf)  
**作者**：Daqian Shao  

**一句话要点**：提出基于工具变量和条件矩限制的算法，以解决离线决策学习中隐藏混淆变量导致的样本效率与最优性保证问题。

**关键词**：离线强化学习, 因果推断, 工具变量, 条件矩限制, 模仿学习, 线性时序逻辑

## 3 点简述
- 核心问题：离线决策学习中隐藏混淆变量导致虚假相关性和次优策略，传统强化学习依赖在线交互成本高。
- 方法要点：利用工具变量识别因果效应，基于双机器学习推导样本高效算法，并扩展至模仿学习和线性时序逻辑目标学习。
- 实验或效果：在强化学习基准和合成数据集上验证算法优于现有方法，提供收敛和最优性保证。

## 摘要（原文）

> The paradigm of decision-making has been revolutionised by reinforcement learning and deep learning. Although this has led to significant progress in domains such as robotics, healthcare, and finance, the use of RL in practice is challenging, particularly when learning decision policies in high-stakes applications that may require guarantees. Traditional RL algorithms rely on a large number of online interactions with the environment, which is problematic in scenarios where online interactions are costly, dangerous, or infeasible. However, learning from offline datasets is hindered by the presence of hidden confounders. Such confounders can cause spurious correlations in the dataset and can mislead the agent into taking suboptimal or adversarial actions. Firstly, we address the problem of learning from offline datasets in the presence of hidden confounders. We work with instrumental variables (IVs) to identify the causal effect, which is an instance of a conditional moment restrictions (CMR) problem. Inspired by double/debiased machine learning, we derive a sample-efficient algorithm for solving CMR problems with convergence and optimality guarantees, which outperforms state-of-the-art algorithms. Secondly, we relax the conditions on the hidden confounders in the setting of (offline) imitation learning, and adapt our CMR estimator to derive an algorithm that can learn effective imitator policies with convergence rate guarantees. Finally, we consider the problem of learning high-level objectives expressed in linear temporal logic (LTL) and develop a provably optimal learning algorithm that improves sample efficiency over existing methods. Through evaluation on reinforcement learning benchmarks and synthetic and semi-synthetic datasets, we demonstrate the usefulness of the methods developed in this thesis in real-world decision making.

