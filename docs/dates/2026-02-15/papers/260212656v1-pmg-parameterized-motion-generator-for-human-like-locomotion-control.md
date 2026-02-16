---
layout: default
title: PMG: Parameterized Motion Generator for Human-like Locomotion Control
---

# PMG: Parameterized Motion Generator for Human-like Locomotion Control
**arXiv**：[2602.12656v1](https://arxiv.org/abs/2602.12656) · [PDF](https://arxiv.org/pdf/2602.12656.pdf)  
**作者**：Chenxi Han, Yuheng Min, Zihao Huang, Ao Hong, Hang Liu, Yi Cheng, Houde Liu  

**一句话要点**：提出参数化运动生成器以解决人形机器人全身参考引导控制适应性问题

**关键词**：人形机器人控制, 参数化运动生成, 仿真到现实迁移, 模仿学习, 运动跟踪

## 3 点简述
- 现有全身参考引导方法难以适应高层命令接口和多样任务场景，需大量高质量数据且鲁棒性差
- PMG基于人类运动结构分析，使用紧凑参数化数据和多维控制命令实时合成参考轨迹
- 结合模仿学习和优化模块，在人形机器人ZERITH Z1上验证了自然运动、精确响应和高效仿真到现实迁移

## 摘要（原文）

> Recent advances in data-driven reinforcement learning and motion tracking have substantially improved humanoid locomotion, yet critical practical challenges remain. In particular, while low-level motion tracking and trajectory-following controllers are mature, whole-body reference-guided methods are difficult to adapt to higher-level command interfaces and diverse task contexts: they require large, high-quality datasets, are brittle across speed and pose regimes, and are sensitive to robot-specific calibration. To address these limitations, we propose the Parameterized Motion Generator (PMG), a real-time motion generator grounded in an analysis of human motion structure that synthesizes reference trajectories using only a compact set of parameterized motion data together with High-dimensional control commands. Combined with an imitation-learning pipeline and an optimization-based sim-to-real motor parameter identification module, we validate the complete approach on our humanoid prototype ZERITH Z1 and show that, within a single integrated system, PMG produces natural, human-like locomotion, responds precisely to high-dimensional control inputs-including VR-based teleoperation-and enables efficient, verifiable sim-to-real transfer. Together, these results establish a practical, experimentally validated pathway toward natural and deployable humanoid control.

