---
layout: default
title: Compositional Planning with Jumpy World Models
---

# Compositional Planning with Jumpy World Models
**arXiv**：[2602.19634v1](https://arxiv.org/abs/2602.19634) · [PDF](https://arxiv.org/pdf/2602.19634.pdf)  
**作者**：Jesse Farebrother, Matteo Pirotta, Andrea Tirinzoni, Marc G. Bellemare, Alessandro Lazaric, Ahmed Touati  

**一句话要点**：提出跳步世界模型以解决组合规划中的长时程预测误差问题

**关键词**：组合规划, 跳步世界模型, 长时程预测, 策略序列, 零样本学习, 强化学习

## 3 点简述
- 核心问题：组合规划中长时程预测误差累积，难以估计策略序列的访问分布
- 方法要点：学习多步动态预测模型，结合跨时间尺度一致性目标提升预测精度
- 实验或效果：在操控和导航任务中，零样本性能显著提升，长时程任务相对改进200%

## 摘要（原文）

> The ability to plan with temporal abstractions is central to intelligent decision-making. Rather than reasoning over primitive actions, we study agents that compose pre-trained policies as temporally extended actions, enabling solutions to complex tasks that no constituent alone can solve. Such compositional planning remains elusive as compounding errors in long-horizon predictions make it challenging to estimate the visitation distribution induced by sequencing policies. Motivated by the geometric policy composition framework introduced in arXiv:2206.08736, we address these challenges by learning predictive models of multi-step dynamics -- so-called jumpy world models -- that capture state occupancies induced by pre-trained policies across multiple timescales in an off-policy manner. Building on Temporal Difference Flows (arXiv:2503.09817), we enhance these models with a novel consistency objective that aligns predictions across timescales, improving long-horizon predictive accuracy. We further demonstrate how to combine these generative predictions to estimate the value of executing arbitrary sequences of policies over varying timescales. Empirically, we find that compositional planning with jumpy world models significantly improves zero-shot performance across a wide range of base policies on challenging manipulation and navigation tasks, yielding, on average, a 200% relative improvement over planning with primitive actions on long-horizon tasks.

