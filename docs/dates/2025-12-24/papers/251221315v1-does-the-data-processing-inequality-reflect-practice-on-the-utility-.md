---
layout: default
title: Does the Data Processing Inequality Reflect Practice? On the Utility of Low-Level Tasks
---

# Does the Data Processing Inequality Reflect Practice? On the Utility of Low-Level Tasks
**arXiv**：[2512.21315v1](https://arxiv.org/abs/2512.21315) · [PDF](https://arxiv.org/pdf/2512.21315.pdf)  
**作者**：Roy Turgeman, Tom Tirer  

**一句话要点**：提出理论框架证明有限样本下低层处理提升分类精度，挑战数据处理不等式实践适用性。

**关键词**：数据处理不等式, 低层任务, 分类精度, 贝叶斯分类器, 去噪处理, 训练样本规模

## 3 点简述
- 核心问题：数据处理不等式在实践中的局限性，低层任务对分类的潜在益处。
- 方法要点：基于贝叶斯分类器理论分析，证明有限训练样本时预处理可提高准确率。
- 实验或效果：理论验证与基准数据集实证，展示去噪和编码对深度分类器性能的影响趋势。

## 摘要（原文）

> The data processing inequality is an information-theoretic principle stating that the information content of a signal cannot be increased by processing the observations. In particular, it suggests that there is no benefit in enhancing the signal or encoding it before addressing a classification problem. This assertion can be proven to be true for the case of the optimal Bayes classifier. However, in practice, it is common to perform "low-level" tasks before "high-level" downstream tasks despite the overwhelming capabilities of modern deep neural networks. In this paper, we aim to understand when and why low-level processing can be beneficial for classification. We present a comprehensive theoretical study of a binary classification setup, where we consider a classifier that is tightly connected to the optimal Bayes classifier and converges to it as the number of training samples increases. We prove that for any finite number of training samples, there exists a pre-classification processing that improves the classification accuracy. We also explore the effect of class separation, training set size, and class balance on the relative gain from this procedure. We support our theory with an empirical investigation of the theoretical setup. Finally, we conduct an empirical study where we investigate the effect of denoising and encoding on the performance of practical deep classifiers on benchmark datasets. Specifically, we vary the size and class distribution of the training set, and the noise level, and demonstrate trends that are consistent with our theoretical results.

