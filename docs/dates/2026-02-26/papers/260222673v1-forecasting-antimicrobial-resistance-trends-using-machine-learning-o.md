---
layout: default
title: Forecasting Antimicrobial Resistance Trends Using Machine Learning on WHO GLASS Surveillance Data: A Retrieval-Augmented Generation Approach for Policy Decision Support
---

# Forecasting Antimicrobial Resistance Trends Using Machine Learning on WHO GLASS Surveillance Data: A Retrieval-Augmented Generation Approach for Policy Decision Support
**arXiv**：[2602.22673v1](https://arxiv.org/abs/2602.22673) · [PDF](https://arxiv.org/pdf/2602.22673.pdf)  
**作者**：Md Tanvir Hasan Turja  

**一句话要点**：提出基于机器学习和检索增强生成的框架，以预测抗菌素耐药性趋势并支持政策决策

**关键词**：抗菌素耐药性预测, 机器学习基准测试, 检索增强生成, WHO GLASS数据, 政策决策支持

## 3 点简述
- 核心问题：抗菌素耐药性（AMR）是全球危机，需基于WHO GLASS数据预测趋势以支持政策。
- 方法要点：使用六种机器学习模型（如XGBoost）进行预测，并集成检索增强生成（RAG）提供政策建议。
- 实验或效果：XGBoost在测试集上MAE为7.07%，R平方为0.854，优于基线83.1%；RAG结合WHO文档生成可信政策答案。

## 摘要（原文）

> Antimicrobial resistance (AMR) is a growing global crisis projected to cause 10 million deaths per year by 2050. While the WHO Global Antimicrobial Resistance and Use Surveillance System (GLASS) provides standardized surveillance data across 44 countries, few studies have applied machine learning to forecast population-level resistance trends from this data. This paper presents a two-component framework for AMR trend forecasting and evidence-grounded policy decision support. We benchmark six models -- Naive, Linear Regression, Ridge Regression, XGBoost, LightGBM, and LSTM -- on 5,909 WHO GLASS observations across six WHO regions (2021-2023). XGBoost achieved the best performance with a test MAE of 7.07% and R-squared of 0.854, outperforming the naive baseline by 83.1%. Feature importance analysis identified the prior-year resistance rate as the dominant predictor (50.5% importance), while regional MAE ranged from 4.16% (European Region) to 10.14% (South-East Asia Region). We additionally implemented a Retrieval-Augmented Generation (RAG) pipeline combining a ChromaDB vector store of WHO policy documents with a locally deployed Phi-3 Mini language model, producing source-attributed, hallucination-constrained policy answers. Code and data are available at https://github.com/TanvirTurja

