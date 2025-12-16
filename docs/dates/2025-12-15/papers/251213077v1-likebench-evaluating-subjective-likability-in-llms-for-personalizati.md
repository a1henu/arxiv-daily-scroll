---
layout: default
title: LikeBench: Evaluating Subjective Likability in LLMs for Personalization
---

# LikeBench: Evaluating Subjective Likability in LLMs for Personalization
**arXiv**：[2512.13077v1](https://arxiv.org/abs/2512.13077) · [PDF](https://arxiv.org/pdf/2512.13077.pdf)  
**作者**：Md Awsafur Rahman, Adam Gabrys, Doug Kang, Jingjing Sun, Tian Tan, Ashwin Chandramouli  

**一句话要点**：提出LikeBench评估框架，以多维度主观喜好性衡量LLM个性化能力

**关键词**：LLM个性化评估, 主观喜好性, 多维度诊断, 动态交互框架, 心理人物模拟

## 3 点简述
- 核心问题：现有LLM个性化基准忽视主观喜好性，影响用户体验评估
- 方法要点：引入多会话动态框架，分解喜好性为七个诊断维度，使用细粒度心理人物模拟
- 实验或效果：实验显示记忆准确性不保证高喜好性，SOTA模型在长噪声交互中适应性有限

## 摘要（原文）

> A personalized LLM should remember user facts, apply them correctly, and adapt over time to provide responses that the user prefers. Existing LLM personalization benchmarks are largely centered on two axes: accurately recalling user information and accurately applying remembered information in downstream tasks. We argue that a third axis, likability, is both subjective and central to user experience, yet under-measured by current benchmarks. To measure likability holistically, we introduce LikeBench, a multi-session, dynamic evaluation framework that measures likability across multiple dimensions by how much an LLM can adapt over time to a user's preferences to provide more likable responses. In LikeBench, the LLMs engage in conversation with a simulated user and learn preferences only from the ongoing dialogue. As the interaction unfolds, models try to adapt to responses, and after each turn, they are evaluated for likability across seven dimensions by the same simulated user. To the best of our knowledge, we are the first to decompose likability into multiple diagnostic metrics: emotional adaptation, formality matching, knowledge adaptation, reference understanding, conversation length fit, humor fit, and callback, which makes it easier to pinpoint where a model falls short. To make the simulated user more realistic and discriminative, LikeBench uses fine-grained, psychologically grounded descriptive personas rather than the coarse high/low trait rating based personas used in prior work. Our benchmark shows that strong memory performance does not guarantee high likability: DeepSeek R1, with lower memory accuracy (86%, 17 facts/profile), outperformed Qwen3 by 28% on likability score despite Qwen3's higher memory accuracy (93%, 43 facts/profile). Even SOTA models like GPT-5 adapt well in short exchanges but show only limited robustness in longer, noisier interactions.

