---
layout: default
title: Seeing the Goal, Missing the Truth: Human Accountability for AI Bias
---

# Seeing the Goal, Missing the Truth: Human Accountability for AI Bias
**arXiv**：[2602.09504v1](https://arxiv.org/abs/2602.09504) · [PDF](https://arxiv.org/pdf/2602.09504.pdf)  
**作者**：Sean Cao, Wei Jiang, Hui Xu  

**一句话要点**：揭示目标泄露导致大语言模型偏见，强调人类在AI研究设计中的责任

**关键词**：大语言模型偏见, 目的条件认知, 金融预测, 目标泄露, 人类责任, 研究设计

## 3 点简述
- 研究探讨人类定义目标如何通过目的条件认知影响大语言模型行为
- 在金融预测任务中，揭示下游用途导致模型生成有偏见的中间测量
- 目标泄露在知识截止前提升性能，但之后无优势，偏见源于研究设计

## 摘要（原文）

> This research explores how human-defined goals influence the behavior of Large Language Models (LLMs) through purpose-conditioned cognition. Using financial prediction tasks, we show that revealing the downstream use (e.g., predicting stock returns or earnings) of LLM outputs leads the LLM to generate biased sentiment and competition measures, even though these measures are intended to be downstream task-independent. Goal-aware prompting shifts intermediate measures toward the disclosed downstream objective. This purpose leakage improves performance before the LLM's knowledge cutoff, but with no advantage post-cutoff. AI bias due to "seeing the goal" is not an algorithmic flaw, but stems from human accountability in research design to ensure the statistical validity and reliability of AI-generated measurements.

