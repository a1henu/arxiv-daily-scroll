---
layout: default
title: The Mini Wheelbot Dataset: High-Fidelity Data for Robot Learning
---

# The Mini Wheelbot Dataset: High-Fidelity Data for Robot Learning
**arXiv**：[2601.11394v1](https://arxiv.org/abs/2601.11394) · [PDF](https://arxiv.org/pdf/2601.11394.pdf)  
**作者**：Henrik Hose, Paul Brunzema, Devdutt Subhasish, Sebastian Trimpe  

**一句话要点**：提出Mini Wheelbot数据集以解决机器人学习中高质量真实世界数据获取难的问题

**关键词**：机器人学习, 数据集, 动态模型学习, 状态估计, 时间序列分类

## 3 点简述
- 核心问题：不稳定系统学习控制算法需高质量数据，但专用机器人硬件获取困难
- 方法要点：提供1kHz同步数据，包括传感器、状态估计、运动捕捉真值和第三方视频
- 实验或效果：涵盖多硬件实例和表面，使用多种控制范式，并展示示例应用

## 摘要（原文）

> The development of robust learning-based control algorithms for unstable systems requires high-quality, real-world data, yet access to specialized robotic hardware remains a significant barrier for many researchers. This paper introduces a comprehensive dynamics dataset for the Mini Wheelbot, an open-source, quasi-symmetric balancing reaction wheel unicycle. The dataset provides 1 kHz synchronized data encompassing all onboard sensor readings, state estimates, ground-truth poses from a motion capture system, and third-person video logs. To ensure data diversity, we include experiments across multiple hardware instances and surfaces using various control paradigms, including pseudo-random binary excitation, nonlinear model predictive control, and reinforcement learning agents. We include several example applications in dynamics model learning, state estimation, and time-series classification to illustrate common robotics algorithms that can be benchmarked on our dataset.

