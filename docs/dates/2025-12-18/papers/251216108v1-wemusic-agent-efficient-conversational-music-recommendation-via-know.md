---
layout: default
title: WeMusic-Agent: Efficient Conversational Music Recommendation via Knowledge Internalization and Agentic Boundary Learning
---

# WeMusic-Agent: Efficient Conversational Music Recommendation via Knowledge Internalization and Agentic Boundary Learning
**arXiv**：[2512.16108v1](https://arxiv.org/abs/2512.16108) · [PDF](https://arxiv.org/pdf/2512.16108.pdf)  
**作者**：Wendong Bi, Yirong Mao, Xianglong Liu, Kai Tian, Jian Zhang, Hanjie Wang, Wenhui Que  

**一句话要点**：提出WeMusic-Agent框架以解决对话式音乐推荐中知识内化与工具调用的平衡问题

**关键词**：对话式音乐推荐, 知识内化, 代理边界学习, 大语言模型训练, 音乐推荐基准

## 3 点简述
- 核心问题：对话式音乐推荐需平衡专业音乐知识与灵活工具集成，现有方法常难以兼顾
- 方法要点：通过知识内化与代理边界学习，训练模型智能决策何时使用内部知识或调用外部工具
- 实验或效果：在真实数据上实验，WeMusic-Agent相比现有模型取得显著改进，并构建了开源基准

## 摘要（原文）

> Personalized music recommendation in conversational scenarios usually requires a deep understanding of user preferences and nuanced musical context, yet existing methods often struggle with balancing specialized domain knowledge and flexible tool integration. This paper proposes WeMusic-Agent, a training framework for efficient LLM-based conversational music recommendation. By integrating the knowledge internalization and agentic boundary learning, the framework aims to teach the model to intelligently decide when to leverage internalized knowledge and when to call specialized tools (e.g., music retrieval APIs, music recommendation systems). Under this framework, we present WeMusic-Agent-M1, an agentic model that internalizes extensive musical knowledge via continued pretraining on 50B music-related corpus while acquiring the ability to invoke external tools when necessary. Additionally, considering the lack of open-source benchmarks for conversational music recommendation, we also construct a benchmark for personalized music recommendations derived from real-world data in WeChat Listen. This benchmark enables comprehensive evaluation across multiple dimensions, including relevance, personalization, and diversity of the recommendations. Experiments on real-world data demonstrate that WeMusic-Agent achieves significant improvements over existing models.

