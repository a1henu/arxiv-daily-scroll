---
layout: default
title: Drift-Aware Variational Autoencoder-based Anomaly Detection with Two-level Ensembling
---

# Drift-Aware Variational Autoencoder-based Anomaly Detection with Two-level Ensembling
**arXiv**：[2602.12976v1](https://arxiv.org/abs/2602.12976) · [PDF](https://arxiv.org/pdf/2602.12976.pdf)  
**作者**：Jin Li, Kleanthis Malialis, Christos G. Panayiotou, Marios M. Polycarpou  

**一句话要点**：提出VAE++ESDD方法，通过增量学习和两级集成解决非平稳环境中的异常检测问题。

**关键词**：异常检测, 概念漂移, 变分自编码器, 集成学习, 增量学习, 非平稳环境

## 3 点简述
- 核心问题：非平稳环境中概念漂移导致异常检测模型性能下降，数据无标签且异常率极低。
- 方法要点：使用变分自编码器集成进行异常预测，结合统计概念漂移检测器集成，支持增量学习。
- 实验或效果：在真实和合成数据集上验证，显著优于强基线和先进方法，适用于严重漂移场景。

## 摘要（原文）

> In today's digital world, the generation of vast amounts of streaming data in various domains has become ubiquitous. However, many of these data are unlabeled, making it challenging to identify events, particularly anomalies. This task becomes even more formidable in nonstationary environments where model performance can deteriorate over time due to concept drift. To address these challenges, this paper presents a novel method, VAE++ESDD, which employs incremental learning and two-level ensembling: an ensemble of Variational AutoEncoder(VAEs) for anomaly prediction, along with an ensemble of concept drift detectors. Each drift detector utilizes a statistical-based concept drift mechanism. To evaluate the effectiveness of VAE++ESDD, we conduct a comprehensive experimental study using real-world and synthetic datasets characterized by severely or extremely low anomalous rates and various drift characteristics. Our study reveals that the proposed method significantly outperforms both strong baselines and state-of-the-art methods.

