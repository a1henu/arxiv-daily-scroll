---
layout: default
title: From Narrow to Panoramic Vision: Attention-Guided Cold-Start Reshapes Multimodal Reasoning
---

# From Narrow to Panoramic Vision: Attention-Guided Cold-Start Reshapes Multimodal Reasoning
**arXiv**：[2603.03825v1](https://arxiv.org/abs/2603.03825) · [PDF](https://arxiv.org/pdf/2603.03825.pdf)  
**作者**：Ruilin Luo, Chufan Shi, Yizhen Zhang, Cheng Yang, Songtao Jiang, Tongkun Guan, Ruizhe Chen, Ruihang Chu, Peng Wang, Mingkun Yang, Yujiu Yang, Junyang Lin, Zhibo Yang  

**一句话要点**：提出注意力引导的视觉锚定与反思框架以提升多模态大推理模型的冷启动性能

**关键词**：多模态推理, 冷启动初始化, 注意力机制, 视觉锚定, 训练干预, 基准测试

## 3 点简述
- 核心问题：多模态冷启动阶段未能有效提升模型对视觉信息的注意力，导致推理性能受限。
- 方法要点：引入视觉注意力分数量化注意力，设计训练免费干预和AVAR框架整合数据合成与奖励塑造。
- 实验或效果：在Qwen2.5-VL-7B上实现平均7.0%的性能提升，验证了注意力机制的关键作用。

## 摘要（原文）

> The cold-start initialization stage plays a pivotal role in training Multimodal Large Reasoning Models (MLRMs), yet its mechanisms remain insufficiently understood. To analyze this stage, we introduce the Visual Attention Score (VAS), an attention-based metric that quantifies how much a model attends to visual tokens. We find that reasoning performance is strongly correlated with VAS (r=0.9616): models with higher VAS achieve substantially stronger multimodal reasoning. Surprisingly, multimodal cold-start fails to elevate VAS, resulting in attention distributions close to the base model, whereas text-only cold-start leads to a clear increase. We term this counter-intuitive phenomenon Lazy Attention Localization. To validate its causal role, we design training-free interventions that directly modulate attention allocation during inference, performance gains of 1$-$2% without any retraining. Building on these insights, we further propose Attention-Guided Visual Anchoring and Reflection (AVAR), a comprehensive cold-start framework that integrates visual-anchored data synthesis, attention-guided objectives, and visual-anchored reward shaping. Applied to Qwen2.5-VL-7B, AVAR achieves an average gain of 7.0% across 7 multimodal reasoning benchmarks. Ablation studies further confirm that each component of AVAR contributes step-wise to the overall gains. The code, data, and models are available at https://github.com/lrlbbzl/Qwen-AVAR.

