---
layout: default
title: CR-QAT: Curriculum Relational Quantization-Aware Training for Open-Vocabulary Object Detection
---

# CR-QAT: Curriculum Relational Quantization-Aware Training for Open-Vocabulary Object Detection
**arXiv**：[2603.05964v1](https://arxiv.org/abs/2603.05964) · [PDF](https://arxiv.org/pdf/2603.05964.pdf)  
**作者**：Jinyeong Park, Donghwa Kim, Brent ByungHoon Kang, Hyeongboo Baek, Jibum Kim  

**一句话要点**：提出CR-QAT框架，通过课程量化与关系蒸馏解决开放词汇目标检测的低比特量化性能下降问题。

**关键词**：开放词汇目标检测, 量化感知训练, 知识蒸馏, 低比特量化, 视觉语言对齐

## 3 点简述
- 核心问题：开放词汇目标检测中，极端低比特量化会损害视觉-语言对齐和区域间关系结构。
- 方法要点：结合分阶段课程量化以隔离误差，并应用文本中心关系知识蒸馏来传递多维度关系知识。
- 实验或效果：在LVIS和COCO零样本基准上，CR-QAT显著优于现有QAT基线，相对AP提升最高达40.9%。

## 摘要（原文）

> Open-vocabulary object detection (OVOD) enables novel category detection via vision-language alignment, but massive model sizes hinder deployment on resource-constrained devices. While quantization offers practical compression, we reveal that naive extreme low-bit (e.g., 4-bit) quantization severely degrades fine-grained vision-language alignment and distorts inter-region relational structures. To address this, we propose curriculum relational quantization-aware training (CR-QAT), an integrated framework combining stage-by-stage optimization with relational knowledge distillation. Within CR-QAT, curriculum QAT (CQAT) mitigates error accumulation by partitioning the model for progressive quantization, ensuring stable optimization via error isolation. Concurrently, text-centric relational KD (TRKD) is applied to task-relevant modules. By constructing text-anchored pairwise similarity matrices, TRKD comprehensively transfers the teacher's multi-dimensional relational knowledge. Experiments on LVIS and COCO zero-shot benchmarks demonstrate that CR-QAT consistently outperforms existing QAT baselines under aggressive low-bit settings, achieving relative AP improvements of up to 38.9% and 40.9%, respectively.

