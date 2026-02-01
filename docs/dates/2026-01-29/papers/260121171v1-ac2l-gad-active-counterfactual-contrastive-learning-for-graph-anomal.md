---
layout: default
title: AC2L-GAD: Active Counterfactual Contrastive Learning for Graph Anomaly Detection
---

# AC2L-GAD: Active Counterfactual Contrastive Learning for Graph Anomaly Detection
**arXiv**：[2601.21171v1](https://arxiv.org/abs/2601.21171) · [PDF](https://arxiv.org/pdf/2601.21171.pdf)  
**作者**：Kamal Berahmand, Saman Forouzandeh, Mehrnoush Mohammadi, Parham Moradi, Mahdi Jalili  

**一句话要点**：提出AC2L-GAD框架，通过主动反事实对比学习解决图异常检测中的标签稀缺和类别不平衡问题。

**关键词**：图异常检测, 对比学习, 反事实推理, 主动学习, 计算优化, 金融交易图

## 3 点简述
- 核心问题：图异常检测面临标签稀缺和极端类别不平衡，现有对比学习方法存在语义不一致和负样本简单化问题。
- 方法要点：结合信息论主动选择和反事实生成，生成异常保留的正样本增强和正常负样本对比，减少计算开销约65%。
- 实验或效果：在九个基准数据集上表现竞争或优于先进基线，尤其在异常具有复杂属性-结构交互的数据集中增益显著。

## 摘要（原文）

> Graph anomaly detection aims to identify abnormal patterns in networks, but faces significant challenges from label scarcity and extreme class imbalance. While graph contrastive learning offers a promising unsupervised solution, existing methods suffer from two critical limitations: random augmentations break semantic consistency in positive pairs, while naive negative sampling produces trivial, uninformative contrasts. We propose AC2L-GAD, an Active Counterfactual Contrastive Learning framework that addresses both limitations through principled counterfactual reasoning. By combining information-theoretic active selection with counterfactual generation, our approach identifies structurally complex nodes and generates anomaly-preserving positive augmentations alongside normal negative counterparts that provide hard contrasts, while restricting expensive counterfactual generation to a strategically selected subset. This design reduces computational overhead by approximately 65% compared to full-graph counterfactual generation while maintaining detection quality. Experiments on nine benchmark datasets, including real-world financial transaction graphs from GADBench, show that AC2L-GAD achieves competitive or superior performance compared to state-of-the-art baselines, with notable gains in datasets where anomalies exhibit complex attribute-structure interactions.

