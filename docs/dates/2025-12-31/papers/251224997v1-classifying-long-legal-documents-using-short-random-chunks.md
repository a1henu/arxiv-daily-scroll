---
layout: default
title: Classifying long legal documents using short random chunks
---

# Classifying long legal documents using short random chunks
**arXiv**：[2512.24997v1](https://arxiv.org/abs/2512.24997) · [PDF](https://arxiv.org/pdf/2512.24997.pdf)  
**作者**：Luis Adrián Cabrera-Diego  

**一句话要点**：提出基于DeBERTa V3和LSTM的随机短块分类方法，以解决长法律文档分类的挑战。

**关键词**：长文档分类, 法律文本处理, 随机块采样, DeBERTa V3, LSTM, Temporal部署

## 3 点简述
- 核心问题：长法律文档分类因文档长度和专用词汇导致Transformer模型处理困难、昂贵或缓慢。
- 方法要点：使用48个随机选择的短块（最多128个令牌）作为输入，结合DeBERTa V3和LSTM构建分类器。
- 实验或效果：最佳模型加权F分数为0.898，CPU上处理100个文件的流程中位时间为498秒。

## 摘要（原文）

> Classifying legal documents is a challenge, besides their specialized vocabulary, sometimes they can be very long. This means that feeding full documents to a Transformers-based models for classification might be impossible, expensive or slow. Thus, we present a legal document classifier based on DeBERTa V3 and a LSTM, that uses as input a collection of 48 randomly-selected short chunks (max 128 tokens). Besides, we present its deployment pipeline using Temporal, a durable execution solution, which allow us to have a reliable and robust processing workflow. The best model had a weighted F-score of 0.898, while the pipeline running on CPU had a processing median time of 498 seconds per 100 files.

