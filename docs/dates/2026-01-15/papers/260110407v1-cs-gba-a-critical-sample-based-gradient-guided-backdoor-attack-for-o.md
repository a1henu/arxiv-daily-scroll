---
layout: default
title: CS-GBA: A Critical Sample-based Gradient-guided Backdoor Attack for Offline Reinforcement Learning
---

# CS-GBA: A Critical Sample-based Gradient-guided Backdoor Attack for Offline Reinforcement Learning
**arXiv**：[2601.10407v1](https://arxiv.org/abs/2601.10407) · [PDF](https://arxiv.org/pdf/2601.10407.pdf)  
**作者**：Yuanjie Zhao, Junnan Qiu, Yue Ding, Jie Li  

**一句话要点**：提出CS-GBA，一种基于关键样本和梯度引导的后门攻击方法，针对离线强化学习的安全约束算法。

**关键词**：离线强化学习, 后门攻击, 安全约束算法, 关键样本选择, 梯度引导优化, D4RL基准

## 3 点简述
- 核心问题：离线强化学习易受后门攻击，现有方法对安全约束算法（如CQL）效果差，因随机投毒效率低且触发器易被检测。
- 方法要点：采用关键样本选择策略，基于TD误差集中攻击预算；设计相关性破坏触发器，利用状态特征互斥性保持隐蔽；使用梯度引导动作生成机制，在数据流形内搜索最差动作。
- 实验或效果：在D4RL基准测试中，以5%投毒预算显著超越基线，对安全约束算法实现高攻击成功率，同时保持干净环境性能。

## 摘要（原文）

> Offline Reinforcement Learning (RL) enables policy optimization from static datasets but is inherently vulnerable to backdoor attacks. Existing attack strategies typically struggle against safety-constrained algorithms (e.g., CQL) due to inefficient random poisoning and the use of easily detectable Out-of-Distribution (OOD) triggers. In this paper, we propose CS-GBA (Critical Sample-based Gradient-guided Backdoor Attack), a novel framework designed to achieve high stealthiness and destructiveness under a strict budget. Leveraging the theoretical insight that samples with high Temporal Difference (TD) errors are pivotal for value function convergence, we introduce an adaptive Critical Sample Selection strategy that concentrates the attack budget on the most influential transitions. To evade OOD detection, we propose a Correlation-Breaking Trigger mechanism that exploits the physical mutual exclusivity of state features (e.g., 95th percentile boundaries) to remain statistically concealed. Furthermore, we replace the conventional label inversion with a Gradient-Guided Action Generation mechanism, which searches for worst-case actions within the data manifold using the victim Q-network's gradient. Empirical results on D4RL benchmarks demonstrate that our method significantly outperforms state-of-the-art baselines, achieving high attack success rates against representative safety-constrained algorithms with a minimal 5% poisoning budget, while maintaining the agent's performance in clean environments.

