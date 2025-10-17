---
layout: default
title: CLEAR: Causal Learning Framework For Robust Histopathology Tumor Detection Under Out-Of-Distribution Shifts
---

# CLEAR: Causal Learning Framework For Robust Histopathology Tumor Detection Under Out-Of-Distribution Shifts
**arXiv**：[2510.14273v1](https://arxiv.org/abs/2510.14273) · [PDF](https://arxiv.org/pdf/2510.14273.pdf)  
**作者**：Kieu-Anh Truong Thi, Huy-Hieu Pham, Duc-Trong Le  

**一句话要点**：提出因果学习框架CLEAR以解决组织病理学肿瘤检测中的域偏移问题

**关键词**：因果推断, 组织病理学, 域偏移, 肿瘤检测, 深度学习, 前门原则

## 3 点简述
- 核心问题：组织病理学图像中的域偏移影响深度学习模型泛化能力
- 方法要点：基于因果推断，利用前门原则设计变换策略，结合中介变量和观察组织切片
- 实验或效果：在CAMELYON17和私有数据集上验证，性能提升达7%，优于基线方法

## 摘要（原文）

> Domain shift in histopathology, often caused by differences in acquisition
> processes or data sources, poses a major challenge to the generalization
> ability of deep learning models. Existing methods primarily rely on modeling
> statistical correlations by aligning feature distributions or introducing
> statistical variation, yet they often overlook causal relationships. In this
> work, we propose a novel causal-inference-based framework that leverages
> semantic features while mitigating the impact of confounders. Our method
> implements the front-door principle by designing transformation strategies that
> explicitly incorporate mediators and observed tissue slides. We validate our
> method on the CAMELYON17 dataset and a private histopathology dataset,
> demonstrating consistent performance gains across unseen domains. As a result,
> our approach achieved up to a 7% improvement in both the CAMELYON17 dataset and
> the private histopathology dataset, outperforming existing baselines. These
> results highlight the potential of causal inference as a powerful tool for
> addressing domain shift in histopathology image analysis.

