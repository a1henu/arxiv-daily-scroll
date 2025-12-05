---
layout: default
title: HTR-ConvText: Leveraging Convolution and Textual Information for Handwritten Text Recognition
---

# HTR-ConvText: Leveraging Convolution and Textual Information for Handwritten Text Recognition
**arXiv**：[2512.05021v1](https://arxiv.org/abs/2512.05021) · [PDF](https://arxiv.org/pdf/2512.05021.pdf)  
**作者**：Pham Thach Thanh Truc, Dang Hoai Nam, Huynh Tong Dang Khoa, Vo Nguyen Le Duy  

**一句话要点**：提出HTR-ConvText模型，结合卷积与文本信息以提升手写文本识别的泛化能力。

**关键词**：手写文本识别, 卷积神经网络, MobileViT, 序列建模, 泛化能力

## 3 点简述
- 核心问题：手写文本识别面临数据有限、书写风格多样和复杂变音符号的挑战。
- 方法要点：集成残差CNN与MobileViT，引入ConvText编码器结合全局上下文与局部特征。
- 实验或效果：在IAM等数据集上验证，在有限样本和高多样性场景中表现优于现有方法。

## 摘要（原文）

> Handwritten Text Recognition remains challenging due to the limited data, high writing style variance, and scripts with complex diacritics. Existing approaches, though partially address these issues, often struggle to generalize without massive synthetic data. To address these challenges, we propose HTR-ConvText, a model designed to capture fine-grained, stroke-level local features while preserving global contextual dependencies. In the feature extraction stage, we integrate a residual Convolutional Neural Network backbone with a MobileViT with Positional Encoding block. This enables the model to both capture structural patterns and learn subtle writing details. We then introduce the ConvText encoder, a hybrid architecture combining global context and local features within a hierarchical structure that reduces sequence length for improved efficiency. Additionally, an auxiliary module injects textual context to mitigate the weakness of Connectionist Temporal Classification. Evaluations on IAM, READ2016, LAM and HANDS-VNOnDB demonstrate that our approach achieves improved performance and better generalization compared to existing methods, especially in scenarios with limited training samples and high handwriting diversity.

