---
layout: default
title: KnowMe-Bench: Benchmarking Person Understanding for Lifelong Digital Companions
---

# KnowMe-Bench: Benchmarking Person Understanding for Lifelong Digital Companions
**arXiv**：[2601.04745v1](https://arxiv.org/abs/2601.04745) · [PDF](https://arxiv.org/pdf/2601.04745.pdf)  
**作者**：Tingyu Wu, Zhisheng Chen, Ziyan Weng, Shuhe Wang, Chenglong Li, Shuo Zhang, Sen Hu, Silin Wu, Qizhen Lan, Huacan Wang, Ronghao Chen  

**一句话要点**：提出KnowMe-Bench基准，基于自传叙事评估终身数字伴侣的人物理解能力。

**关键词**：人物理解基准, 长期记忆评估, 自传叙事分析, 检索增强系统, 高级推理任务

## 3 点简述
- 核心问题：现有长期记忆基准依赖多轮对话或合成历史，检索性能不能准确反映人物理解。
- 方法要点：构建公开基准，使用长篇自传叙事，通过行动、上下文和内心思想推断稳定动机和决策原则。
- 实验或效果：评估显示检索增强系统主要提升事实准确性，但在时间解释和高级推理上仍有错误。

## 摘要（原文）

> Existing long-horizon memory benchmarks mostly use multi-turn dialogues or synthetic user histories, which makes retrieval performance an imperfect proxy for person understanding. We present \BenchName, a publicly releasable benchmark built from long-form autobiographical narratives, where actions, context, and inner thoughts provide dense evidence for inferring stable motivations and decision principles. \BenchName~reconstructs each narrative into a flashback-aware, time-anchored stream and evaluates models with evidence-linked questions spanning factual recall, subjective state attribution, and principle-level reasoning. Across diverse narrative sources, retrieval-augmented systems mainly improve factual accuracy, while errors persist on temporally grounded explanations and higher-level inferences, highlighting the need for memory mechanisms beyond retrieval. Our data is in \href{KnowMeBench}{https://github.com/QuantaAlpha/KnowMeBench}.

