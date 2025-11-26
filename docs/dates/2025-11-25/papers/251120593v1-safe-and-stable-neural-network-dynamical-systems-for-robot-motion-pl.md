---
layout: default
title: Safe and Stable Neural Network Dynamical Systems for Robot Motion Planning
---

# Safe and Stable Neural Network Dynamical Systems for Robot Motion Planning
**arXiv**：[2511.20593v1](https://arxiv.org/abs/2511.20593) · [PDF](https://arxiv.org/pdf/2511.20593.pdf)  
**作者**：Allen Emmanuel Binny, Mahathi Anand, Hugo T. M. Kussaba, Lingyun Chen, Shreenabh Agrawal, Fares J. Abu-Dakka, Abdalla Swikir  

**一句话要点**：提出S²-NNDS框架以解决机器人运动规划中的安全与稳定性问题

**关键词**：机器人运动规划, 神经网络动力学系统, 学习从演示, Lyapunov稳定性, 屏障安全证书, 分形共形预测

## 3 点简述
- 核心问题：从演示中学习安全稳定的机器人运动，尤其在复杂非线性动态环境中
- 方法要点：结合神经网络动力学系统与Lyapunov稳定性和屏障安全证书学习
- 实验或效果：在2D和3D数据集上验证，从潜在不安全演示中学习鲁棒运动

## 摘要（原文）

> Learning safe and stable robot motions from demonstrations remains a challenge, especially in complex, nonlinear tasks involving dynamic, obstacle-rich environments. In this paper, we propose Safe and Stable Neural Network Dynamical Systems S$^2$-NNDS, a learning-from-demonstration framework that simultaneously learns expressive neural dynamical systems alongside neural Lyapunov stability and barrier safety certificates. Unlike traditional approaches with restrictive polynomial parameterizations, S$^2$-NNDS leverages neural networks to capture complex robot motions providing probabilistic guarantees through split conformal prediction in learned certificates. Experimental results on various 2D and 3D datasets -- including LASA handwriting and demonstrations recorded kinesthetically from the Franka Emika Panda robot -- validate S$^2$-NNDS effectiveness in learning robust, safe, and stable motions from potentially unsafe demonstrations.

