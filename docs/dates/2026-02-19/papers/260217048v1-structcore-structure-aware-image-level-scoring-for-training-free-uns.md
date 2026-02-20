---
layout: default
title: StructCore: Structure-Aware Image-Level Scoring for Training-Free Unsupervised Anomaly Detection
---

# StructCore: Structure-Aware Image-Level Scoring for Training-Free Unsupervised Anomaly Detection
**arXiv**：[2602.17048v1](https://arxiv.org/abs/2602.17048) · [PDF](https://arxiv.org/pdf/2602.17048.pdf)  
**作者**：Joongwon Chae, Lihui Luo, Yang Liu, Runming Wang, Dongmei Yu, Zeming Liang, Xi Yuan, Dayan Zhang, Zhenglin Chen, Peiwu Qin, Ilmoon Chae  

**一句话要点**：提出StructCore以解决基于内存库的无监督异常检测中图像级评分忽略结构信息的问题。

**关键词**：无监督异常检测, 图像级评分, 结构感知, 内存库方法, 训练免费

## 3 点简述
- 核心问题：最大池化在图像级异常评分中丢弃异常证据的分布和空间结构信息，导致正常与异常分数重叠。
- 方法要点：通过计算低维结构描述符捕获异常得分图的结构特征，并使用训练样本估计对角马氏距离进行校准。
- 实验或效果：在MVTec AD和VisA数据集上分别达到99.6%和98.4%的图像级AUROC，优于最大池化。

## 摘要（原文）

> Max pooling is the de facto standard for converting anomaly score maps into image-level decisions in memory-bank-based unsupervised anomaly detection (UAD). However, because it relies on a single extreme response, it discards most information about how anomaly evidence is distributed and structured across the image, often causing normal and anomalous scores to overlap.
>   We propose StructCore, a training-free, structure-aware image-level scoring method that goes beyond max pooling. Given an anomaly score map, StructCore computes a low-dimensional structural descriptor phi(S) that captures distributional and spatial characteristics, and refines image-level scoring via a diagonal Mahalanobis calibration estimated from train-good samples, without modifying pixel-level localization.
>   StructCore achieves image-level AUROC scores of 99.6% on MVTec AD and 98.4% on VisA, demonstrating robust image-level anomaly detection by exploiting structural signatures missed by max pooling.

