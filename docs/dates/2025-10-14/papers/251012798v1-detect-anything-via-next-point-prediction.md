---
layout: default
title: Detect Anything via Next Point Prediction
---

# Detect Anything via Next Point Prediction
**arXiv**：[2510.12798v1](https://arxiv.org/abs/2510.12798) · [PDF](https://arxiv.org/pdf/2510.12798.pdf)  
**作者**：Qing Jiang, Junan Huo, Xingyu Chen, Yuda Xiong, Zhaoyang Zeng, Yihao Chen, Tianhe Ren, Junzhi Yu, Lei Zhang  

**一句话要点**：提出Rex-Omni模型，通过下一点预测实现零样本物体检测与多任务感知

**关键词**：多模态大语言模型, 物体检测, 零样本学习, 坐标量化, 强化学习训练, 视觉语言任务

## 3 点简述
- 传统回归模型在物体检测中存在召回率低、重复预测等问题，MLLMs应用受限。
- 采用量化坐标表示、多数据引擎生成和两阶段训练，提升坐标预测精度与效率。
- 在COCO和LVIS基准上零样本性能媲美回归模型，并支持多种语言感知任务。

## 摘要（原文）

> Object detection has long been dominated by traditional coordinate
> regression-based models, such as YOLO, DETR, and Grounding DINO. Although
> recent efforts have attempted to leverage MLLMs to tackle this task, they face
> challenges like low recall rate, duplicate predictions, coordinate
> misalignment, etc. In this work, we bridge this gap and propose Rex-Omni, a
> 3B-scale MLLM that achieves state-of-the-art object perception performance. On
> benchmarks like COCO and LVIS, Rex-Omni attains performance comparable to or
> exceeding regression-based models (e.g., DINO, Grounding DINO) in a zero-shot
> setting. This is enabled by three key designs: 1) Task Formulation: we use
> special tokens to represent quantized coordinates from 0 to 999, reducing the
> model's learning difficulty and improving token efficiency for coordinate
> prediction; 2) Data Engines: we construct multiple data engines to generate
> high-quality grounding, referring, and pointing data, providing semantically
> rich supervision for training; \3) Training Pipelines: we employ a two-stage
> training process, combining supervised fine-tuning on 22 million data with
> GRPO-based reinforcement post-training. This RL post-training leverages
> geometry-aware rewards to effectively bridge the discrete-to-continuous
> coordinate prediction gap, improve box accuracy, and mitigate undesirable
> behaviors like duplicate predictions that stem from the teacher-guided nature
> of the initial SFT stage. Beyond conventional detection, Rex-Omni's inherent
> language understanding enables versatile capabilities such as object referring,
> pointing, visual prompting, GUI grounding, spatial referring, OCR and
> key-pointing, all systematically evaluated on dedicated benchmarks. We believe
> that Rex-Omni paves the way for more versatile and language-aware visual
> perception systems.

