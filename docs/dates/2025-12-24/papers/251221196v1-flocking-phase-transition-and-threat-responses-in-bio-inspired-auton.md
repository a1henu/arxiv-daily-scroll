---
layout: default
title: Flocking phase transition and threat responses in bio-inspired autonomous drone swarms
---

# Flocking phase transition and threat responses in bio-inspired autonomous drone swarms
**arXiv**：[2512.21196v1](https://arxiv.org/abs/2512.21196) · [PDF](https://arxiv.org/pdf/2512.21196.pdf)  
**作者**：Matthieu Verdoucq, Dari Trendafilov, Clément Sire, Ramón Escobedo, Guy Theraulaz, Gautier Hattenberger  

**一句话要点**：提出基于局部对齐和吸引的3D集群算法，通过增益调谐实现无人机群相位转变与威胁响应增强。

**关键词**：无人机集群, 生物启发算法, 相位转变, 局部交互, 集体运动, 威胁响应

## 3 点简述
- 核心问题：如何设计自主无人机群算法以模拟动物集群运动，实现稳定性和灵活性平衡。
- 方法要点：使用最小邻居交互规则，仅依赖局部对齐和吸引增益，系统调谐以映射相位图。
- 实验或效果：十架无人机户外实验结合模拟，显示在临界区域操作可提升对外部干扰的响应能力。

## 摘要（原文）

> Collective motion inspired by animal groups offers powerful design principles for autonomous aerial swarms. We present a bio-inspired 3D flocking algorithm in which each drone interacts only with a minimal set of influential neighbors, relying solely on local alignment and attraction cues. By systematically tuning these two interaction gains, we map a phase diagram revealing sharp transitions between swarming and schooling, as well as a critical region where susceptibility, polarization fluctuations, and reorganization capacity peak. Outdoor experiments with a swarm of ten drones, combined with simulations using a calibrated flight-dynamics model, show that operating near this transition enhances responsiveness to external disturbances. When confronted with an intruder, the swarm performs rapid collective turns, transient expansions, and reliably recovers high alignment within seconds. These results demonstrate that minimal local-interaction rules are sufficient to generate multiple collective phases and that simple gain modulation offers an efficient mechanism to adjust stability, flexibility, and resilience in drone swarms.

