---
layout: default
title: Unsupervised MRI-US Multimodal Image Registration with Multilevel Correlation Pyramidal Optimization
---

# Unsupervised MRI-US Multimodal Image Registration with Multilevel Correlation Pyramidal Optimization
**arXiv**：[2602.06288v1](https://arxiv.org/abs/2602.06288) · [PDF](https://arxiv.org/pdf/2602.06288.pdf)  
**作者**：Jiazheng Wang, Zeyu Liu, Min Liu, Xiang Chen, Hang Zhang  

**一句话要点**：提出基于多级相关金字塔优化的无监督MRI-US多模态图像配准方法，用于术前到术中导航。

**关键词**：多模态图像配准, 无监督学习, 金字塔优化, 医学图像处理, 手术导航

## 3 点简述
- 核心问题：多模态图像差异及术中组织变形导致术前与术中图像配准困难。
- 方法要点：使用模态独立邻域描述符提取特征，通过多级金字塔融合优化位移场。
- 实验或效果：在Learn2Reg 2025的ReMIND2Reg任务中验证和测试阶段均排名第一，Resect数据集上平均TRE为1.798毫米。

## 摘要（原文）

> Surgical navigation based on multimodal image registration has played a significant role in providing intraoperative guidance to surgeons by showing the relative position of the target area to critical anatomical structures during surgery. However, due to the differences between multimodal images and intraoperative image deformation caused by tissue displacement and removal during the surgery, effective registration of preoperative and intraoperative multimodal images faces significant challenges. To address the multimodal image registration challenges in Learn2Reg 2025, an unsupervised multimodal medical image registration method based on multilevel correlation pyramidal optimization (MCPO) is designed to solve these problems. First, the features of each modality are extracted based on the modality independent neighborhood descriptor, and the multimodal images is mapped to the feature space. Second, a multilevel pyramidal fusion optimization mechanism is designed to achieve global optimization and local detail complementation of the displacement field through dense correlation analysis and weight-balanced coupled convex optimization for input features at different scales. Our method focuses on the ReMIND2Reg task in Learn2Reg 2025. Based on the results, our method achieved the first place in the validation phase and test phase of ReMIND2Reg. The MCPO is also validated on the Resect dataset, achieving an average TRE of 1.798 mm. This demonstrates the broad applicability of our method in preoperative-to-intraoperative image registration. The code is avaliable at https://github.com/wjiazheng/MCPO.

