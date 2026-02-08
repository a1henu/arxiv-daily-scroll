---
layout: default
title: Multi-AD: Cross-Domain Unsupervised Anomaly Detection for Medical and Industrial Applications
---

# Multi-AD: Cross-Domain Unsupervised Anomaly Detection for Medical and Industrial Applications
**arXiv**：[2602.05426v1](https://arxiv.org/abs/2602.05426) · [PDF](https://arxiv.org/pdf/2602.05426.pdf)  
**作者**：Wahyu Rahmaniar, Kenji Suzuki  

**一句话要点**：提出Multi-AD模型，通过跨域无监督异常检测解决医学和工业图像中标注数据缺乏的问题。

**关键词**：跨域异常检测, 无监督学习, 卷积神经网络, 知识蒸馏, 医学图像分析, 工业缺陷检测

## 3 点简述
- 核心问题：传统深度学习在跨域异常检测中因标注数据不足而受限，影响医学早期诊断和工业缺陷检测。
- 方法要点：结合SE块增强特征提取、知识蒸馏传递信息、判别器网络区分正常与异常数据，采用师生架构和多尺度特征集成。
- 实验或效果：在脑MRI、肝CT、视网膜OCT和MVTec AD等数据集上评估，图像级和像素级AUROC均优于现有方法，展现强泛化能力。

## 摘要（原文）

> Traditional deep learning models often lack annotated data, especially in cross-domain applications such as anomaly detection, which is critical for early disease diagnosis in medicine and defect detection in industry. To address this challenge, we propose Multi-AD, a convolutional neural network (CNN) model for robust unsupervised anomaly detection across medical and industrial images. Our approach employs the squeeze-and-excitation (SE) block to enhance feature extraction via channel-wise attention, enabling the model to focus on the most relevant features and detect subtle anomalies. Knowledge distillation (KD) transfers informative features from the teacher to the student model, enabling effective learning of the differences between normal and anomalous data. Then, the discriminator network further enhances the model's capacity to distinguish between normal and anomalous data. At the inference stage, by integrating multi-scale features, the student model can detect anomalies of varying sizes. The teacher-student (T-S) architecture ensures consistent representation of high-dimensional features while adapting them to enhance anomaly detection. Multi-AD was evaluated on several medical datasets, including brain MRI, liver CT, and retina OCT, as well as industrial datasets, such as MVTec AD, demonstrating strong generalization across multiple domains. Experimental results demonstrated that our approach consistently outperformed state-of-the-art models, achieving the best average AUROC for both image-level (81.4% for medical and 99.6% for industrial) and pixel-level (97.0% for medical and 98.4% for industrial) tasks, making it effective for real-world applications.

