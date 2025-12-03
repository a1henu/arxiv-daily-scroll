---
layout: default
title: Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach
---

# Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach
**arXiv**：[2512.02834v1](https://arxiv.org/abs/2512.02834) · [PDF](https://arxiv.org/pdf/2512.02834.pdf)  
**作者**：Siyuan Yang, Yang Zhang, Haoran He, Ling Pan, Xiu Li, Chenjia Bai, Xuelong Li  

**一句话要点**：提出TACO测试时缩放框架，以解决视觉-语言-动作模型在下游任务中的推理不稳定性问题。

**关键词**：视觉-语言-动作模型, 测试时缩放, 伪计数估计, 推理稳定性, 离线强化学习, 分布偏移

## 3 点简述
- 核心问题：预训练VLA模型在微调后存在冗余动作模式，导致推理时分布偏移和不稳定性。
- 方法要点：使用轻量级伪计数估计器作为动作块验证器，在推理时选择最大伪计数的动作，防止分布偏移。
- 实验或效果：在多个仿真基准和双臂平台上显著提升推理稳定性和下游任务成功率。

## 摘要（原文）

> Vision-Language-Action (VLA) models, trained via flow-matching or diffusion objectives, excel at learning complex behaviors from large-scale, multi-modal datasets (e.g., human teleoperation, scripted policies). However, since VLAs incorporate diverse data modes in the pre-training stage, and the finetuning dataset often contains demonstration data collected in a kinematically suboptimal or undesirable way, it exists redundant action modes that are irrelevant to the success action modes of the downstream task. Specifically, we observe a critical inference-time fragility among various sampled noises after supervised finetuning of pre-trained VLAs. In this paper, we attribute this instability to the distribution shift between the VLA policy and the policy induced by stable success modes of the downstream task dataset. Thus, we propose \textbf{TACO}, a test-time-scaling (TTS) framework that applies a lightweight pseudo-count estimator as a high-fidelity verifier of action chunks. The VLA models integrated with TACO can execute the actions with maximum pseudo-count from all sampled action chunks, thereby preventing distribution shifts while preserving the generalization ability of VLAs since the constraint is applied only during inference. Our method resembles the classical anti-exploration principle in offline reinforcement learning (RL), and being gradient-free, it incurs significant computational benefits compared to RL update, especially for flow or diffusion-based VLAs which are difficult to perform RL update due to denoising process. Extensive experiments across four simulation benchmarks (RoboTwin2.0, Robotwin, LIBERO, SimplerEnv) and a dual-arm platform demonstrate that our method significantly improves the inference stability and success rates in downstream-task adaptations.

