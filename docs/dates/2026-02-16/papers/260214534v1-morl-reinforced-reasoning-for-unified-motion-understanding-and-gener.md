---
layout: default
title: MoRL: Reinforced Reasoning for Unified Motion Understanding and Generation
---

# MoRL: Reinforced Reasoning for Unified Motion Understanding and Generation
**arXiv**：[2602.14534v1](https://arxiv.org/abs/2602.14534) · [PDF](https://arxiv.org/pdf/2602.14534.pdf)  
**作者**：Hongpeng Wang, Zeyu Zhang, Wenhao Li, Hao Tang  

**一句话要点**：提出MoRL模型，通过强化学习与推理链增强运动理解与生成的统一能力。

**关键词**：运动理解, 运动生成, 强化学习, 推理链, 多模态模型, 数据集构建

## 3 点简述
- 核心问题：现有运动理解与生成模型在推理能力和测试时规划方面受限。
- 方法要点：结合监督微调与强化学习，设计任务特定奖励，并引入Chain-of-Motion推理方法。
- 实验或效果：在HumanML3D和KIT-ML数据集上超越先进基线，提升逻辑推理和感知真实性。

## 摘要（原文）

> Human motion understanding and generation are crucial for vision and robotics but remain limited in reasoning capability and test-time planning. We propose MoRL, a unified multimodal motion model trained with supervised fine-tuning and reinforcement learning with verifiable rewards. Our task-specific reward design combines semantic alignment and reasoning coherence for understanding with physical plausibility and text-motion consistency for generation, improving both logical reasoning and perceptual realism. To further enhance inference, we introduce Chain-of-Motion (CoM), a test-time reasoning method that enables step-by-step planning and reflection. We also construct two large-scale CoT datasets, MoUnd-CoT-140K and MoGen-CoT-140K, to align motion sequences with reasoning traces and action descriptions. Experiments on HumanML3D and KIT-ML show that MoRL achieves significant gains over state-of-the-art baselines. Code: https://github.com/AIGeeksGroup/MoRL. Website: https://aigeeksgroup.github.io/MoRL.

