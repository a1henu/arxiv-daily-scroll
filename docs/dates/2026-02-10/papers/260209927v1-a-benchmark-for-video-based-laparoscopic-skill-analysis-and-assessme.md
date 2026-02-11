---
layout: default
title: A benchmark for video-based laparoscopic skill analysis and assessment
---

# A benchmark for video-based laparoscopic skill analysis and assessment
**arXiv**：[2602.09927v1](https://arxiv.org/abs/2602.09927) · [PDF](https://arxiv.org/pdf/2602.09927.pdf)  
**作者**：Isabel Funke, Sebastian Bodenstedt, Felix von Bechtolsheim, Florian Oehme, Michael Maruschke, Stefanie Herrlich, Jürgen Weitz, Marius Distler, Sören Torge Mees, Stefanie Speidel  

**一句话要点**：提出LASANA数据集以解决腹腔镜手术技能视频评估中标注数据不足的问题。

**关键词**：腹腔镜手术技能评估, 视频数据集, 深度学习基准测试, 结构化技能评分, 错误识别

## 3 点简述
- 核心问题：腹腔镜手术技能评估依赖深度学习，但现有标注视频数据集规模有限，阻碍模型开发与评估。
- 方法要点：引入LASANA数据集，包含1270个立体视频记录，覆盖四个基本训练任务，提供结构化技能评分和错误标签。
- 实验或效果：提供预定义数据分割和深度学习基线结果，便于视频技能评估和错误识别方法的基准测试。

## 摘要（原文）

> Laparoscopic surgery is a complex surgical technique that requires extensive training. Recent advances in deep learning have shown promise in supporting this training by enabling automatic video-based assessment of surgical skills. However, the development and evaluation of deep learning models is currently hindered by the limited size of available annotated datasets. To address this gap, we introduce the Laparoscopic Skill Analysis and Assessment (LASANA) dataset, comprising 1270 stereo video recordings of four basic laparoscopic training tasks. Each recording is annotated with a structured skill rating, aggregated from three independent raters, as well as binary labels indicating the presence or absence of task-specific errors. The majority of recordings originate from a laparoscopic training course, thereby reflecting a natural variation in the skill of participants. To facilitate benchmarking of both existing and novel approaches for video-based skill assessment and error recognition, we provide predefined data splits for each task. Furthermore, we present baseline results from a deep learning model as a reference point for future comparisons.

