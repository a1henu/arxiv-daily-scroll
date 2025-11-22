---
layout: default
title: Supervised Contrastive Learning for Few-Shot AI-Generated Image Detection and Attribution
---

# Supervised Contrastive Learning for Few-Shot AI-Generated Image Detection and Attribution
**arXiv**：[2511.16541v1](https://arxiv.org/abs/2511.16541) · [PDF](https://arxiv.org/pdf/2511.16541.pdf)  
**作者**：Jaime Álvarez Urueña, David Camacho, Javier Huertas Tato  

**一句话要点**：提出监督对比学习与k-NN的两阶段框架，以解决少样本AI生成图像检测与溯源问题

**关键词**：监督对比学习, 少样本学习, AI生成图像检测, 图像溯源, k-NN分类, 泛化能力

## 3 点简述
- 核心问题：生成AI模型快速迭代，传统检测方法因需频繁重训练而不可行
- 方法要点：首阶段用监督对比学习提取嵌入，次阶段用k-NN进行少样本分类
- 实验效果：仅150样本/类，检测准确率达91.3%，溯源AUC提升14.70%

## 摘要（原文）

> The rapid advancement of generative artificial intelligence has enabled the creation of synthetic images that are increasingly indistinguishable from authentic content, posing significant challenges for digital media integrity. This problem is compounded by the accelerated release cycle of novel generative models, which renders traditional detection approaches (reliant on periodic retraining) computationally infeasible and operationally impractical.
>   This work proposes a novel two-stage detection framework designed to address the generalization challenge inherent in synthetic image detection. The first stage employs a vision deep learning model trained via supervised contrastive learning to extract discriminative embeddings from input imagery. Critically, this model was trained on a strategically partitioned subset of available generators, with specific architectures withheld from training to rigorously ablate cross-generator generalization capabilities. The second stage utilizes a k-nearest neighbors (k-NN) classifier operating on the learned embedding space, trained in a few-shot learning paradigm incorporating limited samples from previously unseen test generators.
>   With merely 150 images per class in the few-shot learning regime, which are easily obtainable from current generation models, the proposed framework achieves an average detection accuracy of 91.3\%, representing a 5.2 percentage point improvement over existing approaches . For the source attribution task, the proposed approach obtains improvements of of 14.70\% and 4.27\% in AUC and OSCR respectively on an open set classification context, marking a significant advancement toward robust, scalable forensic attribution systems capable of adapting to the evolving generative AI landscape without requiring exhaustive retraining protocols.

