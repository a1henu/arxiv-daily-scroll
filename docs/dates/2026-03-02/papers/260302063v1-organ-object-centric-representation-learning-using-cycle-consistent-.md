---
layout: default
title: ORGAN: Object-Centric Representation Learning using Cycle Consistent Generative Adversarial Networks
---

# ORGAN: Object-Centric Representation Learning using Cycle Consistent Generative Adversarial Networks
**arXiv**：[2603.02063v1](https://arxiv.org/abs/2603.02063) · [PDF](https://arxiv.org/pdf/2603.02063.pdf)  
**作者**：Joël Küchler, Ellen van Maren, Vaiva Vasiliauskaitė, Katarina Vulić, Reza Abbasi-Asl, Stephan J. Ihle  

**一句话要点**：提出ORGAN，基于循环一致生成对抗网络实现无监督物体中心表示学习。

**关键词**：物体中心表示学习, 生成对抗网络, 循环一致性, 无监督学习, 图像分割

## 3 点简述
- 核心问题：无监督图像信息提取困难，现有方法多基于自编码器，难以处理复杂真实数据集。
- 方法要点：采用循环一致生成对抗网络，分割图像为物体并编码到低维潜在空间。
- 实验或效果：在合成数据集上性能媲美先进方法，在真实数据集上表现更优，支持物体操作和良好扩展性。

## 摘要（原文）

> Although data generation is often straightforward, extracting information from data is more difficult. Object-centric representation learning can extract information from images in an unsupervised manner. It does so by segmenting an image into its subcomponents: the objects. Each object is then represented in a low-dimensional latent space that can be used for downstream processing. Object-centric representation learning is dominated by autoencoder architectures (AEs). Here, we present ORGAN, a novel approach for object-centric representation learning, which is based on cycle-consistent Generative Adversarial Networks instead. We show that it performs similarly to other state-of-the-art approaches on synthetic datasets, while at the same time being the only approach tested here capable of handling more challenging real-world datasets with many objects and low visual contrast. Complementing these results, ORGAN creates expressive latent space representations that allow for object manipulation. Finally, we show that ORGAN scales well both with respect to the number of objects and the size of the images, giving it a unique edge over current state-of-the-art approaches.

