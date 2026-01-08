---
layout: default
title: Evaluating LLMs for Police Decision-Making: A Framework Based on Police Action Scenarios
---

# Evaluating LLMs for Police Decision-Making: A Framework Based on Police Action Scenarios
**arXiv**：[2601.03553v1](https://arxiv.org/abs/2601.03553) · [PDF](https://arxiv.org/pdf/2601.03553.pdf)  
**作者**：Sangyub Lee, Heedou Kim, Hyeoncheol Kim  

**一句话要点**：提出PAS框架以评估大语言模型在警务决策中的可靠性

**关键词**：大语言模型评估, 警务决策, PAS框架, 问答数据集, 统计分析验证

## 3 点简述
- 核心问题：缺乏针对警务操作的大语言模型评估框架，可能导致非法逮捕等严重问题。
- 方法要点：构建PAS框架，基于8000多份官方文档创建问答数据集，并建立经统计分析验证的关键指标。
- 实验或效果：实验显示商业大语言模型在警务相关任务中表现不佳，特别是在提供基于事实的建议方面。

## 摘要（原文）

> The use of Large Language Models (LLMs) in police operations is growing, yet an evaluation framework tailored to police operations remains absent. While LLM's responses may not always be legally incorrect, their unverified use still can lead to severe issues such as unlawful arrests and improper evidence collection. To address this, we propose PAS (Police Action Scenarios), a systematic framework covering the entire evaluation process. Applying this framework, we constructed a novel QA dataset from over 8,000 official documents and established key metrics validated through statistical analysis with police expert judgements. Experimental results show that commercial LLMs struggle with our new police-related tasks, particularly in providing fact-based recommendations. This study highlights the necessity of an expandable evaluation framework to ensure reliable AI-driven police operations. We release our data and prompt template.

