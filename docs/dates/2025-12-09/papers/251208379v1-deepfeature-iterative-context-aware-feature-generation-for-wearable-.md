---
layout: default
title: DeepFeature: Iterative Context-aware Feature Generation for Wearable Biosignals
---

# DeepFeature: Iterative Context-aware Feature Generation for Wearable Biosignals
**arXiv**：[2512.08379v1](https://arxiv.org/abs/2512.08379) · [PDF](https://arxiv.org/pdf/2512.08379.pdf)  
**作者**：Kaiwei Liu, Yuting He, Bufang Yang, Mu Yuan, Chun Man Victor Wong, Ho Pong Andrew Sze, Zhenyu Yan, Hongkai Chen  

**一句话要点**：提出DeepFeature框架，利用LLM生成可穿戴生物信号的任务感知特征以提升医疗应用性能

**关键词**：可穿戴生物信号, 特征生成, 大语言模型, 上下文感知, 迭代精炼, 医疗应用

## 3 点简述
- 核心问题：现有特征提取方法缺乏任务上下文知识，在高维空间难以优化，易产生代码错误
- 方法要点：集成专家知识与任务设置的多源生成机制，基于评估反馈的迭代特征精炼
- 实验或效果：在八项任务中平均AUROC提升4.21-9.67%，优于或持平现有方法

## 摘要（原文）

> Biosignals collected from wearable devices are widely utilized in healthcare applications. Machine learning models used in these applications often rely on features extracted from biosignals due to their effectiveness, lower data dimensionality, and wide compatibility across various model architectures. However, existing feature extraction methods often lack task-specific contextual knowledge, struggle to identify optimal feature extraction settings in high-dimensional feature space, and are prone to code generation and automation errors. In this paper, we propose DeepFeature, the first LLM-empowered, context-aware feature generation framework for wearable biosignals. DeepFeature introduces a multi-source feature generation mechanism that integrates expert knowledge with task settings. It also employs an iterative feature refinement process that uses feature assessment-based feedback for feature re-selection. Additionally, DeepFeature utilizes a robust multi-layer filtering and verification approach for robust feature-to-code translation to ensure that the extraction functions run without crashing. Experimental evaluation results show that DeepFeature achieves an average AUROC improvement of 4.21-9.67% across eight diverse tasks compared to baseline methods. It outperforms state-of-the-art approaches on five tasks while maintaining comparable performance on the remaining tasks.

