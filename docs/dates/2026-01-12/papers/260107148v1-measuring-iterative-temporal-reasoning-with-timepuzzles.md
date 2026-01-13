---
layout: default
title: Measuring Iterative Temporal Reasoning with TimePuzzles
---

# Measuring Iterative Temporal Reasoning with TimePuzzles
**arXiv**：[2601.07148v1](https://arxiv.org/abs/2601.07148) · [PDF](https://arxiv.org/pdf/2601.07148.pdf)  
**作者**：Zhengxiang Wang, Zeyu Dong  

**一句话要点**：提出TimePuzzles以评估大语言模型的迭代时序推理能力

**关键词**：时序推理, 约束推理, 大语言模型评估, 算法生成数据集, 工具增强推理, 日历关系

## 3 点简述
- 核心问题：评估大语言模型在约束条件下的迭代时序推理能力，现有任务缺乏动态和可控性
- 方法要点：基于算法生成结合事实时间锚点和跨文化日历关系的日期推理谜题，支持多解
- 实验或效果：在13个模型中，GPT-5准确率仅49.3%，其他低于31%，工具使用能提升性能但存在差距

## 摘要（原文）

> We introduce TimePuzzles, a constraint-based date inference task for evaluating iterative temporal reasoning. Each puzzle combines factual temporal anchors with (cross-cultural) calendar relations, admits one or multiple valid solution dates, and is algorithmically generated for controlled, dynamic, and continual evaluation. Across 13 diverse LLMs, TimePuzzles well distinguishes their iterative temporal reasoning capabilities and remains challenging without tools: GPT-5 reaches only 49.3% accuracy and all other models stay below 31%, despite the dataset's simplicity. Web search consistently yields substantial gains and using code interpreter shows mixed effects, but all models perform much better when constraints are rewritten with explicit dates, revealing a gap in reliable tool use. Overall, TimePuzzles presents a simple, cost-effective diagnostic for tool-augmented iterative temporal reasoning.

