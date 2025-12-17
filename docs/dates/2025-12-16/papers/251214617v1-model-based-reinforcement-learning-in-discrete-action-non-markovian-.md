---
layout: default
title: Model-Based Reinforcement Learning in Discrete-Action Non-Markovian Reward Decision Processes
---

# Model-Based Reinforcement Learning in Discrete-Action Non-Markovian Reward Decision Processes
**arXiv**：[2512.14617v1](https://arxiv.org/abs/2512.14617) · [PDF](https://arxiv.org/pdf/2512.14617.pdf)  
**作者**：Alessandro Trapasso, Luca Iocchi, Fabio Patrizi  

**一句话要点**：提出QR-MAX算法以解决离散动作非马尔可夫奖励决策过程中的样本效率和最优性保证问题

**关键词**：非马尔可夫奖励决策过程, 模型强化学习, 奖励机, 样本效率, PAC收敛, 连续状态空间

## 3 点简述
- 核心问题：非马尔可夫奖励决策过程缺乏样本效率和最优性保证，传统马尔可夫强化学习不适用
- 方法要点：QR-MAX通过奖励机分解马尔可夫转移学习与非马尔可夫奖励处理，实现多项式样本复杂度的PAC收敛
- 实验或效果：在复杂环境中相比现有方法显著提升样本效率和鲁棒性，并扩展至连续状态空间

## 摘要（原文）

> Many practical decision-making problems involve tasks whose success depends on the entire system history, rather than on achieving a state with desired properties. Markovian Reinforcement Learning (RL) approaches are not suitable for such tasks, while RL with non-Markovian reward decision processes (NMRDPs) enables agents to tackle temporal-dependency tasks. This approach has long been known to lack formal guarantees on both (near-)optimality and sample efficiency. We contribute to solving both issues with QR-MAX, a novel model-based algorithm for discrete NMRDPs that factorizes Markovian transition learning from non-Markovian reward handling via reward machines. To the best of our knowledge, this is the first model-based RL algorithm for discrete-action NMRDPs that exploits this factorization to obtain PAC convergence to $\varepsilon$-optimal policies with polynomial sample complexity. We then extend QR-MAX to continuous state spaces with Bucket-QR-MAX, a SimHash-based discretiser that preserves the same factorized structure and achieves fast and stable learning without manual gridding or function approximation. We experimentally compare our method with modern state-of-the-art model-based RL approaches on environments of increasing complexity, showing a significant improvement in sample efficiency and increased robustness in finding optimal policies.

