---
layout: default
title: Diffusion Policies with Value-Conditional Optimization for Offline Reinforcement Learning
---

# Diffusion Policies with Value-Conditional Optimization for Offline Reinforcement Learning
**arXiv**：[2511.08922v1](https://arxiv.org/abs/2511.08922) · [PDF](https://arxiv.org/pdf/2511.08922.pdf)  
**作者**：Yunchang Ma, Tenglong Liu, Yixing Lan, Xin Yin, Changxin Zhang, Xinglong Zhang, Xin Xu  

**一句话要点**：提出DIVO以解决离线强化学习中价值高估和保守性失衡问题

**关键词**：离线强化学习, 扩散模型, 价值优化, 策略改进, D4RL基准

## 3 点简述
- 核心问题：离线强化学习中，分布外动作导致价值高估，限制策略性能。
- 方法要点：引入基于优势值的二元加权机制，指导扩散模型训练。
- 实验或效果：在D4RL基准测试中，DIVO在运动任务和AntMaze领域表现优异。

## 摘要（原文）

> In offline reinforcement learning, value overestimation caused by out-of-distribution (OOD) actions significantly limits policy performance. Recently, diffusion models have been leveraged for their strong distribution-matching capabilities, enforcing conservatism through behavior policy constraints. However, existing methods often apply indiscriminate regularization to redundant actions in low-quality datasets, resulting in excessive conservatism and an imbalance between the expressiveness and efficiency of diffusion modeling. To address these issues, we propose DIffusion policies with Value-conditional Optimization (DIVO), a novel approach that leverages diffusion models to generate high-quality, broadly covered in-distribution state-action samples while facilitating efficient policy improvement. Specifically, DIVO introduces a binary-weighted mechanism that utilizes the advantage values of actions in the offline dataset to guide diffusion model training. This enables a more precise alignment with the dataset's distribution while selectively expanding the boundaries of high-advantage actions. During policy improvement, DIVO dynamically filters high-return-potential actions from the diffusion model, effectively guiding the learned policy toward better performance. This approach achieves a critical balance between conservatism and explorability in offline RL. We evaluate DIVO on the D4RL benchmark and compare it against state-of-the-art baselines. Empirical results demonstrate that DIVO achieves superior performance, delivering significant improvements in average returns across locomotion tasks and outperforming existing methods in the challenging AntMaze domain, where sparse rewards pose a major difficulty.

