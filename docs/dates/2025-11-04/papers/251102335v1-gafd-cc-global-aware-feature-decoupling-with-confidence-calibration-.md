---
layout: default
title: GAFD-CC: Global-Aware Feature Decoupling with Confidence Calibration for OOD Detection
---

# GAFD-CC: Global-Aware Feature Decoupling with Confidence Calibration for OOD Detection
**arXiv**：[2511.02335v1](https://arxiv.org/abs/2511.02335) · [PDF](https://arxiv.org/pdf/2511.02335.pdf)  
**作者**：Kun Zou, Yongheng Xu, Jianxing Yu, Yan Pan, Jian Yin, Hanjiang Lai  

**一句话要点**：提出GAFD-CC方法，通过全局感知特征解耦与置信度校准提升OOD检测性能

**关键词**：OOD检测, 特征解耦, 置信度校准, 后处理方法, 决策边界优化

## 3 点简述
- 核心问题：现有后处理OOD检测方法忽略特征与logits的内在相关性，影响检测效果
- 方法要点：利用全局分类权重解耦特征，提取正负相关特征以优化决策边界
- 实验或效果：在大规模基准测试中展现竞争性性能和强泛化能力

## 摘要（原文）

> Out-of-distribution (OOD) detection is paramount to ensuring the reliability
> and robustness of learning models in real-world applications. Existing post-hoc
> OOD detection methods detect OOD samples by leveraging their features and
> logits information without retraining. However, they often overlook the
> inherent correlation between features and logits, which is crucial for
> effective OOD detection. To address this limitation, we propose Global-Aware
> Feature Decoupling with Confidence Calibration (GAFD-CC). GAFD-CC aims to
> refine decision boundaries and increase discriminative performance. Firstly, it
> performs global-aware feature decoupling guided by classification weights. This
> involves aligning features with the direction of global classification weights
> to decouple them. From this, GAFD-CC extracts two types of critical
> information: positively correlated features that promote in-distribution
> (ID)/OOD boundary refinement and negatively correlated features that suppress
> false positives and tighten these boundaries. Secondly, it adaptively fuses
> these decoupled features with multi-scale logit-based confidence for
> comprehensive and robust OOD detection. Extensive experiments on large-scale
> benchmarks demonstrate GAFD-CC's competitive performance and strong
> generalization ability compared to those of state-of-the-art methods.

