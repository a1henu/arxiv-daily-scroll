---
layout: default
title: Faster, Cheaper, More Accurate: Specialised Knowledge Tracing Models Outperform LLMs
---

# Faster, Cheaper, More Accurate: Specialised Knowledge Tracing Models Outperform LLMs
**arXiv**：[2603.02830v1](https://arxiv.org/abs/2603.02830) · [PDF](https://arxiv.org/pdf/2603.02830.pdf)  
**作者**：Prarthana Bhattacharyya, Joshua Mitton, Ralph Abboud, Simon Woodhead  

**一句话要点**：比较知识追踪模型与大型语言模型在教育预测任务中的性能、成本与速度

**关键词**：知识追踪, 大型语言模型, 教育预测, 模型比较, 部署成本, 推理速度

## 3 点简述
- 核心问题：评估LLMs在预测学生未来答题表现上的能力、可扩展性及与KT模型的对比
- 方法要点：通过多模型比较，分析预测准确性、部署成本和推理速度
- 实验或效果：KT模型在准确性和F1分数上优于LLMs，且速度更快、成本更低

## 摘要（原文）

> Predicting future student responses to questions is particularly valuable for educational learning platforms where it enables effective interventions. One of the key approaches to do this has been through the use of knowledge tracing (KT) models. These are small, domain-specific, temporal models trained on student question-response data. KT models are optimised for high accuracy on specific educational domains and have fast inference and scalable deployments. The rise of Large Language Models (LLMs) motivates us to ask the following questions: (1) How well can LLMs perform at predicting students' future responses to questions? (2) Are LLMs scalable for this domain? (3) How do LLMs compare to KT models on this domain-specific task? In this paper, we compare multiple LLMs and KT models across predictive performance, deployment cost, and inference speed to answer the above questions. We show that KT models outperform LLMs with respect to accuracy and F1 scores on this domain-specific task. Further, we demonstrate that LLMs are orders of magnitude slower than KT models and cost orders of magnitude more to deploy. This highlights the importance of domain-specific models for education prediction tasks and the fact that current closed source LLMs should not be used as a universal solution for all tasks.

