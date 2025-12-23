---
layout: default
title: A Dataset and Preliminary Study of Using GPT-5 for Code-change Impact Analysis
---

# A Dataset and Preliminary Study of Using GPT-5 for Code-change Impact Analysis
**arXiv**：[2512.19481v1](https://arxiv.org/abs/2512.19481) · [PDF](https://arxiv.org/pdf/2512.19481.pdf)  
**作者**：Katharina Stengg, Christian Macho, Martin Pinzger  

**一句话要点**：提出基于GPT-5的代码变更影响分析数据集与初步评估，以辅助软件开发中的变更理解。

**关键词**：代码变更影响分析, 大型语言模型, 软件工程数据集, GPT-5评估, 自动化代码分析

## 3 点简述
- 核心问题：现有数据集缺乏种子变更和受影响代码实体的关键信息，阻碍自动化代码变更影响分析。
- 方法要点：构建包含种子变更、变更对和变更类型的数据集，评估GPT-5和GPT-5-mini在两种配置下的预测能力。
- 实验或效果：模型在实验中表现不佳，GPT-5优于GPT-5-mini，提供差异块可轻微提升性能。

## 摘要（原文）

> Understanding source code changes and their impact on other code entities is a crucial skill in software development. However, the analysis of code changes and their impact is often performed manually and therefore is time-consuming. Recent advancements in AI, and in particular large language models (LLMs) show promises to help developers in various code analysis tasks. However, the extent to which this potential can be utilized for understanding code changes and their impact is underexplored. To address this gap, we study the capabilities of GPT-5 and GPT-5-mini to predict the code entities impacted by given source code changes. We construct a dataset containing information about seed-changes, change pairs, and change types for each commit. Existing datasets lack crucial information about seed changes and impacted code entities. Our experiments evaluate the LLMs in two configurations: (1) seed-change information and the parent commit tree and (2) seed-change information, the parent commit tree, and the diff hunk of each seed change. We found that both LLMs perform poorly in the two experiments, whereas GPT-5 outperforms GPT-5-mini. Furthermore, the provision of the diff hunks helps both models to slightly improve their performance.

