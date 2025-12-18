---
layout: default
title: Cross-modal ultra-scale learning with tri-modalities of renal biopsy images for glomerular multi-disease auxiliary diagnosis
---

# Cross-modal ultra-scale learning with tri-modalities of renal biopsy images for glomerular multi-disease auxiliary diagnosis
**arXiv**：[2512.15171v1](https://arxiv.org/abs/2512.15171) · [PDF](https://arxiv.org/pdf/2512.15171.pdf)  
**作者**：Kaixing Long, Danyi Weng, Yun Mi, Zhentai Zhang, Yanmeng Lu, Jian Geng, Zhitao Zhou, Liming Zhong, Qianjin Feng, Wei Yang, Lei Cao  

**一句话要点**：提出跨模态超尺度学习网络，以解决肾活检图像中纳米与微米尺度差异问题，辅助肾小球多疾病诊断。

**关键词**：跨模态学习, 超尺度融合, 肾活检图像分析, 多疾病分类, 注意力机制, 多模态医学影像

## 3 点简述
- 核心问题：透射电镜图像与光学/免疫荧光显微镜图像间存在纳米与微米尺度差异，阻碍多模态特征融合与分类精度提升。
- 方法要点：设计稀疏多实例学习模块聚合透射电镜特征，并引入跨模态尺度注意力模块促进特征交互，结合多损失函数优化分类。
- 实验或效果：在内部数据集上实现高准确率（ACC 95.37%±2.41%）和AUC（99.05%±0.53%），优于现有方法，并展示在膜性肾病分期中的泛化能力。

## 摘要（原文）

> Constructing a multi-modal automatic classification model based on three types of renal biopsy images can assist pathologists in glomerular multi-disease identification. However, the substantial scale difference between transmission electron microscopy (TEM) image features at the nanoscale and optical microscopy (OM) or immunofluorescence microscopy (IM) images at the microscale poses a challenge for existing multi-modal and multi-scale models in achieving effective feature fusion and improving classification accuracy. To address this issue, we propose a cross-modal ultra-scale learning network (CMUS-Net) for the auxiliary diagnosis of multiple glomerular diseases. CMUS-Net utilizes multiple ultrastructural information to bridge the scale difference between nanometer and micrometer images. Specifically, we introduce a sparse multi-instance learning module to aggregate features from TEM images. Furthermore, we design a cross-modal scale attention module to facilitate feature interaction, enhancing pathological semantic information. Finally, multiple loss functions are combined, allowing the model to weigh the importance among different modalities and achieve precise classification of glomerular diseases. Our method follows the conventional process of renal biopsy pathology diagnosis and, for the first time, performs automatic classification of multiple glomerular diseases including IgA nephropathy (IgAN), membranous nephropathy (MN), and lupus nephritis (LN) based on images from three modalities and two scales. On an in-house dataset, CMUS-Net achieves an ACC of 95.37+/-2.41%, an AUC of 99.05+/-0.53%, and an F1-score of 95.32+/-2.41%. Extensive experiments demonstrate that CMUS-Net outperforms other well-known multi-modal or multi-scale methods and show its generalization capability in staging MN. Code is available at https://github.com/SMU-GL-Group/MultiModal_lkx/tree/main.

