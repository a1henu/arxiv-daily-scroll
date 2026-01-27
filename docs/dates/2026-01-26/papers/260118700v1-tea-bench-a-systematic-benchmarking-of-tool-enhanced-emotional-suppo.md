---
layout: default
title: TEA-Bench: A Systematic Benchmarking of Tool-enhanced Emotional Support Dialogue Agent
---

# TEA-Bench: A Systematic Benchmarking of Tool-enhanced Emotional Support Dialogue Agent
**arXiv**：[2601.18700v1](https://arxiv.org/abs/2601.18700) · [PDF](https://arxiv.org/pdf/2601.18700.pdf)  
**作者**：Xingyu Sui, Yanyan Zhao, Yulin Hu, Jiahe Guo, Weixiang Zhao, Bing Qin  

**一句话要点**：提出TEA-Bench基准以评估工具增强情感支持对话代理，解决现有系统忽视工具使用导致幻觉的问题。

**关键词**：情感支持对话, 工具增强, 基准测试, 幻觉减少, 对话代理, 事实基础

## 3 点简述
- 核心问题：现有情感支持对话系统多关注文本情感表达，缺乏工具使用以提供事实基础，易产生幻觉。
- 方法要点：引入TEA-Bench，首个交互式基准，包含真实情感场景、MCP风格工具环境和过程级评估指标。
- 实验或效果：实验显示工具增强普遍提升支持质量并减少幻觉，但效果强烈依赖模型能力，强模型使用工具更有效。

## 摘要（原文）

> Emotional Support Conversation requires not only affective expression but also grounded instrumental support to provide trustworthy guidance. However, existing ESC systems and benchmarks largely focus on affective support in text-only settings, overlooking how external tools can enable factual grounding and reduce hallucination in multi-turn emotional support. We introduce TEA-Bench, the first interactive benchmark for evaluating tool-augmented agents in ESC, featuring realistic emotional scenarios, an MCP-style tool environment, and process-level metrics that jointly assess the quality and factual grounding of emotional support. Experiments on nine LLMs show that tool augmentation generally improves emotional support quality and reduces hallucination, but the gains are strongly capacity-dependent: stronger models use tools more selectively and effectively, while weaker models benefit only marginally. We further release TEA-Dialog, a dataset of tool-enhanced ESC dialogues, and find that supervised fine-tuning improves in-distribution support but generalizes poorly. Our results underscore the importance of tool use in building reliable emotional support agents.

