---
layout: default
title: BlendCLIP: Bridging Synthetic and Real Domains for Zero-Shot 3D Object Classification with Multimodal Pretraining
---

# BlendCLIP: Bridging Synthetic and Real Domains for Zero-Shot 3D Object Classification with Multimodal Pretraining
**arXiv**：[2510.18244v1](https://arxiv.org/abs/2510.18244) · [PDF](https://arxiv.org/pdf/2510.18244.pdf)  
**作者**：Ajinkya Khoche, Gergő László Nagy, Maciej Wozniak, Thomas Gustafsson, Patric Jensfelt  

**一句话要点**：提出BlendCLIP框架，通过多模态预训练弥合合成与真实域差距，实现零样本3D物体分类。

**关键词**：零样本学习, 3D物体分类, 多模态预训练, 域适应, LiDAR数据, 合成数据

## 3 点简述
- 核心问题：零样本3D分类受合成与真实数据域差距影响，导致泛化能力差。
- 方法要点：采用课程式数据混合策略，结合合成CAD数据和真实LiDAR扫描进行多模态预训练。
- 实验效果：在nuScenes基准上，仅添加少量真实样本即可提升零样本准确率27%，达到SOTA性能。

## 摘要（原文）

> Zero-shot 3D object classification is crucial for real-world applications
> like autonomous driving, however it is often hindered by a significant domain
> gap between the synthetic data used for training and the sparse, noisy LiDAR
> scans encountered in the real-world. Current methods trained solely on
> synthetic data fail to generalize to outdoor scenes, while those trained only
> on real data lack the semantic diversity to recognize rare or unseen objects.
>   We introduce BlendCLIP, a multimodal pretraining framework that bridges this
> synthetic-to-real gap by strategically combining the strengths of both domains.
> We first propose a pipeline to generate a large-scale dataset of object-level
> triplets -- consisting of a point cloud, image, and text description -- mined
> directly from real-world driving data and human annotated 3D boxes. Our core
> contribution is a curriculum-based data mixing strategy that first grounds the
> model in the semantically rich synthetic CAD data before progressively adapting
> it to the specific characteristics of real-world scans.
>   Our experiments show that our approach is highly label-efficient: introducing
> as few as 1.5\% real-world samples per batch into training boosts zero-shot
> accuracy on the nuScenes benchmark by 27\%. Consequently, our final model
> achieves state-of-the-art performance on challenging outdoor datasets like
> nuScenes and TruckScenes, improving over the best prior method by 19.3\% on
> nuScenes, while maintaining strong generalization on diverse synthetic
> benchmarks. Our findings demonstrate that effective domain adaptation, not
> full-scale real-world annotation, is the key to unlocking robust
> open-vocabulary 3D perception. Our code and dataset will be released upon
> acceptance on https://github.com/kesu1/BlendCLIP.

