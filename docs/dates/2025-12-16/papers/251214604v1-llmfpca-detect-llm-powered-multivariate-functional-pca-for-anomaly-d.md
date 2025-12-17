---
layout: default
title: LLmFPCA-detect: LLM-powered Multivariate Functional PCA for Anomaly Detection in Sparse Longitudinal Texts
---

# LLmFPCA-detect: LLM-powered Multivariate Functional PCA for Anomaly Detection in Sparse Longitudinal Texts
**arXiv**：[2512.14604v1](https://arxiv.org/abs/2512.14604) · [PDF](https://arxiv.org/pdf/2512.14604.pdf)  
**作者**：Prasanjit Dubey, Aritra Guha, Zhengyi Zhou, Qiong Wu, Xiaoming Huo, Paromita Dubey  

**一句话要点**：提出LLmFPCA-detect框架，结合LLM嵌入与功能数据分析，用于稀疏纵向文本的异常检测与聚类

**关键词**：稀疏纵向文本分析, 功能主成分分析, 异常检测, LLM文本嵌入, 聚类分析, 动态关键词分析

## 3 点简述
- 核心问题：稀疏纵向文本数据（如客户评论、社交媒体帖子）因观测频率和时机不一，缺乏专用方法，难以检测关键模式和异常
- 方法要点：使用LLM提示将文本嵌入数值空间，应用稀疏多元功能主成分分析恢复群体特征，结合静态协变量进行数据分割和异常检测
- 实验或效果：在亚马逊评论和维基百科评论数据集上验证，优于现有基线，并提升下游预测性能

## 摘要（原文）

> Sparse longitudinal (SL) textual data arises when individuals generate text repeatedly over time (e.g., customer reviews, occasional social media posts, electronic medical records across visits), but the frequency and timing of observations vary across individuals. These complex textual data sets have immense potential to inform future policy and targeted recommendations. However, because SL text data lack dedicated methods and are noisy, heterogeneous, and prone to anomalies, detecting and inferring key patterns is challenging. We introduce LLmFPCA-detect, a flexible framework that pairs LLM-based text embeddings with functional data analysis to detect clusters and infer anomalies in large SL text datasets. First, LLmFPCA-detect embeds each piece of text into an application-specific numeric space using LLM prompts. Sparse multivariate functional principal component analysis (mFPCA) conducted in the numeric space forms the workhorse to recover primary population characteristics, and produces subject-level scores which, together with baseline static covariates, facilitate data segmentation, unsupervised anomaly detection and inference, and enable other downstream tasks. In particular, we leverage LLMs to perform dynamic keyword profiling guided by the data segments and anomalies discovered by LLmFPCA-detect, and we show that cluster-specific functional PC scores from LLmFPCA-detect, used as features in existing pipelines, help boost prediction performance. We support the stability of LLmFPCA-detect with experiments and evaluate it on two different applications using public datasets, Amazon customer-review trajectories, and Wikipedia talk-page comment streams, demonstrating utility across domains and outperforming state-of-the-art baselines.

