---
layout: default
title: Monte Carlo Tree Search with Reasoning Path Refinement for Small Language Models in Conversational Text-to-NoSQL
---

# Monte Carlo Tree Search with Reasoning Path Refinement for Small Language Models in Conversational Text-to-NoSQL
**arXiv**：[2602.12574v1](https://arxiv.org/abs/2602.12574) · [PDF](https://arxiv.org/pdf/2602.12574.pdf)  
**作者**：Xubang Xiong, Raymond Chi-Wing Wong, Yuanfeng Song  

**一句话要点**：提出Stage-MCTS框架，通过蒙特卡洛树搜索增强小语言模型在对话式文本到NoSQL查询中的推理能力。

**关键词**：对话式文本到NoSQL, 蒙特卡洛树搜索, 小语言模型, 推理路径优化, 渐进微调, 跨域数据集

## 3 点简述
- 核心问题：现有文本到NoSQL研究忽略对话历史，难以处理真实世界多轮查询交互。
- 方法要点：使用基于规则的奖励引导蒙特卡洛树搜索生成逐步推理数据，结合渐进监督微调和自训练策略。
- 实验或效果：在CoNoSQL数据集上超越先进大模型，执行值匹配准确率最高提升7.93%。

## 摘要（原文）

> NoSQL databases have been widely adopted in big data analytics, geospatial applications, and healthcare services, due to their flexibility and scalability. However, querying NoSQL databases requires specialized technical expertise, creating a high barrier for users. While recent studies have explored text-to-NoSQL problem, they primarily focus on single-turn interactions, ignoring the conversational nature of real-world queries. To bridge this gap, we introduce the Conversational Text-to-NoSQL task, which generates NoSQL queries given a natural language question, a NoSQL database, and the dialogue history. To address this task, we propose Stage-MCTS, a framework that endows small language models (SLMs) with NoSQL-specific reasoning capabilities by formulating query generation as a search problem. The framework employs Monte Carlo Tree Search (MCTS) guided by a rule-based reward to produce stepwise reasoning data, followed by progressive supervised fine-tuning (SFT) and self-training strategies. We further construct CoNoSQL, a cross-domain dataset with over 2,000 dialogues and 150 databases, to support evaluation. Experiments demonstrate that our approach outperforms state-of-the-art large reasoning models, improving execution value match (EVM) accuracy by up to 7.93%.

