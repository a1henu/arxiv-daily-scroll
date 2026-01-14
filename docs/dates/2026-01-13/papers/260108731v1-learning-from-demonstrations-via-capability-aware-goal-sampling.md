---
layout: default
title: Learning from Demonstrations via Capability-Aware Goal Sampling
---

# Learning from Demonstrations via Capability-Aware Goal Sampling
**arXiv**：[2601.08731v1](https://arxiv.org/abs/2601.08731) · [PDF](https://arxiv.org/pdf/2601.08731.pdf)  
**作者**：Yuanlin Duan, Yuning Wang, Wenjie Qiu, He Zhu  

**一句话要点**：提出能力感知目标采样方法以解决模仿学习在长视野环境中的脆弱性问题

**关键词**：模仿学习, 目标采样, 自适应课程, 长视野任务, 稀疏奖励

## 3 点简述
- 核心问题：模仿学习在长视野环境中因小误差累积而失败，依赖专家轨迹脆弱。
- 方法要点：动态跟踪代理能力，采样略超当前能力的目标，形成自适应课程引导学习。
- 实验或效果：在稀疏奖励目标条件任务中显著提升样本效率和最终性能，优于现有基线。

## 摘要（原文）

> Despite its promise, imitation learning often fails in long-horizon environments where perfect replication of demonstrations is unrealistic and small errors can accumulate catastrophically. We introduce Cago (Capability-Aware Goal Sampling), a novel learning-from-demonstrations method that mitigates the brittle dependence on expert trajectories for direct imitation. Unlike prior methods that rely on demonstrations only for policy initialization or reward shaping, Cago dynamically tracks the agent's competence along expert trajectories and uses this signal to select intermediate steps--goals that are just beyond the agent's current reach--to guide learning. This results in an adaptive curriculum that enables steady progress toward solving the full task. Empirical results demonstrate that Cago significantly improves sample efficiency and final performance across a range of sparse-reward, goal-conditioned tasks, consistently outperforming existing learning from-demonstrations baselines.

