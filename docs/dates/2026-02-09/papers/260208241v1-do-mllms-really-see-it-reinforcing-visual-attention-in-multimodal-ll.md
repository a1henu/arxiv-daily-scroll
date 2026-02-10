---
layout: default
title: Do MLLMs Really See It: Reinforcing Visual Attention in Multimodal LLMs
---

# Do MLLMs Really See It: Reinforcing Visual Attention in Multimodal LLMs
**arXiv**：[2602.08241v1](https://arxiv.org/abs/2602.08241) · [PDF](https://arxiv.org/pdf/2602.08241.pdf)  
**作者**：Siqu Ou, Tianrui Wan, Zhiyuan Zhao, Junyu Gao, Xuelong Li  

**一句话要点**：提出SAYO模型，通过强化学习奖励机制解决多模态大语言模型视觉注意力不稳定的问题。

**关键词**：多模态大语言模型, 视觉注意力, 强化学习, 推理任务, 区域级奖励

## 3 点简述
- 核心问题：现有MLLMs视觉注意力弱，早期视觉错位导致推理错误传播。
- 方法要点：引入基于区域级视觉注意力的强化学习奖励，优化视觉注意力策略。
- 实验或效果：在多个多模态基准测试中，SAYO显著提升推理和感知任务性能。

## 摘要（原文）

> While chain-of-thought (CoT) reasoning has substantially improved multimodal large language models (MLLMs) on complex reasoning tasks, existing approaches largely rely on long textual reasoning trajectories and provide limited mechanisms for learning stable visual attention policies. Our analysis shows that current MLLMs exhibit weak visual focus: early-stage visual misalignment is rarely corrected during subsequent reasoning, leading to error propagation and failed inferences. We argue that this limitation stems from inadequate credit assignment for visual attention during training. To address this issue, we propose SAYO, a visual reasoning model trained with a reinforcement learning (RL) framework that introduces a region-level visual attention-based reward. This reward explicitly aligns optimization signals with visually grounded reasoning steps, enabling the model to learn more reliable attention behaviors. Extensive experiments across multiple multimodal benchmarks demonstrate that SAYO consistently improves performance on diverse reasoning and perception tasks.

