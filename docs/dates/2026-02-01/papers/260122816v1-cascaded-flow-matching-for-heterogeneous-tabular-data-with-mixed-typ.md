---
layout: default
title: Cascaded Flow Matching for Heterogeneous Tabular Data with Mixed-Type Features
---

# Cascaded Flow Matching for Heterogeneous Tabular Data with Mixed-Type Features
**arXiv**：[2601.22816v1](https://arxiv.org/abs/2601.22816) · [PDF](https://arxiv.org/pdf/2601.22816.pdf)  
**作者**：Markus Mueller, Kathrin Gruber, Dennis Fok  

**一句话要点**：提出级联流匹配方法以解决表格数据中混合类型特征的生成挑战

**关键词**：表格数据生成, 混合类型特征, 流匹配, 级联模型, 扩散模型, 条件概率路径

## 3 点简述
- 核心问题：表格数据中离散与连续混合的特征生成困难，现有方法难以处理缺失或膨胀值等离散状态
- 方法要点：采用级联策略，先生成低分辨率版本（分类特征和数值特征的粗粒度表示），再通过引导条件概率路径和数据依赖耦合进行高分辨率流匹配
- 实验或效果：模型生成样本更真实，分布细节捕获更准确，检测分数提升40%，并证明级联降低了传输成本界限

## 摘要（原文）

> Advances in generative modeling have recently been adapted to tabular data containing discrete and continuous features. However, generating mixed-type features that combine discrete states with an otherwise continuous distribution in a single feature remains challenging. We advance the state-of-the-art in diffusion models for tabular data with a cascaded approach. We first generate a low-resolution version of a tabular data row, that is, the collection of the purely categorical features and a coarse categorical representation of numerical features. Next, this information is leveraged in the high-resolution flow matching model via a novel guided conditional probability path and data-dependent coupling. The low-resolution representation of numerical features explicitly accounts for discrete outcomes, such as missing or inflated values, and therewith enables a more faithful generation of mixed-type features. We formally prove that this cascade tightens the transport cost bound. The results indicate that our model generates significantly more realistic samples and captures distributional details more accurately, for example, the detection score increases by 40%.

