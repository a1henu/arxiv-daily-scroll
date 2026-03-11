---
layout: default
title: SCDP: Learning Humanoid Locomotion from Partial Observations via Mixed-Observation Distillation
---

# SCDP: Learning Humanoid Locomotion from Partial Observations via Mixed-Observation Distillation
**arXiv**：[2603.09574v1](https://arxiv.org/abs/2603.09574) · [PDF](https://arxiv.org/pdf/2603.09574.pdf)  
**作者**：Milo Carroll, Tianhu Peng, Lingfan Bao, Chengxu Zhou, Zhibin Li  

**一句话要点**：提出SCDP方法，通过混合观测蒸馏实现仅用机载传感器的人形机器人运动控制

**关键词**：人形机器人运动控制, 扩散策略, 混合观测蒸馏, 隐式状态估计, 机载传感器, 离线数据集

## 3 点简述
- 核心问题：现有方法依赖特权全身状态，需要复杂不可靠的状态估计，限制了部署。
- 方法要点：使用混合观测训练，扩散模型基于传感器历史预测特权未来轨迹，促进隐式状态推断。
- 实验或效果：在仿真中达到高成功率，并在真实G1人形机器人上以50Hz部署，无需外部感知。

## 摘要（原文）

> Distilling humanoid locomotion control from offline datasets into deployable policies remains a challenge, as existing methods rely on privileged full-body states that require complex and often unreliable state estimation. We present Sensor-Conditioned Diffusion Policies (SCDP) that enables humanoid locomotion using only onboard sensors, eliminating the need for explicit state estimation. SCDP decouples sensing from supervision through mixed-observation training: diffusion model conditions on sensor histories while being supervised to predict privileged future state-action trajectories, enforcing the model to infer the motion dynamics under partial observability. We further develop restricted denoising, context distribution alignment, and context-aware attention masking to encourage implicit state estimation within the model and to prevent train-deploy mismatch. We validate SCDP on velocity-commanded locomotion and motion reference tracking tasks. In simulation, SCDP achieves near-perfect success on velocity control (99-100%) and 93% tracking success in AMASS test set, performing comparable to privileged baselines while using only onboard sensors. Finally, we deploy the trained policy on a real G1 humanoid at 50 Hz, demonstrating robust real robot locomotion without external sensing or state estimation.

