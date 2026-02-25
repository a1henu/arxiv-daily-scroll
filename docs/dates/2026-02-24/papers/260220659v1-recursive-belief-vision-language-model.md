---
layout: default
title: Recursive Belief Vision Language Model
---

# Recursive Belief Vision Language Model
**arXiv**：[2602.20659v1](https://arxiv.org/abs/2602.20659) · [PDF](https://arxiv.org/pdf/2602.20659.pdf)  
**作者**：Vaidehi Bagaria, Bijo Sebastian, Nirav Patel  

**一句话要点**：提出RB-VLA模型，通过信念状态表示解决部分可观测下的长时程视觉语言动作任务

**关键词**：视觉语言动作模型, 部分可观测性, 信念状态表示, 长时程操作, 自监督学习, 扩散策略

## 3 点简述
- 当前视觉语言动作模型在部分可观测下处理长时程操作时，因缺乏持久状态表示而性能受限
- RB-VLA采用信念中心架构，结合自监督世界模型目标，维护紧凑潜在状态以编码任务历史与动态
- 实验显示RB-VLA在长时程基准上优于先前模型，提升成功率并降低推理延迟，信念模块是关键驱动因素

## 摘要（原文）

> Current vision-language-action (VLA) models struggle with long-horizon manipulation under partial observability. Most existing approaches remain observation-driven, relying on short context windows or repeated queries to vision-language models (VLMs). This leads to loss of task progress, action repetition under perceptual aliasing, and high inference latency. Semantic reasoning alone is not the primary bottleneck in long-horizon manipulation. Instead, VLAs lack persistent, action-conditioned state representations and exhibit limited temporal and physical reasoning, making them ill-suited for multi-stage control. This paper introduces RB-VLA, a belief-centric architecture trained with self-supervised world-model objectives that maintains a compact latent state encoding task-relevant history, dynamics, and object interactions. Queried once for high-level intent, the VLM provides task specification, while the belief tracks task progress and enables phase-aware, causally grounded control under partial observability without storing raw observations or scaling memory with time. The belief and intent jointly condition a diffusion policy for robust closed-loop execution. RB-VLA outperforms prior VLAs on long-horizon benchmarks, achieving 52.5% and 37.5% higher success on multi-stage pick-and-place and stacking tasks, respectively, compared to π0. It also reduces inference latency by up to 5x relative to baselines and eliminates memory growth across timesteps observed in existing VLAs. Ablations show that the belief module is the primary driver of performance, increasing success rates from 32.5% to 77.5%. These results demonstrate the effectiveness of belief-based state representations for long-horizon VLA policies.

