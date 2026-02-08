---
layout: default
title: Chunky Post-Training: Data Driven Failures of Generalization
---

# Chunky Post-Training: Data Driven Failures of Generalization
**arXiv**：[2602.05910v1](https://arxiv.org/abs/2602.05910) · [PDF](https://arxiv.org/pdf/2602.05910.pdf)  
**作者**：Seoirse Murray, Allison Qi, Timothy Qian, John Schulman, Collin Burns, Sara Price  

**一句话要点**：提出SURF和TURF工具以检测和溯源大语言模型后训练中的虚假相关性行为

**关键词**：大语言模型后训练, 虚假相关性检测, 行为溯源工具, 模型泛化失败, 数据驱动分析

## 3 点简述
- 核心问题：后训练数据中的偶然模式导致模型学习虚假相关性，产生意外行为
- 方法要点：SURF为黑盒运行时检测工具，TURF用于追踪失败至具体后训练数据
- 实验或效果：应用于前沿和开源模型，显示后训练数据不平衡或未指定导致行为失准

## 摘要（原文）

> LLM post-training involves many diverse datasets, each targeting a specific behavior. But these datasets encode incidental patterns alongside intended ones: correlations between formatting and content, narrow phrasings across diverse problems, and implicit associations arising from the discrete data curation process. These patterns are often invisible to developers yet salient to models, producing behaviors that surprise their creators, such as rejecting true facts presented in a particular question format. We call this chunky post-training: the model learns spurious correlations as a result of distinct chunks of post-training data. We introduce SURF, a black-box pipeline which surfaces these unintended behaviors at run time, and TURF, a tool that traces these failures back to specific post-training data. Applying these tools to frontier models (Claude 4.5, GPT-5.1, Grok 4.1, Gemini 3) and open models (Tülu 3), we show that chunky post-training produces miscalibrated behaviors, which often result from imbalanced or underspecified chunks of post-training data.

