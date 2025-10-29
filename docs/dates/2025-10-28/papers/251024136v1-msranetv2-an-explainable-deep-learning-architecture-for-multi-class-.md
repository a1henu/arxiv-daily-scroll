---
layout: default
title: MSRANetV2: An Explainable Deep Learning Architecture for Multi-class Classification of Colorectal Histopathological Images
---

# MSRANetV2: An Explainable Deep Learning Architecture for Multi-class Classification of Colorectal Histopathological Images
**arXiv**：[2510.24136v1](https://arxiv.org/abs/2510.24136) · [PDF](https://arxiv.org/pdf/2510.24136.pdf)  
**作者**：Ovi Sarkar, Md Shafiuzzaman, Md. Faysal Ahamed, Golam Mahmud, Muhammad E. H. Chowdhury  

**一句话要点**：提出MSRANetV2架构以提升结直肠组织图像多分类的准确性与可解释性

**关键词**：结直肠组织分类, 深度残差网络, 注意力机制, 多尺度特征融合, 模型可解释性, 医学图像分析

## 3 点简述
- 结直肠癌诊断存在主观性和耗时问题，需自动化方法提升精度
- 基于ResNet50V2，集成残差注意力和SE块，融合多尺度特征增强分类鲁棒性
- 在公开数据集上验证，平均准确率超0.99，并采用Grad-CAM提高模型可解释性

## 摘要（原文）

> Colorectal cancer (CRC) is a leading worldwide cause of cancer-related
> mortality, and the role of prompt precise detection is of paramount interest in
> improving patient outcomes. Conventional diagnostic methods such as colonoscopy
> and histological examination routinely exhibit subjectivity, are extremely
> time-consuming, and are susceptible to variation. Through the development of
> digital pathology, deep learning algorithms have become a powerful approach in
> enhancing diagnostic precision and efficiency. In our work, we proposed a
> convolutional neural network architecture named MSRANetV2, specially optimized
> for the classification of colorectal tissue images. The model employs a
> ResNet50V2 backbone, extended with residual attention mechanisms and
> squeeze-and-excitation (SE) blocks, to extract deep semantic and fine-grained
> spatial features. With channel alignment and upsampling operations, MSRANetV2
> effectively fuses multi-scale representations, thereby enhancing the robustness
> of the classification. We evaluated our model on a five-fold stratified
> cross-validation strategy on two publicly available datasets: CRC-VAL-HE-7K and
> NCT-CRC-HE-100K. The proposed model achieved remarkable average Precision,
> recall, F1-score, AUC, and test accuracy were 0.9884 plus-minus 0.0151, 0.9900
> plus-minus 0.0151, 0.9900 plus-minus 0.0145, 0.9999 plus-minus 0.00006, and
> 0.9905 plus-minus 0.0025 on the 7K dataset. On the 100K dataset, they were
> 0.9904 plus-minus 0.0091, 0.9900 plus-minus 0.0071, 0.9900 plus-minus 0.0071,
> 0.9997 plus-minus 0.00016, and 0.9902 plus-minus 0.0006. Additionally, Grad-CAM
> visualizations were incorporated to enhance model interpretability by
> highlighting tissue areas that are medically relevant. These findings validate
> that MSRANetV2 is a reliable, interpretable, and high-performing architectural
> model for classifying CRC tissues.

