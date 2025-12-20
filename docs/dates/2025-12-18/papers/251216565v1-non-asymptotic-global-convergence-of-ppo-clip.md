---
layout: default
title: Non-Asymptotic Global Convergence of PPO-Clip
---

# Non-Asymptotic Global Convergence of PPO-Clip
**arXiv**：[2512.16565v1](https://arxiv.org/abs/2512.16565) · [PDF](https://arxiv.org/pdf/2512.16565.pdf)  
**作者**：Yin Liu, Qiming Dai, Junyu Zhang, Zaiwen Wen  

**一句话要点**：提出确定性演员PPO算法，在软最大策略参数化下建立非渐进全局收敛理论

**关键词**：强化学习理论, PPO算法, 非渐进收敛, f-散度正则化, 软最大策略

## 3 点简述
- 核心问题：PPO-Clip算法缺乏严格理论分析，尤其在f-散度正则化下的收敛性未知
- 方法要点：分析确定性演员PPO算法，推导非均匀Lipschitz光滑条件和Łojasiewicz不等式
- 实验或效果：针对前向KL正则化建立非渐进线性收敛率，对反向KL正则化证明平稳收敛和局部线性收敛

## 摘要（原文）

> Reinforcement learning (RL) has gained attention for aligning large language models (LLMs) via reinforcement learning from human feedback (RLHF). The actor-only variants of Proximal Policy Optimization (PPO) are widely applied for their efficiency. These algorithms incorporate a clipping mechanism to improve stability. Besides, a regularization term, such as the reverse KL-divergence or a more general \(f\)-divergence, is introduced to prevent policy drift. Despite their empirical success, a rigorous theoretical understanding of the problem and the algorithm's properties is limited. This paper advances the theoretical foundations of the PPO-Clip algorithm by analyzing a deterministic actor-only PPO algorithm within the general RL setting with \(f\)-divergence regularization under the softmax policy parameterization. We derive a non-uniform Lipschitz smoothness condition and a Łojasiewicz inequality for the considered problem. Based on these, a non-asymptotic linear convergence rate to the globally optimal policy is established for the forward KL-regularizer. Furthermore, stationary convergence and local linear convergence are derived for the reverse KL-regularizer.

