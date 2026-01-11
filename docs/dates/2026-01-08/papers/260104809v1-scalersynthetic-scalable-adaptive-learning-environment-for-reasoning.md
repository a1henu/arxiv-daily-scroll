---
layout: default
title: SCALER:Synthetic Scalable Adaptive Learning Environment for Reasoning
---

# SCALER:Synthetic Scalable Adaptive Learning Environment for Reasoning
**arXiv**：[2601.04809v1](https://arxiv.org/abs/2601.04809) · [PDF](https://arxiv.org/pdf/2601.04809.pdf)  
**作者**：Caijun Xu, Changyi Xiao, Zhongyuan Peng, Xinrun Wang, Yixin Cao  

**一句话要点**：提出SCALER框架，通过自适应环境设计解决强化学习中训练信号失效问题，以提升大语言模型的推理能力。

**关键词**：强化学习, 自适应环境设计, 推理能力提升, 可扩展合成, 多环境策略, 编程问题转化

## 3 点简述
- 核心问题：强化学习训练信号在模型能力与任务难度不匹配或问题模式单一时会失效，阻碍推理能力提升。
- 方法要点：构建可扩展合成管道，将编程问题转化为可控难度环境，并采用自适应多环境策略动态调整难度和多样性。
- 实验或效果：在多种推理基准测试中优于基于数据集的强化学习基线，展现出更稳定和长期的训练动态。

## 摘要（原文）

> Reinforcement learning (RL) offers a principled way to enhance the reasoning capabilities of large language models, yet its effectiveness hinges on training signals that remain informative as models evolve. In practice, RL progress often slows when task difficulty becomes poorly aligned with model capability, or when training is dominated by a narrow set of recurring problem patterns. To jointly address these issues, we propose SCALER (Synthetic sCalable Adaptive Learning Environment for Reasoning), a framework that sustains effective learning signals through adaptive environment design. SCALER introduces a scalable synthesis pipeline that converts real-world programming problems into verifiable reasoning environments with controllable difficulty and unbounded instance generation, enabling RL training beyond finite datasets while preserving strong correctness guarantees. Building on this, SCALER further employs an adaptive multi-environment RL strategy that dynamically adjusts instance difficulty and curates the active set of environments to track the model's capability frontier and maintain distributional diversity. This co-adaptation prevents reward sparsity, mitigates overfitting to narrow task patterns, and supports sustained improvement throughout training. Extensive experiments show that SCALER consistently outperforms dataset-based RL baselines across diverse reasoning benchmarks and exhibits more stable, long-horizon training dynamics.

