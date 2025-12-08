---
layout: default
title: Moving object detection from multi-depth images with an attention-enhanced CNN
---

# Moving object detection from multi-depth images with an attention-enhanced CNN
**arXiv**：[2512.05415v1](https://arxiv.org/abs/2512.05415) · [PDF](https://arxiv.org/pdf/2512.05415.pdf)  
**作者**：Masato Shibukawa, Fumi Yoshida, Toshifumi Yanagisawa, Takashi Ito, Hirohisa Kurosaki, Makoto Yoshikawa, Kohki Kamiya, Ji-an Jiang, Wesley Fraser, JJ Kavelaars, Susan Benecchi, Anne Verbiscer, Akira Hatakeyama, Hosei O, Naoya Ozaki  

**一句话要点**：提出多输入注意力增强CNN以提升太阳系移动目标检测的自动化水平

**关键词**：移动目标检测, 多输入卷积神经网络, 注意力机制, 太阳系巡天, 自动化验证

## 3 点简述
- 核心问题：太阳系宽场巡天数据中移动目标检测依赖人工验证，成本高昂。
- 方法要点：采用多输入架构处理堆叠图像，并集成卷积块注意力模块以聚焦关键特征。
- 实验或效果：在约2000张观测图像数据集上，模型准确率近99%，AUC>0.99，减少人工工作量超99%。

## 摘要（原文）

> One of the greatest challenges for detecting moving objects in the solar system from wide-field survey data is determining whether a signal indicates a true object or is due to some other source, like noise. Object verification has relied heavily on human eyes, which usually results in significant labor costs. In order to address this limitation and reduce the reliance on manual intervention, we propose a multi-input convolutional neural network integrated with a convolutional block attention module. This method is specifically tailored to enhance the moving object detection system that we have developed and used previously. The current method introduces two innovations. This first one is a multi-input architecture that processes multiple stacked images simultaneously. The second is the incorporation of the convolutional block attention module which enables the model to focus on essential features in both spatial and channel dimensions. These advancements facilitate efficient learning from multiple inputs, leading to more robust detection of moving objects. The performance of the model is evaluated on a dataset consisting of approximately 2,000 observational images. We achieved an accuracy of nearly 99% with AUC (an Area Under the Curve) of >0.99. These metrics indicate that the proposed model achieves excellent classification performance. By adjusting the threshold for object detection, the new model reduces the human workload by more than 99% compared to manual verification.

