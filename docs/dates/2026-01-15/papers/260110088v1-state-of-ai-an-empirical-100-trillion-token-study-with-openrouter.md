---
layout: default
title: State of AI: An Empirical 100 Trillion Token Study with OpenRouter
---

# State of AI: An Empirical 100 Trillion Token Study with OpenRouter
**arXiv**：[2601.10088v1](https://arxiv.org/abs/2601.10088) · [PDF](https://arxiv.org/pdf/2601.10088.pdf)  
**作者**：Malika Aubakirova, Alex Atallah, Chris Clark, Justin Summerville, Anjney Midha  

**一句话要点**：基于OpenRouter平台分析100万亿令牌，揭示LLM实际使用模式与保留效应

**关键词**：大语言模型使用分析, 多步推理模型, 用户保留效应, 开源模型采用, 创意角色扮演, 编码辅助

## 3 点简述
- 核心问题：LLM从单次生成转向多步推理后，实际使用模式缺乏实证理解
- 方法要点：利用OpenRouter平台分析真实世界LLM交互数据，覆盖任务、地理和时间维度
- 实验或效果：发现开源模型广泛采用、创意角色扮演和编码辅助流行，以及早期用户保留的“玻璃鞋”效应

## 摘要（原文）

> The past year has marked a turning point in the evolution and real-world use of large language models (LLMs). With the release of the first widely adopted reasoning model, o1, on December 5th, 2024, the field shifted from single-pass pattern generation to multi-step deliberation inference, accelerating deployment, experimentation, and new classes of applications. As this shift unfolded at a rapid pace, our empirical understanding of how these models have actually been used in practice has lagged behind. In this work, we leverage the OpenRouter platform, which is an AI inference provider across a wide variety of LLMs, to analyze over 100 trillion tokens of real-world LLM interactions across tasks, geographies, and time. In our empirical study, we observe substantial adoption of open-weight models, the outsized popularity of creative roleplay (beyond just the productivity tasks many assume dominate) and coding assistance categories, plus the rise of agentic inference. Furthermore, our retention analysis identifies foundational cohorts: early users whose engagement persists far longer than later cohorts. We term this phenomenon the Cinderella "Glass Slipper" effect. These findings underscore that the way developers and end-users engage with LLMs "in the wild" is complex and multifaceted. We discuss implications for model builders, AI developers, and infrastructure providers, and outline how a data-driven understanding of usage can inform better design and deployment of LLM systems.

