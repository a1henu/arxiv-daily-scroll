---
layout: default
title: GMP: A Benchmark for Content Moderation under Co-occurring Violations and Dynamic Rules
---

# GMP: A Benchmark for Content Moderation under Co-occurring Violations and Dynamic Rules
**arXiv**：[2603.01724v1](https://arxiv.org/abs/2603.01724) · [PDF](https://arxiv.org/pdf/2603.01724.pdf)  
**作者**：Houde Dong, Yifei She, Kai Ye, Liangcai Su, Chenxiong Qian, Jie Hao  

**一句话要点**：提出GMP基准以评估AI在共现违规和动态规则下的内容审核能力

**关键词**：内容审核, 共现违规, 动态规则, AI基准, 大语言模型, 泛化评估

## 3 点简述
- 核心问题：现有AI系统在共现违规和动态规则场景下审核能力退化，导致不一致性
- 方法要点：构建GMP基准，模拟真实世界中的多政策违规和平台特定动态指南
- 实验或效果：未知，但旨在评估AI在复杂场景下的泛化性能

## 摘要（原文）

> Online content moderation is essential for maintaining a healthy digital environment, and reliance on AI for this task continues to grow. Consider a user comment using national stereotypes to insult a politician. This example illustrates two critical challenges in real-world scenarios: (1) Co-occurring Violations, where a single post violates multiple policies (e.g., prejudice and personal attacks); (2) Dynamic rules of moderation, where determination of a violation depends on platform-specific guidelines that evolve across contexts . The intersection of co-occurring harms and dynamically changing rules highlights a core limitation of current AI systems: although large language models (LLMs) are adept at following fixed guidelines, their judgment capabilities degrade when policies are unstable or context-dependent . In practice, such shortcomings lead to inconsistent moderation: either erroneously restricting legitimate expression or allowing harmful content to remain online . This raises a critical question for evaluation: Does high performance on existing static benchmarks truly guarantee robust generalization of AI judgment to real-world scenarios involving co-occurring violations and dynamically changing rules?

