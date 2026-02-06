---
layout: default
title: PatchFlow: Leveraging a Flow-Based Model with Patch Features
---

# PatchFlow: Leveraging a Flow-Based Model with Patch Features
**arXiv**：[2602.05238v1](https://arxiv.org/abs/2602.05238) · [PDF](https://arxiv.org/pdf/2602.05238.pdf)  
**作者**：Boxiang Zhang, Baijian Yang, Xiaoming Wang, Corey Vian  

**一句话要点**：提出PatchFlow方法，结合局部补丁特征与归一化流模型，提升压铸缺陷检测精度

**关键词**：异常检测, 归一化流模型, 补丁特征, 压铸缺陷检测, 计算机视觉

## 3 点简述
- 核心问题：压铸表面缺陷检测自动化需求高，现有方法在工业图像上精度不足
- 方法要点：引入适配器模块桥接预训练特征提取器与工业图像，结合局部邻域感知补丁特征
- 实验或效果：在MVTec AD数据集上AUROC达99.28%，错误率降低20%，无需异常样本训练

## 摘要（原文）

> Die casting plays a crucial role across various industries due to its ability to craft intricate shapes with high precision and smooth surfaces. However, surface defects remain a major issue that impedes die casting quality control. Recently, computer vision techniques have been explored to automate and improve defect detection. In this work, we combine local neighbor-aware patch features with a normalizing flow model and bridge the gap between the generic pretrained feature extractor and industrial product images by introducing an adapter module to increase the efficiency and accuracy of automated anomaly detection. Compared to state-of-the-art methods, our approach reduces the error rate by 20\% on the MVTec AD dataset, achieving an image-level AUROC of 99.28\%. Our approach has also enhanced performance on the VisA dataset , achieving an image-level AUROC of 96.48\%. Compared to the state-of-the-art models, this represents a 28.2\% reduction in error. Additionally, experiments on a proprietary die casting dataset yield an accuracy of 95.77\% for anomaly detection, without requiring any anomalous samples for training. Our method illustrates the potential of leveraging computer vision and deep learning techniques to advance inspection capabilities for the die casting industry

