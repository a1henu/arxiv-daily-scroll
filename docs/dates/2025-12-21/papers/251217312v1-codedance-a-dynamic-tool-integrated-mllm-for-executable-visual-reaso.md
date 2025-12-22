---
layout: default
title: CodeDance: A Dynamic Tool-integrated MLLM for Executable Visual Reasoning
---

# CodeDance: A Dynamic Tool-integrated MLLM for Executable Visual Reasoning
**arXiv**：[2512.17312v1](https://arxiv.org/abs/2512.17312) · [PDF](https://arxiv.org/pdf/2512.17312.pdf)  
**作者**：Qi Song, Honglin Li, Yingchen Yu, Haoyi Zhou, Lin Yang, Song Bai, Qi She, Zilong Huang, Yunqing Zhao  

**一句话要点**：提出CodeDance，一种基于可执行代码的动态工具集成MLLM，用于增强视觉推理的灵活性和可解释性。

**关键词**：可执行视觉推理, 多模态大语言模型, 工具集成, 代码生成, 强化学习训练, 跨任务迁移

## 3 点简述
- 核心问题：现有开源方法依赖文本链、固定视觉模式或单步流程，限制了复杂任务中的灵活性、可解释性和可迁移性。
- 方法要点：通过定义、组合和执行代码来协调多个工具，计算中间结果并渲染视觉元素，支持透明、可自检的推理。
- 实验或效果：在视觉搜索、数学和图表问答等基准测试中，CodeDance优于模式驱动和纯文本基线，并超越GPT-4o等先进模型。

## 摘要（原文）

> Recent releases such as o3 highlight human-like "thinking with images" reasoning that combines structured tool use with stepwise verification, yet most open-source approaches still rely on text-only chains, rigid visual schemas, or single-step pipelines, limiting flexibility, interpretability, and transferability on complex tasks. We introduce CodeDance, which explores executable code as a general solver for visual reasoning. Unlike fixed-schema calls (e.g., only predicting bounding-box coordinates), CodeDance defines, composes, and executes code to orchestrate multiple tools, compute intermediate results, and render visual artifacts (e.g., boxes, lines, plots) that support transparent, self-checkable reasoning. To guide this process, we introduce a reward for balanced and adaptive tool-call, which balances exploration with efficiency and mitigates tool overuse. Interestingly, beyond the expected capabilities taught by atomic supervision, we empirically observe novel emergent behaviors during RL training: CodeDance demonstrates novel tool invocations, unseen compositions, and cross-task transfer. These behaviors arise without task-specific fine-tuning, suggesting a general and scalable mechanism of executable visual reasoning. Extensive experiments across reasoning benchmarks (e.g., visual search, math, chart QA) show that CodeDance not only consistently outperforms schema-driven and text-only baselines, but also surpasses advanced closed models such as GPT-4o and larger open-source models.

