---
layout: default
title: Outlier detection in mixed-attribute data: a semi-supervised approach with fuzzy approximations and relative entropy
---

# Outlier detection in mixed-attribute data: a semi-supervised approach with fuzzy approximations and relative entropy
**arXiv**：[2512.18978v1](https://arxiv.org/abs/2512.18978) · [PDF](https://arxiv.org/pdf/2512.18978.pdf)  
**作者**：Baiyang Chen, Zhong Yuan, Zheng Liu, Dezhong Peng, Yongxiang Li, Chang Liu, Guiduo Duan  

**一句话要点**：提出基于模糊粗糙集与相对熵的半监督离群点检测方法FROD，以处理混合属性数据的不确定性与异质性。

**关键词**：离群点检测, 半监督学习, 模糊粗糙集, 相对熵, 混合属性数据, 不确定性建模

## 3 点简述
- 核心问题：半监督方法在混合属性数据中常忽略不确定性与异质性，影响离群点检测性能。
- 方法要点：利用标记数据构建模糊决策系统，结合属性分类准确性与未标记数据的模糊相对熵来评估离群点。
- 实验或效果：在16个公开数据集上验证，FROD性能与领先算法相当或更优，代码开源。

## 摘要（原文）

> Outlier detection is a critical task in data mining, aimed at identifying objects that significantly deviate from the norm. Semi-supervised methods improve detection performance by leveraging partially labeled data but typically overlook the uncertainty and heterogeneity of real-world mixed-attribute data. This paper introduces a semi-supervised outlier detection method, namely fuzzy rough sets-based outlier detection (FROD), to effectively handle these challenges. Specifically, we first utilize a small subset of labeled data to construct fuzzy decision systems, through which we introduce the attribute classification accuracy based on fuzzy approximations to evaluate the contribution of attribute sets in outlier detection. Unlabeled data is then used to compute fuzzy relative entropy, which provides a characterization of outliers from the perspective of uncertainty. Finally, we develop the detection algorithm by combining attribute classification accuracy with fuzzy relative entropy. Experimental results on 16 public datasets show that FROD is comparable with or better than leading detection algorithms. All datasets and source codes are accessible at https://github.com/ChenBaiyang/FROD. This manuscript is the accepted author version of a paper published by Elsevier. The final published version is available at https://doi.org/10.1016/j.ijar.2025.109373

