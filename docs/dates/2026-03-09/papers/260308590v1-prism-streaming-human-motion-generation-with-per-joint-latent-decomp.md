---
layout: default
title: PRISM: Streaming Human Motion Generation with Per-Joint Latent Decomposition
---

# PRISM: Streaming Human Motion Generation with Per-Joint Latent Decomposition
**arXiv**：[2603.08590v1](https://arxiv.org/abs/2603.08590) · [PDF](https://arxiv.org/pdf/2603.08590.pdf)  
**作者**：Zeyu Ling, Qing Shuai, Teng Zhang, Shiyang Li, Bo Han, Changqing Zou  

**一句话要点**：提出PRISM模型，通过关节分解潜在空间和噪声自由条件注入，统一处理文本到动作生成和流式合成任务。

**关键词**：动作生成, 潜在空间分解, 流式合成, 文本到动作, 因果VAE, 前向运动学监督

## 3 点简述
- 现有动作生成模型使用单一潜在向量，导致轨迹和关节旋转纠缠，影响生成质量。
- PRISM采用关节分解的潜在空间，每个关节独立编码，结合因果VAE和前向运动学监督，提升生成准确性。
- 通过噪声自由条件注入，统一文本到动作和姿态条件生成，支持流式合成，在多个数据集上达到先进性能。

## 摘要（原文）

> Text-to-motion generation has advanced rapidly, yet two challenges persist. First, existing motion autoencoders compress each frame into a single monolithic latent vector, entangling trajectory and per-joint rotations in an unstructured representation that downstream generators struggle to model faithfully. Second, text-to-motion, pose-conditioned generation, and long-horizon sequential synthesis typically require separate models or task-specific mechanisms, with autoregressive approaches suffering from severe error accumulation over extended rollouts.
>   We present PRISM, addressing each challenge with a dedicated contribution. (1) A joint-factorized motion latent space: each body joint occupies its own token, forming a structured 2D grid (time
>   joints) compressed by a causal VAE with forward-kinematics supervision. This simple change to the latent space -- without modifying the generator -- substantially improves generation quality, revealing that latent space design has been an underestimated bottleneck. (2) Noise-free condition injection: each latent token carries its own timestep embedding, allowing conditioning frames to be injected as clean tokens (timestep0) while the remaining tokens are denoised. This unifies text-to-motion and pose-conditioned generation in a single model, and directly enables autoregressive segment chaining for streaming synthesis. Self-forcing training further suppresses drift in long rollouts. With these two components, we train a single motion generation foundation model that seamlessly handles text-to-motion, pose-conditioned generation, autoregressive sequential generation, and narrative motion composition, achieving state-of-the-art on HumanML3D, MotionHub, BABEL, and a 50-scenario user study.

