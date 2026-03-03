---
layout: default
title: ACDC: Adaptive Curriculum Planning with Dynamic Contrastive Control for Goal-Conditioned Reinforcement Learning in Robotic Manipulation
---

# ACDC: Adaptive Curriculum Planning with Dynamic Contrastive Control for Goal-Conditioned Reinforcement Learning in Robotic Manipulation
**arXiv**：[2603.02104v1](https://arxiv.org/abs/2603.02104) · [PDF](https://arxiv.org/pdf/2603.02104.pdf)  
**作者**：Xuerui Wang, Guangyu Ren, Tianhong Dai, Bintao Hu, Shuangyao Huang, Wenzhang Zhang, Hengyan Liu  

**一句话要点**：提出ACDC方法，通过自适应课程规划与动态对比控制提升机器人操作中目标条件强化学习的性能。

**关键词**：目标条件强化学习, 机器人操作, 自适应课程规划, 对比学习, 样本效率

## 3 点简述
- 核心问题：现有目标条件强化学习依赖经验优先级，导致跨任务性能不佳。
- 方法要点：结合自适应课程规划动态平衡探索与利用，并通过动态对比控制实现课程执行。
- 实验或效果：在机器人操作任务中，ACDC在样本效率和任务成功率上优于现有方法。

## 摘要（原文）

> Goal-conditioned reinforcement learning has shown considerable potential in robotic manipulation; however, existing approaches remain limited by their reliance on prioritizing collected experience, resulting in suboptimal performance across diverse tasks. Inspired by human learning behaviors, we propose a more comprehensive learning paradigm, ACDC, which integrates multidimensional Adaptive Curriculum (AC) Planning with Dynamic Contrastive (DC) Control to guide the agent along a well-designed learning trajectory. More specifically, at the planning level, the AC component schedules the learning curriculum by dynamically balancing diversity-driven exploration and quality-driven exploitation based on the agent's success rate and training progress. At the control level, the DC component implements the curriculum plan through norm-constrained contrastive learning, enabling magnitude-guided experience selection aligned with the current curriculum focus. Extensive experiments on challenging robotic manipulation tasks demonstrate that ACDC consistently outperforms the state-of-the-art baselines in both sample efficiency and final task success rate.

