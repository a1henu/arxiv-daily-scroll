---
layout: default
title: A First-Order Logic-Based Alternative to Reward Models in RLHF
---

# A First-Order Logic-Based Alternative to Reward Models in RLHF
**arXiv**：[2512.14100v1](https://arxiv.org/abs/2512.14100) · [PDF](https://arxiv.org/pdf/2512.14100.pdf)  
**作者**：Chunjin Jian, Xinhua Zhu  

**一句话要点**：提出基于一阶逻辑相似性的奖励机制S-GRPO，替代传统奖励模型以增强RLHF的稳定性和性能。

**关键词**：强化学习人类反馈, 逻辑一致性奖励, 模型对齐, S-GRPO框架, 偏好学习

## 3 点简述
- 核心问题：RLHF中奖励模型的质量和稳定性影响对齐性能，传统方法如PPO依赖启发式奖励估计。
- 方法要点：利用形式逻辑一致性指导模型对齐，引入S-GRPO框架结合监督组件，联合优化生成、KL散度正则化和标签目标。
- 实验或效果：S-GRPO在性能和鲁棒性上优于标准监督微调，扩展了GRPO和DPO等偏好学习框架。

## 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) plays a crucial role in aligning large language models (LLMs) with human values and preferences. However, the quality and stability of the trained reward model largely determine the final alignment performance. Existing approaches such as Proximal Policy Optimization (PPO) rely heavily on reward models to guide LLMs toward human-aligned behaviors.
>   In this work, we propose a logic-similarity-based reward mechanism as an alternative to conventional reward modeling. Instead of relying on heuristic reward estimation, our method leverages formal logical consistency to steer model alignment with human preferences. Since real-world questions can be interpreted from multiple perspectives, to ensure that logic-based reinforcement learning does not cause model collapse, we introduce S-GRPO, a supervised variant of the GRPO framework. S-GRPO incorporates an additional supervised component and jointly optimizes the generation term, KL-divergence regularization, and label-based objective during training.
>   Experimental results demonstrate that S-GRPO consistently outperforms standard supervised fine-tuning (SFT) in both performance and robustness. Furthermore, it extends existing preference-learning frameworks such as GRPO and DPO, offering a more flexible and task-adaptive approach to alignment training. Our code is available at https://github.com/ChunjinJiang/sgrpo.

