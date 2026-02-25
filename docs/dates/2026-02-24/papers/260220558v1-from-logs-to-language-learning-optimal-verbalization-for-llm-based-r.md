---
layout: default
title: From Logs to Language: Learning Optimal Verbalization for LLM-Based Recommendation in Production
---

# From Logs to Language: Learning Optimal Verbalization for LLM-Based Recommendation in Production
**arXiv**：[2602.20558v1](https://arxiv.org/abs/2602.20558) · [PDF](https://arxiv.org/pdf/2602.20558.pdf)  
**作者**：Yucheng Shi, Ying Li, Yu Wang, Yesu Feng, Arjun Rao, Rein Houthooft, Shradha Sehgal, Jin Wang, Hao Zhen, Ninghao Liu, Linas Baltrunas  

**一句话要点**：提出基于强化学习的语言化学习框架，以优化LLM推荐系统中的用户交互日志转换。

**关键词**：语言化学习, LLM推荐系统, 强化学习, 用户交互日志, 上下文优化

## 3 点简述
- 核心问题：现有模板方法在将结构化用户交互日志转换为自然语言输入时效果不佳，影响LLM推荐性能。
- 方法要点：使用强化学习训练语言化代理，自动优化日志转换，包括过滤噪声、整合元数据和重组信息。
- 实验或效果：在工业流式数据集上，相比模板基线，发现项目推荐准确率相对提升达93%。

## 摘要（原文）

> Large language models (LLMs) are promising backbones for generative recommender systems, yet a key challenge remains underexplored: verbalization, i.e., converting structured user interaction logs into effective natural language inputs. Existing methods rely on rigid templates that simply concatenate fields, yielding suboptimal representations for recommendation. We propose a data-centric framework that learns verbalization for LLM-based recommendation. Using reinforcement learning, a verbalization agent transforms raw interaction histories into optimized textual contexts, with recommendation accuracy as the training signal. This agent learns to filter noise, incorporate relevant metadata, and reorganize information to improve downstream predictions. Experiments on a large-scale industrial streaming dataset show that learned verbalization delivers up to 93% relative improvement in discovery item recommendation accuracy over template-based baselines. Further analysis reveals emergent strategies such as user interest summarization, noise removal, and syntax normalization, offering insights into effective context construction for LLM-based recommender systems.

