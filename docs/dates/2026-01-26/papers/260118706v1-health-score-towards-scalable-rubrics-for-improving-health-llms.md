---
layout: default
title: Health-SCORE: Towards Scalable Rubrics for Improving Health-LLMs
---

# Health-SCORE: Towards Scalable Rubrics for Improving Health-LLMs
**arXiv**：[2601.18706v1](https://arxiv.org/abs/2601.18706) · [PDF](https://arxiv.org/pdf/2601.18706.pdf)  
**作者**：Zhichao Yang, Sepehr Janghorbani, Dongxu Zhang, Jun Han, Qian Qian, Andrew Ressler, Gregory D. Lyng, Sanjit Singh Batra, Robert E. Tillman  

**一句话要点**：提出Health-SCORE框架以降低医疗领域LLM评估与训练的标注成本

**关键词**：医疗大语言模型, 标注框架, 强化学习, 上下文学习, 可扩展评估

## 3 点简述
- 核心问题：医疗领域LLM评估需高质量专业标注，成本高且难以扩展。
- 方法要点：开发可泛化、可扩展的标注框架，减少人工标注需求。
- 实验或效果：在开放医疗任务中，评估质量接近人工标注，显著降低开发成本。

## 摘要（原文）

> Rubrics are essential for evaluating open-ended LLM responses, especially in safety-critical domains such as healthcare. However, creating high-quality and domain-specific rubrics typically requires significant human expertise time and development cost, making rubric-based evaluation and training difficult to scale. In this work, we introduce Health-SCORE, a generalizable and scalable rubric-based training and evaluation framework that substantially reduces rubric development costs without sacrificing performance. We show that Health-SCORE provides two practical benefits beyond standalone evaluation: it can be used as a structured reward signal to guide reinforcement learning with safety-aware supervision, and it can be incorporated directly into prompts to improve response quality through in-context learning. Across open-ended healthcare tasks, Health-SCORE achieves evaluation quality comparable to human-created rubrics while significantly lowering development effort, making rubric-based evaluation and training more scalable.

