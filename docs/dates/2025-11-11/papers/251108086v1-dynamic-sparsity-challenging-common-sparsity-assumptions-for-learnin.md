---
layout: default
title: Dynamic Sparsity: Challenging Common Sparsity Assumptions for Learning World Models in Robotic Reinforcement Learning Benchmarks
---

# Dynamic Sparsity: Challenging Common Sparsity Assumptions for Learning World Models in Robotic Reinforcement Learning Benchmarks
**arXiv**：[2511.08086v1](https://arxiv.org/abs/2511.08086) · [PDF](https://arxiv.org/pdf/2511.08086.pdf)  
**作者**：Muthukumar Pandaram, Jakob Hollenstein, David Drexel, Samuele Tosatto, Antonio Rodríguez-Sánchez, Justus Piater  

**一句话要点**：分析机器人强化学习基准中动态稀疏性假设，揭示状态依赖稀疏性结构

**关键词**：强化学习, 世界模型, 稀疏性分析, 机器人基准, 动态建模

## 3 点简述
- 核心问题：检验世界模型中状态和时序稀疏性假设在真实机器人任务中的有效性
- 方法要点：分析MuJoCo Playground基准的真实动态，评估因果图稀疏性和状态依赖性
- 实验或效果：发现全局稀疏性罕见，但存在局部状态依赖稀疏性，挑战常见先验假设

## 摘要（原文）

> The use of learned dynamics models, also known as world models, can improve the sample efficiency of reinforcement learning. Recent work suggests that the underlying causal graphs of such dynamics models are sparsely connected, with each of the future state variables depending only on a small subset of the current state variables, and that learning may therefore benefit from sparsity priors. Similarly, temporal sparsity, i.e. sparsely and abruptly changing local dynamics, has also been proposed as a useful inductive bias.
>   In this work, we critically examine these assumptions by analyzing ground-truth dynamics from a set of robotic reinforcement learning environments in the MuJoCo Playground benchmark suite, aiming to determine whether the proposed notions of state and temporal sparsity actually tend to hold in typical reinforcement learning tasks.
>   We study (i) whether the causal graphs of environment dynamics are sparse, (ii) whether such sparsity is state-dependent, and (iii) whether local system dynamics change sparsely.
>   Our results indicate that global sparsity is rare, but instead the tasks show local, state-dependent sparsity in their dynamics and this sparsity exhibits distinct structures, appearing in temporally localized clusters (e.g., during contact events) and affecting specific subsets of state dimensions. These findings challenge common sparsity prior assumptions in dynamics learning, emphasizing the need for grounded inductive biases that reflect the state-dependent sparsity structure of real-world dynamics.

