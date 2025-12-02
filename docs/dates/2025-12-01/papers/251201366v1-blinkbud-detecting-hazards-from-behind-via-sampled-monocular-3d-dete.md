---
layout: default
title: BlinkBud: Detecting Hazards from Behind via Sampled Monocular 3D Detection on a Single Earbud
---

# BlinkBud: Detecting Hazards from Behind via Sampled Monocular 3D Detection on a Single Earbud
**arXiv**：[2512.01366v1](https://arxiv.org/abs/2512.01366) · [PDF](https://arxiv.org/pdf/2512.01366.pdf)  
**作者**：Yunzhe Li, Jiajun Yan, Yuzhou Wei, Kechen Liu, Yize Zhao, Chong Zhang, Hongzi Zhu, Li Lu, Shan Chang, Minyi Guo  

**一句话要点**：提出BlinkBud系统，利用单耳塞和手机检测用户后方危险物体，保障行人骑行安全。

**关键词**：单目3D检测, 物体跟踪, 低功耗系统, 行人安全, 强化学习采样, 头部运动校正

## 3 点简述
- 核心问题：行人或骑行者难以察觉后方快速接近的车辆，存在安全隐患。
- 方法要点：基于卡尔曼滤波和强化学习采样策略，实现低功耗3D物体跟踪，并校正头部运动影响。
- 实验或效果：原型系统功耗低，耳塞和手机平均功耗分别为29.8 mW和702.6 mW，误报率和漏报率分别为4.90%和1.47%。

## 摘要（原文）

> Failing to be aware of speeding vehicles approaching from behind poses a huge threat to the road safety of pedestrians and cyclists. In this paper, we propose BlinkBud, which utilizes a single earbud and a paired phone to online detect hazardous objects approaching from behind of a user. The core idea is to accurately track visually identified objects utilizing a small number of sampled camera images taken from the earbud. To minimize the power consumption of the earbud and the phone while guaranteeing the best tracking accuracy, a novel 3D object tracking algorithm is devised, integrating both a Kalman filter based trajectory estimation scheme and an optimal image sampling strategy based on reinforcement learning. Moreover, the impact of constant user head movements on the tracking accuracy is significantly eliminated by leveraging the estimated pitch and yaw angles to correct the object depth estimation and align the camera coordinate system to the user's body coordinate system, respectively. We implement a prototype BlinkBud system and conduct extensive real-world experiments. Results show that BlinkBud is lightweight with ultra-low mean power consumptions of 29.8 mW and 702.6 mW on the earbud and smartphone, respectively, and can accurately detect hazards with a low average false positive ratio (FPR) and false negative ratio (FNR) of 4.90% and 1.47%, respectively.

