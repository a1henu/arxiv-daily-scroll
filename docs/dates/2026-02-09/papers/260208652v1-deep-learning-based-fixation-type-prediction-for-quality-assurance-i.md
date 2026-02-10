---
layout: default
title: Deep Learning-Based Fixation Type Prediction for Quality Assurance in Digital Pathology
---

# Deep Learning-Based Fixation Type Prediction for Quality Assurance in Digital Pathology
**arXiv**：[2602.08652v1](https://arxiv.org/abs/2602.08652) · [PDF](https://arxiv.org/pdf/2602.08652.pdf)  
**作者**：Oskar Thaeter, Tanja Niedermair, Johannes Raffler, Ralf Huss, Peter J. Schüffler  

**一句话要点**：提出基于深度学习的低分辨率缩略图预测固定类型方法，以提升数字病理学高通量质量控制效率。

**关键词**：数字病理学, 固定类型预测, 深度学习, 低分辨率图像, 质量控制, 高通量处理

## 3 点简述
- 核心问题：手动标注固定类型易出错，现有方法依赖高分辨率全切片图像，限制高通量应用。
- 方法要点：使用深度学习模型，基于低分辨率预扫描缩略图预测FFPE和冷冻切片固定类型。
- 实验或效果：在TCGA数据集上AUROC达0.88，处理速度比高分辨率方法快400倍，但跨扫描仪泛化能力有待提升。

## 摘要（原文）

> Accurate annotation of fixation type is a critical step in slide preparation for pathology laboratories. However, this manual process is prone to
>   errors, impacting downstream analyses and diagnostic accuracy. Existing methods for verifying formalin-fixed, paraffin-embedded (FFPE), and frozen
>   section (FS) fixation types typically require full-resolution whole-slide images (WSIs), limiting scalability for high-throughput quality control.
>   We propose a deep-learning model to predict fixation types using low-resolution, pre-scan thumbnail images. The model was trained on WSIs from
>   the TUM Institute of Pathology (n=1,200, Leica GT450DX) and evaluated on a class-balanced subset of The Cancer Genome Atlas dataset (TCGA, n=8,800,
>   Leica AT2), as well as on class-balanced datasets from Augsburg (n=695 [392 FFPE, 303 FS], Philips UFS) and Regensburg (n=202, 3DHISTECH P1000).
>   Our model achieves an AUROC of 0.88 on TCGA, outperforming comparable pre-scan methods by 4.8%. It also achieves AUROCs of 0.72 on Regensburg and
>   Augsburg slides, underscoring challenges related to scanner-induced domain shifts. Furthermore, the model processes each slide in 21 ms, $400\times$
>   faster than existing high-magnification, full-resolution methods, enabling rapid, high-throughput processing.
>   This approach provides an efficient solution for detecting labelling errors without relying on high-magnification scans, offering a valuable tool for
>   quality control in high-throughput pathology workflows. Future work will improve and evaluate the model's generalisation to additional scanner
>   types. Our findings suggest that this method can increase accuracy and efficiency in digital pathology workflows and may be extended to other
>   low-resolution slide annotations.

