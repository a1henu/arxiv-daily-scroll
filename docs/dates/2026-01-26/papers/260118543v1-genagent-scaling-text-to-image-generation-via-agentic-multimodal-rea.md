---
layout: default
title: GenAgent: Scaling Text-to-Image Generation via Agentic Multimodal Reasoning
---

# GenAgent: Scaling Text-to-Image Generation via Agentic Multimodal Reasoning
**arXiv**：[2601.18543v1](https://arxiv.org/abs/2601.18543) · [PDF](https://arxiv.org/pdf/2601.18543.pdf)  
**作者**：Kaixun Jiang, Yuzheng Wang, Junjie Zhou, Pandeng Li, Zhihang Liu, Chen-Wei Xie, Zhaoyu Chen, Yun Zheng, Wenqiang Zhang  

**一句话要点**：提出GenAgent，通过智能体多模态推理扩展文生图生成能力

**关键词**：文生图生成, 智能体框架, 多模态推理, 强化学习, 工具调用, 迭代优化

## 3 点简述
- 核心问题：统一模型训练成本高且面临理解与生成权衡，现有模块化系统受限于静态流程。
- 方法要点：采用智能体框架解耦理解与生成，通过多轮交互和链式思维迭代优化输出。
- 实验或效果：在GenEval++和WISE基准上显著提升基础生成器性能，并展示跨工具泛化等关键特性。

## 摘要（原文）

> We introduce GenAgent, unifying visual understanding and generation through an agentic multimodal model. Unlike unified models that face expensive training costs and understanding-generation trade-offs, GenAgent decouples these capabilities through an agentic framework: understanding is handled by the multimodal model itself, while generation is achieved by treating image generation models as invokable tools. Crucially, unlike existing modular systems constrained by static pipelines, this design enables autonomous multi-turn interactions where the agent generates multimodal chains-of-thought encompassing reasoning, tool invocation, judgment, and reflection to iteratively refine outputs. We employ a two-stage training strategy: first, cold-start with supervised fine-tuning on high-quality tool invocation and reflection data to bootstrap agent behaviors; second, end-to-end agentic reinforcement learning combining pointwise rewards (final image quality) and pairwise rewards (reflection accuracy), with trajectory resampling for enhanced multi-turn exploration. GenAgent significantly boosts base generator(FLUX.1-dev) performance on GenEval++ (+23.6\%) and WISE (+14\%). Beyond performance gains, our framework demonstrates three key properties: 1) cross-tool generalization to generators with varying capabilities, 2) test-time scaling with consistent improvements across interaction rounds, and 3) task-adaptive reasoning that automatically adjusts to different tasks. Our code will be available at \href{https://github.com/deep-kaixun/GenAgent}{this url}.

