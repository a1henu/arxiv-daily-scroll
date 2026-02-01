---
layout: default
title: RSGround-R1: Rethinking Remote Sensing Visual Grounding through Spatial Reasoning
---

# RSGround-R1: Rethinking Remote Sensing Visual Grounding through Spatial Reasoning
**arXiv**：[2601.21634v1](https://arxiv.org/abs/2601.21634) · [PDF](https://arxiv.org/pdf/2601.21634.pdf)  
**作者**：Shiqi Huang, Shuting He, Bihan Wen  

**一句话要点**：提出RSGround-R1框架，通过空间推理增强遥感视觉定位能力

**关键词**：遥感视觉定位, 空间推理, 多模态大语言模型, 链式思维微调, 强化学习, 位置感知奖励

## 3 点简述
- 核心问题：遥感场景空间尺度大、语义模糊，描述依赖位置线索，挑战多模态大语言模型的空间推理。
- 方法要点：采用推理引导、位置感知的后训练框架，包括链式思维监督微调和强化微调，引入位置奖励和空间一致性优化。
- 实验或效果：在遥感视觉定位基准测试中展示优越性能和泛化能力。

## 摘要（原文）

> Remote Sensing Visual Grounding (RSVG) aims to localize target objects in large-scale aerial imagery based on natural language descriptions. Owing to the vast spatial scale and high semantic ambiguity of remote sensing scenes, these descriptions often rely heavily on positional cues, posing unique challenges for Multimodal Large Language Models (MLLMs) in spatial reasoning. To leverage this unique feature, we propose a reasoning-guided, position-aware post-training framework, dubbed \textbf{RSGround-R1}, to progressively enhance spatial understanding. Specifically, we first introduce Chain-of-Thought Supervised Fine-Tuning (CoT-SFT) using synthetically generated RSVG reasoning data to establish explicit position awareness. Reinforcement Fine-Tuning (RFT) is then applied, augmented by our newly designed positional reward that provides continuous and distance-aware guidance toward accurate localization. Moreover, to mitigate incoherent localization behaviors across rollouts, we introduce a spatial consistency guided optimization scheme that dynamically adjusts policy updates based on their spatial coherence, ensuring stable and robust convergence. Extensive experiments on RSVG benchmarks demonstrate superior performance and generalization of our model.

