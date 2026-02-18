---
layout: default
title: Joint Enhancement and Classification using Coupled Diffusion Models of Signals and Logits
---

# Joint Enhancement and Classification using Coupled Diffusion Models of Signals and Logits
**arXiv**：[2602.15405v1](https://arxiv.org/abs/2602.15405) · [PDF](https://arxiv.org/pdf/2602.15405.pdf)  
**作者**：Gilad Nurko, Roi Benita, Yehoshua Dissen, Tomohiro Nakatani, Marc Delcroix, Shoko Araki, Joseph Keshet  

**一句话要点**：提出耦合扩散模型框架，联合增强信号与分类对数，提升噪声环境下的鲁棒分类性能。

**关键词**：扩散模型, 联合增强分类, 鲁棒分类, 信号去噪, 对数引导

## 3 点简述
- 核心问题：传统方法将信号增强与分类分离，未利用分类器语义信息指导去噪。
- 方法要点：使用两个交互扩散模型，分别处理输入信号和分类器对数，实现相互引导。
- 实验或效果：在图像分类和语音识别任务中，超越传统基线，提升噪声条件下的分类准确率。

## 摘要（原文）

> Robust classification in noisy environments remains a fundamental challenge in machine learning. Standard approaches typically treat signal enhancement and classification as separate, sequential stages: first enhancing the signal and then applying a classifier. This approach fails to leverage the semantic information in the classifier's output during denoising. In this work, we propose a general, domain-agnostic framework that integrates two interacting diffusion models: one operating on the input signal and the other on the classifier's output logits, without requiring any retraining or fine-tuning of the classifier. This coupled formulation enables mutual guidance, where the enhancing signal refines the class estimation and, conversely, the evolving class logits guide the signal reconstruction towards discriminative regions of the manifold. We introduce three strategies to effectively model the joint distribution of the input and the logit. We evaluated our joint enhancement method for image classification and automatic speech recognition. The proposed framework surpasses traditional sequential enhancement baselines, delivering robust and flexible improvements in classification accuracy under diverse noise conditions.

