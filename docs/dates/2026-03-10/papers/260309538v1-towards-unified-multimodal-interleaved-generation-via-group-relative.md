---
layout: default
title: Towards Unified Multimodal Interleaved Generation via Group Relative Policy Optimization
---

# Towards Unified Multimodal Interleaved Generation via Group Relative Policy Optimization
**arXiv**：[2603.09538v1](https://arxiv.org/abs/2603.09538) · [PDF](https://arxiv.org/pdf/2603.09538.pdf)  
**作者**：Ming Nie, Chunwei Wang, Jianhua Han, Hang Xu, Li Zhang  

**一句话要点**：提出基于强化学习的后训练策略，以增强统一视觉语言模型的多模态交错生成能力

**关键词**：多模态交错生成, 强化学习, 统一视觉语言模型, 后训练策略, 混合奖励

## 3 点简述
- 核心问题：统一视觉语言模型在多模态交错生成（如视觉叙事）方面能力不足
- 方法要点：使用混合数据集预热，并扩展GRPO框架进行统一策略优化，结合混合奖励
- 实验或效果：在MMIE和InterleavedBench上显著提升生成质量和连贯性

## 摘要（原文）

> Unified vision-language models have made significant progress in multimodal understanding and generation, yet they largely fall short in producing multimodal interleaved outputs, which is a crucial capability for tasks like visual storytelling and step-by-step visual reasoning. In this work, we propose a reinforcement learning-based post-training strategy to unlock this capability in existing unified models, without relying on large-scale multimodal interleaved datasets. We begin with a warm-up stage using a hybrid dataset comprising curated interleaved sequences and limited data for multimodal understanding and text-to-image generation, which exposes the model to interleaved generation patterns while preserving its pretrained capabilities. To further refine interleaved generation, we propose a unified policy optimization framework that extends Group Relative Policy Optimization (GRPO) to the multimodal setting. Our approach jointly models text and image generation within a single decoding trajectory and optimizes it with our novel hybrid rewards covering textual relevance, visual-text alignment, and structural fidelity. Additionally, we incorporate process-level rewards to provide step-wise guidance, enhancing training efficiency in complex multimodal tasks. Experiments on MMIE and InterleavedBench demonstrate that our approach significantly enhances the quality and coherence of multimodal interleaved generation.

