---
layout: default
title: SAIL: Test-Time Scaling for In-Context Imitation Learning with VLM
---

# SAIL: Test-Time Scaling for In-Context Imitation Learning with VLM
**arXiv**：[2603.08269v1](https://arxiv.org/abs/2603.08269) · [PDF](https://arxiv.org/pdf/2603.08269.pdf)  
**作者**：Makoto Sato, Yusuke Iwasawa, Yujin Tang, So Kuroki  

**一句话要点**：提出SAIL框架，通过测试时计算扩展解决机器人模仿学习中的环境变化脆弱性问题。

**关键词**：机器人模仿学习, 测试时扩展, 蒙特卡洛树搜索, 视觉语言模型, 轨迹优化

## 3 点简述
- 核心问题：单次轨迹生成在环境变化下脆弱，影响机器人模仿学习效果。
- 方法要点：将模仿学习重构为迭代优化问题，结合蒙特卡洛树搜索、轨迹存档和视觉语言模型评分。
- 实验或效果：在六项任务中，增加测试时计算持续提升成功率，复杂任务达95%。

## 摘要（原文）

> In-context imitation learning allows robots to acquire skills from demonstrations, yet one-shot trajectory generation remains fragile under environmental variation. We propose SAIL, a framework that reframes robot imitation as an iterative refinement problem capable of scaling with test-time compute. SAIL utilizes Monte Carlo Tree Search, where each node is a complete trajectory and edges correspond to trajectory refinements. The process is guided by three core components: an automated archive of successful trajectories for contextually relevant retrieval, a vision language model-based scoring mechanism for trajectory evaluation, and a step-level feedback that provides trajectory-aligned scores for iterative refinement. Experiments across six diverse manipulation tasks in simulation and real-world validation clearly demonstrate that increasing test-time compute consistently improves success rates, achieving up to 95% on complex tasks. Our results suggest that trajectory-level test-time scaling is a robust path toward more generalizable robotic agents.

