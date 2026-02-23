---
layout: default
title: MUOT_3M: A 3 Million Frame Multimodal Underwater Benchmark and the MUTrack Tracking Method
---

# MUOT_3M: A 3 Million Frame Multimodal Underwater Benchmark and the MUTrack Tracking Method
**arXiv**：[2602.18006v1](https://arxiv.org/abs/2602.18006) · [PDF](https://arxiv.org/pdf/2602.18006.pdf)  
**作者**：Ahsan Baidar Bakht, Mohamad Alansari, Muhayy Ud Din, Muzammal Naseer, Sajid Javed, Irfan Hussain, Jiri Matas, Arif Mahmood  

**一句话要点**：提出MUOT_3M基准与MUTrack方法以解决水下目标跟踪中数据集稀缺与多模态融合问题。

**关键词**：水下目标跟踪, 多模态基准, 知识蒸馏, 视觉语言融合, SAM跟踪器

## 3 点简述
- 核心问题：水下目标跟踪因缺乏大规模多模态数据集而受限，现有基准小且仅RGB，难以应对恶劣水下条件。
- 方法要点：构建首个伪多模态基准MUOT_3M，含3百万帧；提出MUTrack跟踪器，基于SAM，融合视觉几何对齐、视觉语言和知识蒸馏。
- 实验或效果：在五个基准上评估，MUTrack比最强基线AUC提升8.40%，精度提升7.80%，运行速度24 FPS。

## 摘要（原文）

> Underwater Object Tracking (UOT) is crucial for efficient marine robotics, large scale ecological monitoring, and ocean exploration; however, progress has been hindered by the scarcity of large, multimodal, and diverse datasets. Existing benchmarks remain small and RGB only, limiting robustness under severe color distortion, turbidity, and low visibility conditions. We introduce MUOT_3M, the first pseudo multimodal UOT benchmark comprising 3 million frames from 3,030 videos (27.8h) annotated with 32 tracking attributes, 677 fine grained classes, and synchronized RGB, estimated enhanced RGB, estimated depth, and language modalities validated by a marine biologist. Building upon MUOT_3M, we propose MUTrack, a SAM-based multimodal to unimodal tracker featuring visual geometric alignment, vision language fusion, and four level knowledge distillation that transfers multimodal knowledge into a unimodal student model. Extensive evaluations across five UOT benchmarks demonstrate that MUTrack achieves up to 8.40% higher AUC and 7.80% higher precision than the strongest SOTA baselines while running at 24 FPS. MUOT_3M and MUTrack establish a new foundation for scalable, multimodally trained yet practically deployable underwater tracking.

