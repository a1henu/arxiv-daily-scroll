---
layout: default
title: GeoSeg: Training-Free Reasoning-Driven Segmentation in Remote Sensing Imagery
---

# GeoSeg: Training-Free Reasoning-Driven Segmentation in Remote Sensing Imagery
**arXiv**：[2603.03983v1](https://arxiv.org/abs/2603.03983) · [PDF](https://arxiv.org/pdf/2603.03983.pdf)  
**作者**：Lifan Jiang, Yuhang Pei, oxi Wu, Yan Zhao, Tianrun Wu, Shulong Yu, Lihui Zhang, Deng Cai  

**一句话要点**：提出GeoSeg框架，以零样本训练方式解决遥感图像中推理驱动分割的监督瓶颈问题。

**关键词**：遥感图像分割, 零样本学习, 多模态大语言模型, 推理驱动定位, 坐标细化, 双路提示

## 3 点简述
- 核心问题：遥感图像缺乏通用推理驱动分割方案，因数据成本高和俯视视角等挑战。
- 方法要点：结合MLLM推理与精确定位，通过偏置感知坐标细化和双路提示机制融合语义与空间信息。
- 实验或效果：在GeoSeg-Bench基准上优于所有基线，消融实验验证各组件有效性和必要性。

## 摘要（原文）

> Recent advances in MLLMs are reframing segmentation from fixed-category prediction to instruction-grounded localization. While reasoning based segmentation has progressed rapidly in natural scenes, remote sensing lacks a generalizable solution due to the prohibitive cost of reasoning-oriented data and domain-specific challenges like overhead viewpoints. We present GeoSeg, a zero-shot, training-free framework that bypasses the supervision bottleneck for reasoning-driven remote sensing segmentation. GeoSeg couples MLLM reasoning with precise localization via: (i) bias-aware coordinate refinement to correct systematic grounding shifts and (ii) a dual-route prompting mechanism to fuse semantic intent with fine-grained spatial cues. We also introduce GeoSeg-Bench, a diagnostic benchmark of 810 image--query pairs with hierarchical difficulty levels. Experiments show that GeoSeg consistently outperforms all baselines, with extensive ablations confirming the effectiveness and necessity of each component.

