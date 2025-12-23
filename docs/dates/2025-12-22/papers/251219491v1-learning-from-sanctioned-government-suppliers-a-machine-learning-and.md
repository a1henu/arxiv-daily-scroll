---
layout: default
title: Learning from sanctioned government suppliers: A machine learning and network science approach to detecting fraud and corruption in Mexico
---

# Learning from sanctioned government suppliers: A machine learning and network science approach to detecting fraud and corruption in Mexico
**arXiv**：[2512.19491v1](https://arxiv.org/abs/2512.19491) · [PDF](https://arxiv.org/pdf/2512.19491.pdf)  
**作者**：Martí Medina-Hern ández, Janos Kertész, Mihály Fazekas  

**一句话要点**：提出正未标记学习结合网络特征的方法，以检测墨西哥政府采购中的欺诈与腐败

**关键词**：正未标记学习, 政府采购欺诈检测, 网络科学, 腐败风险指标, 墨西哥公共采购

## 3 点简述
- 核心问题：政府采购欺诈检测缺乏确认的非腐败负样本，传统监督学习不适用。
- 方法要点：使用正未标记学习算法，整合基于领域知识的红旗特征和网络衍生特征。
- 实验或效果：最佳模型比随机猜测平均提升2.3倍，网络特征如特征向量中心性最重要。

## 摘要（原文）

> Detecting fraud and corruption in public procurement remains a major challenge for governments worldwide. Most research to-date builds on domain-knowledge-based corruption risk indicators of individual contract-level features and some also analyzes contracting network patterns. A critical barrier for supervised machine learning is the absence of confirmed non-corrupt, negative, examples, which makes conventional machine learning inappropriate for this task. Using publicly available data on federally funded procurement in Mexico and company sanction records, this study implements positive-unlabeled (PU) learning algorithms that integrate domain-knowledge-based red flags with network-derived features to identify likely corrupt and fraudulent contracts. The best-performing PU model on average captures 32 percent more known positives and performs on average 2.3 times better than random guessing, substantially outperforming approaches based solely on traditional red flags. The analysis of the Shapley Additive Explanations reveals that network-derived features, particularly those associated with contracts in the network core or suppliers with high eigenvector centrality, are the most important. Traditional red flags further enhance model performance in line with expectations, albeit mainly for contracts awarded through competitive tenders. This methodology can support law enforcement in Mexico, and it can be adapted to other national contexts too.

