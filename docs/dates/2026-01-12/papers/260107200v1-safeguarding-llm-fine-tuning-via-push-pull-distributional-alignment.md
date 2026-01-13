---
layout: default
title: Safeguarding LLM Fine-tuning via Push-Pull Distributional Alignment
---

# Safeguarding LLM Fine-tuning via Push-Pull Distributional Alignment
**arXiv**：[2601.07200v1](https://arxiv.org/abs/2601.07200) · [PDF](https://arxiv.org/pdf/2601.07200.pdf)  
**作者**：Haozhong Wang, Zhuo Li, Yibo Yang, He Zhao, Hongyuan Zha, Dandan Guo  

**一句话要点**：提出Safety Optimal Transport框架，通过推拉分布对齐解决大语言模型微调中的安全侵蚀问题。

**关键词**：大语言模型安全, 微调防御, 分布对齐, 最优传输, 推拉机制, 安全-效用权衡

## 3 点简述
- 核心问题：大语言模型微调时安全对齐易受侵蚀，现有防御方法依赖启发式实例级评估，忽略数据分布全局几何结构。
- 方法要点：基于最优传输理论，引入双参考推拉权重学习机制，主动拉近下游分布至安全锚点并推离有害参考。
- 实验或效果：多模型和领域实验显示，SOT显著提升模型安全性，保持下游性能，实现更优安全-效用权衡。

## 摘要（原文）

> The inherent safety alignment of Large Language Models (LLMs) is prone to erosion during fine-tuning, even when using seemingly innocuous datasets. While existing defenses attempt to mitigate this via data selection, they typically rely on heuristic, instance-level assessments that neglect the global geometry of the data distribution and fail to explicitly repel harmful patterns. To address this, we introduce Safety Optimal Transport (SOT), a novel framework that reframes safe fine-tuning from an instance-level filtering challenge to a distribution-level alignment task grounded in Optimal Transport (OT). At its core is a dual-reference ``push-pull'' weight-learning mechanism: SOT optimizes sample importance by actively pulling the downstream distribution towards a trusted safe anchor while simultaneously pushing it away from a general harmful reference. This establishes a robust geometric safety boundary that effectively purifies the training data. Extensive experiments across diverse model families and domains demonstrate that SOT significantly enhances model safety while maintaining competitive downstream performance, achieving a superior safety-utility trade-off compared to baselines.

