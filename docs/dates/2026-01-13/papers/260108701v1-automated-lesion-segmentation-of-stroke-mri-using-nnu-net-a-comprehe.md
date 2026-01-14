---
layout: default
title: Automated Lesion Segmentation of Stroke MRI Using nnU-Net: A Comprehensive External Validation Across Acute and Chronic Lesions
---

# Automated Lesion Segmentation of Stroke MRI Using nnU-Net: A Comprehensive External Validation Across Acute and Chronic Lesions
**arXiv**：[2601.08701v1](https://arxiv.org/abs/2601.08701) · [PDF](https://arxiv.org/pdf/2601.08701.pdf)  
**作者**：Tammar Truzman, Matthew A. Lambon Ralph, Ajay D. Halai  

**一句话要点**：使用nnU-Net框架评估中风MRI病灶分割，验证其在急性和慢性病灶中的泛化性能

**关键词**：中风病灶分割, nnU-Net框架, MRI图像分析, 泛化性能评估, 深度学习应用

## 3 点简述
- 核心问题：现有深度学习模型在中风MRI病灶分割中泛化能力差，难以适应不同数据集、模态和病程阶段。
- 方法要点：采用nnU-Net框架，在多个公开MRI数据集上训练和测试，覆盖DWI、FLAIR和T1加权图像。
- 实验或效果：模型在急性和慢性中风阶段均表现出稳健泛化，分割精度接近人工标注可靠性，并识别出影响性能的关键因素。

## 摘要（原文）

> Accurate and generalisable segmentation of stroke lesions from magnetic resonance imaging (MRI) is essential for advancing clinical research, prognostic modelling, and personalised interventions. Although deep learning has improved automated lesion delineation, many existing models are optimised for narrow imaging contexts and generalise poorly to independent datasets, modalities, and stroke stages. Here, we systematically evaluated stroke lesion segmentation using the nnU-Net framework across multiple heterogeneous, publicly available MRI datasets spanning acute and chronic stroke. Models were trained and tested on diffusion-weighted imaging (DWI), fluid-attenuated inversion recovery (FLAIR), and T1-weighted MRI, and evaluated on independent datasets. Across stroke stages, models showed robust generalisation, with segmentation accuracy approaching reported inter-rater reliability. Performance varied with imaging modality and training data characteristics. In acute stroke, DWI-trained models consistently outperformed FLAIR-based models, with only modest gains from multimodal combinations. In chronic stroke, increasing training set size improved performance, with diminishing returns beyond several hundred cases. Lesion volume was a key determinant of accuracy: smaller lesions were harder to segment, and models trained on restricted volume ranges generalised poorly. MRI image quality further constrained generalisability: models trained on lower-quality scans transferred poorly, whereas those trained on higher-quality data generalised well to noisier images. Discrepancies between predictions and reference masks were often attributable to limitations in manual annotations. Together, these findings show that automated lesion segmentation can approach human-level performance while identifying key factors governing generalisability and informing the development of lesion segmentation tools.

