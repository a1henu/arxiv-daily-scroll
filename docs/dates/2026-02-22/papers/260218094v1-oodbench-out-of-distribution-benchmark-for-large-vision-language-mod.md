---
layout: default
title: OODBench: Out-of-Distribution Benchmark for Large Vision-Language Models
---

# OODBench: Out-of-Distribution Benchmark for Large Vision-Language Models
**arXiv**：[2602.18094v1](https://arxiv.org/abs/2602.18094) · [PDF](https://arxiv.org/pdf/2602.18094.pdf)  
**作者**：Ling Lin, Yang Bai, Heng Su, Congcong Zhu, Yaoxing Wang, Yang Zhou, Huazhu Fu, Jingrun Chen  

**一句话要点**：提出OODBench基准以评估大视觉语言模型处理分布外数据的能力

**关键词**：分布外基准, 视觉语言模型, 自动评估, 安全风险, 性能评估

## 3 点简述
- 现有视觉语言模型在IID假设下训练，但现实场景常遇分布外数据，可能引发安全风险
- OODBench为自动化基准，含40K实例对，显示当前模型在常见类别上性能仍显著下降
- 提出基于提示问题进阶的自动评估指标，总结发现以促进未来分布外数据研究

## 摘要（原文）

> Existing Visual-Language Models (VLMs) have achieved significant progress by being trained on massive-scale datasets, typically under the assumption that data are independent and identically distributed (IID). However, in real-world scenarios, it is often impractical to expect that all data processed by an AI system satisfy this assumption. Furthermore, failure to appropriately handle out-of-distribution (OOD) objects may introduce safety risks in real-world applications (e.g., autonomous driving or medical assistance). Unfortunately, current research has not yet provided valid benchmarks that can comprehensively assess the performance of VLMs in response to OOD data. Therefore, we propose OODBench, a predominantly automated method with minimal human verification, for constructing new benchmarks and evaluating the ability of VLMs to process OOD data. OODBench contains 40K instance-level OOD instance-category pairs, and we show that current VLMs still exhibit notable performance degradation on OODBench, even when the underlying image categories are common. In addition, we propose a reliable automated assessment metric that employs a Basic-to-Advanced Progression of prompted questions to assess the impact of OOD data on questions of varying difficulty more fully. Lastly, we summarize substantial findings and insights to facilitate future research in the acquisition and evaluation of OOD data.

