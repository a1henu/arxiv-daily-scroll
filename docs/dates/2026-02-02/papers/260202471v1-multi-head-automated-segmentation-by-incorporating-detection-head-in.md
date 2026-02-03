---
layout: default
title: Multi-head automated segmentation by incorporating detection head into the contextual layer neural network
---

# Multi-head automated segmentation by incorporating detection head into the contextual layer neural network
**arXiv**：[2602.02471v1](https://arxiv.org/abs/2602.02471) · [PDF](https://arxiv.org/pdf/2602.02471.pdf)  
**作者**：Edwin Kys, Febian Febian  

**一句话要点**：提出基于检测门控的多头Transformer架构，以解决放疗自动分割中的假阳性问题。

**关键词**：自动分割, Transformer架构, 检测门控, 放疗应用, 假阳性抑制, 解剖学合理性

## 3 点简述
- 核心问题：传统深度学习分割模型在缺乏目标结构的切片中产生解剖学上不合理的假阳性。
- 方法要点：结合Swin U-Net，通过并行检测头和多层感知机进行切片级检测，门控分割预测以抑制假阳性。
- 实验或效果：在Prostate-Anatomical-Edge-Cases数据集上，门控模型显著优于非门控基线，Dice损失降低，有效消除虚假分割。

## 摘要（原文）

> Deep learning based auto segmentation is increasingly used in radiotherapy, but conventional models often produce anatomically implausible false positives, or hallucinations, in slices lacking target structures. We propose a gated multi-head Transformer architecture based on Swin U-Net, augmented with inter-slice context integration and a parallel detection head, which jointly performs slice-level structure detection via a multi-layer perceptron and pixel-level segmentation through a context-enhanced stream. Detection outputs gate the segmentation predictions to suppress false positives in anatomically invalid slices, and training uses slice-wise Tversky loss to address class imbalance. Experiments on the Prostate-Anatomical-Edge-Cases dataset from The Cancer Imaging Archive demonstrate that the gated model substantially outperforms a non-gated segmentation-only baseline, achieving a mean Dice loss of $0.013 \pm 0.036$ versus $0.732 \pm 0.314$, with detection probabilities strongly correlated with anatomical presence, effectively eliminating spurious segmentations. In contrast, the non-gated model exhibited higher variability and persistent false positives across all slices. These results indicate that detection-based gating enhances robustness and anatomical plausibility in automated segmentation applications, reducing hallucinated predictions without compromising segmentation quality in valid slices, and offers a promising approach for improving the reliability of clinical radiotherapy auto-contouring workflows.

