---
layout: default
title: Can vision language models learn intuitive physics from interaction?
---

# Can vision language models learn intuitive physics from interaction?
**arXiv**：[2602.06033v1](https://arxiv.org/abs/2602.06033) · [PDF](https://arxiv.org/pdf/2602.06033.pdf)  
**作者**：Luca M. Schulze Buschoff, Konstantinos Voudouris, Can Demircan, Eric Schulz  

**一句话要点**：通过交互训练提升视觉语言模型的物理直觉，但泛化能力有限

**关键词**：视觉语言模型, 物理直觉学习, 强化学习, 交互训练, 泛化能力, 认知科学

## 3 点简述
- 预训练视觉语言模型缺乏物理世界直觉，监督微调效果不稳健。
- 基于认知科学假设，采用强化学习让模型通过环境交互学习物理动态。
- 交互训练能提升任务内性能，但无法实现跨任务的泛化物理直觉。

## 摘要（原文）

> Pre-trained vision language models do not have good intuitions about the physical world. Recent work has shown that supervised fine-tuning can improve model performance on simple physical tasks. However, fine-tuned models do not appear to learn robust physical rules that can generalize to new contexts. Based on research in cognitive science, we hypothesize that models need to interact with an environment to properly learn its physical dynamics. We train models that learn through interaction with the environment using reinforcement learning. While learning from interaction allows models to improve their within-task performance, it fails to produce models with generalizable physical intuitions. We find that models trained on one task do not reliably generalize to related tasks, even if the tasks share visual statistics and physical principles, and regardless of whether the models are trained through interaction.

