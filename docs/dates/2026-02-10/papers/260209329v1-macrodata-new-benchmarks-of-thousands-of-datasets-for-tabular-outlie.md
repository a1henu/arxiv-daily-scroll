---
layout: default
title: MacrOData: New Benchmarks of Thousands of Datasets for Tabular Outlier Detection
---

# MacrOData: New Benchmarks of Thousands of Datasets for Tabular Outlier Detection
**arXiv**：[2602.09329v1](https://arxiv.org/abs/2602.09329) · [PDF](https://arxiv.org/pdf/2602.09329.pdf)  
**作者**：Xueying Ding, Simon Klüttermann, Haomin Wen, Yilong Chen, Leman Akoglu  

**一句话要点**：提出MacrOData大规模基准套件以解决表格异常检测基准规模小、多样性不足的问题

**关键词**：表格异常检测, 基准套件, 大规模数据集, 统计评估, 语义元数据, 在线排行榜

## 3 点简述
- 现有表格异常检测基准如AdBench仅含57个数据集，规模小限制多样性和统计效力
- MacrOData包含三个组件：OddBench（790个真实语义异常）、OvrBench（856个真实统计异常）和SynBench（800个合成数据集），共2446个数据集
- 提供标准化训练/测试分割、公开/私有基准分区、语义元数据标注，并进行广泛实验评估多种方法

## 摘要（原文）

> Quality benchmarks are essential for fairly and accurately tracking scientific progress and enabling practitioners to make informed methodological choices. Outlier detection (OD) on tabular data underpins numerous real-world applications, yet existing OD benchmarks remain limited. The prominent OD benchmark AdBench is the de facto standard in the literature, yet comprises only 57 datasets. In addition to other shortcomings discussed in this work, its small scale severely restricts diversity and statistical power. We introduce MacrOData, a large-scale benchmark suite for tabular OD comprising three carefully curated components: OddBench, with 790 datasets containing real-world semantic anomalies; OvrBench, with 856 datasets featuring real-world statistical outliers; and SynBench, with 800 synthetically generated datasets spanning diverse data priors and outlier archetypes. Owing to its scale and diversity, MacrOData enables comprehensive and statistically robust evaluation of tabular OD methods. Our benchmarks further satisfy several key desiderata: We provide standardized train/test splits for all datasets, public/private benchmark partitions with held-out test labels for the latter reserved toward an online leaderboard, and annotate our datasets with semantic metadata. We conduct extensive experiments across all benchmarks, evaluating a broad range of OD methods comprising classical, deep, and foundation models, over diverse hyperparameter configurations. We report detailed empirical findings, practical guidelines, as well as individual performances as references for future research. All benchmarks containing 2,446 datasets combined are open-sourced, along with a publicly accessible leaderboard hosted at https://huggingface.co/MacrOData-CMU.

