---
layout: default
title: ChimeraLoRA: Multi-Head LoRA-Guided Synthetic Datasets
---

# ChimeraLoRA: Multi-Head LoRA-Guided Synthetic Datasets
**arXiv**：[2602.19708v1](https://arxiv.org/abs/2602.19708) · [PDF](https://arxiv.org/pdf/2602.19708.pdf)  
**作者**：Hoyoung Kim, Minwoo Jang, Jabin Koo, Sangdoo Yun, Jungseul Ok  

**一句话要点**：提出ChimeraLoRA方法，结合类共享与每图像LoRA，以解决少样本数据下合成图像多样性与细节保留的平衡问题。

**关键词**：少样本学习, 扩散模型, LoRA微调, 图像合成, 数据增强

## 3 点简述
- 核心问题：少样本场景下，现有LoRA方法在合成图像时难以同时保证多样性和细节准确性。
- 方法要点：分离LoRA为类共享部分和每图像部分，通过语义增强和Dirichlet分布混合生成图像。
- 实验或效果：在多个数据集上，合成图像更接近真实分布，提升下游分类准确性。

## 摘要（原文）

> Beyond general recognition tasks, specialized domains including privacy-constrained medical applications and fine-grained settings often encounter data scarcity, especially for tail classes. To obtain less biased and more reliable models under such scarcity, practitioners leverage diffusion models to supplement underrepresented regions of real data. Specifically, recent studies fine-tune pretrained diffusion models with LoRA on few-shot real sets to synthesize additional images. While an image-wise LoRA trained on a single image captures fine-grained details yet offers limited diversity, a class-wise LoRA trained over all shots produces diverse images as it encodes class priors yet tends to overlook fine details. To combine both benefits, we separate the adapter into a class-shared LoRA~$A$ for class priors and per-image LoRAs~$\mathcal{B}$ for image-specific characteristics. To expose coherent class semantics in the shared LoRA~$A$, we propose a semantic boosting by preserving class bounding boxes during training. For generation, we compose $A$ with a mixture of $\mathcal{B}$ using coefficients drawn from a Dirichlet distribution. Across diverse datasets, our synthesized images are both diverse and detail-rich while closely aligning with the few-shot real distribution, yielding robust gains in downstream classification accuracy.

