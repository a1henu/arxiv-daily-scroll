---
layout: default
title: AdaReasoner: Dynamic Tool Orchestration for Iterative Visual Reasoning
---

# AdaReasoner: Dynamic Tool Orchestration for Iterative Visual Reasoning
**arXiv**：[2601.18631v1](https://arxiv.org/abs/2601.18631) · [PDF](https://arxiv.org/pdf/2601.18631.pdf)  
**作者**：Mingyang Song, Haoyu Sun, Jiawei Gu, Linjie Li, Luxin Xu, Ranjay Krishna, Yu Cheng  

**一句话要点**：提出AdaReasoner，通过动态工具编排解决多模态大语言模型在迭代视觉推理中的工具使用问题。

**关键词**：多模态大语言模型, 视觉推理, 工具编排, 强化学习, 自适应学习, 泛化能力

## 3 点简述
- 核心问题：多模态大语言模型在视觉推理中需有效选择、调用和组合工具，面临新工具或新任务的挑战。
- 方法要点：结合可扩展数据管道、Tool-GRPO强化学习算法和自适应学习机制，学习工具使用作为通用推理技能。
- 实验或效果：在多个基准测试中实现最先进性能，提升7B基础模型平均24.9%，超越GPT-5等系统。

## 摘要（原文）

> When humans face problems beyond their immediate capabilities, they rely on tools, providing a promising paradigm for improving visual reasoning in multimodal large language models (MLLMs). Effective reasoning, therefore, hinges on knowing which tools to use, when to invoke them, and how to compose them over multiple steps, even when faced with new tools or new tasks. We introduce \textbf{AdaReasoner}, a family of multimodal models that learn tool use as a general reasoning skill rather than as tool-specific or explicitly supervised behavior. AdaReasoner is enabled by (i) a scalable data curation pipeline exposing models to long-horizon, multi-step tool interactions; (ii) Tool-GRPO, a reinforcement learning algorithm that optimizes tool selection and sequencing based on end-task success; and (iii) an adaptive learning mechanism that dynamically regulates tool usage. Together, these components allow models to infer tool utility from task context and intermediate outcomes, enabling coordination of multiple tools and generalization to unseen tools. Empirically, AdaReasoner exhibits strong tool-adaptive and generalization behaviors: it autonomously adopts beneficial tools, suppresses irrelevant ones, and adjusts tool usage frequency based on task demands, despite never being explicitly trained to do so. These capabilities translate into state-of-the-art performance across challenging benchmarks, improving the 7B base model by +24.9\% on average and surpassing strong proprietary systems such as GPT-5 on multiple tasks, including VSP and Jigsaw.

