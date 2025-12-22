---
layout: default
title: Deep Learning-based Robust Autonomous Navigation of Aerial Robots in Dense Forests
---

# Deep Learning-based Robust Autonomous Navigation of Aerial Robots in Dense Forests
**arXiv**：[2512.17553v1](https://arxiv.org/abs/2512.17553) · [PDF](https://arxiv.org/pdf/2512.17553.pdf)  
**作者**：Guglielmo Del Col, Väinö Karjalainen, Teemu Hakala, Yibo Zhang, Eija Honkavaara  

**一句话要点**：提出改进深度学习导航框架，集成语义增强深度编码与神经运动基元评估，用于密集森林中无人机鲁棒飞行。

**关键词**：无人机导航, 深度学习, 森林环境, 视觉惯性里程计, 运动规划, 实时安全

## 3 点简述
- 核心问题：密集自然环境中无人机自主导航面临能见度低、细薄不规则障碍、GNSS缺失和感知退化等挑战。
- 方法要点：在sevae-ORACLE算法基础上，增加横向控制、时间一致性机制、立体视觉惯性里程计和安全层，优化深度表示和GPU推理。
- 实验或效果：在相同环境和硬件下，相比现有方法，成功率更高、轨迹更稳定、避障更优，在三种森林环境中实现全自主飞行。

## 摘要（原文）

> Autonomous aerial navigation in dense natural environments remains challenging due to limited visibility, thin and irregular obstacles, GNSS-denied operation, and frequent perceptual degradation. This work presents an improved deep learning-based navigation framework that integrates semantically enhanced depth encoding with neural motion-primitive evaluation for robust flight in cluttered forests. Several modules are incorporated on top of the original sevae-ORACLE algorithm to address limitations observed during real-world deployment, including lateral control for sharper maneuvering, a temporal consistency mechanism to suppress oscillatory planning decisions, a stereo-based visual-inertial odometry solution for drift-resilient state estimation, and a supervisory safety layer that filters unsafe actions in real time. A depth refinement stage is included to improve the representation of thin branches and reduce stereo noise, while GPU optimization increases onboard inference throughput from 4 Hz to 10 Hz.
>   The proposed approach is evaluated against several existing learning-based navigation methods under identical environmental conditions and hardware constraints. It demonstrates higher success rates, more stable trajectories, and improved collision avoidance, particularly in highly cluttered forest settings. The system is deployed on a custom quadrotor in three boreal forest environments, achieving fully autonomous completion in all flights in moderate and dense clutter, and 12 out of 15 flights in highly dense underbrush. These results demonstrate improved reliability and safety over existing navigation methods in complex natural environments.

