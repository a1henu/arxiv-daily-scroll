---
layout: default
title: MVP: Multiple View Prediction Improves GUI Grounding
---

# MVP: Multiple View Prediction Improves GUI Grounding
**arXiv**：[2512.08529v1](https://arxiv.org/abs/2512.08529) · [PDF](https://arxiv.org/pdf/2512.08529.pdf)  
**作者**：Yunzhu Zhang, Zeyu Pan, Zhengwen Zeng, Shuheng Shen, Changhua Meng, Linchao Zhu  

**一句话要点**：提出多视图预测框架以解决GUI grounding中的坐标预测不稳定问题

**关键词**：GUI grounding, 坐标预测稳定性, 多视图推理, 注意力引导, 无训练框架, 视觉扰动鲁棒性

## 3 点简述
- 核心问题：现有GUI grounding模型对微小视觉扰动敏感，导致坐标预测不稳定，影响高分辨率和小UI元素样本的性能。
- 方法要点：通过注意力引导视图提议和多坐标聚类，无训练地聚合多视图预测，区分正确坐标与异常值。
- 实验或效果：在ScreenSpot-Pro等基准上显著提升多种模型性能，如将Qwen3VL-32B-Instruct提升至74.0%。

## 摘要（原文）

> GUI grounding, which translates natural language instructions into precise pixel coordinates, is essential for developing practical GUI agents. However, we observe that existing grounding models exhibit significant coordinate prediction instability, minor visual perturbations (e.g. cropping a few pixels) can drastically alter predictions, flipping results between correct and incorrect. This instability severely undermines model performance, especially for samples with high-resolution and small UI elements. To address this issue, we propose Multi-View Prediction (MVP), a training-free framework that enhances grounding performance through multi-view inference. Our key insight is that while single-view predictions may be unstable, aggregating predictions from multiple carefully cropped views can effectively distinguish correct coordinates from outliers. MVP comprises two components: (1) Attention-Guided View Proposal, which derives diverse views guided by instruction-to-image attention scores, and (2) Multi-Coordinates Clustering, which ensembles predictions by selecting the centroid of the densest spatial cluster. Extensive experiments demonstrate MVP's effectiveness across various models and benchmarks. Notably, on ScreenSpot-Pro, MVP boosts UI-TARS-1.5-7B to 56.1%, GTA1-7B to 61.7%, Qwen3VL-8B-Instruct to 65.3%, and Qwen3VL-32B-Instruct to 74.0%. The code is available at https://github.com/ZJUSCL/MVP.

