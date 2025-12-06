---
layout: default
title: Not All Birds Look The Same: Identity-Preserving Generation For Birds
---

# Not All Birds Look The Same: Identity-Preserving Generation For Birds
**arXiv**：[2512.04485v1](https://arxiv.org/abs/2512.04485) · [PDF](https://arxiv.org/pdf/2512.04485.pdf)  
**作者**：Aaron Sun, Oindrila Saha, Subhransu Maji  

**一句话要点**：提出NABirds Look-Alikes数据集以评估鸟类身份保持生成，并基于物种、年龄和性别分组训练提升性能。

**关键词**：身份保持生成, 细粒度视觉识别, 鸟类图像数据集, 可控图像生成, 零样本学习

## 3 点简述
- 核心问题：现有身份保持生成模型在非刚性或细粒度类别（如鸟类）上表现不佳，缺乏高质量数据用于评估和改进。
- 方法要点：引入NABirds Look-Alikes数据集，包含专家策划的图像对，并利用物种、年龄和性别作为身份代理进行分组训练。
- 实验或效果：在NABirds Look-Alikes数据集上，现有基线模型失败，而分组训练方法显著提升了在可见和未见物种上的性能。

## 摘要（原文）

> Since the advent of controllable image generation, increasingly rich modes of control have enabled greater customization and accessibility for everyday users. Zero-shot, identity-preserving models such as Insert Anything and OminiControl now support applications like virtual try-on without requiring additional fine-tuning. While these models may be fitting for humans and rigid everyday objects, they still have limitations for non-rigid or fine-grained categories. These domains often lack accessible, high-quality data -- especially videos or multi-view observations of the same subject -- making them difficult both to evaluate and to improve upon. Yet, such domains are essential for moving beyond content creation toward applications that demand accuracy and fine detail. Birds are an excellent domain for this task: they exhibit high diversity, require fine-grained cues for identification, and come in a wide variety of poses. We introduce the NABirds Look-Alikes (NABLA) dataset, consisting of 4,759 expert-curated image pairs. Together with 1,073 pairs collected from multi-image observations on iNaturalist and a small set of videos, this forms a benchmark for evaluating identity-preserving generation of birds. We show that state-of-the-art baselines fail to maintain identity on this dataset, and we demonstrate that training on images grouped by species, age, and sex -- used as a proxy for identity -- substantially improves performance on both seen and unseen species.

