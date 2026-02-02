---
layout: default
title: Continual Policy Distillation from Distributed Reinforcement Learning Teachers
---

# Continual Policy Distillation from Distributed Reinforcement Learning Teachers
**arXiv**：[2601.22475v1](https://arxiv.org/abs/2601.22475) · [PDF](https://arxiv.org/pdf/2601.22475.pdf)  
**作者**：Yuxuan Li, Qijun He, Mingqi Yuan, Wen-Tse Chen, Jeff Schneider, Jiayu Chen  

**一句话要点**：提出分布式强化学习教师与持续策略蒸馏框架以解决持续强化学习中的可扩展性问题

**关键词**：持续强化学习, 策略蒸馏, 分布式强化学习, 教师-学生框架, 混合专家架构, 任务遗忘控制

## 3 点简述
- 核心问题：持续强化学习面临稳定性-可塑性困境，直接应用强化学习于序列任务流难以实现可扩展性能
- 方法要点：将CRL解耦为分布式RL训练单任务教师模型和持续蒸馏到中央通用模型，结合MoE架构和回放方法增强稳定性与可塑性
- 实验或效果：在Meta-World基准测试中，恢复超过85%教师性能，任务遗忘率控制在10%以内

## 摘要（原文）

> Continual Reinforcement Learning (CRL) aims to develop lifelong learning agents to continuously acquire knowledge across diverse tasks while mitigating catastrophic forgetting. This requires efficiently managing the stability-plasticity dilemma and leveraging prior experience to rapidly generalize to novel tasks. While various enhancement strategies for both aspects have been proposed, achieving scalable performance by directly applying RL to sequential task streams remains challenging. In this paper, we propose a novel teacher-student framework that decouples CRL into two independent processes: training single-task teacher models through distributed RL and continually distilling them into a central generalist model. This design is motivated by the observation that RL excels at solving single tasks, while policy distillation -- a relatively stable supervised learning process -- is well aligned with large foundation models and multi-task learning. Moreover, a mixture-of-experts (MoE) architecture and a replay-based approach are employed to enhance the plasticity and stability of the continual policy distillation process. Extensive experiments on the Meta-World benchmark demonstrate that our framework enables efficient continual RL, recovering over 85% of teacher performance while constraining task-wise forgetting to within 10%.

