---
layout: default
title: X-Loco: Towards Generalist Humanoid Locomotion Control via Synergetic Policy Distillation
---

# X-Loco: Towards Generalist Humanoid Locomotion Control via Synergetic Policy Distillation
**arXiv**：[2603.03733v1](https://arxiv.org/abs/2603.03733) · [PDF](https://arxiv.org/pdf/2603.03733.pdf)  
**作者**：Dewei Wang, Xinmiao Wang, Chenyun Zhang, Jiyuan Shi, Yingnan Zhao, Chenjia Bai, Xuelong Li  

**一句话要点**：提出X-Loco框架，通过协同策略蒸馏训练视觉基础的人形机器人通用运动控制策略

**关键词**：人形机器人运动控制, 策略蒸馏, 视觉基础控制, 通用运动技能, 协同学习

## 3 点简述
- 核心问题：单一策略难以掌握人形机器人多样运动技能，如直立行走、摔倒恢复和全身协调
- 方法要点：训练多个专家策略，采用协同蒸馏和自适应选择机制，动态指导视觉学生策略
- 实验或效果：在摔倒恢复和地形穿越等任务中表现优异，有效利用专家知识并提升学习效率

## 摘要（原文）

> While recent advances have demonstrated strong performance in individual humanoid skills such as upright locomotion, fall recovery and whole-body coordination, learning a single policy that masters all these skills remains challenging due to the diverse dynamics and conflicting control objectives involved. To address this, we introduce X-Loco, a framework for training a vision-based generalist humanoid locomotion policy. X-Loco trains multiple oracle specialist policies and adopts a synergetic policy distillation with a case-adaptive specialist selection mechanism, which dynamically leverages multiple specialist policies to guide a vision-based student policy. This design enables the student to acquire a broad spectrum of locomotion skills, ranging from fall recovery to terrain traversal and whole-body coordination skills. To the best of our knowledge, X-Loco is the first framework to demonstrate vision-based humanoid locomotion that jointly integrates upright locomotion, whole-body coordination and fall recovery, while operating solely under velocity commands without relying on reference motions. Experimental results show that X-Loco achieves superior performance, demonstrated by tasks such as fall recovery and terrain traversal. Ablation studies further highlight that our framework effectively leverages specialist expertise and enhances learning efficiency.

