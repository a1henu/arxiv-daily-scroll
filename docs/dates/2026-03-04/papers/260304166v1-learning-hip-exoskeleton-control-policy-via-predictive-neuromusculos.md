---
layout: default
title: Learning Hip Exoskeleton Control Policy via Predictive Neuromusculoskeletal Simulation
---

# Learning Hip Exoskeleton Control Policy via Predictive Neuromusculoskeletal Simulation
**arXiv**：[2603.04166v1](https://arxiv.org/abs/2603.04166) · [PDF](https://arxiv.org/pdf/2603.04166.pdf)  
**作者**：Ilseung Park, Changseob Song, Inseung Kang  

**一句话要点**：提出基于物理的神经肌肉骨骼学习框架，通过模拟训练髋外骨骼控制策略并实现硬件部署。

**关键词**：外骨骼控制, 神经肌肉骨骼模拟, 强化学习, 模拟到现实转移, 策略蒸馏

## 3 点简述
- 问题：外骨骼控制器开发依赖大量运动捕捉数据，限制在实验室外的可扩展性。
- 方法：在模拟中训练强化学习策略，使用肌肉协同动作先验，通过课程学习覆盖多种行走条件。
- 效果：模拟中减少肌肉激活和关节功率，硬件上实现模拟到现实的转移，无需额外调优。

## 摘要（原文）

> Developing exoskeleton controllers that generalize across diverse locomotor conditions typically requires extensive motion-capture data and biomechanical labeling, limiting scalability beyond instrumented laboratory settings. Here, we present a physics-based neuromusculoskeletal learning framework that trains a hip-exoskeleton control policy entirely in simulation, without motion-capture demonstrations, and deploys it on hardware via policy distillation. A reinforcement learning teacher policy is trained using a muscle-synergy action prior over a wide range of walking speeds and slopes through a two-stage curriculum, enabling direct comparison between assisted and no-exoskeleton conditions. In simulation, exoskeleton assistance reduces mean muscle activation by up to 3.4% and mean positive joint power by up to 7.0% on level ground and ramp ascent, with benefits increasing systematically with walking speed. On hardware, the assistance profiles learned in simulation are preserved across matched speed-slope conditions (r: 0.82, RMSE: 0.03 Nm/kg), providing quantitative evidence of sim-to-real transfer without additional hardware tuning. These results demonstrate that physics-based neuromusculoskeletal simulation can serve as a practical and scalable foundation for exoskeleton controller development, substantially reducing experimental burden during the design phase.

