---
layout: default
title: Poodle: Seamlessly Scaling Down Large Language Models with Just-in-Time Model Replacement
---

# Poodle: Seamlessly Scaling Down Large Language Models with Just-in-Time Model Replacement
**arXiv**：[2512.05525v1](https://arxiv.org/abs/2512.05525) · [PDF](https://arxiv.org/pdf/2512.05525.pdf)  
**作者**：Nils Strassenburg, Boris Glavic, Tilmann Rabl  

**一句话要点**：提出即时模型替换以降低大语言模型在重复任务中的资源消耗

**关键词**：即时模型替换, 大语言模型优化, 资源效率, 迁移学习, 模型搜索

## 3 点简述
- 核心问题：大语言模型处理简单重复任务时资源消耗高，而小模型性能相近
- 方法要点：通过识别重复任务，透明替换为更便宜的定制模型，结合模型搜索和迁移学习
- 实验或效果：原型Poodle在示例任务中实现显著成本与能源节省

## 摘要（原文）

> Businesses increasingly rely on large language models (LLMs) to automate simple repetitive tasks instead of developing custom machine learning models. LLMs require few, if any, training examples and can be utilized by users without expertise in model development. However, this comes at the cost of substantially higher resource and energy consumption compared to smaller models, which often achieve similar predictive performance for simple tasks. In this paper, we present our vision for just-in-time model replacement (JITR), where, upon identifying a recurring task in calls to an LLM, the model is replaced transparently with a cheaper alternative that performs well for this specific task. JITR retains the ease of use and low development effort of LLMs, while saving significant cost and energy. We discuss the main challenges in realizing our vision regarding the identification of recurring tasks and the creation of a custom model. Specifically, we argue that model search and transfer learning will play a crucial role in JITR to efficiently identify and fine-tune models for a recurring task. Using our JITR prototype Poodle, we achieve significant savings for exemplary tasks.

