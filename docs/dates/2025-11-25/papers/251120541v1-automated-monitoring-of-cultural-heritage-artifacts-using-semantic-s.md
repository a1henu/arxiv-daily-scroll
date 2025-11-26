---
layout: default
title: Automated Monitoring of Cultural Heritage Artifacts Using Semantic Segmentation
---

# Automated Monitoring of Cultural Heritage Artifacts Using Semantic Segmentation
**arXiv**：[2511.20541v1](https://arxiv.org/abs/2511.20541) · [PDF](https://arxiv.org/pdf/2511.20541.pdf)  
**作者**：Andrea Ranieri, Giorgio Palmieri, Silvia Biasotti  

**一句话要点**：比较U-Net架构与CNN编码器，用于文化遗产裂缝的语义分割监测

**关键词**：语义分割, 裂缝检测, 文化遗产监测, U-Net架构, CNN编码器, 泛化能力

## 3 点简述
- 核心问题：自动化检测文化遗产中的裂缝，以支持保护工作。
- 方法要点：使用U-Net架构和多种CNN编码器进行像素级裂缝分割。
- 实验或效果：在OmniCrack30k数据集上评估，模型在未见过的文化遗产场景中表现出泛化能力。

## 摘要（原文）

> This paper addresses the critical need for automated crack detection in the preservation of cultural heritage through semantic segmentation. We present a comparative study of U-Net architectures, using various convolutional neural network (CNN) encoders, for pixel-level crack identification on statues and monuments. A comparative quantitative evaluation is performed on the test set of the OmniCrack30k dataset [1] using popular segmentation metrics including Mean Intersection over Union (mIoU), Dice coefficient, and Jaccard index. This is complemented by an out-of-distribution qualitative evaluation on an unlabeled test set of real-world cracked statues and monuments. Our findings provide valuable insights into the capabilities of different CNN- based encoders for fine-grained crack segmentation. We show that the models exhibit promising generalization capabilities to unseen cultural heritage contexts, despite never having been explicitly trained on images of statues or monuments.

