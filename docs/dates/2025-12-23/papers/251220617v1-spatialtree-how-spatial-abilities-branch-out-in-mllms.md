---
layout: default
title: SpatialTree: How Spatial Abilities Branch Out in MLLMs
---

# SpatialTree: How Spatial Abilities Branch Out in MLLMs
**arXiv**：[2512.20617v1](https://arxiv.org/abs/2512.20617) · [PDF](https://arxiv.org/pdf/2512.20617.pdf)  
**作者**：Yuxi Xiao, Longfei Li, Shen Yan, Xinhang Liu, Sida Peng, Yunchao Wei, Xiaowei Zhou, Bingyi Kang  

**一句话要点**：提出SpatialTree层次框架以系统评估和提升多模态大语言模型的空间能力

**关键词**：空间能力层次, 多模态大语言模型评估, 认知科学启发, 能力基准构建, 跨层转移学习, 自动思考策略

## 3 点简述
- 核心问题：多模态大语言模型的空间能力层次结构不明确，现有研究任务范围狭窄。
- 方法要点：基于认知科学构建四层空间能力分类，并创建首个能力中心化层次基准进行评估。
- 实验或效果：发现低层能力正交、高层能力相关，通过微调和自动思考策略实现跨层转移和整体提升。

## 摘要（原文）

> Cognitive science suggests that spatial ability develops progressively-from perception to reasoning and interaction. Yet in multimodal LLMs (MLLMs), this hierarchy remains poorly understood, as most studies focus on a narrow set of tasks. We introduce SpatialTree, a cognitive-science-inspired hierarchy that organizes spatial abilities into four levels: low-level perception (L1), mental mapping (L2), simulation (L3), and agentic competence (L4). Based on this taxonomy, we construct the first capability-centric hierarchical benchmark, thoroughly evaluating mainstream MLLMs across 27 sub-abilities. The evaluation results reveal a clear structure: L1 skills are largely orthogonal, whereas higher-level skills are strongly correlated, indicating increasing interdependency. Through targeted supervised fine-tuning, we uncover a surprising transfer dynamic-negative transfer within L1, but strong cross-level transfer from low- to high-level abilities with notable synergy. Finally, we explore how to improve the entire hierarchy. We find that naive RL that encourages extensive "thinking" is unreliable: it helps complex reasoning but hurts intuitive perception. We propose a simple auto-think strategy that suppresses unnecessary deliberation, enabling RL to consistently improve performance across all levels. By building SpatialTree, we provide a proof-of-concept framework for understanding and systematically scaling spatial abilities in MLLMs.

