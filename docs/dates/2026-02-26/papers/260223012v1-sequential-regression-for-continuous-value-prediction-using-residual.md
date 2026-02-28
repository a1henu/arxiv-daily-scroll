---
layout: default
title: Sequential Regression for Continuous Value Prediction using Residual Quantization
---

# Sequential Regression for Continuous Value Prediction using Residual Quantization
**arXiv**：[2602.23012v1](https://arxiv.org/abs/2602.23012) · [PDF](https://arxiv.org/pdf/2602.23012.pdf)  
**作者**：Runpeng Cui, Zhipeng Sun, Chi Lu, Peng Jiang  

**一句话要点**：提出基于残差量化的序列学习框架，用于推荐系统中的连续值预测任务。

**关键词**：连续值预测, 残差量化, 序列学习, 推荐系统, 表示学习, 量化误差

## 3 点简述
- 核心问题：连续值预测面临数据分布复杂和长尾的挑战，现有生成方法依赖参数化分布假设，性能受限。
- 方法要点：将目标连续值表示为有序量化码之和，通过从粗到细的递归预测减少量化误差，并引入表示学习目标对齐嵌入空间。
- 实验或效果：在LTV、观看时长预测基准和工业短视频平台GMV预测实验中，均优于现有方法，展现强泛化能力。

## 摘要（原文）

> Continuous value prediction plays a crucial role in industrial-scale recommendation systems, including tasks such as predicting users' watch-time and estimating the gross merchandise value (GMV) in e-commerce transactions. However, it remains challenging due to the highly complex and long-tailed nature of the data distributions. Existing generative approaches rely on rigid parametric distribution assumptions, which fundamentally limits their performance when such assumptions misalign with real-world data. Overly simplified forms cannot adequately model real-world complexities, while more intricate assumptions often suffer from poor scalability and generalization.
>   To address these challenges, we propose a residual quantization (RQ)-based sequence learning framework that represents target continuous values as a sum of ordered quantization codes, predicted recursively from coarse to fine granularity with diminishing quantization errors. We introduce a representation learning objective that aligns RQ code embedding space with the ordinal structure of target values, allowing the model to capture continuous representations for quantization codes and further improving prediction accuracy. We perform extensive evaluations on public benchmarks for lifetime value (LTV) and watch-time prediction, alongside a large-scale online experiment for GMV prediction on an industrial short-video recommendation platform. The results consistently show that our approach outperforms state-of-the-art methods, while demonstrating strong generalization across diverse continuous value prediction tasks in recommendation systems.

