---
layout: default
title: Exploring Fine-Tuning for Tabular Foundation Models
---

# Exploring Fine-Tuning for Tabular Foundation Models
**arXiv**：[2601.09654v1](https://arxiv.org/abs/2601.09654) · [PDF](https://arxiv.org/pdf/2601.09654.pdf)  
**作者**：Aditya Tanna, Pratinav Seth, Mohamed Bouadi, Vinay Kumar Sankarapu  

**一句话要点**：探索表格基础模型的微调效果，分析其在不同数据集条件下的性能与局限性

**关键词**：表格基础模型, 微调策略, 零样本学习, 参数高效微调, 数据集分析

## 3 点简述
- 核心问题：表格基础模型微调的有效性及影响因素，如数据集不平衡、大小和维度
- 方法要点：比较零样本、元学习、全监督微调和参数高效微调方法，评估性能、校准和公平性
- 实验或效果：发现微调收益高度依赖模型和数据，全监督微调常降低准确性或校准质量

## 摘要（原文）

> Tabular Foundation Models (TFMs) have recently shown strong in-context learning capabilities on structured data, achieving zero-shot performance comparable to traditional machine learning methods. We find that zero-shot TFMs already achieve strong performance, while the benefits of fine-tuning are highly model and data-dependent. Meta-learning and PEFT provide moderate gains under specific conditions, whereas full supervised fine-tuning (SFT) often reduces accuracy or calibration quality. This work presents the first comprehensive study of fine-tuning in TFMs across benchmarks including TALENT, OpenML-CC18, and TabZilla. We compare Zero-Shot, Meta-Learning, Supervised (SFT), and parameter-efficient (PEFT) approaches, analyzing how dataset factors such as imbalance, size, and dimensionality affect outcomes. Our findings cover performance, calibration, and fairness, offering practical guidelines on when fine-tuning is most beneficial and its limitations.

