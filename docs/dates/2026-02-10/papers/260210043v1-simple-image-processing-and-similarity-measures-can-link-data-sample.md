---
layout: default
title: Simple Image Processing and Similarity Measures Can Link Data Samples across Databases through Brain MRI
---

# Simple Image Processing and Similarity Measures Can Link Data Samples across Databases through Brain MRI
**arXiv**：[2602.10043v1](https://arxiv.org/abs/2602.10043) · [PDF](https://arxiv.org/pdf/2602.10043.pdf)  
**作者**：Gaurang Sharma, Harri Polonen, Juha Pajula, Jutta Suksi, Jussi Tohka  

**一句话要点**：提出基于简单图像处理与相似度计算的脑MRI跨数据库个体链接方法，揭示隐私风险。

**关键词**：脑磁共振成像, 隐私风险, 图像相似度计算, 跨数据库匹配, 去标识化

## 3 点简述
- 核心问题：脑MRI去标识化后仍含独特签名，跨数据库匹配可导致再识别隐私风险。
- 方法要点：使用标准预处理和图像相似度计算，无需训练或高计算成本，实现个体链接。
- 实验或效果：在多种时间间隔、扫描仪类型和协议下，实现近乎完美的链接准确性。

## 摘要（原文）

> Head Magnetic Resonance Imaging (MRI) is routinely collected and shared for research under strict regulatory frameworks. These frameworks require removing potential identifiers before sharing. But, even after skull stripping, the brain parenchyma contains unique signatures that can match other MRIs from the same participants across databases, posing a privacy risk if additional data features are available. Current regulatory frameworks often mandate evaluating such risks based on the assessment of a certain level of reasonableness. Prior studies have already suggested that a brain MRI could enable participant linkage, but they have relied on training-based or computationally intensive methods.
>   Here, we demonstrate that linking an individual's skull-stripped T1-weighted MRI, which may lead to re-identification if other identifiers are available, is possible using standard preprocessing followed by image similarity computation. Nearly perfect linkage accuracy was achieved in matching data samples across various time intervals, scanner types, spatial resolutions, and acquisition protocols, despite potential cognitive decline, simulating MRI matching across databases. These results aim to contribute meaningfully to the development of thoughtful, forward-looking policies in medical data sharing.

