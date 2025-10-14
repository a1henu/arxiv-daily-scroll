---
layout: default
title: Benchmarking foundation models for hyperspectral image classification: Application to cereal crop type mapping
---

# Benchmarking foundation models for hyperspectral image classification: Application to cereal crop type mapping
**arXiv**：[2510.11576v1](https://arxiv.org/abs/2510.11576) · [PDF](https://arxiv.org/pdf/2510.11576.pdf)  
**作者**：Walid Elbarz, Mohamed Bourriz, Hicham Hajji, Hamd Ait Abdelali, François Bourzeix  

**一句话要点**：基准测试基础模型用于高光谱图像分类，应用于谷物作物类型制图

**关键词**：高光谱图像分类, 基础模型基准测试, 谷物作物制图, 模型微调, 遥感应用

## 3 点简述
- 核心问题：基础模型在高光谱作物制图中的应用潜力未被充分探索。
- 方法要点：对HyperSigma、DOFA和SpectralEarth预训练模型进行微调与评估。
- 实验或效果：SpectralEarth模型总体准确率达93.5%，优于其他模型。

## 摘要（原文）

> Foundation models are transforming Earth observation, but their potential for
> hyperspectral crop mapping remains underexplored. This study benchmarks three
> foundation models for cereal crop mapping using hyperspectral imagery:
> HyperSigma, DOFA, and Vision Transformers pre-trained on the SpectralEarth
> dataset (a large multitemporal hyperspectral archive). Models were fine-tuned
> on manually labeled data from a training region and evaluated on an independent
> test region. Performance was measured with overall accuracy (OA), average
> accuracy (AA), and F1-score. HyperSigma achieved an OA of 34.5% (+/- 1.8%),
> DOFA reached 62.6% (+/- 3.5%), and the SpectralEarth model achieved an OA of
> 93.5% (+/- 0.8%). A compact SpectralEarth variant trained from scratch achieved
> 91%, highlighting the importance of model architecture for strong
> generalization across geographic regions and sensor platforms. These results
> provide a systematic evaluation of foundation models for operational
> hyperspectral crop mapping and outline directions for future model development.

