---
layout: default
title: On the Complexity of Offline Reinforcement Learning with $Q^\star$-Approximation and Partial Coverage
---

# On the Complexity of Offline Reinforcement Learning with $Q^\star$-Approximation and Partial Coverage
**arXiv**：[2602.12107v1](https://arxiv.org/abs/2602.12107) · [PDF](https://arxiv.org/pdf/2602.12107.pdf)  
**作者**：Haolin Liu, Braham Snyder, Chen-Yu Wei  

**一句话要点**：提出基于决策估计分解的框架，刻画离线强化学习在Q*近似与部分覆盖下的内在复杂度

**关键词**：离线强化学习, Q*近似, 部分覆盖, 样本复杂度, 决策估计系数, 贝尔曼完备性

## 3 点简述
- 研究Q*可实现性与贝尔曼完备性是否足以实现部分覆盖下的样本高效离线RL，给出否定答案并建立信息论下界
- 引入基于决策估计系数的通用框架，模块化Q*估计过程，统一并改进现有理论保证
- 通过二阶性能差异引理，将软Q学习的样本复杂度从ε^{-4}提升至ε^{-2}，并扩展至低贝尔曼秩MDP等新场景

## 摘要（原文）

> We study offline reinforcement learning under $Q^\star$-approximation and partial coverage, a setting that motivates practical algorithms such as Conservative $Q$-Learning (CQL; Kumar et al., 2020) but has received limited theoretical attention. Our work is inspired by the following open question: "Are $Q^\star$-realizability and Bellman completeness sufficient for sample-efficient offline RL under partial coverage?"
>   We answer in the negative by establishing an information-theoretic lower bound. Going substantially beyond this, we introduce a general framework that characterizes the intrinsic complexity of a given $Q^\star$ function class, inspired by model-free decision-estimation coefficients (DEC) for online RL (Foster et al., 2023b; Liu et al., 2025b). This complexity recovers and improves the quantities underlying the guarantees of Chen and Jiang (2022) and Uehara et al. (2023), and extends to broader settings. Our decision-estimation decomposition can be combined with a wide range of $Q^\star$ estimation procedures, modularizing and generalizing existing approaches.
>   Beyond the general framework, we make further contributions: By developing a novel second-order performance difference lemma, we obtain the first $ε^{-2}$ sample complexity under partial coverage for soft $Q$-learning, improving the $ε^{-4}$ bound of Uehara et al. (2023). We remove Chen and Jiang's (2022) need for additional online interaction when the value gap of $Q^\star$ is unknown. We also give the first characterization of offline learnability for general low-Bellman-rank MDPs without Bellman completeness (Jiang et al., 2017; Du et al., 2021; Jin et al., 2021), a canonical setting in online RL that remains unexplored in offline RL except for special cases. Finally, we provide the first analysis for CQL under $Q^\star$-realizability and Bellman completeness beyond the tabular case.

