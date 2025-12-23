---
layout: default
title: MapTrace: Scalable Data Generation for Route Tracing on Maps
---

# MapTrace: Scalable Data Generation for Route Tracing on Maps
**arXiv**：[2512.19609v1](https://arxiv.org/abs/2512.19609) · [PDF](https://arxiv.org/pdf/2512.19609.pdf)  
**作者**：Artemis Panagopoulou, Aveek Purohit, Achin Kulshrestha, Soroosh Yazdani, Mohit Goyal  

**一句话要点**：提出MapTrace合成数据生成管道以解决地图路径追踪中多模态大语言模型空间理解不足的问题

**关键词**：地图路径追踪, 合成数据生成, 多模态大语言模型, 细粒度空间理解, 像素级标注, 模型微调

## 3 点简述
- 多模态大语言模型在地图路径追踪等细粒度空间理解任务上表现有限，部分由于像素级标注数据收集困难
- 引入可扩展的合成数据生成管道，利用合成地图图像和像素级解析自动生成精确标注
- 基于23k路径样本数据集微调模型，在MapBench上提升成功率并降低路径追踪误差

## 摘要（原文）

> While Multimodal Large Language Models have achieved human-like performance on many visual and textual reasoning tasks, their proficiency in fine-grained spatial understanding, such as route tracing on maps remains limited. Unlike humans, who can quickly learn to parse and navigate maps, current models often fail to respect fundamental path constraints, in part due to the prohibitive cost and difficulty of collecting large-scale, pixel-accurate path annotations. To address this, we introduce a scalable synthetic data generation pipeline that leverages synthetic map images and pixel-level parsing to automatically produce precise annotations for this challenging task. Using this pipeline, we construct a fine-tuning dataset of 23k path samples across 4k maps, enabling models to acquire more human-like spatial capabilities. Using this dataset, we fine-tune both open-source and proprietary MLLMs. Results on MapBench show that finetuning substantially improves robustness, raising success rates by up to 6.4 points, while also reducing path-tracing error (NDTW). These gains highlight that fine-grained spatial reasoning, absent in pretrained models, can be explicitly taught with synthetic supervision.

