---
layout: default
title: RAID: Retrieval-Augmented Anomaly Detection
---

# RAID: Retrieval-Augmented Anomaly Detection
**arXiv**：[2602.19611v1](https://arxiv.org/abs/2602.19611) · [PDF](https://arxiv.org/pdf/2602.19611.pdf)  
**作者**：Mingxiu Cai, Zhe Zhang, Gaochang Wu, Tianyou Chai, Xiatian Zhu  

**一句话要点**：提出RAID框架，通过检索增强抑制匹配噪声，提升无监督异常检测性能。

**关键词**：无监督异常检测, 检索增强, 噪声抑制, 分层检索, 混合专家网络, 异常定位

## 3 点简述
- 核心问题：无监督异常检测中，测试图像与正常模板匹配因类内变化等引入噪声，影响准确性。
- 方法要点：基于检索增强生成思想，构建分层向量数据库，利用引导混合专家网络自适应抑制噪声，生成细粒度异常图。
- 实验或效果：在MVTec等基准上，RAID在全样本、少样本和多数据集设置中达到最先进性能。

## 摘要（原文）

> Unsupervised Anomaly Detection (UAD) aims to identify abnormal regions by establishing correspondences between test images and normal templates. Existing methods primarily rely on image reconstruction or template retrieval but face a fundamental challenge: matching between test images and normal templates inevitably introduces noise due to intra-class variations, imperfect correspondences, and limited templates. Observing that Retrieval-Augmented Generation (RAG) leverages retrieved samples directly in the generation process, we reinterpret UAD through this lens and introduce \textbf{RAID}, a retrieval-augmented UAD framework designed for noise-resilient anomaly detection and localization. Unlike standard RAG that enriches context or knowledge, we focus on using retrieved normal samples to guide noise suppression in anomaly map generation. RAID retrieves class-, semantic-, and instance-level representations from a hierarchical vector database, forming a coarse-to-fine pipeline. A matching cost volume correlates the input with retrieved exemplars, followed by a guided Mixture-of-Experts (MoE) network that leverages the retrieved samples to adaptively suppress matching noise and produce fine-grained anomaly maps. RAID achieves state-of-the-art performance across full-shot, few-shot, and multi-dataset settings on MVTec, VisA, MPDD, and BTAD benchmarks. \href{https://github.com/Mingxiu-Cai/RAID}{https://github.com/Mingxiu-Cai/RAID}.

