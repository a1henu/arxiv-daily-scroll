---
layout: default
title: 3D CT-Based Coronary Calcium Assessment: A Feature-Driven Machine Learning Framework
---

# 3D CT-Based Coronary Calcium Assessment: A Feature-Driven Machine Learning Framework
**arXiv**：[2510.25347v1](https://arxiv.org/abs/2510.25347) · [PDF](https://arxiv.org/pdf/2510.25347.pdf)  
**作者**：Ayman Abaid, Gianpiero Guidone, Sara Alsubai, Foziyah Alquahtani, Talha Iqbal, Ruth Sharif, Hesham Elzomor, Emiliano Bianchini, Naeif Almagal, Michael G. Madden, Faisal Sharif, Ihsan Ullah  

**一句话要点**：提出基于放射组学和伪标签的机器学习框架，用于无专家标注的冠状动脉钙化评估。

**关键词**：冠状动脉钙化评分, 放射组学, 伪标签, 预训练模型, 非对比CT, 机器学习框架

## 3 点简述
- 核心问题：冠状动脉钙化评分依赖专家标注，数据标注成本高且稀缺。
- 方法要点：利用伪标签生成训练数据，结合放射组学和预训练模型提取特征。
- 实验或效果：在182患者数据集上，放射组学模型准确率达84%，优于深度学习特征。

## 摘要（原文）

> Coronary artery calcium (CAC) scoring plays a crucial role in the early
> detection and risk stratification of coronary artery disease (CAD). In this
> study, we focus on non-contrast coronary computed tomography angiography (CCTA)
> scans, which are commonly used for early calcification detection in clinical
> settings. To address the challenge of limited annotated data, we propose a
> radiomics-based pipeline that leverages pseudo-labeling to generate training
> labels, thereby eliminating the need for expert-defined segmentations.
> Additionally, we explore the use of pretrained foundation models, specifically
> CT-FM and RadImageNet, to extract image features, which are then used with
> traditional classifiers. We compare the performance of these deep learning
> features with that of radiomics features. Evaluation is conducted on a clinical
> CCTA dataset comprising 182 patients, where individuals are classified into two
> groups: zero versus non-zero calcium scores. We further investigate the impact
> of training on non-contrast datasets versus combined contrast and non-contrast
> datasets, with testing performed only on non contrast scans. Results show that
> radiomics-based models significantly outperform CNN-derived embeddings from
> foundation models (achieving 84% accuracy and p<0.05), despite the
> unavailability of expert annotations.

