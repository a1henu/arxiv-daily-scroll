---
layout: default
title: Semi-Supervised 3D Segmentation for Type-B Aortic Dissection with Slim UNETR
---

# Semi-Supervised 3D Segmentation for Type-B Aortic Dissection with Slim UNETR
**arXiv**：[2512.17610v1](https://arxiv.org/abs/2512.17610) · [PDF](https://arxiv.org/pdf/2512.17610.pdf)  
**作者**：Denis Mikhailapov, Vladimir Berikov  

**一句话要点**：提出基于Slim UNETR的半监督多输出分割方法，用于B型主动脉夹层3D分割。

**关键词**：半监督学习, 3D医学图像分割, 多输出模型, B型主动脉夹层, Slim UNETR

## 3 点简述
- 核心问题：医学图像分割需大量标注数据，多输出模型半监督方法研究不足。
- 方法要点：采用额外旋转和翻转，不依赖概率假设，适用于多输出架构。
- 实验或效果：基于ImageTBDA数据集，分割主动脉真腔、假腔和血栓，提升标注效率。

## 摘要（原文）

> Convolutional neural networks (CNN) for multi-class segmentation of medical images are widely used today. Especially models with multiple outputs that can separately predict segmentation classes (regions) without relying on a probabilistic formulation of the segmentation of regions. These models allow for more precise segmentation by tailoring the network's components to each class (region). They have a common encoder part of the architecture but branch out at the output layers, leading to improved accuracy.
>   These methods are used to diagnose type B aortic dissection (TBAD), which requires accurate segmentation of aortic structures based on the ImageTBDA dataset, which contains 100 3D computed tomography angiography (CTA) images. These images identify three key classes: true lumen (TL), false lumen (FL), and false lumen thrombus (FLT) of the aorta, which is critical for diagnosis and treatment decisions. In the dataset, 68 examples have a false lumen, while the remaining 32 do not, creating additional complexity for pathology detection.
>   However, implementing these CNN methods requires a large amount of high-quality labeled data. Obtaining accurate labels for the regions of interest can be an expensive and time-consuming process, particularly for 3D data. Semi-supervised learning methods allow models to be trained by using both labeled and unlabeled data, which is a promising approach for overcoming the challenge of obtaining accurate labels. However, these learning methods are not well understood for models with multiple outputs.
>   This paper presents a semi-supervised learning method for models with multiple outputs. The method is based on the additional rotations and flipping, and does not assume the probabilistic nature of the model's responses. This makes it a universal approach, which is especially important for architectures that involve separate segmentation.

