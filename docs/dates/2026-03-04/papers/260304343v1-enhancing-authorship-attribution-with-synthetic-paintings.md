---
layout: default
title: Enhancing Authorship Attribution with Synthetic Paintings
---

# Enhancing Authorship Attribution with Synthetic Paintings
**arXiv**：[2603.04343v1](https://arxiv.org/abs/2603.04343) · [PDF](https://arxiv.org/pdf/2603.04343.pdf)  
**作者**：Clarissa Loures, Caio Hosken, Luan Oliveira, Gianlucca Zuin, Adriano Veloso  

**一句话要点**：提出结合真实与合成图像的混合方法，以增强数据稀缺场景下的画作作者归属分类性能。

**关键词**：作者归属, 合成图像生成, 混合数据训练, 艺术品认证, 计算机视觉

## 3 点简述
- 核心问题：画作作者归属任务中，真实艺术品数据有限，影响模型训练效果。
- 方法要点：使用DreamBooth微调Stable Diffusion生成合成图像，结合真实数据构建混合训练集。
- 实验或效果：实验显示，添加合成图像能提高ROC-AUC和准确率，优于仅用真实画作。

## 摘要（原文）

> Attributing authorship to paintings is a historically complex task, and one of its main challenges is the limited availability of real artworks for training computational models. This study investigates whether synthetic images, generated through DreamBooth fine-tuning of Stable Diffusion, can improve the performance of classification models in this context. We propose a hybrid approach that combines real and synthetic data to enhance model accuracy and generalization across similar artistic styles. Experimental results show that adding synthetic images leads to higher ROC-AUC and accuracy compared to using only real paintings. By integrating generative and discriminative methods, this work contributes to the development of computer vision techniques for artwork authentication in data-scarce scenarios.

