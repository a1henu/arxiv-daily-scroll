---
layout: default
title: Annotation Free Spacecraft Detection and Segmentation using Vision Language Models
---

# Annotation Free Spacecraft Detection and Segmentation using Vision Language Models
**arXiv**：[2602.04699v1](https://arxiv.org/abs/2602.04699) · [PDF](https://arxiv.org/pdf/2602.04699.pdf)  
**作者**：Samet Hicsonmez, Jose Sosa, Dan Pineau, Inder Pal Singh, Arunkumar Rathinam, Abd El Rahman Shabayek, Djamila Aouada  

**一句话要点**：提出基于视觉语言模型的标注自由航天器检测与分割方法，以解决空间目标识别中手动标注困难的问题。

**关键词**：视觉语言模型, 标注自由检测, 航天器分割, 伪标签生成, 师生蒸馏, 空间目标识别

## 3 点简述
- 核心问题：空间应用中手动标注因低可见度、光照变化和背景融合而极具挑战，需开发免标注方法。
- 方法要点：利用预训练视觉语言模型自动生成伪标签，通过师生标签蒸馏框架训练轻量模型，提升性能。
- 实验或效果：在多个数据集上评估，分割任务的平均精度提升高达10点，代码和模型已开源。

## 摘要（原文）

> Vision Language Models (VLMs) have demonstrated remarkable performance in open-world zero-shot visual recognition. However, their potential in space-related applications remains largely unexplored. In the space domain, accurate manual annotation is particularly challenging due to factors such as low visibility, illumination variations, and object blending with planetary backgrounds. Developing methods that can detect and segment spacecraft and orbital targets without requiring extensive manual labeling is therefore of critical importance. In this work, we propose an annotation-free detection and segmentation pipeline for space targets using VLMs. Our approach begins by automatically generating pseudo-labels for a small subset of unlabeled real data with a pre-trained VLM. These pseudo-labels are then leveraged in a teacher-student label distillation framework to train lightweight models. Despite the inherent noise in the pseudo-labels, the distillation process leads to substantial performance gains over direct zero-shot VLM inference. Experimental evaluations on the SPARK-2024, SPEED+, and TANGO datasets on segmentation tasks demonstrate consistent improvements in average precision (AP) by up to 10 points. Code and models are available at https://github.com/giddyyupp/annotation-free-spacecraft-segmentation.

