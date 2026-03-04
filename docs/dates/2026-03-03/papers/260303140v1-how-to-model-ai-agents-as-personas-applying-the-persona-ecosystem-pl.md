---
layout: default
title: How to Model AI Agents as Personas?: Applying the Persona Ecosystem Playground to 41,300 Posts on Moltbook for Behavioral Insights
---

# How to Model AI Agents as Personas?: Applying the Persona Ecosystem Playground to 41,300 Posts on Moltbook for Behavioral Insights
**arXiv**：[2603.03140v1](https://arxiv.org/abs/2603.03140) · [PDF](https://arxiv.org/pdf/2603.03140.pdf)  
**作者**：Danial Amin, Joni Salminen, Bernard J. Jansen  

**一句话要点**：应用Persona Ecosystem Playground于Moltbook平台，通过聚类和生成方法建模AI代理行为多样性。

**关键词**：AI代理行为建模, 对话角色生成, 社交媒体分析, 聚类验证, 检索增强生成

## 3 点简述
- 核心问题：AI代理在社交媒体上的行为多样性缺乏理解，缺少类型表征和话题参与研究方法。
- 方法要点：使用k-means聚类和检索增强生成，从41,300个帖子中生成并验证对话角色。
- 实验或效果：跨角色验证显示角色语义更接近自身聚类，模拟讨论中消息归属显著高于随机。

## 摘要（原文）

> AI agents are increasingly active on social media platforms, generating content and interacting with one another at scale. Yet the behavioral diversity of these agents remains poorly understood, and methods for characterizing distinct agent types and studying how they engage with shared topics are largely absent from current research. We apply the Persona Ecosystem Playground (PEP) to Moltbook, a social platform for AI agents, to generate and validate conversational personas from 41,300 posts using k-means clustering and retrieval-augmented generation. Cross-persona validation confirms that personas are semantically closer to their own source cluster than to others (t(61) = 17.85, p < .001, d = 2.20; own-cluster M = 0.71 vs. other-cluster M = 0.35). These personas are then deployed in a nine-turn structured discussion, and simulation messages were attributed to their source persona significantly above chance (binomial test, p < .001). The results indicate that persona-based ecosystem modeling can represent behavioral diversity in AI agent populations.

