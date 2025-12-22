---
layout: default
title: Interpretable Plant Leaf Disease Detection Using Attention-Enhanced CNN
---

# Interpretable Plant Leaf Disease Detection Using Attention-Enhanced CNN
**arXiv**：[2512.17864v1](https://arxiv.org/abs/2512.17864) · [PDF](https://arxiv.org/pdf/2512.17864.pdf)  
**作者**：Balram Singh, Ram Prakash Sharma, Somnath Dey  

**一句话要点**：提出基于注意力增强CNN的CBAM-VGG16模型，用于可解释的植物叶片病害检测。

**关键词**：植物病害检测, 注意力机制, 可解释AI, 卷积神经网络, 农业诊断

## 3 点简述
- 核心问题：植物病害威胁粮食安全，需准确且可解释的检测方法。
- 方法要点：在CNN各卷积阶段集成CBAM，增强特征提取和病害定位能力。
- 实验或效果：在五个数据集上优于现有技术，准确率达98.87%，并通过多种方法验证可解释性。

## 摘要（原文）

> Plant diseases pose a significant threat to global food security, necessitating accurate and interpretable disease detection methods. This study introduces an interpretable attention-guided Convolutional Neural Network (CNN), CBAM-VGG16, for plant leaf disease detection. By integrating Convolution Block Attention Module (CBAM) at each convolutional stage, the model enhances feature extraction and disease localization. Trained on five diverse plant disease datasets, our approach outperforms recent techniques, achieving high accuracy (up to 98.87%) and demonstrating robust generalization. Here, we show the effectiveness of our method through comprehensive evaluation and interpretability analysis using CBAM attention maps, Grad-CAM, Grad-CAM++, and Layer-wise Relevance Propagation (LRP). This study advances the application of explainable AI in agricultural diagnostics, offering a transparent and reliable system for smart farming. The code of our proposed work is available at https://github.com/BS0111/PlantAttentionCBAM.

