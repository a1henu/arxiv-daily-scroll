---
layout: default
title: A Multicenter Benchmark of Multiple Instance Learning Models for Lymphoma Subtyping from HE-stained Whole Slide Images
---

# A Multicenter Benchmark of Multiple Instance Learning Models for Lymphoma Subtyping from HE-stained Whole Slide Images
**arXiv**：[2512.14640v1](https://arxiv.org/abs/2512.14640) · [PDF](https://arxiv.org/pdf/2512.14640.pdf)  
**作者**：Rao Muhammad Umer, Daniel Sens, Jonathan Noll, Christian Matek, Lukas Wolfseher, Rainer Spang, Ralf Huss, Johannes Raffler, Sarah Reinke, Wolfram Klapper, Katja Steiger, Kristina Schwamborn, Carsten Marr  

**一句话要点**：提出首个多中心淋巴瘤分型基准数据集，评估病理基础模型与多实例学习聚合器在HE染色全切片图像上的性能。

**关键词**：淋巴瘤分型, 多实例学习, 病理基础模型, HE染色全切片图像, 多中心基准, 泛化性能

## 3 点简述
- 核心问题：淋巴瘤分型依赖多模态检测，导致诊断延迟，缺乏基于HE染色图像的多中心深度学习基准。
- 方法要点：使用五种病理基础模型结合AB-MIL和TransMIL聚合器，在三个放大倍数下进行系统评估。
- 实验或效果：在分布内测试集上平衡准确率超80%，但分布外测试集性能降至约60%，揭示泛化挑战。

## 摘要（原文）

> Timely and accurate lymphoma diagnosis is essential for guiding cancer treatment. Standard diagnostic practice combines hematoxylin and eosin (HE)-stained whole slide images with immunohistochemistry, flow cytometry, and molecular genetic tests to determine lymphoma subtypes, a process requiring costly equipment, skilled personnel, and causing treatment delays. Deep learning methods could assist pathologists by extracting diagnostic information from routinely available HE-stained slides, yet comprehensive benchmarks for lymphoma subtyping on multicenter data are lacking. In this work, we present the first multicenter lymphoma benchmarking dataset covering four common lymphoma subtypes and healthy control tissue. We systematically evaluate five publicly available pathology foundation models (H-optimus-1, H0-mini, Virchow2, UNI2, Titan) combined with attention-based (AB-MIL) and transformer-based (TransMIL) multiple instance learning aggregators across three magnifications (10x, 20x, 40x). On in-distribution test sets, models achieve multiclass balanced accuracies exceeding 80% across all magnifications, with all foundation models performing similarly and both aggregation methods showing comparable results. The magnification study reveals that 40x resolution is sufficient, with no performance gains from higher resolutions or cross-magnification aggregation. However, on out-of-distribution test sets, performance drops substantially to around 60%, highlighting significant generalization challenges. To advance the field, larger multicenter studies covering additional rare lymphoma subtypes are needed. We provide an automated benchmarking pipeline to facilitate such future research.

