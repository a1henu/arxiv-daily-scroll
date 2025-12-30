---
layout: default
title: Web World Models
---

# Web World Models
**arXiv**：[2512.23676v1](https://arxiv.org/abs/2512.23676) · [PDF](https://arxiv.org/pdf/2512.23676.pdf)  
**作者**：Jichen Feng, Yifan Zhang, Chenggong Zhang, Yifu Lu, Shilong Liu, Mengdi Wang  

**一句话要点**：提出Web World Models以在可控性与开放性之间平衡，实现语言代理的持久世界环境。

**关键词**：语言代理, 世界模型, Web栈, 可控生成, 结构化探索

## 3 点简述
- 核心问题：现有方法在固定数据库环境与不可控生成世界模型之间缺乏平衡。
- 方法要点：结合Web代码定义世界状态与LLM生成内容，确保逻辑一致与开放探索。
- 实验或效果：构建多种Web World Models，展示其在旅行、叙事等场景中的可扩展性。

## 摘要（原文）

> Language agents increasingly require persistent worlds in which they can act, remember, and learn. Existing approaches sit at two extremes: conventional web frameworks provide reliable but fixed contexts backed by databases, while fully generative world models aim for unlimited environments at the expense of controllability and practical engineering. In this work, we introduce the Web World Model (WWM), a middle ground where world state and ``physics'' are implemented in ordinary web code to ensure logical consistency, while large language models generate context, narratives, and high-level decisions on top of this structured latent state. We build a suite of WWMs on a realistic web stack, including an infinite travel atlas grounded in real geography, fictional galaxy explorers, web-scale encyclopedic and narrative worlds, and simulation- and game-like environments. Across these systems, we identify practical design principles for WWMs: separating code-defined rules from model-driven imagination, representing latent state as typed web interfaces, and utilizing deterministic generation to achieve unlimited but structured exploration. Our results suggest that web stacks themselves can serve as a scalable substrate for world models, enabling controllable yet open-ended environments. Project Page: https://github.com/Princeton-AI2-Lab/Web-World-Models.

