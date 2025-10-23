---
layout: default
title: Learning To Defer To A Population With Limited Demonstrations
---

# Learning To Defer To A Population With Limited Demonstrations
**arXiv**：[2510.19351v1](https://arxiv.org/abs/2510.19351) · [PDF](https://arxiv.org/pdf/2510.19351.pdf)  
**作者**：Nilesh Ramgolam, Gustavo Carneiro, Hsiang-Ting, Chen  

**一句话要点**：提出基于元学习的上下文感知半监督框架，以解决学习延迟系统中数据稀缺问题。

**关键词**：学习延迟, 元学习, 半监督学习, 专家嵌入, 伪标签生成, 自适应系统

## 3 点简述
- 核心问题：学习延迟系统在部署中面临数据稀缺，限制其适应人群。
- 方法要点：使用元学习从少量演示生成专家特定嵌入，并用于伪标签生成和测试时适应。
- 实验或效果：在三个数据集上验证，模型通过合成标签训练快速接近Oracle性能。

## 摘要（原文）

> This paper addresses the critical data scarcity that hinders the practical
> deployment of learning to defer (L2D) systems to the population. We introduce a
> context-aware, semi-supervised framework that uses meta-learning to generate
> expert-specific embeddings from only a few demonstrations. We demonstrate the
> efficacy of a dual-purpose mechanism, where these embeddings are used first to
> generate a large corpus of pseudo-labels for training, and subsequently to
> enable on-the-fly adaptation to new experts at test-time. The experiment
> results on three different datasets confirm that a model trained on these
> synthetic labels rapidly approaches oracle-level performance, validating the
> data efficiency of our approach. By resolving a key training bottleneck, this
> work makes adaptive L2D systems more practical and scalable, paving the way for
> human-AI collaboration in real-world environments. To facilitate
> reproducibility and address implementation details not covered in the main
> text, we provide our source code and training configurations at
> https://github.com/nil123532/learning-to-defer-to-a-population-with-limited-demonstrations.

