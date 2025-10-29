---
layout: default
title: Mars-Bench: A Benchmark for Evaluating Foundation Models for Mars Science Tasks
---

# Mars-Bench: A Benchmark for Evaluating Foundation Models for Mars Science Tasks
**arXiv**：[2510.24010v1](https://arxiv.org/abs/2510.24010) · [PDF](https://arxiv.org/pdf/2510.24010.pdf)  
**作者**：Mirali Purohit, Bimal Gajera, Vatsal Malaviya, Irish Mehta, Kunal Kasodekar, Jacob Adler, Steven Lu, Umaa Rebbapragada, Hannah Kerner  

**一句话要点**：提出Mars-Bench基准以评估火星科学任务的基础模型

**关键词**：火星科学基准, 基础模型评估, 地质特征识别, 轨道与表面图像, 标准化数据集

## 3 点简述
- 火星科学缺乏标准化基准，限制了基础模型的发展
- 引入20个数据集，涵盖分类、分割和检测任务，聚焦地质特征
- 基线评估显示火星特定模型可能优于通用模型，推动领域适应预训练

## 摘要（原文）

> Foundation models have enabled rapid progress across many specialized domains
> by leveraging large-scale pre-training on unlabeled data, demonstrating strong
> generalization to a variety of downstream tasks. While such models have gained
> significant attention in fields like Earth Observation, their application to
> Mars science remains limited. A key enabler of progress in other domains has
> been the availability of standardized benchmarks that support systematic
> evaluation. In contrast, Mars science lacks such benchmarks and standardized
> evaluation frameworks, which have limited progress toward developing foundation
> models for Martian tasks. To address this gap, we introduce Mars-Bench, the
> first benchmark designed to systematically evaluate models across a broad range
> of Mars-related tasks using both orbital and surface imagery. Mars-Bench
> comprises 20 datasets spanning classification, segmentation, and object
> detection, focused on key geologic features such as craters, cones, boulders,
> and frost. We provide standardized, ready-to-use datasets and baseline
> evaluations using models pre-trained on natural images, Earth satellite data,
> and state-of-the-art vision-language models. Results from all analyses suggest
> that Mars-specific foundation models may offer advantages over general-domain
> counterparts, motivating further exploration of domain-adapted pre-training.
> Mars-Bench aims to establish a standardized foundation for developing and
> comparing machine learning models for Mars science. Our data, models, and code
> are available at: https://mars-bench.github.io/.

