---
layout: default
title: Theoretical Closed-loop Stability Bounds for Dynamical System Coupled with Diffusion Policies
---

# Theoretical Closed-loop Stability Bounds for Dynamical System Coupled with Diffusion Policies
**arXiv**：[2511.15520v1](https://arxiv.org/abs/2511.15520) · [PDF](https://arxiv.org/pdf/2511.15520.pdf)  
**作者**：Gabriel Lauzier, Alexandre Girard, François Ferland  

**一句话要点**：提出扩散策略闭环稳定性理论框架以加速机器人模仿学习

**关键词**：扩散策略, 闭环稳定性, 模仿学习, 机器人控制, 动力学耦合

## 3 点简述
- 核心问题：扩散策略在实时应用中因计算密集的反向扩散过程难以快速决策
- 方法要点：部分执行去噪过程，耦合植物动力学与扩散动力学以提升效率
- 实验或效果：提供稳定性边界和度量，基于演示方差预测控制器稳定性

## 摘要（原文）

> Diffusion Policy has shown great performance in robotic manipulation tasks under stochastic perturbations, due to its ability to model multimodal action distributions. Nonetheless, its reliance on a computationally expensive reverse-time diffusion (denoising) process, for action inference, makes it challenging to use for real-time applications where quick decision-making is mandatory. This work studies the possibility of conducting the denoising process only partially before executing an action, allowing the plant to evolve according to its dynamics in parallel to the reverse-time diffusion dynamics ongoing on the computer. In a classical diffusion policy setting, the plant dynamics are usually slow and the two dynamical processes are uncoupled. Here, we investigate theoretical bounds on the stability of closed-loop systems using diffusion policies when the plant dynamics and the denoising dynamics are coupled. The contribution of this work gives a framework for faster imitation learning and a metric that yields if a controller will be stable based on the variance of the demonstrations.

