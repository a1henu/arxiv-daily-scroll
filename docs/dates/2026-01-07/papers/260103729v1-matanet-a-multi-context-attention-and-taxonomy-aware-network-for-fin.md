---
layout: default
title: MATANet: A Multi-context Attention and Taxonomy-Aware Network for Fine-Grained Underwater Recognition of Marine Species
---

# MATANet: A Multi-context Attention and Taxonomy-Aware Network for Fine-Grained Underwater Recognition of Marine Species
**arXiv**：[2601.03729v1](https://arxiv.org/abs/2601.03729) · [PDF](https://arxiv.org/pdf/2601.03729.pdf)  
**作者**：Donghwan Lee, Byeongjin Kim, Geunhee Kim, Hyukjin Kwon, Nahyeon Maeng, Wooju Kim  

**一句话要点**：提出MATANet，通过多上下文注意力和分类学感知网络解决海洋物种细粒度识别问题。

**关键词**：细粒度分类, 海洋物种识别, 多上下文注意力, 分类学感知网络, 水下图像分析

## 3 点简述
- 核心问题：现有方法忽视环境上下文交互和海洋生物分类学层次结构，影响细粒度分类准确性。
- 方法要点：结合多上下文环境注意力模块学习兴趣区域与环境关系，以及层次分离诱导学习模块编码分类学层次到特征空间。
- 实验或效果：在FathomNet2025等数据集上实现先进性能，代码已开源。

## 摘要（原文）

> Fine-grained classification of marine animals supports ecology, biodiversity and habitat conservation, and evidence-based policy-making. However, existing methods often overlook contextual interactions from the surrounding environment and insufficiently incorporate the hierarchical structure of marine biological taxonomy. To address these challenges, we propose MATANet (Multi-context Attention and Taxonomy-Aware Network), a novel model designed for fine-grained marine species classification. MATANet mimics expert strategies by using taxonomy and environmental context to interpret ambiguous features of underwater animals. It consists of two key components: a Multi-Context Environmental Attention Module (MCEAM), which learns relationships between regions of interest (ROIs) and their surrounding environments, and a Hierarchical Separation-Induced Learning Module (HSLM), which encodes taxonomic hierarchy into the feature space. MATANet combines instance and environmental features with taxonomic structure to enhance fine-grained classification. Experiments on the FathomNet2025, FAIR1M, and LifeCLEF2015-Fish datasets demonstrate state-of-the-art performance. The source code is available at: https://github.com/dhlee-work/fathomnet-cvpr2025-ssl

