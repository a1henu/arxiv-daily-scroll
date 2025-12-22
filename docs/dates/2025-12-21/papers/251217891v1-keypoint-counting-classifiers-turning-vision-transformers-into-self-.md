---
layout: default
title: Keypoint Counting Classifiers: Turning Vision Transformers into Self-Explainable Models Without Training
---

# Keypoint Counting Classifiers: Turning Vision Transformers into Self-Explainable Models Without Training
**arXiv**：[2512.17891v1](https://arxiv.org/abs/2512.17891) · [PDF](https://arxiv.org/pdf/2512.17891.pdf)  
**作者**：Kristoffer Wickstrøm, Teresa Dorszewski, Siyan Chen, Michael Kampffmeyer, Elisabeth Wetzer, Robert Jenssen  

**一句话要点**：提出关键点计数分类器，将预训练视觉Transformer转化为无需训练的自解释模型。

**关键词**：自解释模型, 视觉Transformer, 关键点识别, 模型透明度, 无需训练

## 3 点简述
- 核心问题：现有自解释模型训练复杂且架构特定，不适用于视觉Transformer基础模型。
- 方法要点：利用视觉Transformer自动识别图像关键点的能力，构建可视化决策过程。
- 实验或效果：评估显示关键点计数分类器在提升人机通信方面优于基线方法。

## 摘要（原文）

> Current approaches for designing self-explainable models (SEMs) require complicated training procedures and specific architectures which makes them impractical. With the advance of general purpose foundation models based on Vision Transformers (ViTs), this impracticability becomes even more problematic. Therefore, new methods are necessary to provide transparency and reliability to ViT-based foundation models. In this work, we present a new method for turning any well-trained ViT-based model into a SEM without retraining, which we call Keypoint Counting Classifiers (KCCs). Recent works have shown that ViTs can automatically identify matching keypoints between images with high precision, and we build on these results to create an easily interpretable decision process that is inherently visualizable in the input. We perform an extensive evaluation which show that KCCs improve the human-machine communication compared to recent baselines. We believe that KCCs constitute an important step towards making ViT-based foundation models more transparent and reliable.

