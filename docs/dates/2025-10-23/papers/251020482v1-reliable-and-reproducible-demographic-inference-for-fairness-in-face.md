---
layout: default
title: Reliable and Reproducible Demographic Inference for Fairness in Face Analysis
---

# Reliable and Reproducible Demographic Inference for Fairness in Face Analysis
**arXiv**：[2510.20482v1](https://arxiv.org/abs/2510.20482) · [PDF](https://arxiv.org/pdf/2510.20482.pdf)  
**作者**：Alexandre Fournier-Montgieux, Hervé Le Borgne, Adrian Popescu, Bertrand Luvison  

**一句话要点**：提出可重现的人口属性推断管道以提升人脸分析公平性审计的可靠性

**关键词**：人脸分析, 公平性审计, 人口属性推断, 迁移学习, 鲁棒性评估

## 3 点简述
- 人脸分析系统公平性审计依赖人口属性推断，但其可靠性影响审计有效性
- 采用模块化迁移学习方法，结合预训练人脸编码器与非线形分类头
- 在性别和种族推断基准测试中表现优于基线，尤其对种族属性更有效

## 摘要（原文）

> Fairness evaluation in face analysis systems (FAS) typically depends on
> automatic demographic attribute inference (DAI), which itself relies on
> predefined demographic segmentation. However, the validity of fairness auditing
> hinges on the reliability of the DAI process. We begin by providing a
> theoretical motivation for this dependency, showing that improved DAI
> reliability leads to less biased and lower-variance estimates of FAS fairness.
> To address this, we propose a fully reproducible DAI pipeline that replaces
> conventional end-to-end training with a modular transfer learning approach. Our
> design integrates pretrained face recognition encoders with non-linear
> classification heads. We audit this pipeline across three dimensions: accuracy,
> fairness, and a newly introduced notion of robustness, defined via
> intra-identity consistency. The proposed robustness metric is applicable to any
> demographic segmentation scheme. We benchmark the pipeline on gender and
> ethnicity inference across multiple datasets and training setups. Our results
> show that the proposed method outperforms strong baselines, particularly on
> ethnicity, which is the more challenging attribute. To promote transparency and
> reproducibility, we will publicly release the training dataset metadata, full
> codebase, pretrained models, and evaluation toolkit. This work contributes a
> reliable foundation for demographic inference in fairness auditing.

