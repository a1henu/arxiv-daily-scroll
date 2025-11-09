---
layout: default
title: X-Diffusion: Training Diffusion Policies on Cross-Embodiment Human Demonstrations
---

# X-Diffusion: Training Diffusion Policies on Cross-Embodiment Human Demonstrations
**arXiv**：[2511.04671v1](https://arxiv.org/abs/2511.04671) · [PDF](https://arxiv.org/pdf/2511.04671.pdf)  
**作者**：Maximus A. Pace, Prithwish Dan, Chuanruo Ning, Atiksh Bhardwaj, Audrey Du, Edward W. Duan, Wei-Chiu Ma, Kushal Kedia  

**一句话要点**：提出X-Diffusion框架，利用跨具身人类演示训练扩散策略以解决动作执行不匹配问题。

**关键词**：扩散策略, 跨具身学习, 人类演示, 动作重定向, 机器人操作

## 3 点简述
- 核心问题：人类与机器人具身差异导致直接动作重定向产生物理不可行动作。
- 方法要点：通过噪声添加模糊低层执行差异，保留高层任务指导，训练分类器控制噪声水平。
- 实验效果：在五个操作任务中，平均成功率比最佳基线提高16%。

## 摘要（原文）

> Human videos can be recorded quickly and at scale, making them an appealing
> source of training data for robot learning. However, humans and robots differ
> fundamentally in embodiment, resulting in mismatched action execution. Direct
> kinematic retargeting of human hand motion can therefore produce actions that
> are physically infeasible for robots. Despite these low-level differences,
> human demonstrations provide valuable motion cues about how to manipulate and
> interact with objects. Our key idea is to exploit the forward diffusion
> process: as noise is added to actions, low-level execution differences fade
> while high-level task guidance is preserved. We present X-Diffusion, a
> principled framework for training diffusion policies that maximally leverages
> human data without learning dynamically infeasible motions. X-Diffusion first
> trains a classifier to predict whether a noisy action is executed by a human or
> robot. Then, a human action is incorporated into policy training only after
> adding sufficient noise such that the classifier cannot discern its embodiment.
> Actions consistent with robot execution supervise fine-grained denoising at low
> noise levels, while mismatched human actions provide only coarse guidance at
> higher noise levels. Our experiments show that naive co-training under
> execution mismatches degrades policy performance, while X-Diffusion
> consistently improves it. Across five manipulation tasks, X-Diffusion achieves
> a 16% higher average success rate than the best baseline. The project website
> is available at https://portal-cornell.github.io/X-Diffusion/.

