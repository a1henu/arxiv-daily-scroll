---
layout: default
title: Unsupervised Synthetic Image Attribution: Alignment and Disentanglement
---

# Unsupervised Synthetic Image Attribution: Alignment and Disentanglement
**arXiv**：[2601.22663v1](https://arxiv.org/abs/2601.22663) · [PDF](https://arxiv.org/pdf/2601.22663.pdf)  
**作者**：Zongfang Liu, Guangyi Chen, Boyang Sun, Tongliang Liu, Kun Zhang  

**一句话要点**：提出无监督对齐与解耦方法，解决合成图像溯源问题，无需配对标注

**关键词**：合成图像溯源, 无监督学习, 表示对齐, 表示解耦, 对比学习, 版权保护

## 3 点简述
- 核心问题：合成图像溯源需配对标注，获取成本高且困难
- 方法要点：通过对比自监督学习对齐概念，利用Infomax损失解耦表示增强溯源能力
- 实验或效果：在AbC基准上，无监督方法意外超越有监督方法

## 摘要（原文）

> As the quality of synthetic images improves, identifying the underlying concepts of model-generated images is becoming increasingly crucial for copyright protection and ensuring model transparency. Existing methods achieve this attribution goal by training models using annotated pairs of synthetic images and their original training sources. However, obtaining such paired supervision is challenging, as it requires either well-designed synthetic concepts or precise annotations from millions of training sources. To eliminate the need for costly paired annotations, in this paper, we explore the possibility of unsupervised synthetic image attribution. We propose a simple yet effective unsupervised method called Alignment and Disentanglement. Specifically, we begin by performing basic concept alignment using contrastive self-supervised learning. Next, we enhance the model's attribution ability by promoting representation disentanglement with the Infomax loss. This approach is motivated by an interesting observation: contrastive self-supervised models, such as MoCo and DINO, inherently exhibit the ability to perform simple cross-domain alignment. By formulating this observation as a theoretical assumption on cross-covariance, we provide a theoretical explanation of how alignment and disentanglement can approximate the concept-matching process through a decomposition of the canonical correlation analysis objective. On the real-world benchmarks, AbC, we show that our unsupervised method surprisingly outperforms the supervised methods. As a starting point, we expect our intuitive insights and experimental findings to provide a fresh perspective on this challenging task.

