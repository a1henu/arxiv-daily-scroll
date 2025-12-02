---
layout: default
title: A unified framework for geometry-independent operator learning in cardiac electrophysiology simulations
---

# A unified framework for geometry-independent operator learning in cardiac electrophysiology simulations
**arXiv**：[2512.01702v1](https://arxiv.org/abs/2512.01702) · [PDF](https://arxiv.org/pdf/2512.01702.pdf)  
**作者**：Bei Zhou, Cesare Corrado, Shuang Qian, Maximilian Balmus, Angela W. C. Lee, Cristobal Rodero, Marco J. W. Gotte, Luuk H. G. A. Hopman, Mengyun Qiao, Steven Niederer  

**一句话要点**：提出几何无关算子学习框架，用于快速预测心房电激活时间，支持实时临床和大规模分析。

**关键词**：算子学习, 心脏电生理模拟, 几何无关表示, 神经算子, 实时预测, 心房电激活

## 3 点简述
- 核心问题：心房电激活图计算密集，难以实时或大规模应用。
- 方法要点：使用通用心房坐标系和视觉变换器神经算子，解耦电生理模式与网格拓扑。
- 实验或效果：在308,700个模拟上训练，预测误差5.1 ms，推理速度0.12 ms/样本。

## 摘要（原文）

> Accurate maps of atrial electrical activation are essential for personalised treatment of arrhythmias, yet biophysically detailed simulations remain computationally intensive for real-time clinical use or population-scale analyses. Here we introduce a geometry-independent operator-learning framework that predicts local activation time (LAT) fields across diverse left atrial anatomies with near-instantaneous inference. We generated a dataset of 308,700 simulations using a GPU-accelerated electrophysiology solver, systematically varying multiple pacing sites and physiologically varied conduction properties across 147 patient-specific geometries derived from two independent clinical cohorts. All anatomical and functional data are expressed in a Universal Atrium Coordinate system, providing a consistent representation that decouples electrophysiological patterns from mesh topology. Within this coordinate space, we designed a neural operator with a vision-transformer backbone to learn the mapping from structural and electrophysiological inputs to LAT fields. With a mean prediction error of 5.1 ms over a 455 ms maximum simulation time, the model outperforms established operator-learning approaches and performs inference in 0.12 ms per sample. Our framework establishes a general strategy for learning domain-invariant biophysical mappings across variable anatomical domains and enables integration of computational electrophysiology into real-time and large-scale clinical workflows.

