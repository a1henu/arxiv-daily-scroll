---
layout: default
title: CASR-Net: An Image Processing-focused Deep Learning-based Coronary Artery Segmentation and Refinement Network for X-ray Coronary Angiogram
---

# CASR-Net: An Image Processing-focused Deep Learning-based Coronary Artery Segmentation and Refinement Network for X-ray Coronary Angiogram
**arXiv**：[2510.27315v1](https://arxiv.org/abs/2510.27315) · [PDF](https://arxiv.org/pdf/2510.27315.pdf)  
**作者**：Alvee Hassan, Rusab Sarmun, Muhammad E. H. Chowdhury, M. Murugappan, Md. Sakib Abrar Hossain, Sakib Mahmud, Abdulrahman Alqahtani, Sohaib Bassam Zoghoul, Amith Khandakar, Susu M. Zughaier, Somaya Al-Maadeed, Anwarul Hasan  

**一句话要点**：提出CASR-Net以改进X射线冠脉造影图像中的冠状动脉分割

**关键词**：冠状动脉分割, 图像预处理, 深度学习网络, X射线造影分析, 医学图像分割

## 3 点简述
- 核心问题：X射线冠脉造影图像质量差影响冠状动脉疾病早期检测。
- 方法要点：采用三阶段流程，包括预处理、基于UNet与Self-ONN的分割和轮廓精炼。
- 实验或效果：在公开数据集上评估，IoU达61.43%，DSC达76.10%。

## 摘要（原文）

> Early detection of coronary artery disease (CAD) is critical for reducing
> mortality and improving patient treatment planning. While angiographic image
> analysis from X-rays is a common and cost-effective method for identifying
> cardiac abnormalities, including stenotic coronary arteries, poor image quality
> can significantly impede clinical diagnosis. We present the Coronary Artery
> Segmentation and Refinement Network (CASR-Net), a three-stage pipeline
> comprising image preprocessing, segmentation, and refinement. A novel
> multichannel preprocessing strategy combining CLAHE and an improved Ben Graham
> method provides incremental gains, increasing Dice Score Coefficient (DSC) by
> 0.31-0.89% and Intersection over Union (IoU) by 0.40-1.16% compared with using
> the techniques individually. The core innovation is a segmentation network
> built on a UNet with a DenseNet121 encoder and a Self-organized Operational
> Neural Network (Self-ONN) based decoder, which preserves the continuity of
> narrow and stenotic vessel branches. A final contour refinement module further
> suppresses false positives. Evaluated with 5-fold cross-validation on a
> combination of two public datasets that contain both healthy and stenotic
> arteries, CASR-Net outperformed several state-of-the-art models, achieving an
> IoU of 61.43%, a DSC of 76.10%, and clDice of 79.36%. These results highlight a
> robust approach to automated coronary artery segmentation, offering a valuable
> tool to support clinicians in diagnosis and treatment planning.

