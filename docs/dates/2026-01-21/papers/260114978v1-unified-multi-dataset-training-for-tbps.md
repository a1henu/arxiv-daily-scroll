---
layout: default
title: Unified Multi-Dataset Training for TBPS
---

# Unified Multi-Dataset Training for TBPS
**arXiv**：[2601.14978v1](https://arxiv.org/abs/2601.14978) · [PDF](https://arxiv.org/pdf/2601.14978.pdf)  
**作者**：Nilanjana Chatterjee, Sidharatha Garg, A V Subramanyam, Brejesh Lall  

**一句话要点**：提出Scale-TBPS方法，通过噪声感知数据集合并和可扩展身份学习框架，实现跨多数据集的统一文本行人搜索模型训练。

**关键词**：文本行人搜索, 多数据集训练, 噪声感知学习, 身份识别框架, 视觉语言模型

## 3 点简述
- 核心问题：现有文本行人搜索方法依赖数据集特定微调，导致模型分散，无法统一训练。
- 方法要点：引入噪声感知数据集合并策略和可扩展身份学习框架，以处理多数据集中的噪声和大规模身份识别。
- 实验或效果：在多个数据集上验证，单一Scale-TBPS模型优于数据集特定优化模型和简单联合训练。

## 摘要（原文）

> Text-Based Person Search (TBPS) has seen significant progress with vision-language models (VLMs), yet it remains constrained by limited training data and the fact that VLMs are not inherently pre-trained for pedestrian-centric recognition. Existing TBPS methods therefore rely on dataset-centric fine-tuning to handle distribution shift, resulting in multiple independently trained models for different datasets. While synthetic data can increase the scale needed to fine-tune VLMs, it does not eliminate dataset-specific adaptation. This motivates a fundamental question: can we train a single unified TBPS model across multiple datasets? We show that naive joint training over all datasets remains sub-optimal because current training paradigms do not scale to a large number of unique person identities and are vulnerable to noisy image-text pairs. To address these challenges, we propose Scale-TBPS with two contributions: (i) a noise-aware unified dataset curation strategy that cohesively merges diverse TBPS datasets; and (ii) a scalable discriminative identity learning framework that remains effective under a large number of unique identities. Extensive experiments on CUHK-PEDES, ICFG-PEDES, RSTPReid, IIITD-20K, and UFine6926 demonstrate that a single Scale-TBPS model outperforms dataset-centric optimized models and naive joint training.

