---
layout: default
title: Forensic Activity Classification Using Digital Traces from iPhones: A Machine Learning-based Approach
---

# Forensic Activity Classification Using Digital Traces from iPhones: A Machine Learning-based Approach
**arXiv**：[2512.03786v1](https://arxiv.org/abs/2512.03786) · [PDF](https://arxiv.org/pdf/2512.03786.pdf)  
**作者**：Conor McCarthy, Jan Peter van Zandwijk, Marcel Worring, Zeno Geradts  

**一句话要点**：提出基于机器学习的数字痕迹分析方法，用于iPhone法医活动分类与时间线构建。

**关键词**：法医活动分类, 数字痕迹分析, 机器学习, 似然比系统, iPhone传感器, 活动时间线

## 3 点简述
- 核心问题：利用iPhone内置运动传感器的数字痕迹推断用户物理活动，支持法医调查。
- 方法要点：开发机器学习模型将数字痕迹转换为活动似然比，并扩展至多活动分析与时间线生成。
- 实验或效果：在NFI_FARED数据集上评估，能区分167/171活动对，公开数据集与代码促进研究。

## 摘要（原文）

> Smartphones and smartwatches are ever-present in daily life, and provide a rich source of information on their users' behaviour. In particular, digital traces derived from the phone's embedded movement sensors present an opportunity for a forensic investigator to gain insight into a person's physical activities. In this work, we present a machine learning-based approach to translate digital traces into likelihood ratios (LRs) for different types of physical activities. Evaluating on a new dataset, NFI\_FARED, which contains digital traces from four different types of iPhones labelled with 19 activities, it was found that our approach could produce useful LR systems to distinguish 167 out of a possible 171 activity pairings. The same approach was extended to analyse likelihoods for multiple activities (or groups of activities) simultaneously and create activity timelines to aid in both the early and latter stages of forensic investigations. The dataset and all code required to replicate the results have also been made public to encourage further research on this topic.

