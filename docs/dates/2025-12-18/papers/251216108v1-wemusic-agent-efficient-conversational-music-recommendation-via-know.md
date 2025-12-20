---
layout: default
title: WeMusic-Agent: Efficient Conversational Music Recommendation via Knowledge Internalization and Agentic Boundary Learning
---

# WeMusic-Agent: Efficient Conversational Music Recommendation via Knowledge Internalization and Agentic Boundary Learning
**arXiv**：[2512.16108v1](https://arxiv.org/abs/2512.16108) · [PDF](https://arxiv.org/pdf/2512.16108.pdf)  
**作者**：Wendong Bi, Yirong Mao, Xianglong Liu, Kai Tian, Jian Zhang, Hanjie Wang, Wenhui Que  

**一句话要点**：提出WeMusic-Agent框架，通过知识内化与代理边界学习优化对话式音乐推荐效率

**关键词**：对话式音乐推荐, 知识内化, 代理边界学习, LLM训练框架, 音乐推荐基准

## 3 点简述
- 核心问题：对话式音乐推荐需平衡领域知识与工具调用，现有方法效率不足
- 方法要点：结合知识内化（50B语料预训练）与代理边界学习，智能决策知识使用与工具调用
- 实验或效果：在真实数据上显著超越现有模型，并构建开源基准用于多维度评估

## 摘要（原文）

> Personalized music recommendation in conversational scenarios usually requires a deep understanding of user preferences and nuanced musical context, yet existing methods often struggle with balancing specialized domain knowledge and flexible tool integration. This paper proposes WeMusic-Agent, a training framework for efficient LLM-based conversational music recommendation. By integrating the knowledge internalization and agentic boundary learning, the framework aims to teach the model to intelligently decide when to leverage internalized knowledge and when to call specialized tools (e.g., music retrieval APIs, music recommendation systems). Under this framework, we present WeMusic-Agent-M1, an agentic model that internalizes extensive musical knowledge via continued pretraining on 50B music-related corpus while acquiring the ability to invoke external tools when necessary. Additionally, considering the lack of open-source benchmarks for conversational music recommendation, we also construct a benchmark for personalized music recommendations derived from real-world data in WeChat Listen. This benchmark enables comprehensive evaluation across multiple dimensions, including relevance, personalization, and diversity of the recommendations. Experiments on real-world data demonstrate that WeMusic-Agent achieves significant improvements over existing models.

