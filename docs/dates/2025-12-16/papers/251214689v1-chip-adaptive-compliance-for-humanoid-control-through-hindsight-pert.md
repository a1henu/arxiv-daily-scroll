---
layout: default
title: CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation
---

# CHIP: Adaptive Compliance for Humanoid Control through Hindsight Perturbation
**arXiv**：[2512.14689v1](https://arxiv.org/abs/2512.14689) · [PDF](https://arxiv.org/pdf/2512.14689.pdf)  
**作者**：Sirui Chen, Zi-ang Cao, Zhengyi Luo, Fernando Castañeda, Chenran Li, Tingwu Wang, Ye Yuan, Linxi "Jim" Fan, C. Karen Liu, Yuke Zhu  

**一句话要点**：提出CHIP模块以解决人形机器人执行强力操作任务时末端执行器刚度控制与动态运动跟踪的平衡问题

**关键词**：人形机器人控制, 自适应柔顺控制, 后见扰动, 强力操作, 运动跟踪, 末端执行器刚度

## 3 点简述
- 核心问题：人形机器人在执行强力操作任务（如移动物体、擦拭）时，难以同时实现末端执行器刚度控制与动态运动跟踪
- 方法要点：CHIP通过后见扰动实现自适应柔顺控制，无需数据增强或额外奖励调优，可即插即用
- 实验或效果：在多种任务（如多机器人协作、开门）中展示出可控末端刚度与敏捷运动跟踪能力

## 摘要（原文）

> Recent progress in humanoid robots has unlocked agile locomotion skills, including backflipping, running, and crawling. Yet it remains challenging for a humanoid robot to perform forceful manipulation tasks such as moving objects, wiping, and pushing a cart. We propose adaptive Compliance Humanoid control through hIsight Perturbation (CHIP), a plug-and-play module that enables controllable end-effector stiffness while preserving agile tracking of dynamic reference motions. CHIP is easy to implement and requires neither data augmentation nor additional reward tuning. We show that a generalist motion-tracking controller trained with CHIP can perform a diverse set of forceful manipulation tasks that require different end-effector compliance, such as multi-robot collaboration, wiping, box delivery, and door opening.

