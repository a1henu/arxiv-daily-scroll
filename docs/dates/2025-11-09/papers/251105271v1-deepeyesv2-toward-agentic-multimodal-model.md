---
layout: default
title: DeepEyesV2: Toward Agentic Multimodal Model
---

# DeepEyesV2: Toward Agentic Multimodal Model
**arXiv**：[2511.05271v1](https://arxiv.org/abs/2511.05271) · [PDF](https://arxiv.org/pdf/2511.05271.pdf)  
**作者**：Jack Hong, Chenxiao Zhao, ChengLin Zhu, Weiheng Lu, Guohai Xu, Xing Yu  

**一句话要点**：提出DeepEyesV2以构建代理式多模态模型，通过两阶段训练优化工具调用。

**关键词**：代理式多模态模型, 工具调用训练, 两阶段训练, 多模态基准评估, 强化学习优化

## 3 点简述
- 核心问题：代理式多模态模型需主动调用外部工具并整合到推理中，但直接强化学习难以诱导稳健工具使用行为。
- 方法要点：采用两阶段训练流程，包括冷启动阶段建立工具使用模式和强化学习阶段精炼工具调用。
- 实验或效果：在RealX-Bench等基准测试中，模型在真实世界理解、数学推理和搜索密集型任务中表现有效。

## 摘要（原文）

> Agentic multimodal models should not only comprehend text and images, but
> also actively invoke external tools, such as code execution environments and
> web search, and integrate these operations into reasoning. In this work, we
> introduce DeepEyesV2 and explore how to build an agentic multimodal model from
> the perspectives of data construction, training methods, and model evaluation.
> We observe that direct reinforcement learning alone fails to induce robust
> tool-use behavior. This phenomenon motivates a two-stage training pipeline: a
> cold-start stage to establish tool-use patterns, and reinforcement learning
> stage to further refine tool invocation. We curate a diverse, moderately
> challenging training dataset, specifically including examples where tool use is
> beneficial. We further introduce RealX-Bench, a comprehensive benchmark
> designed to evaluate real-world multimodal reasoning, which inherently requires
> the integration of multiple capabilities, including perception, search, and
> reasoning. We evaluate DeepEyesV2 on RealX-Bench and other representative
> benchmarks, demonstrating its effectiveness across real-world understanding,
> mathematical reasoning, and search-intensive tasks. Moreover, DeepEyesV2
> exhibits task-adaptive tool invocation, tending to use image operations for
> perception tasks and numerical computations for reasoning tasks. Reinforcement
> learning further enables complex tool combinations and allows model to
> selectively invoke tools based on context. We hope our study can provide
> guidance for community in developing agentic multimodal models.

