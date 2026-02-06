---
layout: default
title: Parallel Swin Transformer-Enhanced 3D MRI-to-CT Synthesis for MRI-Only Radiotherapy Planning
---

# Parallel Swin Transformer-Enhanced 3D MRI-to-CT Synthesis for MRI-Only Radiotherapy Planning
**arXiv**：[2602.05387v1](https://arxiv.org/abs/2602.05387) · [PDF](https://arxiv.org/pdf/2602.05387.pdf)  
**作者**：Zolnamar Dorjsembe, Hung-Yi Chen, Furen Xiao, Hsing-Kuo Pao  

**一句话要点**：提出并行Swin Transformer增强的3D MRI-CT合成方法，用于仅MRI放疗规划。

**关键词**：医学图像合成, Swin Transformer, 放疗规划, 3D架构, 剂量计算

## 3 点简述
- 核心问题：MRI缺乏电子密度信息，无法直接用于放疗剂量计算，需结合CT增加不确定性。
- 方法要点：集成卷积编码与双Swin Transformer分支，建模局部细节和长程上下文依赖，提升解剖保真度。
- 实验或效果：在公开和临床数据集上，相比基线方法，图像相似度和几何精度更高，剂量误差平均1.69%。

## 摘要（原文）

> MRI provides superior soft tissue contrast without ionizing radiation; however, the absence of electron density information limits its direct use for dose calculation. As a result, current radiotherapy workflows rely on combined MRI and CT acquisitions, increasing registration uncertainty and procedural complexity. Synthetic CT generation enables MRI only planning but remains challenging due to nonlinear MRI-CT relationships and anatomical variability. We propose Parallel Swin Transformer-Enhanced Med2Transformer, a 3D architecture that integrates convolutional encoding with dual Swin Transformer branches to model both local anatomical detail and long-range contextual dependencies. Multi-scale shifted window attention with hierarchical feature aggregation improves anatomical fidelity. Experiments on public and clinical datasets demonstrate higher image similarity and improved geometric accuracy compared with baseline methods. Dosimetric evaluation shows clinically acceptable performance, with a mean target dose error of 1.69%. Code is available at: https://github.com/mobaidoctor/med2transformer.

