---
layout: default
title: Crab$^{+}$: A Scalable and Unified Audio-Visual Scene Understanding Model with Explicit Cooperation
---

# Crab$^{+}$: A Scalable and Unified Audio-Visual Scene Understanding Model with Explicit Cooperation
**arXiv**：[2603.04128v1](https://arxiv.org/abs/2603.04128) · [PDF](https://arxiv.org/pdf/2603.04128.pdf)  
**作者**：Dongnuan Cai, Henghui Du, Chang Zhou, Xi Chen, Dan Guo, Hongyuan Zhang, Xuelong Li, Di Hu  

**一句话要点**：提出Crab⁺模型，通过显式合作解决音频-视觉任务异质性，实现可扩展的统一场景理解。

**关键词**：音频-视觉大语言模型, 多任务统一, 负迁移缓解, 指令调优, 动态路由, 场景理解

## 3 点简述
- 核心问题：传统多任务统一方法存在严重负迁移，约55%任务性能下降，归因于音频-视觉任务异质性。
- 方法要点：引入AV-UIE v2数据集和Interaction-aware LoRA，从数据和模型角度显式建模跨任务关系以协调交互模式。
- 实验或效果：在近88%任务中实现正迁移，超越单任务基线，并在多个基准上优于专用模型。

## 摘要（原文）

> Developing Audio-Visual Large Language Models (AV-LLMs) for unified scene understanding is pivotal in multimodal intelligence. While instruction tuning enables pre-trained models with multi-task abilities, we observe that conventional multi-task unification methods often suffer from severe negative transfer, where nearly 55% of tasks degrade compared to single-task training. We attribute this phenomenon to audio-visual task heterogeneity, characterized by disparate task granularity and divergent capability demands, which lead to negative interference under joint training. To tackle this, we present Crab$^{+}$, a scalable and unified audio-visual scene understanding model that addresses task heterogeneity through explicit cooperation from both data and model perspectives. On the data side, we introduce AV-UIE v2, a comprehensive Audio-Visual Unified Instruction-tuning dataset with Explicit reasoning processes. It contains approximately 222K samples spanning 17 datasets and 7 tasks, enabling the model to capture cross-task relationships at different levels of granularity. On the model side, we design a unified interface to align heterogeneous task formulations, and propose Interaction-aware LoRA (I-LoRA), which explicitly models inter-task relationships via dynamic routing to coordinate distinct audio-visual interaction patterns, mitigating parameter interference. Extensive experiments show Crab$^{+}$ covers broader tasks than existing unified models while outperforming specialized models on various benchmarks. We successfully reverse the negative transfer trend, achieving positive transfer where multi-task learning surpasses single-task baselines in nearly 88% of tasks. These results hold across diverse AV-LLM paradigms and are validated through in-depth visualization, positioning Crab$^{+}$ as a robust step towards holistic audio-visual scene understanding.

