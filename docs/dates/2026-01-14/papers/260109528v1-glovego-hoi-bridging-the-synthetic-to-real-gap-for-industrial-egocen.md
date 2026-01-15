---
layout: default
title: GlovEgo-HOI: Bridging the Synthetic-to-Real Gap for Industrial Egocentric Human-Object Interaction Detection
---

# GlovEgo-HOI: Bridging the Synthetic-to-Real Gap for Industrial Egocentric Human-Object Interaction Detection
**arXiv**：[2601.09528v1](https://arxiv.org/abs/2601.09528) · [PDF](https://arxiv.org/pdf/2601.09528.pdf)  
**作者**：Alfio Spoto, Rosario Leonardi, Francesco Ragusa, Giovanni Maria Farinella  

**一句话要点**：提出GlovEgo-HOI数据集与GlovEgo-Net模型，结合合成数据与扩散增强解决工业第一人称人-物交互检测的数据稀缺问题。

**关键词**：第一人称人-物交互检测, 合成数据增强, 扩散模型, 工业安全, 个人防护装备, 基准数据集

## 3 点简述
- 核心问题：工业第一人称人-物交互检测因领域特定标注数据稀缺而受限。
- 方法要点：开发数据生成框架，融合合成数据与扩散过程，在真实图像中增强个人防护装备以提升真实性。
- 实验或效果：通过广泛实验验证数据生成框架和GlovEgo-Net模型的有效性，并发布数据集、增强流程和预训练模型。

## 摘要（原文）

> Egocentric Human-Object Interaction (EHOI) analysis is crucial for industrial safety, yet the development of robust models is hindered by the scarcity of annotated domain-specific data. We address this challenge by introducing a data generation framework that combines synthetic data with a diffusion-based process to augment real-world images with realistic Personal Protective Equipment (PPE). We present GlovEgo-HOI, a new benchmark dataset for industrial EHOI, and GlovEgo-Net, a model integrating Glove-Head and Keypoint- Head modules to leverage hand pose information for enhanced interaction detection. Extensive experiments demonstrate the effectiveness of the proposed data generation framework and GlovEgo-Net. To foster further research, we release the GlovEgo-HOI dataset, augmentation pipeline, and pre-trained models at: GitHub project.

