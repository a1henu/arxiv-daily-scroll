---
layout: default
title: Squeezed-Eff-Net: Edge-Computed Boost of Tomography Based Brain Tumor Classification leveraging Hybrid Neural Network Architecture
---

# Squeezed-Eff-Net: Edge-Computed Boost of Tomography Based Brain Tumor Classification leveraging Hybrid Neural Network Architecture
**arXiv**：[2512.07241v1](https://arxiv.org/abs/2512.07241) · [PDF](https://arxiv.org/pdf/2512.07241.pdf)  
**作者**：Md. Srabon Chowdhury, Syeda Fahmida Tanzim, Sheekar Banerjee, Ishtiak Al Mamoon, AKM Muzahidul Islam  

**一句话要点**：提出Squeezed-Eff-Net混合网络，结合轻量SqueezeNet与高效EfficientNet，增强手工特征，用于MRI脑肿瘤分类。

**关键词**：脑肿瘤分类, 混合神经网络, MRI图像分析, 手工特征增强, 边缘计算优化

## 3 点简述
- 核心问题：MRI脑肿瘤分类依赖人工，耗时且易出错，需自动化高精度诊断。
- 方法要点：融合SqueezeNet v1和EfficientNet-B0，集成HOG、LBP等手工特征，平衡计算效率与准确性。
- 实验或效果：在Nickparvar数据集上测试准确率达98.93%，TTA后达99.08%，参数少于210万，计算量低于1.2 GFLOPs。

## 摘要（原文）

> Brain tumors are one of the most common and dangerous neurological diseases which require a timely and correct diagnosis to provide the right treatment procedures. Even with the promotion of magnetic resonance imaging (MRI), the process of tumor delineation is difficult and time-consuming, which is prone to inter-observer error. In order to overcome these limitations, this work proposes a hybrid deep learning model based on SqueezeNet v1 which is a lightweight model, and EfficientNet-B0, which is a high-performing model, and is enhanced with handcrafted radiomic descriptors, including Histogram of Oriented Gradients (HOG), Local Binary Patterns (LBP), Gabor filters and Wavelet transforms. The framework was trained and tested only on publicly available Nickparvar Brain Tumor MRI dataset, which consisted of 7,023 contrast-enhanced T1-weighted axial MRI slices which were categorized into four groups: glioma, meningioma, pituitary tumor, and no tumor. The testing accuracy of the model was 98.93% that reached a level of 99.08% with Test Time Augmentation (TTA) showing great generalization and power. The proposed hybrid network offers a compromise between computation efficiency and diagnostic accuracy compared to current deep learning structures and only has to be trained using fewer than 2.1 million parameters and less than 1.2 GFLOPs. The handcrafted feature addition allowed greater sensitivity in texture and the EfficientNet-B0 backbone represented intricate hierarchical features. The resulting model has almost clinical reliability in automated MRI-based classification of tumors highlighting its possibility of use in clinical decision-support systems.

