---
layout: default
title: Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments
---

# Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for Vision-Language Navigation in Continuous Environments
**arXiv**：[2603.09740v1](https://arxiv.org/abs/2603.09740) · [PDF](https://arxiv.org/pdf/2603.09740.pdf)  
**作者**：Haoyuan Li, Rui Liu, Hehe Fan, Yi Yang  

**一句话要点**：提出步感知对比对齐框架以解决连续环境中视觉语言导航的训练挑战

**关键词**：视觉语言导航, 连续环境, 步感知对比对齐, 密集监督, 训练稳定性, 多模态大语言模型

## 3 点简述
- 核心问题：现有方法在泛化能力、错误恢复和训练稳定性间难以平衡，如SFT导致复合错误，RFT因稀疏奖励而梯度信号崩溃。
- 方法要点：通过感知基础的步感知审计器评估轨迹进展，动态路由批次至专门的重采样和优化策略，提取密集监督。
- 实验或效果：在VLN-CE基准测试中实现最先进性能，验证了框架的有效性。

## 摘要（原文）

> Vision-Language Navigation in Continuous Environments (VLN-CE) requires agents to learn complex reasoning from long-horizon human interactions. While Multi-modal Large Language Models (MLLMs) have driven recent progress, current training paradigms struggle to balance generalization capability, error recovery and training stability. Specifically, (i) policies derived from SFT suffer from compounding errors, struggling to recover from out-of-distribution states, and (ii) Reinforcement Fine-Tuning (RFT) methods e.g. GRPO are bottlenecked by sparse outcome rewards. Their binary feedback fails to assign credit to individual steps, leading to gradient signal collapse in failure dominant batches. To address these challenges, we introduce Step-Aware Contrastive Alignment (SACA), a framework designed to extract dense supervision from imperfect trajectories. At its core, the Perception-Grounded Step-Aware auditor evaluates progress step-by-step, disentangling failed trajectories into valid prefixes and exact divergence points. Leveraging these signals, Scenario-Conditioned Group Construction mechanism dynamically routes batches to specialized resampling and optimization strategies. Extensive experiments on VLN-CE benchmarks demonstrate that SACA achieves state-of-the-art performance.

