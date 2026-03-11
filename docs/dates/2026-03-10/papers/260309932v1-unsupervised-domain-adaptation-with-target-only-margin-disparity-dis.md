---
layout: default
title: Unsupervised Domain Adaptation with Target-Only Margin Disparity Discrepancy
---

# Unsupervised Domain Adaptation with Target-Only Margin Disparity Discrepancy
**arXiv**：[2603.09932v1](https://arxiv.org/abs/2603.09932) · [PDF](https://arxiv.org/pdf/2603.09932.pdf)  
**作者**：Gauthier Miralles, Loïc Le Folgoc, Vincent Jugnon, Pietro Gori  

**一句话要点**：提出基于目标域边际差异差异的无监督域适应框架，以提升CBCT肝脏分割性能。

**关键词**：无监督域适应, 肝脏分割, CBCT成像, 边际差异差异, 模态转换

## 3 点简述
- 核心问题：CBCT数据稀缺且无标注，与CT存在模态差异，影响肝脏分割。
- 方法要点：改进边际差异差异优化框架，实现无监督域适应，减少模态差距。
- 实验或效果：在CT和CBCT数据集上实现SOTA性能，包括少样本设置。

## 摘要（原文）

> In interventional radiology, Cone-Beam Computed Tomography (CBCT) is a helpful imaging modality that provides guidance to practicians during minimally invasive procedures. CBCT differs from traditional Computed Tomography (CT) due to its limited reconstructed field of view, specific artefacts, and the intra-arterial administration of contrast medium. While CT benefits from abundant publicly available annotated datasets, interventional CBCT data remain scarce and largely unannotated, with existing datasets focused primarily on radiotherapy applications. To address this limitation, we leverage a proprietary collection of unannotated interventional CBCT scans in conjunction with annotated CT data, employing domain adaptation techniques to bridge the modality gap and enhance liver segmentation performance on CBCT. We propose a novel unsupervised domain adaptation (UDA) framework based on the formalism of Margin Disparity Discrepancy (MDD), which improves target domain performance through a reformulation of the original MDD optimization framework. Experimental results on CT and CBCT datasets for liver segmentation demonstrate that our method achieves state-of-the-art performance in UDA, as well as in the few-shot setting.

