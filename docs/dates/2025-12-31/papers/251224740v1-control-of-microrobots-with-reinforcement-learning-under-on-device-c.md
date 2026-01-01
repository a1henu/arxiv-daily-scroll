---
layout: default
title: Control of Microrobots with Reinforcement Learning under On-Device Compute Constraints
---

# Control of Microrobots with Reinforcement Learning under On-Device Compute Constraints
**arXiv**：[2512.24740v1](https://arxiv.org/abs/2512.24740) · [PDF](https://arxiv.org/pdf/2512.24740.pdf)  
**作者**：Yichen Liu, Kesava Viswanadha, Zhongyu Li, Nelson Lojo, Kristofer S. J. Pister  

**一句话要点**：提出基于强化学习的微机器人控制方法，在设备计算约束下实现低延迟边缘控制。

**关键词**：微机器人控制, 强化学习, 边缘计算, 整数量化, 域随机化, 步态调度

## 3 点简述
- 核心问题：微机器人在计算、内存和功率受限下实现稳健运动控制。
- 方法要点：使用强化学习训练紧凑MLP策略，结合域随机化和整数量化优化推理。
- 实验或效果：在ARM Cortex-M0硬件上部署，通过资源感知步态调度提升性能，并在真实机器人上验证稳定性。

## 摘要（原文）

> An important function of autonomous microrobots is the ability to perform robust movement over terrain. This paper explores an edge ML approach to microrobot locomotion, allowing for on-device, lower latency control under compute, memory, and power constraints. This paper explores the locomotion of a sub-centimeter quadrupedal microrobot via reinforcement learning (RL) and deploys the resulting controller on an ultra-small system-on-chip (SoC), SC$μ$M-3C, featuring an ARM Cortex-M0 microcontroller running at 5 MHz. We train a compact FP32 multilayer perceptron (MLP) policy with two hidden layers ($[128, 64]$) in a massively parallel GPU simulation and enhance robustness by utilizing domain randomization over simulation parameters. We then study integer (Int8) quantization (per-tensor and per-feature) to allow for higher inference update rates on our resource-limited hardware, and we connect hardware power budgets to achievable update frequency via a cycles-per-update model for inference on our Cortex-M0. We propose a resource-aware gait scheduling viewpoint: given a device power budget, we can select the gait mode (trot/intermediate/gallop) that maximizes expected RL reward at a corresponding feasible update frequency. Finally, we deploy our MLP policy on a real-world large-scale robot on uneven terrain, qualitatively noting that domain-randomized training can improve out-of-distribution stability. We do not claim real-world large-robot empirical zero-shot transfer in this work.

