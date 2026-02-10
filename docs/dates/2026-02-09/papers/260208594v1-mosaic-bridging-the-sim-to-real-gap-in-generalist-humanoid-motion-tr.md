---
layout: default
title: MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation
---

# MOSAIC: Bridging the Sim-to-Real Gap in Generalist Humanoid Motion Tracking and Teleoperation with Rapid Residual Adaptation
**arXiv**：[2602.08594v1](https://arxiv.org/abs/2602.08594) · [PDF](https://arxiv.org/pdf/2602.08594.pdf)  
**作者**：Zhenguo Sun, Bo-Sheng Huang, Yibo Peng, Xukun Li, Jingyu Ma, Yu Sun, Zhe Li, Haojun Jiang, Biao Gao, Zhenshan Bing, Xinlong Wang, Alois Knoll  

**一句话要点**：提出MOSAIC系统，通过快速残差适配桥接仿真与现实的接口差距，实现人形机器人稳健运动跟踪与全身遥操作。

**关键词**：人形机器人运动跟踪, 仿真到现实迁移, 快速残差适配, 全身遥操作, 强化学习, 策略蒸馏

## 3 点简述
- 核心问题：通用人形运动跟踪器在仿真中表现良好，但在硬件遥操作中因接口和动力学误差而脆弱。
- 方法要点：先训练通用运动跟踪器，再通过快速残差适配将接口特定策略蒸馏到通用跟踪器中。
- 实验或效果：通过系统消融、分布外基准测试和真实机器人实验验证了稳健的离线运动回放和在线长时遥操作。

## 摘要（原文）

> Generalist humanoid motion trackers have recently achieved strong simulation metrics by scaling data and training, yet often remain brittle on hardware during sustained teleoperation due to interface- and dynamics-induced errors. We present MOSAIC, an open-source, full-stack system for humanoid motion tracking and whole-body teleoperation across multiple interfaces. MOSAIC first learns a teleoperation-oriented general motion tracker via RL on a multi-source motion bank with adaptive resampling and rewards that emphasize world-frame motion consistency, which is critical for mobile teleoperation. To bridge the sim-to-real interface gap without sacrificing generality, MOSAIC then performs rapid residual adaptation: an interface-specific policy is trained using minimal interface-specific data, and then distilled into the general tracker through an additive residual module, outperforming naive fine-tuning or continual learning. We validate MOSAIC with systematic ablations, out-of-distribution benchmarking, and real-robot experiments demonstrating robust offline motion replay and online long-horizon teleoperation under realistic latency and noise.

