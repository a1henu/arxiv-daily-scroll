---
layout: default
title: Demystifying Prediction Powered Inference
---

# Demystifying Prediction Powered Inference
**arXiv**：[2601.20819v1](https://arxiv.org/abs/2601.20819) · [PDF](https://arxiv.org/pdf/2601.20819.pdf)  
**作者**：Yilin Song, Dan M. Kluger, Harsh Parikh, Tian Gu  

**一句话要点**：提出预测增强推断统一框架，以利用未标注数据提升统计效率并保持有效推断。

**关键词**：预测增强推断, 统计推断, 偏差校正, 未标注数据, 置信区间, 缺失数据机制

## 3 点简述
- 核心问题：机器学习预测作为补充数据时，直接使用会引入偏差，忽略则浪费信息。
- 方法要点：通过小标注子集进行显式偏差校正，结合大未标注数据集预测，提供原则性推断框架。
- 实验或效果：在房价数据中，PPI变体比完整案例分析产生更紧置信区间，但数据重用导致反保守推断。

## 摘要（原文）

> Machine learning predictions are increasingly used to supplement incomplete or costly-to-measure outcomes in fields such as biomedical research, environmental science, and social science. However, treating predictions as ground truth introduces bias while ignoring them wastes valuable information. Prediction-Powered Inference (PPI) offers a principled framework that leverages predictions from large unlabeled datasets to improve statistical efficiency while maintaining valid inference through explicit bias correction using a smaller labeled subset. Despite its potential, the growing PPI variants and the subtle distinctions between them have made it challenging for practitioners to determine when and how to apply these methods responsibly. This paper demystifies PPI by synthesizing its theoretical foundations, methodological extensions, connections to existing statistics literature, and diagnostic tools into a unified practical workflow. Using the Mosaiks housing price data, we show that PPI variants produce tighter confidence intervals than complete-case analysis, but that double-dipping, i.e. reusing training data for inference, leads to anti-conservative confidence intervals and coverages. Under missing-not-at-random mechanisms, all methods, including classical inference using only labeled data, yield biased estimates. We provide a decision flowchart linking assumption violations to appropriate PPI variants, a summary table of selective methods, and practical diagnostic strategies for evaluating core assumptions. By framing PPI as a general recipe rather than a single estimator, this work bridges methodological innovation and applied practice, helping researchers responsibly integrate predictions into valid inference.

