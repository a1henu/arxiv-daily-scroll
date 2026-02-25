---
layout: default
title: Qwen-BIM: developing large language model for BIM-based design with domain-specific benchmark and dataset
---

# Qwen-BIM: developing large language model for BIM-based design with domain-specific benchmark and dataset
**arXiv**：[2602.20812v1](https://arxiv.org/abs/2602.20812) · [PDF](https://arxiv.org/pdf/2602.20812.pdf)  
**作者**：Jia-Rui Lin, Yun-Hong Cai, Xiang-Rui Ni, Shaojie Zhou, Peng Pan  

**一句话要点**：提出Qwen-BIM大语言模型，通过领域基准与数据集解决BIM设计中的LLM性能不足问题。

**关键词**：BIM设计, 大语言模型, 领域基准, 数据集构建, 模型微调, 性能评估

## 3 点简述
- 核心问题：BIM设计领域缺乏专用数据集和评估基准，限制大语言模型性能。
- 方法要点：构建BIM设计评估基准、从BIM生成文本数据的方法及LLM微调策略。
- 实验或效果：Qwen-BIM在G-Eval得分上平均提升21.0%，14B参数模型性能媲美671B通用模型。

## 摘要（原文）

> As the construction industry advances toward digital transformation, BIM (Building Information Modeling)-based design has become a key driver supporting intelligent construction. Despite Large Language Models (LLMs) have shown potential in promoting BIM-based design, the lack of specific datasets and LLM evaluation benchmarks has significantly hindered the performance of LLMs. Therefore, this paper addresses this gap by proposing: 1) an evaluation benchmark for BIM-based design together with corresponding quantitative indicators to evaluate the performance of LLMs, 2) a method for generating textual data from BIM and constructing corresponding BIM-derived datasets for LLM evaluation and fine-tuning, and 3) a fine-tuning strategy to adapt LLMs for BIM-based design. Results demonstrate that the proposed domain-specific benchmark effectively and comprehensively assesses LLM capabilities, highlighting that general LLMs are still incompetent for domain-specific tasks. Meanwhile, with the proposed benchmark and datasets, Qwen-BIM is developed and achieves a 21.0% average increase in G-Eval score compared to the base LLM model. Notably, with only 14B parameters, performance of Qwen-BIM is comparable to that of general LLMs with 671B parameters for BIM-based design tasks. Overall, this study develops the first domain-specific LLM for BIM-based design by introducing a comprehensive benchmark and high-quality dataset, which provide a solid foundation for developing BIM-related LLMs in various fields.

