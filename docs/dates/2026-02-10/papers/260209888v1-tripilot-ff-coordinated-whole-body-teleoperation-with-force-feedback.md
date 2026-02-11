---
layout: default
title: TriPilot-FF: Coordinated Whole-Body Teleoperation with Force Feedback
---

# TriPilot-FF: Coordinated Whole-Body Teleoperation with Force Feedback
**arXiv**：[2602.09888v1](https://arxiv.org/abs/2602.09888) · [PDF](https://arxiv.org/pdf/2602.09888.pdf)  
**作者**：Zihao Li, Yanan Zhou, Ranpeng Qiu, Hangyu Wu, Guoqiang Ren, Weiming Zhi  

**一句话要点**：提出TriPilot-FF系统，通过脚控踏板与力反馈实现移动机械臂全身遥操作协调

**关键词**：全身遥操作, 力反馈, 移动机械臂, 脚控界面, 激光雷达触觉, ACT策略

## 3 点简述
- 移动机械臂全身遥操作需协调轮式底座与双臂，现有界面多手控，脚控通道未充分利用
- 系统引入脚控踏板，基于激光雷达提供接近障碍物触觉反馈，无需显式避障控制器
- 结合臂部力反射与实时操作指导，提升操作精度，并集成反馈信号增强ACT策略性能

## 摘要（原文）

> Mobile manipulators broaden the operational envelope for robot manipulation. However, the whole-body teleoperation of such robots remains a problem: operators must coordinate a wheeled base and two arms while reasoning about obstacles and contact. Existing interfaces are predominantly hand-centric (e.g., VR controllers and joysticks), leaving foot-operated channels underexplored for continuous base control. We present TriPilot-FF, an open-source whole-body teleoperation system for a custom bimanual mobile manipulator that introduces a foot-operated pedal with lidar-driven pedal haptics, coupled with upper-body bimanual leader-follower teleoperation. Using only a low-cost base-mounted lidar, TriPilot-FF renders a resistive pedal cue from proximity-to-obstacle signals in the commanded direction, shaping operator commands toward collision-averse behaviour without an explicit collision-avoidance controller. The system also supports arm-side force reflection for contact awareness and provides real-time force and visual guidance of bimanual manipulability to prompt mobile base repositioning, thereby improving reach. We demonstrate the capability of TriPilot-FF to effectively ``co-pilot'' the human operator over long time-horizons and tasks requiring precise mobile base movement and coordination. Finally, we incorporate teleoperation feedback signals into an Action Chunking with Transformers (ACT) policy and demonstrate improved performance when the additional information is available. We release the pedal device design, full software stack, and conduct extensive real-world evaluations on a bimanual wheeled platform. The project page of TriPilot-FF is http://bit.ly/46H3ZJT.

