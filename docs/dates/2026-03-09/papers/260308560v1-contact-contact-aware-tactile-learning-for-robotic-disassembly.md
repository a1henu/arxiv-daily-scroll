---
layout: default
title: CONTACT: CONtact-aware TACTile Learning for Robotic Disassembly
---

# CONTACT: CONtact-aware TACTile Learning for Robotic Disassembly
**arXiv**：[2603.08560v1](https://arxiv.org/abs/2603.08560) · [PDF](https://arxiv.org/pdf/2603.08560.pdf)  
**作者**：Yosuke Saka, Jyun-Chi Hu, Adeesh Desai, Zhiyuan Zhang, Bihao Zhang, Quan Khanh Luu, Md Rakibul Islam Prince, Minghui Zheng, Yu She  

**一句话要点**：提出CONTACT框架，通过触觉力场学习提升机器人拆卸在接触密集场景中的性能。

**关键词**：机器人拆卸, 触觉学习, 力场表示, 接触感知, 多模态传感

## 3 点简述
- 核心问题：机器人拆卸在紧密公差、接触主导或可变形场景中，视觉策略可靠性下降。
- 方法要点：在统一学习框架中，比较视觉、视觉+触觉RGB、视觉+触觉力场三种传感配置。
- 实验或效果：触觉力场策略在仿真和真实实验中均取得最高成功率，尤其在接触依赖和可变形任务中。

## 摘要（原文）

> Robotic disassembly involves contact-rich interactions in which successful manipulation depends not only on geometric alignment but also on force-dependent state transitions. While vision-based policies perform well in structured settings, their reliability often degrades in tight-tolerance, contact-dominated, or deformable scenarios. In this work, we systematically investigate the role of tactile sensing in robotic disassembly through both simulation and real-world experiments. We construct five rigid-body disassembly tasks in simulation with increasing geometric constraints and extraction difficulty. We further design five real-world tasks, including three rigid and two deformable scenarios, to evaluate contact-dependent manipulation. Within a unified learning framework, we compare three sensing configurations: Vision Only, Vision + tactile RGB (TacRGB), and Vision + tactile force field (TacFF). Across both simulation and real-world experiments, TacFF-based policies consistently achieve the highest success rates, with particularly notable gains in contact-dependent and deformable settings. Notably, naive fusion of TacRGB and TacFF underperforms either modality alone, indicating that simple concatenation can dilute task-relevant force information. Our results show that tactile sensing plays a critical, task-dependent role in robotic disassembly, with structured force-field representations being particularly effective in contact-dominated scenarios.

