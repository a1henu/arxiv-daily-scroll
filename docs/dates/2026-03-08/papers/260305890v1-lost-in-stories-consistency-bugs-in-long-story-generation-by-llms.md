---
layout: default
title: Lost in Stories: Consistency Bugs in Long Story Generation by LLMs
---

# Lost in Stories: Consistency Bugs in Long Story Generation by LLMs
**arXiv**：[2603.05890v1](https://arxiv.org/abs/2603.05890) · [PDF](https://arxiv.org/pdf/2603.05890.pdf)  
**作者**：Junjie Li, Xinrui Guo, Yuhao Wu, Roy Ka-Wei Lee, Hongzhi Li, Yutao Xie  

**一句话要点**：提出ConStory-Bench基准与ConStory-Checker工具以评估和检测长故事生成中的一致性错误

**关键词**：长故事生成, 一致性错误, 基准构建, 自动检测, LLM评估

## 3 点简述
- 核心问题：LLMs生成长故事时易出现事实、角色和世界规则的自相矛盾，现有基准忽略一致性评估
- 方法要点：构建包含2000提示和五类错误分类的基准，开发基于文本证据的自动检测管道
- 实验或效果：评估发现错误多集中于事实与时间维度，常出现在叙事中段和高熵文本段

## 摘要（原文）

> What happens when a storyteller forgets its own story? Large Language Models (LLMs) can now generate narratives spanning tens of thousands of words, but they often fail to maintain consistency throughout. When generating long-form narratives, these models can contradict their own established facts, character traits, and world rules. Existing story generation benchmarks focus mainly on plot quality and fluency, leaving consistency errors largely unexplored. To address this gap, we present ConStory-Bench, a benchmark designed to evaluate narrative consistency in long-form story generation. It contains 2,000 prompts across four task scenarios and defines a taxonomy of five error categories with 19 fine-grained subtypes. We also develop ConStory-Checker, an automated pipeline that detects contradictions and grounds each judgment in explicit textual evidence. Evaluating a range of LLMs through five research questions, we find that consistency errors show clear tendencies: they are most common in factual and temporal dimensions, tend to appear around the middle of narratives, occur in text segments with higher token-level entropy, and certain error types tend to co-occur. These findings can inform future efforts to improve consistency in long-form narrative generation. Our project page is available at https://picrew.github.io/constory-bench.github.io/.

