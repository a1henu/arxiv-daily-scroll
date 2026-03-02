---
layout: default
title: OmniTrack: General Motion Tracking via Physics-Consistent Reference
---

# OmniTrack: General Motion Tracking via Physics-Consistent Reference
**arXiv**：[2602.23832v1](https://arxiv.org/abs/2602.23832) · [PDF](https://arxiv.org/pdf/2602.23832.pdf)  
**作者**：Yuhan Li, Peiyuan Zhi, Yunshen Wang, Tengyu Liu, Sixu Yan, Wenyu Liu, Xinggang Wang, Baoxiong Jia, Siyuan Huang  

**一句话要点**：提出OmniTrack框架，通过物理一致参考解决人形机器人通用运动跟踪中的物理不可行性问题

**关键词**：人形机器人控制, 运动跟踪, 物理一致性, 仿真训练, 通用策略, 实时操作

## 3 点简述
- 核心问题：人类与机器人形态和动力学差异及数据噪声导致参考运动存在物理不可行伪影，如漂浮和穿透，影响跟踪策略泛化性
- 方法要点：分两阶段框架，首阶段特权通用策略在仿真中生成物理可行运动，次阶段通用控制策略跟踪这些运动，确保稳定控制转移
- 实验或效果：实验显示OmniTrack提升跟踪精度，对未见运动有强泛化性，真实测试中实现小时级稳定跟踪，包括复杂杂技动作

## 摘要（原文）

> Learning motion tracking from rich human motion data is a foundational task for achieving general control in humanoid robots, enabling them to perform diverse behaviors. However, discrepancies in morphology and dynamics between humans and robots, combined with data noise, introduce physically infeasible artifacts in reference motions, such as floating and penetration. During both training and execution, these artifacts create a conflict between following inaccurate reference motions and maintaining the robot's stability, hindering the development of a generalizable motion tracking policy. To address these challenges, we introduce OmniTrack, a general tracking framework that explicitly decouples physical feasibility from general motion tracking. In the first stage, a privileged generalist policy generates physically plausible motions that strictly adhere to the robot's dynamics via trajectory rollout in simulation. In the second stage, the general control policy is trained to track these physically feasible motions, ensuring stable and coherent control transfer to the real robot. Experiments show that OmniTrack improves tracking accuracy and demonstrates strong generalization to unseen motions. In real-world tests, OmniTrack achieves hour-long, consistent, and stable tracking, including complex acrobatic motions such as flips and cartwheels. Additionally, we show that OmniTrack supports human-style stable and dynamic online teleoperation, highlighting its robustness and adaptability to varying user inputs.

