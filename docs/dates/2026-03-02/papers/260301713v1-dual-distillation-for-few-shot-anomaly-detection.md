---
layout: default
title: Dual Distillation for Few-Shot Anomaly Detection
---

# Dual Distillation for Few-Shot Anomaly Detection
**arXiv**：[2603.01713v1](https://arxiv.org/abs/2603.01713) · [PDF](https://arxiv.org/pdf/2603.01713.pdf)  
**作者**：Le Dong, Qinzhong Tan, Chunlei Li, Jingliang Hu, Yilei Shi, Weisheng Dong, Xiao Xiang Zhu, Lichao Mou  

**一句话要点**：提出D$^2$4FAD双蒸馏框架以解决医学图像少样本异常检测问题。

**关键词**：少样本异常检测, 双蒸馏框架, 医学图像分析, 自蒸馏学习, 动态权重机制

## 3 点简述
- 核心问题：现有无监督异常检测方法需大量正常数据且跨解剖环境泛化能力差。
- 方法要点：利用预训练编码器作为教师网络提取多尺度特征，学生解码器通过查询图像蒸馏和支撑图像自蒸馏学习。
- 实验或效果：在包含13,084张图像的基准数据集上显著优于现有方法，达到新SOTA。

## 摘要（原文）

> Anomaly detection is a critical task in computer vision with profound implications for medical imaging, where identifying pathologies early can directly impact patient outcomes. While recent unsupervised anomaly detection approaches show promise, they require substantial normal training data and struggle to generalize across anatomical contexts. We introduce D$^2$4FAD, a novel dual distillation framework for few-shot anomaly detection that identifies anomalies in previously unseen tasks using only a small number of normal reference images. Our approach leverages a pre-trained encoder as a teacher network to extract multi-scale features from both support and query images, while a student decoder learns to distill knowledge from the teacher on query images and self-distill on support images. We further propose a learn-to-weight mechanism that dynamically assesses the reference value of each support image conditioned on the query, optimizing anomaly detection performance. To evaluate our method, we curate a comprehensive benchmark dataset comprising 13,084 images across four organs, four imaging modalities, and five disease categories. Extensive experiments demonstrate that D$^2$4FAD significantly outperforms existing approaches, establishing a new state-of-the-art in few-shot medical anomaly detection. Code is available at https://github.com/ttttqz/D24FAD.

