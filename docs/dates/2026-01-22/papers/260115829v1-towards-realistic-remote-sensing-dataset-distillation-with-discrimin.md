---
layout: default
title: Towards Realistic Remote Sensing Dataset Distillation with Discriminative Prototype-guided Diffusion
---

# Towards Realistic Remote Sensing Dataset Distillation with Discriminative Prototype-guided Diffusion
**arXiv**：[2601.15829v1](https://arxiv.org/abs/2601.15829) · [PDF](https://arxiv.org/pdf/2601.15829.pdf)  
**作者**：Yonghao Xu, Pedram Ghamisi, Qihao Weng  

**一句话要点**：提出基于判别原型引导扩散的遥感数据集蒸馏方法，以解决大规模数据存储、计算成本高和数据泄露风险问题。

**关键词**：遥感图像解释, 数据集蒸馏, 扩散模型, 判别原型引导, 场景分类, 数据压缩

## 3 点简述
- 核心问题：遥感图像解释依赖大规模数据集，导致高存储计算成本和数据泄露风险。
- 方法要点：使用文本到图像扩散模型蒸馏数据集，结合分类一致性损失和原型聚类提升样本判别性。
- 实验或效果：在三个高分辨率遥感场景分类基准上验证，能生成真实多样样本用于下游训练。

## 摘要（原文）

> Recent years have witnessed the remarkable success of deep learning in remote sensing image interpretation, driven by the availability of large-scale benchmark datasets. However, this reliance on massive training data also brings two major challenges: (1) high storage and computational costs, and (2) the risk of data leakage, especially when sensitive categories are involved. To address these challenges, this study introduces the concept of dataset distillation into the field of remote sensing image interpretation for the first time. Specifically, we train a text-to-image diffusion model to condense a large-scale remote sensing dataset into a compact and representative distilled dataset. To improve the discriminative quality of the synthesized samples, we propose a classifier-driven guidance by injecting a classification consistency loss from a pre-trained model into the diffusion training process. Besides, considering the rich semantic complexity of remote sensing imagery, we further perform latent space clustering on training samples to select representative and diverse prototypes as visual style guidance, while using a visual language model to provide aggregated text descriptions. Experiments on three high-resolution remote sensing scene classification benchmarks show that the proposed method can distill realistic and diverse samples for downstream model training. Code and pre-trained models are available online (https://github.com/YonghaoXu/DPD).

