---
layout: default
title: VGG Induced Deep Hand Sign Language Detection
---

# VGG Induced Deep Hand Sign Language Detection
**arXiv**：[2601.08262v1](https://arxiv.org/abs/2601.08262) · [PDF](https://arxiv.org/pdf/2601.08262.pdf)  
**作者**：Subham Sharma, Sharmila Subudhi  

**一句话要点**：提出基于VGG-16的手语识别系统，用于辅助残障人士人机交互。

**关键词**：手语识别, VGG-16, 迁移学习, 图像数据增强, 人机交互

## 3 点简述
- 核心问题：手语识别对视觉障碍者人机交互至关重要，需高精度模型。
- 方法要点：使用VGG-16卷积神经网络，结合迁移学习和图像数据增强进行训练。
- 实验或效果：在NUS数据集验证，并通过自建测试集实验，准确率约98%。

## 摘要（原文）

> Hand gesture recognition is an important aspect of human-computer interaction. It forms the basis of sign language for the visually impaired people. This work proposes a novel hand gesture recognizing system for the differently-abled persons. The model uses a convolutional neural network, known as VGG-16 net, for building a trained model on a widely used image dataset by employing Python and Keras libraries. Furthermore, the result is validated by the NUS dataset, consisting of 10 classes of hand gestures, fed to the model as the validation set. Afterwards, a testing dataset of 10 classes is built by employing Google's open source Application Programming Interface (API) that captures different gestures of human hand and the efficacy is then measured by carrying out experiments. The experimental results show that by combining a transfer learning mechanism together with the image data augmentation, the VGG-16 net produced around 98% accuracy.

