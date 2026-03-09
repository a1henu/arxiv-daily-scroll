---
layout: default
title: CDF-Glove: A Cable-Driven Force Feedback Glove for Dexterous Teleoperation
---

# CDF-Glove: A Cable-Driven Force Feedback Glove for Dexterous Teleoperation
**arXiv**：[2603.05804v1](https://arxiv.org/abs/2603.05804) · [PDF](https://arxiv.org/pdf/2603.05804.pdf)  
**作者**：Huayue Liang, Ruochong Li, Yaodong Yang, Long Zeng, Yuanpei Chen, Xueqian Wang  

**一句话要点**：提出CDF-Glove以解决灵巧遥操作中触觉反馈缺失、设备笨重昂贵的问题。

**关键词**：触觉反馈手套, 灵巧遥操作, 电缆驱动, 模仿学习, 力反馈延迟, 开源硬件

## 3 点简述
- 核心问题：灵巧遥操作平台通常缺乏触觉反馈，导致演示质量低，且设备笨重昂贵。
- 方法要点：开发轻量低成本电缆驱动触觉反馈手套，支持20个手指自由度，实现实时状态感知与力反馈。
- 实验或效果：相比无反馈遥操作，任务成功率提升4倍；基于收集的数据训练策略，成功率提高55%，完成时间减少47.2%。

## 摘要（原文）

> High-quality teleoperated demonstrations are a primary bottleneck for imitation learning (IL) in dexterous manipulation. However, haptic feedback provides operators with real-time contact information, enabling real-time finger posture adjustments, and thereby improving demonstration quality. Existing dexterous teleoperation platforms typically omit haptic feedback and remain bulky and expensive. We introduce CDF-Glove, a lightweight and low cost cable-driven force-feedback glove. The real-time state is available for 20 finger degrees of freedom (DoF), of which 16 are directly sensed and 4 are passively coupled (inferred from kinematic constraints). We develop a kinematic model and control stack for the glove, and validate them across multiple robotic hands with diverse kinematics and DoF. The CDF-Glove achieves distal joint repeatability of 0.4 degrees, and delivers about 200 ms force feedback latency, yielding a 4x improvement in task success rate relative to no-feedback teleoperation. We collect two bimanual teleoperation datasets, on which we train and evaluate Diffusion Policy baselines. Compared to kinesthetic teaching, the policies trained in our teleoperated demonstrations increase the average success rate by 55% and reduce the mean completion time by approximately 15.2 seconds (a 47.2% relative reduction). In particular, the CDF-Glove costs approximately US$230. The code and designs are released as open source at https://cdfglove.github.io/.

