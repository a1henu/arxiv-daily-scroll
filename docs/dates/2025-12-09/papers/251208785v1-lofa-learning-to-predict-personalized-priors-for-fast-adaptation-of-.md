---
layout: default
title: LoFA: Learning to Predict Personalized Priors for Fast Adaptation of Visual Generative Models
---

# LoFA: Learning to Predict Personalized Priors for Fast Adaptation of Visual Generative Models
**arXiv**：[2512.08785v1](https://arxiv.org/abs/2512.08785) · [PDF](https://arxiv.org/pdf/2512.08785.pdf)  
**作者**：Yiming Hao, Mutian Xu, Chongjie Ye, Jie Qin, Shunlin Lu, Yipeng Qin, Xiaoguang Han  

**一句话要点**：提出LoFA框架以快速预测个性化先验，实现视觉生成模型的高效适配

**关键词**：视觉生成模型, 个性化适配, 超网络, 快速优化, LoRA分布预测

## 3 点简述
- 核心问题：现有方法如LoRA需任务特定数据和长时间优化，超网络方法难以映射细粒度提示到复杂LoRA分布
- 方法要点：基于LoRA参数相对变化的结构化分布模式，设计两阶段超网络预测相对分布模式并指导最终权重预测
- 实验或效果：在多个任务和用户提示下，秒级预测高质量个性化先验，性能优于需数小时处理的传统LoRA

## 摘要（原文）

> Personalizing visual generative models to meet specific user needs has gained increasing attention, yet current methods like Low-Rank Adaptation (LoRA) remain impractical due to their demand for task-specific data and lengthy optimization. While a few hypernetwork-based approaches attempt to predict adaptation weights directly, they struggle to map fine-grained user prompts to complex LoRA distributions, limiting their practical applicability. To bridge this gap, we propose LoFA, a general framework that efficiently predicts personalized priors for fast model adaptation. We first identify a key property of LoRA: structured distribution patterns emerge in the relative changes between LoRA and base model parameters. Building on this, we design a two-stage hypernetwork: first predicting relative distribution patterns that capture key adaptation regions, then using these to guide final LoRA weight prediction. Extensive experiments demonstrate that our method consistently predicts high-quality personalized priors within seconds, across multiple tasks and user prompts, even outperforming conventional LoRA that requires hours of processing. Project page: https://jaeger416.github.io/lofa/.

