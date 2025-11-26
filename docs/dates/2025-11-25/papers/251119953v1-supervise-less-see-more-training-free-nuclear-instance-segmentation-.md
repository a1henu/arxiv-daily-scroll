---
layout: default
title: Supervise Less, See More: Training-free Nuclear Instance Segmentation with Prototype-Guided Prompting
---

# Supervise Less, See More: Training-free Nuclear Instance Segmentation with Prototype-Guided Prompting
**arXiv**：[2511.19953v1](https://arxiv.org/abs/2511.19953) · [PDF](https://arxiv.org/pdf/2511.19953.pdf)  
**作者**：Wen Zhang, Qin Ren, Wenjing Liu, Haibin Ling, Chenyu You  

**一句话要点**：提出SPROUT框架以解决无监督核实例分割问题

**关键词**：核实例分割, 训练自由方法, 原型引导提示, Segment Anything Model, 计算病理学, 部分最优传输

## 3 点简述
- 核心问题：现有方法依赖密集监督和微调，训练自由方法研究不足
- 方法要点：利用组织学先验构建原型，通过部分最优传输引导特征对齐
- 实验或效果：在多个病理基准测试中实现竞争性性能，无需监督或重训练

## 摘要（原文）

> Accurate nuclear instance segmentation is a pivotal task in computational pathology, supporting data-driven clinical insights and facilitating downstream translational applications. While large vision foundation models have shown promise for zero-shot biomedical segmentation, most existing approaches still depend on dense supervision and computationally expensive fine-tuning. Consequently, training-free methods present a compelling research direction, yet remain largely unexplored. In this work, we introduce SPROUT, a fully training- and annotation-free prompting framework for nuclear instance segmentation. SPROUT leverages histology-informed priors to construct slide-specific reference prototypes that mitigate domain gaps. These prototypes progressively guide feature alignment through a partial optimal transport scheme. The resulting foreground and background features are transformed into positive and negative point prompts, enabling the Segment Anything Model (SAM) to produce precise nuclear delineations without any parameter updates. Extensive experiments across multiple histopathology benchmarks demonstrate that SPROUT achieves competitive performance without supervision or retraining, establishing a novel paradigm for scalable, training-free nuclear instance segmentation in pathology.

