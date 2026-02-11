---
layout: default
title: Why the Counterintuitive Phenomenon of Likelihood Rarely Appears in Tabular Anomaly Detection with Deep Generative Models?
---

# Why the Counterintuitive Phenomenon of Likelihood Rarely Appears in Tabular Anomaly Detection with Deep Generative Models?
**arXiv**：[2602.09593v1](https://arxiv.org/abs/2602.09593) · [PDF](https://arxiv.org/pdf/2602.09593.pdf)  
**作者**：Donghwan Kim, Junghun Phee, Hyunsoo Yoon  

**一句话要点**：提出领域无关公式化方法，证明表格异常检测中深度生成模型的反直觉似然现象罕见

**关键词**：表格异常检测, 深度生成模型, 似然评分, 正常化流, 反直觉现象, 数据维度分析

## 3 点简述
- 核心问题：深度生成模型在图像域常为异常数据分配更高似然，但在表格域此反直觉现象是否常见未知
- 方法要点：引入领域无关公式化，统一检测与评估反直觉现象，聚焦数据维度和特征相关性差异
- 实验或效果：在47个表格数据集和10个CV/NLP嵌入数据集上实验，基于13个基线模型，证明现象在表格数据中罕见

## 摘要（原文）

> Deep generative models with tractable and analytically computable likelihoods, exemplified by normalizing flows, offer an effective basis for anomaly detection through likelihood-based scoring. We demonstrate that, unlike in the image domain where deep generative models frequently assign higher likelihoods to anomalous data, such counterintuitive behavior occurs far less often in tabular settings. We first introduce a domain-agnostic formulation that enables consistent detection and evaluation of the counterintuitive phenomenon, addressing the absence of precise definition. Through extensive experiments on 47 tabular datasets and 10 CV/NLP embedding datasets in ADBench, benchmarked against 13 baseline models, we demonstrate that the phenomenon, as defined, is consistently rare in general tabular data. We further investigate this phenomenon from both theoretical and empirical perspectives, focusing on the roles of data dimensionality and difference in feature correlation. Our results suggest that likelihood-only detection with normalizing flows offers a practical and reliable approach for anomaly detection in tabular domains.

