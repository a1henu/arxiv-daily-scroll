---
layout: default
title: Semantic Content Determines Algorithmic Performance
---

# Semantic Content Determines Algorithmic Performance
**arXiv**：[2601.21618v1](https://arxiv.org/abs/2601.21618) · [PDF](https://arxiv.org/pdf/2601.21618.pdf)  
**作者**：Martiño Ríos-García, Nawaf Alampara, Kevin Maik Jablonka  

**一句话要点**：提出WhatCounts测试框架，揭示LLM算法性能受语义内容影响

**关键词**：语义敏感性, 算法近似, LLM评估, 计数任务, 微调影响

## 3 点简述
- 核心问题：算法行为应独立于输入语义，但LLM可能违反此原则
- 方法要点：设计原子化WhatCounts测试，隔离语义敏感性，避免混淆因素
- 实验或效果：前沿LLM在计数任务中准确率差异超40%，语义依赖随微调变化

## 摘要（原文）

> Counting should not depend on what is being counted; more generally, any algorithm's behavior should be invariant to the semantic content of its arguments. We introduce WhatCounts to test this property in isolation. Unlike prior work that conflates semantic sensitivity with reasoning complexity or prompt variation, WhatCounts is atomic: count items in an unambiguous, delimited list with no duplicates, distractors, or reasoning steps for different semantic types. Frontier LLMs show over 40% accuracy variation depending solely on what is being counted - cities versus chemicals, names versus symbols. Controlled ablations rule out confounds. The gap is semantic, and it shifts unpredictably with small amounts of unrelated fine-tuning. LLMs do not implement algorithms; they approximate them, and the approximation is argument-dependent. As we show with an agentic example, this has implications beyond counting: any LLM function may carry hidden dependencies on the meaning of its inputs.

