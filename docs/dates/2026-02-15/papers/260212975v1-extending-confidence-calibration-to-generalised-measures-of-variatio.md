---
layout: default
title: Extending confidence calibration to generalised measures of variation
---

# Extending confidence calibration to generalised measures of variation
**arXiv**：[2602.12975v1](https://arxiv.org/abs/2602.12975) · [PDF](https://arxiv.org/pdf/2602.12975.pdf)  
**作者**：Andrew Thompson, Vivek Desai  

**一句话要点**：提出变分校准误差（VCE）以评估机器学习分类器的校准性能，扩展了预期校准误差（ECE）的应用范围。

**关键词**：校准评估, 变分度量, 机器学习分类器, 预期校准误差, 香农熵, 合成数据验证

## 3 点简述
- 核心问题：现有校准评估指标如ECE仅关注最大概率或置信度，未充分利用整个概率分布的信息。
- 方法要点：将ECE方法扩展至评估任何变分度量（如香农熵）的校准，提出VCE作为通用校准误差指标。
- 实验或效果：在合成预测数据上验证VCE随样本数增加趋近于零，优于文献中另一熵基校准指标（UCE）。

## 摘要（原文）

> We propose the Variation Calibration Error (VCE) metric for assessing the calibration of machine learning classifiers. The metric can be viewed as an extension of the well-known Expected Calibration Error (ECE) which assesses the calibration of the maximum probability or confidence. Other ways of measuring the variation of a probability distribution exist which have the advantage of taking into account the full probability distribution, for example the Shannon entropy. We show how the ECE approach can be extended from assessing confidence calibration to assessing the calibration of any metric of variation. We present numerical examples upon synthetic predictions which are perfectly calibrated by design, demonstrating that, in this scenario, the VCE has the desired property of approaching zero as the number of data samples increases, in contrast to another entropy-based calibration metric (the UCE) which has been proposed in the literature.

