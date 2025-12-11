---
layout: default
title: One-Shot Real-World Demonstration Synthesis for Scalable Bimanual Manipulation
---

# One-Shot Real-World Demonstration Synthesis for Scalable Bimanual Manipulation
**arXiv**：[2512.09297v1](https://arxiv.org/abs/2512.09297) · [PDF](https://arxiv.org/pdf/2512.09297.pdf)  
**作者**：Huayi Zhou, Kui Jia  

**一句话要点**：提出BiDemoSyn框架，从单次真实演示合成大规模双手机器人操作数据以解决效率与真实性的权衡问题。

**关键词**：双手机器人操作, 演示合成, 模仿学习, 轨迹优化, 物理可行性, 泛化能力

## 3 点简述
- 核心问题：双手机器人操作学习依赖大规模高质量演示，但现有方法在效率与真实性间存在权衡。
- 方法要点：将任务分解为不变协调块和可变调整，通过视觉对齐和轻量轨迹优化合成物理可行的演示。
- 实验或效果：在六个任务中，基于合成数据的策略对新物体姿态和形状具有鲁棒泛化能力，优于基线方法。

## 摘要（原文）

> Learning dexterous bimanual manipulation policies critically depends on large-scale, high-quality demonstrations, yet current paradigms face inherent trade-offs: teleoperation provides physically grounded data but is prohibitively labor-intensive, while simulation-based synthesis scales efficiently but suffers from sim-to-real gaps. We present BiDemoSyn, a framework that synthesizes contact-rich, physically feasible bimanual demonstrations from a single real-world example. The key idea is to decompose tasks into invariant coordination blocks and variable, object-dependent adjustments, then adapt them through vision-guided alignment and lightweight trajectory optimization. This enables the generation of thousands of diverse and feasible demonstrations within several hour, without repeated teleoperation or reliance on imperfect simulation. Across six dual-arm tasks, we show that policies trained on BiDemoSyn data generalize robustly to novel object poses and shapes, significantly outperforming recent baselines. By bridging the gap between efficiency and real-world fidelity, BiDemoSyn provides a scalable path toward practical imitation learning for complex bimanual manipulation without compromising physical grounding.

