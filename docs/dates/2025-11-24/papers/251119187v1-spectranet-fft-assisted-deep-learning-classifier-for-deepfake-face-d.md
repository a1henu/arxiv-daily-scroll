---
layout: default
title: SpectraNet: FFT-assisted Deep Learning Classifier for Deepfake Face Detection
---

# SpectraNet: FFT-assisted Deep Learning Classifier for Deepfake Face Detection
**arXiv**：[2511.19187v1](https://arxiv.org/abs/2511.19187) · [PDF](https://arxiv.org/pdf/2511.19187.pdf)  
**作者**：Nithira Jayarathne, Naveen Basnayake, Keshawa Jayasundara, Pasindu Dodampegama, Praveen Wijesinghe, Hirushika Pelagewatta, Kavishka Abeywardana, Sandushan Ranaweera, Chamira Edussooriya  

**一句话要点**：提出基于EfficientNet-B6的轻量级深度伪造人脸检测模型，以应对类别不平衡问题。

**关键词**：深度伪造检测, 类别不平衡处理, EfficientNet微调, 轻量级模型, 图像分类

## 3 点简述
- 核心问题：检测深度伪造图像以对抗错误信息，面临严重类别不平衡挑战。
- 方法要点：采用EfficientNet-B6微调，结合预处理、过采样和优化策略提升模型性能。
- 实验或效果：模型实现高准确率、稳定性和泛化能力，但傅里叶变换特征影响未知。

## 摘要（原文）

> Detecting deepfake images is crucial in combating misinformation. We present a lightweight, generalizable binary classification model based on EfficientNet-B6, fine-tuned with transformation techniques to address severe class imbalances. By leveraging robust preprocessing, oversampling, and optimization strategies, our model achieves high accuracy, stability, and generalization. While incorporating Fourier transform-based phase and amplitude features showed minimal impact, our proposed framework helps non-experts to effectively identify deepfake images, making significant strides toward accessible and reliable deepfake detection.

