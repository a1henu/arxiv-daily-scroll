---
layout: default
title: RiskAtlas: Exposing Domain-Specific Risks in LLMs through Knowledge-Graph-Guided Harmful Prompt Generation
---

# RiskAtlas: Exposing Domain-Specific Risks in LLMs through Knowledge-Graph-Guided Harmful Prompt Generation
**arXiv**：[2601.04740v1](https://arxiv.org/abs/2601.04740) · [PDF](https://arxiv.org/pdf/2601.04740.pdf)  
**作者**：Huawei Zheng, Xinqi Jiang, Sen Yang, Shouling Ji, Yingcai Wu, Dazhen Deng  

**一句话要点**：提出RiskAtlas框架，通过知识图谱引导生成领域特定有害提示以增强LLM安全测试

**关键词**：大语言模型安全, 知识图谱引导, 有害提示生成, 隐式攻击, 领域特定风险, 对抗测试

## 3 点简述
- 核心问题：领域特定有害提示数据集稀缺，现有防御难以检测隐式有害提示
- 方法要点：结合知识图谱生成领域相关提示，并应用双路径混淆改写提升隐式性
- 实验或效果：生成高质量数据集，支持更现实的对抗测试，推动LLM安全研究

## 摘要（原文）

> Large language models (LLMs) are increasingly applied in specialized domains such as finance and healthcare, where they introduce unique safety risks. Domain-specific datasets of harmful prompts remain scarce and still largely rely on manual construction; public datasets mainly focus on explicit harmful prompts, which modern LLM defenses can often detect and refuse. In contrast, implicit harmful prompts-expressed through indirect domain knowledge-are harder to detect and better reflect real-world threats. We identify two challenges: transforming domain knowledge into actionable constraints and increasing the implicitness of generated harmful prompts. To address them, we propose an end-to-end framework that first performs knowledge-graph-guided harmful prompt generation to systematically produce domain-relevant prompts, and then applies dual-path obfuscation rewriting to convert explicit harmful prompts into implicit variants via direct and context-enhanced rewriting. This framework yields high-quality datasets combining strong domain relevance with implicitness, enabling more realistic red-teaming and advancing LLM safety research. We release our code and datasets at GitHub.

