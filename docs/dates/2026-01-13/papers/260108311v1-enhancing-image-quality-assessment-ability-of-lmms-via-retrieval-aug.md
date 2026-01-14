---
layout: default
title: Enhancing Image Quality Assessment Ability of LMMs via Retrieval-Augmented Generation
---

# Enhancing Image Quality Assessment Ability of LMMs via Retrieval-Augmented Generation
**arXiv**：[2601.08311v1](https://arxiv.org/abs/2601.08311) · [PDF](https://arxiv.org/pdf/2601.08311.pdf)  
**作者**：Kang Fu, Huiyu Duan, Zicheng Zhang, Yucheng Zhu, Jun Zhao, Xiongkuo Min, Jia Wang, Guangtao Zhai  

**一句话要点**：提出IQARAG框架，通过检索增强生成提升大型多模态模型的图像质量评估能力

**关键词**：图像质量评估, 检索增强生成, 大型多模态模型, 零样本学习, 训练免费框架

## 3 点简述
- 核心问题：大型多模态模型在图像质量评估中需昂贵微调才能达到最优性能
- 方法要点：利用检索增强生成，检索语义相似但质量不同的参考图像作为视觉感知锚点
- 实验或效果：在多个数据集上验证IQARAG有效提升性能，提供资源高效替代方案

## 摘要（原文）

> Large Multimodal Models (LMMs) have recently shown remarkable promise in low-level visual perception tasks, particularly in Image Quality Assessment (IQA), demonstrating strong zero-shot capability. However, achieving state-of-the-art performance often requires computationally expensive fine-tuning methods, which aim to align the distribution of quality-related token in output with image quality levels. Inspired by recent training-free works for LMM, we introduce IQARAG, a novel, training-free framework that enhances LMMs' IQA ability. IQARAG leverages Retrieval-Augmented Generation (RAG) to retrieve some semantically similar but quality-variant reference images with corresponding Mean Opinion Scores (MOSs) for input image. These retrieved images and input image are integrated into a specific prompt. Retrieved images provide the LMM with a visual perception anchor for IQA task. IQARAG contains three key phases: Retrieval Feature Extraction, Image Retrieval, and Integration & Quality Score Generation. Extensive experiments across multiple diverse IQA datasets, including KADID, KonIQ, LIVE Challenge, and SPAQ, demonstrate that the proposed IQARAG effectively boosts the IQA performance of LMMs, offering a resource-efficient alternative to fine-tuning for quality assessment.

