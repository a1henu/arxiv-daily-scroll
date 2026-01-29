---
layout: default
title: Less is More: Benchmarking LLM Based Recommendation Agents
---

# Less is More: Benchmarking LLM Based Recommendation Agents
**arXiv**：[2601.20316v1](https://arxiv.org/abs/2601.20316) · [PDF](https://arxiv.org/pdf/2601.20316.pdf)  
**作者**：Kargi Chauhan, Mahalakshmi Venkateswarlu  

**一句话要点**：挑战长上下文假设，提出短历史优化LLM推荐系统以降低成本

**关键词**：LLM推荐系统, 上下文长度优化, 成本效益分析, 基准测试, 个性化推荐

## 3 点简述
- 核心问题：长用户购买历史是否提升LLM推荐质量，假设可能不成立
- 方法要点：系统基准测试四款先进LLM，在REGEN数据集上比较5至50项上下文长度
- 实验或效果：质量分数无显著提升，使用短上下文可降低约88%推理成本

## 摘要（原文）

> Large Language Models (LLMs) are increasingly deployed for personalized product recommendations, with practitioners commonly assuming that longer user purchase histories lead to better predictions. We challenge this assumption through a systematic benchmark of four state of the art LLMs GPT-4o-mini, DeepSeek-V3, Qwen2.5-72B, and Gemini 2.5 Flash across context lengths ranging from 5 to 50 items using the REGEN dataset.
>   Surprisingly, our experiments with 50 users in a within subject design reveal no significant quality improvement with increased context length. Quality scores remain flat across all conditions (0.17--0.23). Our findings have significant practical implications: practitioners can reduce inference costs by approximately 88\% by using context (5--10 items) instead of longer histories (50 items), without sacrificing recommendation quality. We also analyze latency patterns across providers and find model specific behaviors that inform deployment decisions. This work challenges the existing ``more context is better'' paradigm and provides actionable guidelines for cost effective LLM based recommendation systems.

