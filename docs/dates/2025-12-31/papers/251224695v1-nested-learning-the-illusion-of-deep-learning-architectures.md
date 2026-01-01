---
layout: default
title: Nested Learning: The Illusion of Deep Learning Architectures
---

# Nested Learning: The Illusion of Deep Learning Architectures
**arXiv**：[2512.24695v1](https://arxiv.org/abs/2512.24695) · [PDF](https://arxiv.org/pdf/2512.24695.pdf)  
**作者**：Ali Behrouz, Meisam Razaviyayn, Peilin Zhong, Vahab Mirrokni  

**一句话要点**：提出嵌套学习范式以增强模型表达与持续学习能力

**关键词**：嵌套学习, 持续学习, 自修改模型, 优化器设计, 记忆系统, 语言建模

## 3 点简述
- 核心问题：现有深度学习模型在持续学习、自改进和有效解决方案发现方面存在挑战
- 方法要点：通过嵌套优化问题表示模型，设计更富表达力的优化器和自修改学习模块
- 实验或效果：在语言建模、知识整合和少样本泛化等任务中展示有希望的结果

## 摘要（原文）

> Despite the recent progresses, particularly in developing Language Models, there are fundamental challenges and unanswered questions about how such models can continually learn/memorize, self-improve, and find effective solutions. In this paper, we present a new learning paradigm, called Nested Learning (NL), that coherently represents a machine learning model with a set of nested, multi-level, and/or parallel optimization problems, each of which with its own context flow. Through the lenses of NL, existing deep learning methods learns from data through compressing their own context flow, and in-context learning naturally emerges in large models. NL suggests a philosophy to design more expressive learning algorithms with more levels, resulting in higher-order in-context learning and potentially unlocking effective continual learning capabilities. We advocate for NL by presenting three core contributions: (1) Expressive Optimizers: We show that known gradient-based optimizers, such as Adam, SGD with Momentum, etc., are in fact associative memory modules that aim to compress the gradients' information (by gradient descent). Building on this insight, we present other more expressive optimizers with deep memory and/or more powerful learning rules; (2) Self-Modifying Learning Module: Taking advantage of NL's insights on learning algorithms, we present a sequence model that learns how to modify itself by learning its own update algorithm; and (3) Continuum Memory System: We present a new formulation for memory system that generalizes the traditional viewpoint of long/short-term memory. Combining our self-modifying sequence model with the continuum memory system, we present a continual learning module, called Hope, showing promising results in language modeling, knowledge incorporation, and few-shot generalization tasks, continual learning, and long-context reasoning tasks.

