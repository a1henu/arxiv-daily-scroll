---
layout: default
title: DesignPref: Capturing Personal Preferences in Visual Design Generation
---

# DesignPref: Capturing Personal Preferences in Visual Design Generation
**arXiv**：[2511.20513v1](https://arxiv.org/abs/2511.20513) · [PDF](https://arxiv.org/pdf/2511.20513.pdf)  
**作者**：Yi-Hao Peng, Jeffrey P. Bigham, Jason Wu  

**一句话要点**：提出DesignPref数据集以解决视觉设计生成中的个性化偏好建模问题

**关键词**：视觉设计生成, 个性化偏好建模, 数据集构建, UI设计评估, RAG管道, 微调策略

## 3 点简述
- 视觉设计偏好高度主观，专业设计师间存在显著分歧
- 引入12k对UI设计比较数据集，探索微调与RAG等个性化策略
- 个性化模型在预测个体偏好时优于聚合基线，样本效率高

## 摘要（原文）

> Generative models, such as large language models and text-to-image diffusion models, are increasingly used to create visual designs like user interfaces (UIs) and presentation slides. Finetuning and benchmarking these generative models have often relied on datasets of human-annotated design preferences. Yet, due to the subjective and highly personalized nature of visual design, preference varies widely among individuals. In this paper, we study this problem by introducing DesignPref, a dataset of 12k pairwise comparisons of UI design generation annotated by 20 professional designers with multi-level preference ratings. We found that among trained designers, substantial levels of disagreement exist (Krippendorff's alpha = 0.25 for binary preferences). Natural language rationales provided by these designers indicate that disagreements stem from differing perceptions of various design aspect importance and individual preferences. With DesignPref, we demonstrate that traditional majority-voting methods for training aggregated judge models often do not accurately reflect individual preferences. To address this challenge, we investigate multiple personalization strategies, particularly fine-tuning or incorporating designer-specific annotations into RAG pipelines. Our results show that personalized models consistently outperform aggregated baseline models in predicting individual designers' preferences, even when using 20 times fewer examples. Our work provides the first dataset to study personalized visual design evaluation and support future research into modeling individual design taste.

