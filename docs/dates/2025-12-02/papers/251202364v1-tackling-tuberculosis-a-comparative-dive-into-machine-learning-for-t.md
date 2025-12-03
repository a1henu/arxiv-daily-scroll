---
layout: default
title: Tackling Tuberculosis: A Comparative Dive into Machine Learning for Tuberculosis Detection
---

# Tackling Tuberculosis: A Comparative Dive into Machine Learning for Tuberculosis Detection
**arXiv**：[2512.02364v1](https://arxiv.org/abs/2512.02364) · [PDF](https://arxiv.org/pdf/2512.02364.pdf)  
**作者**：Daanish Hindustani, Sanober Hindustani, Preston Nguyen  

**一句话要点**：比较ResNet-50与SqueezeNet在胸部X光图像中检测结核病的性能

**关键词**：结核病检测, 胸部X光图像, 深度学习, ResNet-50, SqueezeNet, 医疗影像分析

## 3 点简述
- 核心问题：结核病诊断在资源有限环境中效率低下，需探索自动化方法。
- 方法要点：使用预训练ResNet-50和SqueezeNet模型，基于Kaggle数据集进行训练与比较。
- 实验或效果：SqueezeNet表现更优，准确率89%，F1分数87%，优于ResNet-50的73%和65%。

## 摘要（原文）

> This study explores the application of machine learning models, specifically a pretrained ResNet-50 model and a general SqueezeNet model, in diagnosing tuberculosis (TB) using chest X-ray images. TB, a persistent infectious disease affecting humanity for millennia, poses challenges in diagnosis, especially in resource-limited settings. Traditional methods, such as sputum smear microscopy and culture, are inefficient, prompting the exploration of advanced technologies like deep learning and computer vision. The study utilized a dataset from Kaggle, consisting of 4,200 chest X-rays, to develop and compare the performance of the two machine learning models. Preprocessing involved data splitting, augmentation, and resizing to enhance training efficiency. Evaluation metrics, including accuracy, precision, recall, and confusion matrix, were employed to assess model performance. Results showcase that the SqueezeNet achieved a loss of 32%, accuracy of 89%, precision of 98%, recall of 80%, and an F1 score of 87%. In contrast, the ResNet-50 model exhibited a loss of 54%, accuracy of 73%, precision of 88%, recall of 52%, and an F1 score of 65%. This study emphasizes the potential of machine learning in TB detection and possible implications for early identification and treatment initiation. The possibility of integrating such models into mobile devices expands their utility in areas lacking TB detection resources. However, despite promising results, the need for continued development of faster, smaller, and more accurate TB detection models remains crucial in contributing to the global efforts in combating TB.

