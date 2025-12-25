---
layout: default
title: Clever Hans in Chemistry: Chemist Style Signals Confound Activity Prediction on Public Benchmarks
---

# Clever Hans in Chemistry: Chemist Style Signals Confound Activity Prediction on Public Benchmarks
**arXiv**：[2512.20924v1](https://arxiv.org/abs/2512.20924) · [PDF](https://arxiv.org/pdf/2512.20924.pdf)  
**作者**：Andrew D. Blevins, Ian K. Quigley  

**一句话要点**：揭示化学数据中化学家风格信号导致活性预测偏差，提出作者分离分割方法以解决此问题

**关键词**：化学信息学, 机器学习偏差, 数据泄露, 结构-活性关系, 作者分离分割, 公共基准测试

## 3 点简述
- 核心问题：机器学习模型可能利用化学家意图而非因果结构-活性关系预测生物活性，导致‘Clever Hans’失败模式
- 方法要点：通过链接CHEMBL数据与作者信息，训练分类器预测作者，并构建仅基于作者概率向量的活性模型
- 实验或效果：作者仅模型预测能力与简单基线相当，表明化学家风格信号在公共基准中显著影响预测结果

## 摘要（原文）

> Can machine learning models identify which chemist made a molecule from structure alone? If so, models trained on literature data may exploit chemist intent rather than learning causal structure-activity relationships. We test this by linking CHEMBL assays to publication authors and training a 1,815-class classifier to predict authors from molecular fingerprints, achieving 60% top-5 accuracy under scaffold-based splitting. We then train an activity model that receives only a protein identifier and an author-probability vector derived from structure, with no direct access to molecular descriptors. This author-only model achieves predictive power comparable to a simple baseline that has access to structure. This reveals a "Clever Hans" failure mode: models can predict bioactivity largely by inferring chemist goals and favorite targets without requiring a lab-independent understanding of chemistry. We analyze the sources of this leakage, propose author-disjoint splits, and recommend dataset practices to decouple chemist intent from biological outcomes.

