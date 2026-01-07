---
layout: default
title: Unified Thinker: A General Reasoning Modular Core for Image Generation
---

# Unified Thinker: A General Reasoning Modular Core for Image Generation
**arXiv**：[2601.03127v1](https://arxiv.org/abs/2601.03127) · [PDF](https://arxiv.org/pdf/2601.03127.pdf)  
**作者**：Sashuai Zhou, Qiang Zhou, Jijin Hu, Hanqing Yang, Yue Cao, Junpeng Ma, Yinchao Ma, Jun Song, Tiezheng Ge, Cheng Yu, Bo Zheng, Zhou Zhao  

**一句话要点**：提出Unified Thinker作为通用图像生成的模块化推理核心，以解决逻辑密集型指令遵循中的推理-执行差距。

**关键词**：图像生成, 推理模块, 模块化架构, 强化学习, 文本到图像, 图像编辑

## 3 点简述
- 核心问题：生成模型在逻辑密集型指令遵循中存在推理-执行差距，开源模型落后于闭源系统。
- 方法要点：设计任务无关的推理架构，解耦推理模块与生成器，采用两阶段训练范式强化视觉正确性。
- 实验或效果：在文本到图像生成和图像编辑任务中显著提升图像推理和生成质量。

## 摘要（原文）

> Despite impressive progress in high-fidelity image synthesis, generative models still struggle with logic-intensive instruction following, exposing a persistent reasoning--execution gap. Meanwhile, closed-source systems (e.g., Nano Banana) have demonstrated strong reasoning-driven image generation, highlighting a substantial gap to current open-source models. We argue that closing this gap requires not merely better visual generators, but executable reasoning: decomposing high-level intents into grounded, verifiable plans that directly steer the generative process. To this end, we propose Unified Thinker, a task-agnostic reasoning architecture for general image generation, designed as a unified planning core that can plug into diverse generators and workflows. Unified Thinker decouples a dedicated Thinker from the image Generator, enabling modular upgrades of reasoning without retraining the entire generative model. We further introduce a two-stage training paradigm: we first build a structured planning interface for the Thinker, then apply reinforcement learning to ground its policy in pixel-level feedback, encouraging plans that optimize visual correctness over textual plausibility. Extensive experiments on text-to-image generation and image editing show that Unified Thinker substantially improves image reasoning and generation quality.

