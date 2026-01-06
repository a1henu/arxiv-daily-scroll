---
layout: default
title: Multivariate Time-series Anomaly Detection via Dynamic Model Pool & Ensembling
---

# Multivariate Time-series Anomaly Detection via Dynamic Model Pool & Ensembling
**arXiv**：[2601.02037v1](https://arxiv.org/abs/2601.02037) · [PDF](https://arxiv.org/pdf/2601.02037.pdf)  
**作者**：Wei Hu, Zewei Yu, Jianqiu Xu  

**一句话要点**：提出DMPEAD框架，通过动态模型池与集成解决多元时间序列异常检测的局限性。

**关键词**：多元时间序列, 异常检测, 动态模型池, 模型集成, 参数转移, 多样性度量

## 3 点简述
- 核心问题：现有多模型方法在模型选择、集成策略和数据维度固定性方面存在不足。
- 方法要点：构建动态模型池，通过参数转移和多样性度量，结合元模型进行自适应更新与集成。
- 实验或效果：在8个真实数据集上优于基线，展示出更好的适应性和可扩展性。

## 摘要（原文）

> Multivariate time-series (MTS) anomaly detection is critical in domains such as service monitor, IoT, and network security. While multi-model methods based on selection or ensembling outperform single-model ones, they still face limitations: (i) selection methods rely on a single chosen model and are sensitive to the strategy; (ii) ensembling methods often combine all models or are restricted to univariate data; and (iii) most methods depend on fixed data dimensionality, limiting scalability. To address these, we propose DMPEAD, a Dynamic Model Pool and Ensembling framework for MTS Anomaly Detection. The framework first (i) constructs a diverse model pool via parameter transfer and diversity metric, then (ii) updates it with a meta-model and similarity-based strategy for adaptive pool expansion, subset selection, and pool merging, finally (iii) ensembles top-ranked models through proxy metric ranking and top-k aggregation in the selected subset, outputting the final anomaly detection result. Extensive experiments on 8 real-world datasets show that our model outperforms all baselines, demonstrating superior adaptability and scalability.

