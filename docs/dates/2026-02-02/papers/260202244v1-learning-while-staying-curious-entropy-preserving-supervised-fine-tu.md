---
layout: default
title: Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models
---

# Learning While Staying Curious: Entropy-Preserving Supervised Fine-Tuning via Adaptive Self-Distillation for Large Reasoning Models
**arXiv**：[2602.02244v1](https://arxiv.org/abs/2602.02244) · [PDF](https://arxiv.org/pdf/2602.02244.pdf)  
**作者**：Hao Wang, Hao Gu, Hongming Piao, Kaixiong Gong, Yuxiao Ye, Xiangyu Yue, Sirui Han, Yike Guo, Dapeng Wu  

**一句话要点**：提出CurioSFT方法，通过自适应自蒸馏在监督微调中保持熵以增强大推理模型的探索能力。

**关键词**：大推理模型, 监督微调, 熵保持, 自适应蒸馏, 探索能力, 数学推理

## 3 点简述
- 标准SFT-then-RL流程中，SFT导致过自信和多样性降低，限制RL探索空间。
- CurioSFT包含自探索蒸馏和熵引导温度选择，以内在好奇心促进探索并缓解知识遗忘。
- 在数学推理任务上，CurioSFT优于基线SFT，并在RL阶段带来平均5.0分的提升。

## 摘要（原文）

> The standard post-training recipe for large reasoning models, supervised fine-tuning followed by reinforcement learning (SFT-then-RL), may limit the benefits of the RL stage: while SFT imitates expert demonstrations, it often causes overconfidence and reduces generation diversity, leaving RL with a narrowed solution space to explore. Adding entropy regularization during SFT is not a cure-all; it tends to flatten token distributions toward uniformity, increasing entropy without improving meaningful exploration capability. In this paper, we propose CurioSFT, an entropy-preserving SFT method designed to enhance exploration capabilities through intrinsic curiosity. It consists of (a) Self-Exploratory Distillation, which distills the model toward a self-generated, temperature-scaled teacher to encourage exploration within its capability; and (b) Entropy-Guided Temperature Selection, which adaptively adjusts distillation strength to mitigate knowledge forgetting by amplifying exploration at reasoning tokens while stabilizing factual tokens. Extensive experiments on mathematical reasoning tasks demonstrate that, in SFT stage, CurioSFT outperforms the vanilla SFT by 2.5 points on in-distribution tasks and 2.9 points on out-of-distribution tasks. We also verify that exploration capabilities preserved during SFT successfully translate into concrete gains in RL stage, yielding an average improvement of 5.0 points.

