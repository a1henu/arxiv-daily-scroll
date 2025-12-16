---
layout: default
title: A Domain-Adapted Lightweight Ensemble for Resource-Efficient Few-Shot Plant Disease Classification
---

# A Domain-Adapted Lightweight Ensemble for Resource-Efficient Few-Shot Plant Disease Classification
**arXiv**：[2512.13428v1](https://arxiv.org/abs/2512.13428) · [PDF](https://arxiv.org/pdf/2512.13428.pdf)  
**作者**：Anika Islam, Tasfia Tahsin, Zaarin Anjum, Md. Bakhtiar Hasan, Md. Hasanul Kabir  

**一句话要点**：提出轻量级域适应集成框架，用于资源受限环境下的少样本植物病害分类

**关键词**：少样本学习, 植物病害分类, 轻量级模型, 域适应, 注意力机制, 移动计算

## 3 点简述
- 核心问题：传统深度学习方法依赖大数据和计算资源，不适用于数据稀缺和资源受限的农业环境。
- 方法要点：结合域适应MobileNetV2/V3特征提取、特征融合和注意力增强Bi-LSTM分类器，实现高效少样本学习。
- 实验或效果：在PlantVillage数据集上15-shot达98.23%准确率，接近SOTA；在真实场景Dhan Shomadhan数据集上保持稳健性能，模型轻量约40MB。

## 摘要（原文）

> Accurate and timely identification of plant leaf diseases is essential for resilient and sustainable agriculture, yet most deep learning approaches rely on large annotated datasets and computationally intensive models that are unsuitable for data-scarce and resource-constrained environments. To address these challenges we present a few-shot learning approach within a lightweight yet efficient framework that combines domain-adapted MobileNetV2 and MobileNetV3 models as feature extractors, along with a feature fusion technique to generate robust feature representation. For the classification task, the fused features are passed through a Bi-LSTM classifier enhanced with attention mechanisms to capture sequential dependencies and focus on the most relevant features, thereby achieving optimal classification performance even in complex, real-world environments with noisy or cluttered backgrounds. The proposed framework was evaluated across multiple experimental setups, including both laboratory-controlled and field-captured datasets. On tomato leaf diseases from the PlantVillage dataset, it consistently improved performance across 1 to 15 shot scenarios, reaching 98.23+-0.33% at 15 shot, closely approaching the 99.98% SOTA benchmark achieved by a Transductive LSTM with attention, while remaining lightweight and mobile-friendly. Under real-world conditions using field images from the Dhan Shomadhan dataset, it maintained robust performance, reaching 69.28+-1.49% at 15-shot and demonstrating strong resilience to complex backgrounds. Notably, it also outperformed the previous SOTA accuracy of 96.0% on six diseases from PlantVillage, achieving 99.72% with only 15-shot learning. With a compact model size of approximately 40 MB and inference complexity of approximately 1.12 GFLOPs, this work establishes a scalable, mobile-ready foundation for precise plant disease diagnostics in data-scarce regions.

