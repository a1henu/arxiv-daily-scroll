---
layout: default
title: A Review of Longitudinal Radiology Report Generation: Dataset Composition, Methods, and Performance Evaluation
---

# A Review of Longitudinal Radiology Report Generation: Dataset Composition, Methods, and Performance Evaluation
**arXiv**：[2510.12444v1](https://arxiv.org/abs/2510.12444) · [PDF](https://arxiv.org/pdf/2510.12444.pdf)  
**作者**：Shaoyang Zhou, Yingshu Li, Yunyi Liu, Lingqiao Liu, Lei Wang, Luping Zhou  

**一句话要点**：综述纵向放射学报告生成，涵盖数据集、方法和评估，以提升临床准确性。

**关键词**：纵向放射学报告生成, 数据集构建, 模型架构设计, 性能评估, 消融研究, 临床准确性

## 3 点简述
- 核心问题：传统方法依赖单张图像，无法捕捉纵向上下文，影响报告临床准确性。
- 方法要点：整合纵向数据，设计专用架构，模拟放射科医生诊断工作流程。
- 实验或效果：分析性能与消融研究，强调纵向信息和架构设计对模型改进的关键作用。

## 摘要（原文）

> Chest Xray imaging is a widely used diagnostic tool in modern medicine, and
> its high utilization creates substantial workloads for radiologists. To
> alleviate this burden, vision language models are increasingly applied to
> automate Chest Xray radiology report generation (CXRRRG), aiming for clinically
> accurate descriptions while reducing manual effort. Conventional approaches,
> however, typically rely on single images, failing to capture the longitudinal
> context necessary for producing clinically faithful comparison statements.
> Recently, growing attention has been directed toward incorporating longitudinal
> data into CXR RRG, enabling models to leverage historical studies in ways that
> mirror radiologists diagnostic workflows. Nevertheless, existing surveys
> primarily address single image CXRRRG and offer limited guidance for
> longitudinal settings, leaving researchers without a systematic framework for
> model design. To address this gap, this survey provides the first comprehensive
> review of longitudinal radiology report generation (LRRG). Specifically, we
> examine dataset construction strategies, report generation architectures
> alongside longitudinally tailored designs, and evaluation protocols
> encompassing both longitudinal specific measures and widely used benchmarks. We
> further summarize LRRG methods performance, alongside analyses of different
> ablation studies, which collectively highlight the critical role of
> longitudinal information and architectural design choices in improving model
> performance. Finally, we summarize five major limitations of current research
> and outline promising directions for future development, aiming to lay a
> foundation for advancing this emerging field.

