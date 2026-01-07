---
layout: default
title: Empirical Comparison of Encoder-Based Language Models and Feature-Based Supervised Machine Learning Approaches to Automated Scoring of Long Essays
---

# Empirical Comparison of Encoder-Based Language Models and Feature-Based Supervised Machine Learning Approaches to Automated Scoring of Long Essays
**arXiv**：[2601.02659v1](https://arxiv.org/abs/2601.02659) · [PDF](https://arxiv.org/pdf/2601.02659.pdf)  
**作者**：Kuo Wang, Haowei Hua, Pengfei Yan, Hong Jiao, Dan Song  

**一句话要点**：提出集成嵌入模型，结合多预训练语言模型表示与梯度提升分类器，显著提升长作文自动评分性能。

**关键词**：长作文自动评分, 编码器语言模型, 集成学习, 梯度提升分类器, 二次加权Kappa

## 3 点简述
- 核心问题：长上下文对仅编码器语言模型在文本处理中构成挑战，特别是在长作文自动评分任务中。
- 方法要点：训练多种编码器模型，并与基于特征的监督机器学习模型进行性能比较，包括集成嵌入模型。
- 实验或效果：在17,307篇作文数据集上评估，集成嵌入模型在二次加权Kappa指标上显著优于单个语言模型。

## 摘要（原文）

> Long context may impose challenges for encoder-only language models in text processing, specifically for automated scoring of essays. This study trained several commonly used encoder-based language models for automated scoring of long essays. The performance of these trained models was evaluated and compared with the ensemble models built upon the base language models with a token limit of 512?. The experimented models include BERT-based models (BERT, RoBERTa, DistilBERT, and DeBERTa), ensemble models integrating embeddings from multiple encoder models, and ensemble models of feature-based supervised machine learning models, including Gradient-Boosted Decision Trees, eXtreme Gradient Boosting, and Light Gradient Boosting Machine. We trained, validated, and tested each model on a dataset of 17,307 essays, with an 80%/10%/10% split, and evaluated model performance using Quadratic Weighted Kappa. This study revealed that an ensemble-of-embeddings model that combines multiple pre-trained language model representations with gradient-boosting classifier as the ensemble model significantly outperforms individual language models at scoring long essays.

