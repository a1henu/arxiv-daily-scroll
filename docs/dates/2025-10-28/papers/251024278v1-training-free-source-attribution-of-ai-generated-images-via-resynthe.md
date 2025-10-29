---
layout: default
title: Training-free Source Attribution of AI-generated Images via Resynthesis
---

# Training-free Source Attribution of AI-generated Images via Resynthesis
**arXiv**：[2510.24278v1](https://arxiv.org/abs/2510.24278) · [PDF](https://arxiv.org/pdf/2510.24278.pdf)  
**作者**：Pietro Bongini, Valentina Molinari, Andrea Costanzo, Benedetta Tondi, Mauro Barni  

**一句话要点**：提出基于图像重合成的免训练单样本归属方法，以解决数据稀缺下的AI生成图像来源归属问题。

**关键词**：图像来源归属, 免训练方法, 图像重合成, 少样本学习, 零样本分类, 合成图像数据集

## 3 点简述
- 核心问题：在数据稀缺条件下，实现AI生成图像的少样本或零样本来源归属。
- 方法要点：通过生成描述提示，用候选来源重合成图像，并在特征空间中比较与原图的相似度。
- 实验或效果：在新建数据集上，该方法优于现有少样本方法，尤其在训练样本有限时。

## 摘要（原文）

> Synthetic image source attribution is a challenging task, especially in data
> scarcity conditions requiring few-shot or zero-shot classification
> capabilities. We present a new training-free one-shot attribution method based
> on image resynthesis. A prompt describing the image under analysis is
> generated, then it is used to resynthesize the image with all the candidate
> sources. The image is attributed to the model which produced the resynthesis
> closest to the original image in a proper feature space. We also introduce a
> new dataset for synthetic image attribution consisting of face images from
> commercial and open-source text-to-image generators. The dataset provides a
> challenging attribution framework, useful for developing new attribution models
> and testing their capabilities on different generative architectures. The
> dataset structure allows to test approaches based on resynthesis and to compare
> them to few-shot methods. Results from state-of-the-art few-shot approaches and
> other baselines show that the proposed resynthesis method outperforms existing
> techniques when only a few samples are available for training or fine-tuning.
> The experiments also demonstrate that the new dataset is a challenging one and
> represents a valuable benchmark for developing and evaluating future few-shot
> and zero-shot methods.

