---
layout: default
title: Extending 2D foundational DINOv3 representations to 3D segmentation of neonatal brain MR images
---

# Extending 2D foundational DINOv3 representations to 3D segmentation of neonatal brain MR images
**arXiv**：[2602.23962v1](https://arxiv.org/abs/2602.23962) · [PDF](https://arxiv.org/pdf/2602.23962.pdf)  
**作者**：Annayah Usman, Behraj Khan, Tahir Qasim Syed  

**一句话要点**：提出基于结构化窗口分解-重组机制的3D分割方法，以扩展2D基础DINOv3表示至新生儿脑MR图像分割。

**关键词**：3D医学图像分割, 基础模型扩展, 新生儿脑MR, 结构化解码, 海马分割

## 3 点简述
- 核心问题：2D基础编码器难以直接处理3D脑解剖结构，需解决维度不匹配问题。
- 方法要点：通过非重叠3D窗口分解MRI体积，利用冻结特征进行解码，再重组以保持解剖一致性。
- 实验或效果：在ALBERT数据集上，单窗口海马分割Dice分数达0.65，验证方法有效性。

## 摘要（原文）

> Precise volumetric delineation of hippocampal structures is essential for quantifying neurodevelopmental trajectories in pre-term and term infants, where subtle morphological variations may carry prognostic significance. While foundation encoders trained on large-scale visual data offer discriminative representations, their 2D formulation is a limitation with respect to the $3$D organization of brain anatomy. We propose a volumetric segmentation strategy that reconciles this tension through a structured window-based disassembly-reassembly mechanism: the global MRI volume is decomposed into non-overlapping 3D windows or sub-cubes, each processed via a separate decoding arm built upon frozen high-fidelity features, and subsequently reassembled prior to a ground-truth correspendence using a dense-prediction head. This architecture preserves constant a decoder memory footprint while forcing predictions to lie within an anatomically consistent geometry. Evaluated on the ALBERT dataset for hippocampal segmentation, the proposed approach achieves a Dice score of 0.65 for a single 3D window. The method demonstrates that volumetric anatomical structure could be recovered from frozen 2D foundation representations through structured compositional decoding, and offers a principled and generalizable extension for foundation models for 3D medical applications.

