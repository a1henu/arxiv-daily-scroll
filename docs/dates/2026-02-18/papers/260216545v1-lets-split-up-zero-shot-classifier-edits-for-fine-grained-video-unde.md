---
layout: default
title: Let's Split Up: Zero-Shot Classifier Edits for Fine-Grained Video Understanding
---

# Let's Split Up: Zero-Shot Classifier Edits for Fine-Grained Video Understanding
**arXiv**：[2602.16545v1](https://arxiv.org/abs/2602.16545) · [PDF](https://arxiv.org/pdf/2602.16545.pdf)  
**作者**：Kaiting Liu, Hazel Doughty  

**一句话要点**：提出零样本分类器编辑方法，以细粒度视频理解中的类别分裂任务解决固定分类法过粗问题。

**关键词**：零样本学习, 视频分类, 类别分裂, 细粒度识别, 模型编辑

## 3 点简述
- 核心问题：视频识别模型基于固定分类法训练，类别过粗，无法适应新兴细粒度区分，重新标注和训练成本高。
- 方法要点：利用视频分类器的潜在组合结构，零样本编辑现有分类器，将粗类别细分为子类别，无需额外数据。
- 实验或效果：在新视频基准测试中，方法显著优于视觉语言基线，提升分裂类别准确率，同时保持其他类别性能。

## 摘要（原文）

> Video recognition models are typically trained on fixed taxonomies which are often too coarse, collapsing distinctions in object, manner or outcome under a single label. As tasks and definitions evolve, such models cannot accommodate emerging distinctions and collecting new annotations and retraining to accommodate such changes is costly. To address these challenges, we introduce category splitting, a new task where an existing classifier is edited to refine a coarse category into finer subcategories, while preserving accuracy elsewhere. We propose a zero-shot editing method that leverages the latent compositional structure of video classifiers to expose fine-grained distinctions without additional data. We further show that low-shot fine-tuning, while simple, is highly effective and benefits from our zero-shot initialization. Experiments on our new video benchmarks for category splitting demonstrate that our method substantially outperforms vision-language baselines, improving accuracy on the newly split categories without sacrificing performance on the rest. Project page: https://kaitingliu.github.io/Category-Splitting/.

