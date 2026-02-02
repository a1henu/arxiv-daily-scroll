---
layout: default
title: Temporally Coherent Imitation Learning via Latent Action Flow Matching for Robotic Manipulation
---

# Temporally Coherent Imitation Learning via Latent Action Flow Matching for Robotic Manipulation
**arXiv**：[2601.23087v1](https://arxiv.org/abs/2601.23087) · [PDF](https://arxiv.org/pdf/2601.23087.pdf)  
**作者**：Wu Songwei, Jiang Zhiduo, Xie Guanghu, Liu Yang, Liu Hong  

**一句话要点**：提出LG-Flow Policy，通过潜在动作流匹配实现时序一致的机器人操作模仿学习。

**关键词**：机器人操作模仿学习, 流匹配, 潜在动作空间, 时序一致性, 长时程任务

## 3 点简述
- 核心问题：现有生成策略在长时程机器人操作中难以平衡建模能力、推理速度和执行稳定性。
- 方法要点：在连续潜在动作空间进行流匹配，编码动作序列为时序正则化轨迹，解耦全局运动与低层噪声。
- 实验或效果：在仿真和物理机器人上实现近单步推理，提升轨迹平滑度和任务成功率，优于基线方法。

## 摘要（原文）

> Learning long-horizon robotic manipulation requires jointly achieving expressive behavior modeling, real-time inference, and stable execution, which remains challenging for existing generative policies. Diffusion-based approaches provide strong modeling capacity but typically incur high inference latency, while flow matching enables fast one-step generation yet often leads to unstable execution when applied directly in the raw action space.
>   We propose LG-Flow Policy, a trajectory-level imitation learning framework that performs flow matching in a continuous latent action space. By encoding action sequences into temporally regularized latent trajectories and learning an explicit latent-space flow, the proposed approach decouples global motion structure from low-level control noise, resulting in smooth and reliable long-horizon execution.
>   LG-Flow Policy further incorporates geometry-aware point cloud conditioning and execution-time multimodal modulation, with visual cues evaluated as a representative modality in real-world settings. Experimental results in simulation and on physical robot platforms demonstrate that LG-Flow Policy achieves near single-step inference, substantially improves trajectory smoothness and task success over flow-based baselines operating in the raw action space, and remains significantly more efficient than diffusion-based policies.

