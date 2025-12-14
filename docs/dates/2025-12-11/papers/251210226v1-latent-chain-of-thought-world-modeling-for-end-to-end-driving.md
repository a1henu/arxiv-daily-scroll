---
layout: default
title: Latent Chain-of-Thought World Modeling for End-to-End Driving
---

# Latent Chain-of-Thought World Modeling for End-to-End Driving
**arXiv**：[2512.10226v1](https://arxiv.org/abs/2512.10226) · [PDF](https://arxiv.org/pdf/2512.10226.pdf)  
**作者**：Shuhan Tan, Kashyap Chitta, Yuxiao Chen, Ran Tian, Yurong You, Yan Wang, Wenjie Luo, Yulong Cao, Philipp Krahenbuhl, Marco Pavone, Boris Ivanovic  

**一句话要点**：提出Latent-CoT-Drive模型，通过潜在语言链式思维推理提升端到端驾驶性能

**关键词**：自动驾驶, 潜在语言推理, 端到端驾驶, 链式思维, 世界建模, 强化学习

## 3 点简述
- 核心问题：传统文本链式思维推理在自动驾驶中可能效率不足，影响决策质量。
- 方法要点：使用动作对齐潜在空间统一推理与决策，通过动作提议和世界模型令牌表达未来结果。
- 实验或效果：在大规模基准测试中实现更快推理、更好轨迹质量，强化学习后改进显著。

## 摘要（原文）

> Recent Vision-Language-Action (VLA) models for autonomous driving explore inference-time reasoning as a way to improve driving performance and safety in challenging scenarios. Most prior work uses natural language to express chain-of-thought (CoT) reasoning before producing driving actions. However, text may not be the most efficient representation for reasoning. In this work, we present Latent-CoT-Drive (LCDrive): a model that expresses CoT in a latent language that captures possible outcomes of the driving actions being considered. Our approach unifies CoT reasoning and decision making by representing both in an action-aligned latent space. Instead of natural language, the model reasons by interleaving (1) action-proposal tokens, which use the same vocabulary as the model's output actions; and (2) world model tokens, which are grounded in a learned latent world model and express future outcomes of these actions. We cold start latent CoT by supervising the model's action proposals and world model tokens based on ground-truth future rollouts of the scene. We then post-train with closed-loop reinforcement learning to strengthen reasoning capabilities. On a large-scale end-to-end driving benchmark, LCDrive achieves faster inference, better trajectory quality, and larger improvements from interactive reinforcement learning compared to both non-reasoning and text-reasoning baselines.

