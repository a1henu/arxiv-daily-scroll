---
layout: default
title: HalluGen: Synthesizing Realistic and Controllable Hallucinations for Evaluating Image Restoration
---

# HalluGen: Synthesizing Realistic and Controllable Hallucinations for Evaluating Image Restoration
**arXiv**：[2512.03345v1](https://arxiv.org/abs/2512.03345) · [PDF](https://arxiv.org/pdf/2512.03345.pdf)  
**作者**：Seunghoi Kim, Henry F. J. Tregidgo, Chen Jin, Matteo Figini, Daniel C. Alexander  

**一句话要点**：提出HalluGen框架以合成可控幻觉，用于安全关键图像恢复的评估

**关键词**：图像恢复, 幻觉合成, 扩散模型, 安全关键应用, 评估基准

## 3 点简述
- 生成模型在图像恢复中易产生幻觉，影响医疗等安全关键领域的可靠性
- HalluGen基于扩散模型合成类型、位置和严重程度可控的逼真幻觉
- 构建大规模幻觉数据集，开发SHAFE指标和检测器，提升评估能力

## 摘要（原文）

> Generative models are prone to hallucinations: plausible but incorrect structures absent in the ground truth. This issue is problematic in image restoration for safety-critical domains such as medical imaging, industrial inspection, and remote sensing, where such errors undermine reliability and trust. For example, in low-field MRI, widely used in resource-limited settings, restoration models are essential for enhancing low-quality scans, yet hallucinations can lead to serious diagnostic errors. Progress has been hindered by a circular dependency: evaluating hallucinations requires labeled data, yet such labels are costly and subjective. We introduce HalluGen, a diffusion-based framework that synthesizes realistic hallucinations with controllable type, location, and severity, producing perceptually realistic but semantically incorrect outputs (segmentation IoU drops from 0.86 to 0.36). Using HalluGen, we construct the first large-scale hallucination dataset comprising 4,350 annotated images derived from 1,450 brain MR images for low-field enhancement, enabling systematic evaluation of hallucination detection and mitigation. We demonstrate its utility in two applications: (1) benchmarking image quality metrics and developing Semantic Hallucination Assessment via Feature Evaluation (SHAFE), a feature-based metric with soft-attention pooling that improves hallucination sensitivity over traditional metrics; and (2) training reference-free hallucination detectors that generalize to real restoration failures. Together, HalluGen and its open dataset establish the first scalable foundation for evaluating hallucinations in safety-critical image restoration.

