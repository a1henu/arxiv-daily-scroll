---
layout: default
title: Automated Benchmark Generation from Domain Guidelines Informed by Bloom's Taxonomy
---

# Automated Benchmark Generation from Domain Guidelines Informed by Bloom's Taxonomy
**arXiv**：[2601.20253v1](https://arxiv.org/abs/2601.20253) · [PDF](https://arxiv.org/pdf/2601.20253.pdf)  
**作者**：Si Chen, Le Huy Khiem, Annalisa Szymanski, Ronald Metoyer, Ting Hua, Nitesh V. Chawla  

**一句话要点**：提出基于布鲁姆分类法的自动化基准生成框架，以解决实践领域开放问答评估的挑战。

**关键词**：自动化基准生成, 开放问答评估, 布鲁姆分类法, 实践领域, 多认知层次, 心理测量学

## 3 点简述
- 核心问题：实践领域开放问答评估缺乏基于专业指南的基准，依赖现有考试数据集不足。
- 方法要点：从专家指南自动生成基于违规场景的多选题和对话，覆盖四个认知层次。
- 实验或效果：应用于教学、营养学和护理领域，揭示LLM在高阶推理与低阶记忆上的非直观行为差异。

## 摘要（原文）

> Open-ended question answering (QA) evaluates a model's ability to perform contextualized reasoning beyond factual recall. This challenge is especially acute in practice-based domains, where knowledge is procedural and grounded in professional judgment, while most existing LLM benchmarks depend on pre-existing human exam datasets that are often unavailable in such settings. We introduce a framework for automated benchmark generation from expert-authored guidelines informed by Bloom's Taxonomy. It converts expert practices into implicit violation-based scenarios and expands them into auto-graded multiple-choice questions (MCQs) and multi-turn dialogues across four cognitive levels, enabling deterministic, reproducible, and scalable evaluation. Applied to three applied domains: teaching, dietetics, and caregiving, we find differences between model and human-like reasoning: LLMs sometimes perform relatively better on higher-order reasoning (Analyze) but fail more frequently on lower-level items (Remember). We produce large-scale, psychometrically informed benchmarks that surface these non-intuitive model behaviors and enable evaluation of contextualized reasoning in real-world settings.

