---
layout: default
title: CC-OR-Net: A Unified Framework for LTV Prediction through Structural Decoupling
---

# CC-OR-Net: A Unified Framework for LTV Prediction through Structural Decoupling
**arXiv**：[2601.10176v1](https://arxiv.org/abs/2601.10176) · [PDF](https://arxiv.org/pdf/2601.10176.pdf)  
**作者**：Mingyu Zhao, Haoran Bai, Yu Tian, Bing Zhu, Hengliang Luo  

**一句话要点**：提出CC-OR-Net框架，通过结构分解解决LTV预测中的零膨胀和长尾分布问题。

**关键词**：客户终身价值预测, 结构分解, 排序回归, 长尾分布, 高价值用户增强

## 3 点简述
- 核心问题：LTV预测面临零膨胀和长尾分布，导致高价值用户被淹没且低中价值用户异质性大。
- 方法要点：采用结构分解，集成排序模块、残差模块和高价值增强模块，实现架构保证的排序。
- 实验或效果：在超过3亿用户的真实数据集上评估，优于现有方法，平衡全局准确性和高价值精度。

## 摘要（原文）

> Customer Lifetime Value (LTV) prediction, a central problem in modern marketing, is characterized by a unique zero-inflated and long-tail data distribution. This distribution presents two fundamental challenges: (1) the vast majority of low-to-medium value users numerically overwhelm the small but critically important segment of high-value "whale" users, and (2) significant value heterogeneity exists even within the low-to-medium value user base. Common approaches either rely on rigid statistical assumptions or attempt to decouple ranking and regression using ordered buckets; however, they often enforce ordinality through loss-based constraints rather than inherent architectural design, failing to balance global accuracy with high-value precision. To address this gap, we propose \textbf{C}onditional \textbf{C}ascaded \textbf{O}rdinal-\textbf{R}esidual Networks \textbf{(CC-OR-Net)}, a novel unified framework that achieves a more robust decoupling through \textbf{structural decomposition}, where ranking is architecturally guaranteed. CC-OR-Net integrates three specialized components: a \textit{structural ordinal decomposition module} for robust ranking, an \textit{intra-bucket residual module} for fine-grained regression, and a \textit{targeted high-value augmentation module} for precision on top-tier users. Evaluated on real-world datasets with over 300M users, CC-OR-Net achieves a superior trade-off across all key business metrics, outperforming state-of-the-art methods in creating a holistic and commercially valuable LTV prediction solution.

