---
layout: default
title: PICABench: How Far Are We from Physically Realistic Image Editing?
---

# PICABench: How Far Are We from Physically Realistic Image Editing?
**arXiv**：[2510.17681v1](https://arxiv.org/abs/2510.17681) · [PDF](https://arxiv.org/pdf/2510.17681.pdf)  
**作者**：Yuandong Pu, Le Zhuo, Songhao Han, Jinbo Xing, Kaiwen Zhu, Shuo Cao, Bin Fu, Si Liu, Hongsheng Li, Yu Qiao, Wenlong Zhang, Xi Chen, Yihao Liu  

**一句话要点**：提出PICABench以评估图像编辑的物理真实性问题

**关键词**：图像编辑, 物理真实, 基准评估, 视觉语言模型, 数据集构建

## 3 点简述
- 核心问题：现有图像编辑模型忽视物理效果，如阴影和反射的移除
- 方法要点：构建PICABench基准，涵盖八维物理属性和多种编辑操作
- 实验或效果：评估主流模型，发现物理真实性问题仍具挑战性

## 摘要（原文）

> Image editing has achieved remarkable progress recently. Modern editing
> models could already follow complex instructions to manipulate the original
> content. However, beyond completing the editing instructions, the accompanying
> physical effects are the key to the generation realism. For example, removing
> an object should also remove its shadow, reflections, and interactions with
> nearby objects. Unfortunately, existing models and benchmarks mainly focus on
> instruction completion but overlook these physical effects. So, at this moment,
> how far are we from physically realistic image editing? To answer this, we
> introduce PICABench, which systematically evaluates physical realism across
> eight sub-dimension (spanning optics, mechanics, and state transitions) for
> most of the common editing operations (add, remove, attribute change, etc). We
> further propose the PICAEval, a reliable evaluation protocol that uses
> VLM-as-a-judge with per-case, region-level human annotations and questions.
> Beyond benchmarking, we also explore effective solutions by learning physics
> from videos and construct a training dataset PICA-100K. After evaluating most
> of the mainstream models, we observe that physical realism remains a
> challenging problem with large rooms to explore. We hope that our benchmark and
> proposed solutions can serve as a foundation for future work moving from naive
> content editing toward physically consistent realism.

