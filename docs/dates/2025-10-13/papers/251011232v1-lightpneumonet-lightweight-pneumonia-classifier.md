---
layout: default
title: LightPneumoNet: Lightweight Pneumonia Classifier
---

# LightPneumoNet: Lightweight Pneumonia Classifier
**arXiv**：[2510.11232v1](https://arxiv.org/abs/2510.11232) · [PDF](https://arxiv.org/pdf/2510.11232.pdf)  
**作者**：Neilansh Chauhan, Piyush Kumar Gupta, Faraz Doja  

**一句话要点**：提出轻量级CNN LightPneumoNet以在资源受限环境中准确诊断肺炎

**关键词**：肺炎分类, 轻量级CNN, 胸部X光, 计算机辅助诊断, 资源受限部署

## 3 点简述
- 资源受限环境下部署大型深度学习模型困难，影响肺炎诊断
- 设计轻量CNN架构，仅38.8万参数，内存占用1.48MB
- 在独立测试集上准确率0.942，敏感度0.99，减少假阴性

## 摘要（原文）

> Effective pneumonia diagnosis is often challenged by the difficulty of
> deploying large, computationally expensive deep learning models in
> resource-limited settings. This study introduces LightPneumoNet, an efficient,
> lightweight convolutional neural network (CNN) built from scratch to provide an
> accessible and accurate diagnostic solution for pneumonia detection from chest
> X-rays. Our model was trained on a public dataset of 5,856 chest X-ray images.
> Preprocessing included image resizing to 224x224, grayscale conversion, and
> pixel normalization, with data augmentation (rotation, zoom, shear) to prevent
> overfitting. The custom architecture features four blocks of stacked
> convolutional layers and contains only 388,082 trainable parameters, resulting
> in a minimal 1.48 MB memory footprint. On the independent test set, our model
> delivered exceptional performance, achieving an overall accuracy of 0.942,
> precision of 0.92, and an F1-Score of 0.96. Critically, it obtained a
> sensitivity (recall) of 0.99, demonstrating a near-perfect ability to identify
> true pneumonia cases and minimize clinically significant false negatives.
> Notably, LightPneumoNet achieves this high recall on the same dataset where
> existing approaches typically require significantly heavier architectures or
> fail to reach comparable sensitivity levels. The model's efficiency enables
> deployment on low-cost hardware, making advanced computer-aided diagnosis
> accessible in underserved clinics and serving as a reliable second-opinion tool
> to improve patient outcomes.

