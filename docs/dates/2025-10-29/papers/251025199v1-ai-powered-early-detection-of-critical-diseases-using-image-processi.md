---
layout: default
title: AI-Powered Early Detection of Critical Diseases using Image Processing and Audio Analysis
---

# AI-Powered Early Detection of Critical Diseases using Image Processing and Audio Analysis
**arXiv**：[2510.25199v1](https://arxiv.org/abs/2510.25199) · [PDF](https://arxiv.org/pdf/2510.25199.pdf)  
**作者**：Manisha More, Kavya Bhand, Kaustubh Mukdam, Kavya Sharma, Manas Kawtikwar, Hridayansh Kaware, Prajwal Kavhar  

**一句话要点**：提出多模态AI框架，集成图像与音频分析，用于早期检测皮肤癌、血管血栓和心肺异常。

**关键词**：多模态AI诊断, 图像分析, 音频信号处理, 早期疾病检测, 轻量级部署

## 3 点简述
- 核心问题：现有诊断技术成本高、侵入性强，在资源匮乏地区难以普及。
- 方法要点：使用MobileNetV2、SVM和Random Forest，结合图像、热成像和音频信号处理。
- 实验效果：在皮肤癌、血栓和心肺异常检测中，准确率分别达89.3%、86.4%和87.2%。

## 摘要（原文）

> Early diagnosis of critical diseases can significantly improve patient
> survival and reduce treatment costs. However, existing diagnostic techniques
> are often costly, invasive, and inaccessible in low-resource regions. This
> paper presents a multimodal artificial intelligence (AI) diagnostic framework
> integrating image analysis, thermal imaging, and audio signal processing for
> early detection of three major health conditions: skin cancer, vascular blood
> clots, and cardiopulmonary abnormalities. A fine-tuned MobileNetV2
> convolutional neural network was trained on the ISIC 2019 dataset for skin
> lesion classification, achieving 89.3% accuracy, 91.6% sensitivity, and 88.2%
> specificity. A support vector machine (SVM) with handcrafted features was
> employed for thermal clot detection, achieving 86.4% accuracy (AUC = 0.89) on
> synthetic and clinical data. For cardiopulmonary analysis, lung and heart sound
> datasets from PhysioNet and Pascal were processed using Mel-Frequency Cepstral
> Coefficients (MFCC) and classified via Random Forest, reaching 87.2% accuracy
> and 85.7% sensitivity. Comparative evaluation against state-of-the-art models
> demonstrates that the proposed system achieves competitive results while
> remaining lightweight and deployable on low-cost devices. The framework
> provides a promising step toward scalable, real-time, and accessible AI-based
> pre-diagnostic healthcare solutions.

