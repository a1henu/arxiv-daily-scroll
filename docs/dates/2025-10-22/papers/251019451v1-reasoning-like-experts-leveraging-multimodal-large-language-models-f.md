---
layout: default
title: Reasoning Like Experts: Leveraging Multimodal Large Language Models for Drawing-based Psychoanalysis
---

# Reasoning Like Experts: Leveraging Multimodal Large Language Models for Drawing-based Psychoanalysis
**arXiv**：[2510.19451v1](https://arxiv.org/abs/2510.19451) · [PDF](https://arxiv.org/pdf/2510.19451.pdf)  
**作者**：Xueqi Ma, Yanbei Jiang, Sarah Erfani, James Bailey, Weifeng Liu, Krista A. Ehinger, Jey Han Lau  

**一句话要点**：提出PICK框架，利用多模态大语言模型进行基于绘画的心理分析

**关键词**：多模态大语言模型, 心理分析, 绘画测试, 层次分析, 知识注入, 强化学习

## 3 点简述
- 核心问题：多模态大语言模型在主观情感领域如心理分析的应用尚少探索
- 方法要点：通过层次分解、知识注入和强化学习提取心理特征，构建多级分析
- 实验或效果：PICK显著提升心理分析能力，并验证为通用框架扩展至情感理解任务

## 摘要（原文）

> Multimodal Large Language Models (MLLMs) have demonstrated exceptional
> performance across various objective multimodal perception tasks, yet their
> application to subjective, emotionally nuanced domains, such as psychological
> analysis, remains largely unexplored. In this paper, we introduce PICK, a
> multi-step framework designed for Psychoanalytical Image Comprehension through
> hierarchical analysis and Knowledge injection with MLLMs, specifically focusing
> on the House-Tree-Person (HTP) Test, a widely used psychological assessment in
> clinical practice. First, we decompose drawings containing multiple instances
> into semantically meaningful sub-drawings, constructing a hierarchical
> representation that captures spatial structure and content across three levels:
> single-object level, multi-object level, and whole level. Next, we analyze
> these sub-drawings at each level with a targeted focus, extracting
> psychological or emotional insights from their visual cues. We also introduce
> an HTP knowledge base and design a feature extraction module, trained with
> reinforcement learning, to generate a psychological profile for single-object
> level analysis. This profile captures both holistic stylistic features and
> dynamic object-specific features (such as those of the house, tree, or person),
> correlating them with psychological states. Finally, we integrate these
> multi-faceted information to produce a well-informed assessment that aligns
> with expert-level reasoning. Our approach bridges the gap between MLLMs and
> specialized expert domains, offering a structured and interpretable framework
> for understanding human mental states through visual expression. Experimental
> results demonstrate that the proposed PICK significantly enhances the
> capability of MLLMs in psychological analysis. It is further validated as a
> general framework through extensions to emotion understanding tasks.

