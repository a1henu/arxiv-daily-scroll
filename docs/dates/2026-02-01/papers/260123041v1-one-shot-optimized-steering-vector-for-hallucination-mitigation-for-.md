---
layout: default
title: One-shot Optimized Steering Vector for Hallucination Mitigation for VLMs
---

# One-shot Optimized Steering Vector for Hallucination Mitigation for VLMs
**arXiv**：[2601.23041v1](https://arxiv.org/abs/2601.23041) · [PDF](https://arxiv.org/pdf/2601.23041.pdf)  
**作者**：Youxu Shi, Suorong Yang, Dong Liu  

**一句话要点**：提出OSGA框架，通过单次优化生成通用导向向量以缓解视觉语言模型的幻觉问题

**关键词**：视觉语言模型, 幻觉缓解, 导向向量, 单次优化, 安全增强, 输入无关框架

## 3 点简述
- 核心问题：视觉语言模型存在幻觉和安全失败，现有导向方法在效率与效果间需权衡
- 方法要点：基于语义意图对齐，OSGA通过方差数据选择和对比目标学习单导向向量，无需修改模型参数
- 实验或效果：在多个基准测试中，OSGA向量一致改善幻觉缓解和安全增强，开销可忽略

## 摘要（原文）

> Vision Language Models (VLMs) achieve strong performance on multimodal tasks but still suffer from hallucination and safety-related failures that persist even at scale. Steering offers a lightweight technique to improve model performance. However, steering, whether input-dependent or input-independent, achieves a meaningful trade-off between efficiency and effectiveness. In this work, we observe that steering vectors can generalize across inputs when tasks share aligned semantic intent. Based on this insight, we propose \textbf{OSGA} (\textbf{O}ne-shot \textbf{S}teering with \textbf{G}enerative \textbf{A}nchor), an input-independent framework that improves model performance with a single optimization instance. OSGA first selects an informative sample via a variance-based data selection strategy and learns a single steering vector with a contrastive objective with generative anchor regularization. The resulting vector can be universally applied at a certain layer during inference time without modifying model parameters. Experiments across multiple benchmarks show that a single OSGA-optimized steering vector consistently improves hallucination mitigation and safety enhancement with negligible overhead, highlighting one-shot steering as a practical and scalable solution for reliable VLMs.

