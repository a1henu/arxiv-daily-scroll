---
layout: default
title: Heterogeneous Multi-Expert Reinforcement Learning for Long-Horizon Multi-Goal Tasks in Autonomous Forklifts
---

# Heterogeneous Multi-Expert Reinforcement Learning for Long-Horizon Multi-Goal Tasks in Autonomous Forklifts
**arXiv**：[2601.07304v1](https://arxiv.org/abs/2601.07304) · [PDF](https://arxiv.org/pdf/2601.07304.pdf)  
**作者**：Yun Chen, Bowei Huang, Fan Guo, Kang Song  

**一句话要点**：提出异构多专家强化学习框架，以解决自主叉车在长时程多目标任务中的优化干扰问题。

**关键词**：异构多专家强化学习, 长时程多目标任务, 自主叉车, 语义任务规划, 混合模仿-强化训练, 优化干扰

## 3 点简述
- 核心问题：传统端到端学习在自主叉车导航与操作任务中易产生优化干扰，导致性能下降。
- 方法要点：通过语义任务规划器分解任务，分离导航与操作专家，结合混合模仿-强化训练策略。
- 实验或效果：在Gazebo仿真中，任务成功率提升至94.2%，操作时间减少21.4%，放置误差小于1.5厘米。

## 摘要（原文）

> Autonomous mobile manipulation in unstructured warehouses requires a balance between efficient large-scale navigation and high-precision object interaction. Traditional end-to-end learning approaches often struggle to handle the conflicting demands of these distinct phases. Navigation relies on robust decision-making over large spaces, while manipulation needs high sensitivity to fine local details. Forcing a single network to learn these different objectives simultaneously often causes optimization interference, where improving one task degrades the other. To address these limitations, we propose a Heterogeneous Multi-Expert Reinforcement Learning (HMER) framework tailored for autonomous forklifts. HMER decomposes long-horizon tasks into specialized sub-policies controlled by a Semantic Task Planner. This structure separates macro-level navigation from micro-level manipulation, allowing each expert to focus on its specific action space without interference. The planner coordinates the sequential execution of these experts, bridging the gap between task planning and continuous control. Furthermore, to solve the problem of sparse exploration, we introduce a Hybrid Imitation-Reinforcement Training Strategy. This method uses expert demonstrations to initialize the policy and Reinforcement Learning for fine-tuning. Experiments in Gazebo simulations show that HMER significantly outperforms sequential and end-to-end baselines. Our method achieves a task success rate of 94.2\% (compared to 62.5\% for baselines), reduces operation time by 21.4\%, and maintains placement error within 1.5 cm, validating its efficacy for precise material handling.

