---
layout: default
title: Discover, Segment, and Select: A Progressive Mechanism for Zero-shot Camouflaged Object Segmentation
---

# Discover, Segment, and Select: A Progressive Mechanism for Zero-shot Camouflaged Object Segmentation
**arXiv**：[2602.19944v1](https://arxiv.org/abs/2602.19944) · [PDF](https://arxiv.org/pdf/2602.19944.pdf)  
**作者**：Yilong Yang, Jianxin Tian, Shengchuan Zhang, Liujuan Cao  

**一句话要点**：提出渐进式DSS机制以解决零样本伪装物体分割中MLLM定位不准确的问题

**关键词**：零样本学习, 伪装物体分割, 渐进式框架, 多模态大语言模型, SAM分割, 掩码选择

## 3 点简述
- 核心问题：现有零样本伪装物体分割方法依赖MLLM发现物体，易导致定位不准、误检和漏检
- 方法要点：设计渐进式框架，包含特征一致物体发现、SAM分割和语义驱动掩码选择模块
- 实验或效果：无需训练，在多个COS基准上实现最优性能，尤其在多实例场景表现突出

## 摘要（原文）

> Current zero-shot Camouflaged Object Segmentation methods typically employ a two-stage pipeline (discover-then-segment): using MLLMs to obtain visual prompts, followed by SAM segmentation. However, relying solely on MLLMs for camouflaged object discovery often leads to inaccurate localization, false positives, and missed detections. To address these issues, we propose the \textbf{D}iscover-\textbf{S}egment-\textbf{S}elect (\textbf{DSS}) mechanism, a progressive framework designed to refine segmentation step by step. The proposed method contains a Feature-coherent Object Discovery (FOD) module that leverages visual features to generate diverse object proposals, a segmentation module that refines these proposals through SAM segmentation, and a Semantic-driven Mask Selection (SMS) module that employs MLLMs to evaluate and select the optimal segmentation mask from multiple candidates. Without requiring any training or supervision, DSS achieves state-of-the-art performance on multiple COS benchmarks, especially in multiple-instance scenes.

