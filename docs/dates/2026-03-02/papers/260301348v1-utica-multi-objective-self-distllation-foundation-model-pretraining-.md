---
layout: default
title: UTICA: Multi-Objective Self-Distllation Foundation Model Pretraining for Time Series Classification
---

# UTICA: Multi-Objective Self-Distllation Foundation Model Pretraining for Time Series Classification
**arXiv**：[2603.01348v1](https://arxiv.org/abs/2603.01348) · [PDF](https://arxiv.org/pdf/2603.01348.pdf)  
**作者**：Yessin Moakher, Youssef Attia El Hili, Vasilii Feofanov  

**一句话要点**：提出UTICA非对比自蒸馏预训练方法，用于时间序列分类基础模型。

**关键词**：时间序列分类, 自蒸馏预训练, 非对比学习, 基础模型, Transformer架构

## 3 点简述
- 核心问题：非对比方法在时间序列基础模型预训练中应用不足。
- 方法要点：基于DINOv2风格自蒸馏，结合Mantis分词器和Transformer编码器，通过学生-教师框架学习时间不变性和局部结构。
- 实验或效果：在UCR和UEA基准测试中达到最先进的分类性能。

## 摘要（原文）

> Self-supervised foundation models have achieved remarkable success across domains, including time series. However, the potential of non-contrastive methods, a paradigm that has driven significant advances in computer vision, remains underexplored for time series. In this work, we adapt DINOv2-style self-distillation to pretrain a time series foundation model, building on the Mantis tokenizer and transformer encoder architecture as our backbone. Through a student-teacher framework, our method Utica learns representations that capture both temporal invariance via augmented crops and fine-grained local structure via patch masking. Our approach achieves state-of-the-art classification performance on both UCR and UEA benchmarks. These results suggest that non-contrastive methods are a promising and complementary pretraining strategy for time series foundation models.

