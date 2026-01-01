---
layout: default
title: DTI-GP: Bayesian operations for drug-target interactions using deep kernel Gaussian processes
---

# DTI-GP: Bayesian operations for drug-target interactions using deep kernel Gaussian processes
**arXiv**：[2512.24810v1](https://arxiv.org/abs/2512.24810) · [PDF](https://arxiv.org/pdf/2512.24810.pdf)  
**作者**：Bence Bolgár, András Millinghoffer, Péter Antal  

**一句话要点**：提出DTI-GP，基于深度核高斯过程进行药物-靶点相互作用的贝叶斯预测与操作。

**关键词**：药物-靶点相互作用, 高斯过程, 深度核学习, 贝叶斯推断, 预测排名

## 3 点简述
- 核心问题：药物-靶点相互作用预测需精确概率信息以提升性能与理解局限性。
- 方法要点：结合深度核学习与高斯过程，集成神经嵌入模块进行贝叶斯推断。
- 实验或效果：在预测准确性、贝叶斯操作如拒绝分类和排名方面优于现有方法。

## 摘要（原文）

> Precise probabilistic information about drug-target interaction (DTI) predictions is vital for understanding limitations and boosting predictive performance. Gaussian processes (GP) offer a scalable framework to integrate state-of-the-art DTI representations and Bayesian inference, enabling novel operations, such as Bayesian classification with rejection, top-$K$ selection, and ranking. We propose a deep kernel learning-based GP architecture (DTI-GP), which incorporates a combined neural embedding module for chemical compounds and protein targets, and a GP module. The workflow continues with sampling from the predictive distribution to estimate a Bayesian precedence matrix, which is used in fast and accurate selection and ranking operations. DTI-GP outperforms state-of-the-art solutions, and it allows (1) the construction of a Bayesian accuracy-confidence enrichment score, (2) rejection schemes for improved enrichment, and (3) estimation and search for top-$K$ selections and ranking with high expected utility.

