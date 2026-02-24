---
layout: default
title: Unsupervised Anomaly Detection in NSL-KDD Using $β$-VAE: A Latent Space and Reconstruction Error Approach
---

# Unsupervised Anomaly Detection in NSL-KDD Using $β$-VAE: A Latent Space and Reconstruction Error Approach
**arXiv**：[2602.19785v1](https://arxiv.org/abs/2602.19785) · [PDF](https://arxiv.org/pdf/2602.19785.pdf)  
**作者**：Dylan Baptiste, Ramla Saddem, Alexandre Philippot, François Foyer  

**一句话要点**：提出基于β-VAE的无监督异常检测方法，应用于NSL-KDD网络流量数据集，比较潜在空间距离与重构误差两种策略。

**关键词**：无监督异常检测, β-VAE, NSL-KDD数据集, 潜在空间分析, 重构误差, 网络入侵检测

## 3 点简述
- 核心问题：在OT与IT融合背景下，网络入侵检测需求增加，需无监督方法处理未知攻击。
- 方法要点：使用β-VAE进行无监督学习，通过潜在空间距离和重构误差两种方式检测网络流量异常。
- 实验或效果：实验表明，潜在空间利用在分类任务中效果显著，优于传统重构误差方法。

## 摘要（原文）

> As Operational Technology increasingly integrates with Information Technology, the need for Intrusion Detection Systems becomes more important. This paper explores an unsupervised approach to anomaly detection in network traffic using $β$-Variational Autoencoders on the NSL-KDD dataset. We investigate two methods: leveraging the latent space structure by measuring distances from test samples to the training data projections, and using the reconstruction error as a conventional anomaly detection metric. By comparing these approaches, we provide insights into their respective advantages and limitations in an unsupervised setting. Experimental results highlight the effectiveness of latent space exploitation for classification tasks.

