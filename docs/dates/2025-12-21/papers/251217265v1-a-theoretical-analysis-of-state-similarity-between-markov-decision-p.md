---
layout: default
title: A Theoretical Analysis of State Similarity Between Markov Decision Processes
---

# A Theoretical Analysis of State Similarity Between Markov Decision Processes
**arXiv**：[2512.17265v1](https://arxiv.org/abs/2512.17265) · [PDF](https://arxiv.org/pdf/2512.17265.pdf)  
**作者**：Zhenyu Tao, Wei Xu, Xiaohu You  

**一句话要点**：提出广义双模拟度量以分析多马尔可夫决策过程间的状态相似性

**关键词**：广义双模拟度量, 马尔可夫决策过程, 状态相似性, 策略转移, 状态聚合, 样本复杂度

## 3 点简述
- 核心问题：双模拟度量难以直接应用于多MDP间的状态相似性分析，缺乏数学性质支撑
- 方法要点：建立广义双模拟度量，严格证明其对称性、跨MDP三角不等式和距离界等性质
- 实验或效果：理论分析改进策略转移和状态聚合的界限，数值结果验证GBSM在多MDP场景的有效性

## 摘要（原文）

> The bisimulation metric (BSM) is a powerful tool for analyzing state similarities within a Markov decision process (MDP), revealing that states closer in BSM have more similar optimal value functions. While BSM has been successfully utilized in reinforcement learning (RL) for tasks like state representation learning and policy exploration, its application to state similarity between multiple MDPs remains challenging. Prior work has attempted to extend BSM to pairs of MDPs, but a lack of well-established mathematical properties has limited further theoretical analysis between MDPs. In this work, we formally establish a generalized bisimulation metric (GBSM) for measuring state similarity between arbitrary pairs of MDPs, which is rigorously proven with three fundamental metric properties, i.e., GBSM symmetry, inter-MDP triangle inequality, and a distance bound on identical spaces. Leveraging these properties, we theoretically analyze policy transfer, state aggregation, and sampling-based estimation across MDPs, obtaining explicit bounds that are strictly tighter than existing ones derived from the standard BSM. Additionally, GBSM provides a closed-form sample complexity for estimation, improving upon existing asymptotic results based on BSM. Numerical results validate our theoretical findings and demonstrate the effectiveness of GBSM in multi-MDP scenarios.

