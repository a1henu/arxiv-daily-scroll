---
layout: default
title: Transfer Learning from One Cancer to Another via Deep Learning Domain Adaptation
---

# Transfer Learning from One Cancer to Another via Deep Learning Domain Adaptation
**arXiv**：[2601.14678v1](https://arxiv.org/abs/2601.14678) · [PDF](https://arxiv.org/pdf/2601.14678.pdf)  
**作者**：Justin Cheung, Samuel Savine, Calvin Nguyen, Lin Lu, Alhassan S. Yasin  

**一句话要点**：提出基于域对抗神经网络的迁移学习方法，以解决癌症组织病理学图像跨域分类中的泛化问题。

**关键词**：域适应, 癌症组织病理学, 域对抗神经网络, 迁移学习, 跨域分类, 集成梯度

## 3 点简述
- 核心问题：监督深度学习模型在癌症组织病理学中泛化能力差，难以跨不同癌症类型分类。
- 方法要点：使用域对抗神经网络（DANN）进行域适应，从有标签源癌症数据迁移知识到无标签目标癌症数据。
- 实验或效果：DANN在从乳腺和结肠癌适应到肺癌时达到95.56%准确率，显著优于单域模型和集成方法。

## 摘要（原文）

> Supervised deep learning models often achieve excellent performance within their training distribution but struggle to generalize beyond it. In cancer histopathology, for example, a convolutional neural network (CNN) may classify cancer severity accurately for cancer types represented in its training data, yet fail on related but unseen types. Although adenocarcinomas from different organs share morphological features that might support limited cross-domain generalization, addressing domain shift directly is necessary for robust performance. Domain adaptation offers a way to transfer knowledge from labeled data in one cancer type to unlabeled data in another, helping mitigate the scarcity of annotated medical images.
>   This work evaluates cross-domain classification performance among lung, colon, breast, and kidney adenocarcinomas. A ResNet50 trained on any single adenocarcinoma achieves over 98% accuracy on its own domain but shows minimal generalization to others. Ensembling multiple supervised models does not resolve this limitation. In contrast, converting the ResNet50 into a domain adversarial neural network (DANN) substantially improves performance on unlabeled target domains. A DANN trained on labeled breast and colon data and adapted to unlabeled lung data reaches 95.56% accuracy.
>   We also examine the impact of stain normalization on domain adaptation. Its effects vary by target domain: for lung, accuracy drops from 95.56% to 66.60%, while for breast and colon targets, stain normalization boosts accuracy from 49.22% to 81.29% and from 78.48% to 83.36%, respectively. Finally, using Integrated Gradients reveals that DANNs consistently attribute importance to biologically meaningful regions such as densely packed nuclei, indicating that the model learns clinically relevant features and can apply them to unlabeled cancer types.

