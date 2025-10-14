---
layout: default
title: InfiniHuman: Infinite 3D Human Creation with Precise Control
---

# InfiniHuman: Infinite 3D Human Creation with Precise Control
**arXiv**：[2510.11650v1](https://arxiv.org/abs/2510.11650) · [PDF](https://arxiv.org/pdf/2510.11650.pdf)  
**作者**：Yuxuan Xue, Xianghui Xie, Margaret Kostyrko, Gerard Pons-Moll  

**一句话要点**：提出InfiniHuman框架以解决3D人体生成的可控性与多样性问题

**关键词**：3D人体生成, 数据蒸馏, 扩散模型, 多模态数据集, 可控生成

## 3 点简述
- 核心问题：如何利用基础模型生成无限多样且可控的3D人体数据
- 方法要点：通过蒸馏视觉语言和图像生成模型，构建自动数据生成管道
- 实验或效果：用户研究表明生成身份与扫描渲染无法区分，提升视觉质量和可控性

## 摘要（原文）

> Generating realistic and controllable 3D human avatars is a long-standing
> challenge, particularly when covering broad attribute ranges such as ethnicity,
> age, clothing styles, and detailed body shapes. Capturing and annotating
> large-scale human datasets for training generative models is prohibitively
> expensive and limited in scale and diversity. The central question we address
> in this paper is: Can existing foundation models be distilled to generate
> theoretically unbounded, richly annotated 3D human data? We introduce
> InfiniHuman, a framework that synergistically distills these models to produce
> richly annotated human data at minimal cost and with theoretically unlimited
> scalability. We propose InfiniHumanData, a fully automatic pipeline that
> leverages vision-language and image generation models to create a large-scale
> multi-modal dataset. User study shows our automatically generated identities
> are undistinguishable from scan renderings. InfiniHumanData contains 111K
> identities spanning unprecedented diversity. Each identity is annotated with
> multi-granularity text descriptions, multi-view RGB images, detailed clothing
> images, and SMPL body-shape parameters. Building on this dataset, we propose
> InfiniHumanGen, a diffusion-based generative pipeline conditioned on text, body
> shape, and clothing assets. InfiniHumanGen enables fast, realistic, and
> precisely controllable avatar generation. Extensive experiments demonstrate
> significant improvements over state-of-the-art methods in visual quality,
> generation speed, and controllability. Our approach enables high-quality avatar
> generation with fine-grained control at effectively unbounded scale through a
> practical and affordable solution. We will publicly release the automatic data
> generation pipeline, the comprehensive InfiniHumanData dataset, and the
> InfiniHumanGen models at https://yuxuan-xue.com/infini-human.

