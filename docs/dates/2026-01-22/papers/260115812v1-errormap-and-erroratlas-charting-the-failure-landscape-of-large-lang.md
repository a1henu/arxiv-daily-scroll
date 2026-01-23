---
layout: default
title: ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models
---

# ErrorMap and ErrorAtlas: Charting the Failure Landscape of Large Language Models
**arXiv**：[2601.15812v1](https://arxiv.org/abs/2601.15812) · [PDF](https://arxiv.org/pdf/2601.15812.pdf)  
**作者**：Shir Ashury-Tahan, Yifan Mai, Elron Bandel, Michal Shmueli-Scheuer, Leshem Choshen  

**一句话要点**：提出ErrorMap和ErrorAtlas以分析大语言模型失败原因，提升评估深度。

**关键词**：大语言模型评估, 错误分析, 失败签名, 错误分类学, 基准测试改进

## 3 点简述
- 核心问题：现有基准仅揭示模型失败位置，未解析失败原因如格式错误或计算误差。
- 方法要点：ErrorMap提取模型失败签名，ErrorAtlas构建错误分类学，识别重复失败模式。
- 实验或效果：应用于35个数据集和83个模型，揭示未充分探索的错误类型如细节遗漏。

## 摘要（原文）

> Large Language Models (LLM) benchmarks tell us when models fail, but not why they fail. A wrong answer on a reasoning dataset may stem from formatting issues, calculation errors, or dataset noise rather than weak reasoning. Without disentangling such causes, benchmarks remain incomplete and cannot reliably guide model improvement. We introduce ErrorMap, the first method to chart the sources of LLM failure. It extracts a model's unique "failure signature", clarifies what benchmarks measure, and broadens error identification to reduce blind spots. This helps developers debug models, aligns benchmark goals with outcomes, and supports informed model selection. ErrorMap works on any model or dataset with the same logic. Applying our method to 35 datasets and 83 models we generate ErrorAtlas, a taxonomy of model errors, revealing recurring failure patterns. ErrorAtlas highlights error types that are currently underexplored in LLM research, such as omissions of required details in the output and question misinterpretation. By shifting focus from where models succeed to why they fail, ErrorMap and ErrorAtlas enable advanced evaluation - one that exposes hidden weaknesses and directs progress. Unlike success, typically measured by task-level metrics, our approach introduces a deeper evaluation layer that can be applied globally across models and tasks, offering richer insights into model behavior and limitations. We make the taxonomy and code publicly available with plans to periodically update ErrorAtlas as new benchmarks and models emerge.

