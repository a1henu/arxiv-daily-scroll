---
layout: default
title: Detecting High-Potential SMEs with Heterogeneous Graph Neural Networks
---

# Detecting High-Potential SMEs with Heterogeneous Graph Neural Networks
**arXiv**：[2602.19591v1](https://arxiv.org/abs/2602.19591) · [PDF](https://arxiv.org/pdf/2602.19591.pdf)  
**作者**：Yijiashun Qi, Hanzhe Guo, Yijiazhen Qi  

**一句话要点**：提出SME-HGT异构图Transformer框架，利用公开数据预测中小企业获得SBIR二期资助的潜力。

**关键词**：异构图神经网络, 中小企业潜力评估, SBIR资助预测, 图Transformer, 公开数据利用

## 3 点简述
- 核心问题：中小企业占美国企业99.9%，但系统识别高潜力中小企业仍具挑战。
- 方法要点：构建异构图连接公司、研究主题和政府机构，使用Transformer预测资助进展。
- 实验或效果：在时间分割测试集上AUPRC达0.621，优于基线模型，筛选精度提升显著。

## 摘要（原文）

> Small and Medium Enterprises (SMEs) constitute 99.9% of U.S. businesses and generate 44% of economic activity, yet systematically identifying high-potential SMEs remains an open challenge. We introduce SME-HGT, a Heterogeneous Graph Transformer framework that predicts which SBIR Phase I awardees will advance to Phase II funding using exclusively public data. We construct a heterogeneous graph with 32,268 company nodes, 124 research topic nodes, and 13 government agency nodes connected by approximately 99,000 edges across three semantic relation types. SME-HGT achieves an AUPRC of 0.621 0.003 on a temporally-split test set, outperforming an MLP baseline (0.590 0.002) and R-GCN (0.608 0.013) across five random seeds. At a screening depth of 100 companies, SME-HGT attains 89.6% precision with a 2.14 lift over random selection. Our temporal evaluation protocol prevents information leakage, and our reliance on public data ensures reproducibility. These results demonstrate that relational structure among firms, research topics, and funding agencies provides meaningful signal for SME potential assessment, with implications for policymakers and early-stage investors.

