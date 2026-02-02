---
layout: default
title: Metric Hub: A metric library and practical selection workflow for use-case-driven data quality assessment in medical AI
---

# Metric Hub: A metric library and practical selection workflow for use-case-driven data quality assessment in medical AI
**arXiv**：[2601.22702v1](https://arxiv.org/abs/2601.22702) · [PDF](https://arxiv.org/pdf/2601.22702.pdf)  
**作者**：Katinka Becker, Maximilian P. Oppelt, Tobias S. Zech, Martin Seyferth, Sandie Cabon, Vanja Miskovic, Ivan Cimrak, Michal Kozubek, Giuseppe D'Avenio, Ilaria Campioni, Jana Fehr, Kanjar De, Ismail Mahmoudi, Emilio Dolgener Cantu, Laurenz Ottmann, Andreas Klaß, Galaad Altares, Jackie Ma, Alireza Salehi M., Nadine R. Lang-Richter, Tobias Schaeffter, Daniel Schwabe  

**一句话要点**：提出Metric Hub库与选择流程，以支持医疗AI中基于用例的数据质量评估。

**关键词**：数据质量评估, 医疗AI, 度量库, 用例驱动, 可信赖AI, 心电图数据

## 3 点简述
- 核心问题：医疗AI需量化数据质量以建立可信赖性，但缺乏系统化评估方法。
- 方法要点：引入数据质量度量库，提供度量卡片和用例驱动的选择策略。
- 实验或效果：在PTB-XL心电图数据集上示例性展示方法影响。

## 摘要（原文）

> Machine learning (ML) in medicine has transitioned from research to concrete applications aimed at supporting several medical purposes like therapy selection, monitoring and treatment. Acceptance and effective adoption by clinicians and patients, as well as regulatory approval, require evidence of trustworthiness. A major factor for the development of trustworthy AI is the quantification of data quality for AI model training and testing. We have recently proposed the METRIC-framework for systematically evaluating the suitability (fit-for-purpose) of data for medical ML for a given task. Here, we operationalize this theoretical framework by introducing a collection of data quality metrics - the metric library - for practically measuring data quality dimensions. For each metric, we provide a metric card with the most important information, including definition, applicability, examples, pitfalls and recommendations, to support the understanding and implementation of these metrics. Furthermore, we discuss strategies and provide decision trees for choosing an appropriate set of data quality metrics from the metric library given specific use cases. We demonstrate the impact of our approach exemplarily on the PTB-XL ECG-dataset. This is a first step to enable fit-for-purpose evaluation of training and test data in practice as the base for establishing trustworthy AI in medicine.

