---
layout: default
title: Learning to Design Soft Hands using Reward Models
---

# Learning to Design Soft Hands using Reward Models
**arXiv**：[2510.17086v1](https://arxiv.org/abs/2510.17086) · [PDF](https://arxiv.org/pdf/2510.17086.pdf)  
**作者**：Xueqian Bai, Nicklas Hansen, Adabhav Singh, Michael T. Tolley, Yan Duan, Pieter Abbeel, Xiaolong Wang, Sha Yi  

**一句话要点**：提出CEM-RM框架以优化肌腱驱动软体手设计，提升抓取成功率

**关键词**：软体机器人设计, 硬件控制协同优化, 奖励模型, 肌腱驱动, 仿真训练, 抓取成功率

## 3 点简述
- 软体手设计需兼顾柔顺性与功能性，但硬件与控制协同设计空间高维且评估昂贵
- 基于遥操作控制策略，使用CEM-RM框架高效优化设计，减少超半评估次数
- 仿真与硬件实验显示，优化设计在多样挑战物体上抓取成功率显著优于基线

## 摘要（原文）

> Soft robotic hands promise to provide compliant and safe interaction with
> objects and environments. However, designing soft hands to be both compliant
> and functional across diverse use cases remains challenging. Although co-design
> of hardware and control better couples morphology to behavior, the resulting
> search space is high-dimensional, and even simulation-based evaluation is
> computationally expensive. In this paper, we propose a Cross-Entropy Method
> with Reward Model (CEM-RM) framework that efficiently optimizes tendon-driven
> soft robotic hands based on teleoperation control policy, reducing design
> evaluations by more than half compared to pure optimization while learning a
> distribution of optimized hand designs from pre-collected teleoperation data.
> We derive a design space for a soft robotic hand composed of flexural soft
> fingers and implement parallelized training in simulation. The optimized hands
> are then 3D-printed and deployed in the real world using both teleoperation
> data and real-time teleoperation. Experiments in both simulation and hardware
> demonstrate that our optimized design significantly outperforms baseline hands
> in grasping success rates across a diverse set of challenging objects.

