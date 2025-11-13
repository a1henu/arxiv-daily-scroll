---
layout: default
title: RF-DETR: Neural Architecture Search for Real-Time Detection Transformers
---

# RF-DETR: Neural Architecture Search for Real-Time Detection Transformers
**arXiv**：[2511.09554v1](https://arxiv.org/abs/2511.09554) · [PDF](https://arxiv.org/pdf/2511.09554.pdf)  
**作者**：Isaac Robinson, Peter Robicheaux, Matvei Popov, Deva Ramanan, Neehar Peri  

**一句话要点**：提出RF-DETR，通过神经架构搜索实现实时检测变换器，优化目标数据集上的精度-延迟权衡。

**关键词**：实时目标检测, 神经架构搜索, 检测变换器, 精度-延迟权衡, 开放词汇检测

## 3 点简述
- 核心问题：开放词汇检测器在分布外类别的真实数据集上泛化能力不足。
- 方法要点：使用权重共享神经架构搜索，无需重训练即可评估数千种网络配置。
- 实验或效果：在COCO和Roboflow100-VL上显著超越现有实时方法，实现高精度和低延迟。

## 摘要（原文）

> Open-vocabulary detectors achieve impressive performance on COCO, but often fail to generalize to real-world datasets with out-of-distribution classes not typically found in their pre-training. Rather than simply fine-tuning a heavy-weight vision-language model (VLM) for new domains, we introduce RF-DETR, a light-weight specialist detection transformer that discovers accuracy-latency Pareto curves for any target dataset with weight-sharing neural architecture search (NAS). Our approach fine-tunes a pre-trained base network on a target dataset and evaluates thousands of network configurations with different accuracy-latency tradeoffs without re-training. Further, we revisit the "tunable knobs" for NAS to improve the transferability of DETRs to diverse target domains. Notably, RF-DETR significantly improves on prior state-of-the-art real-time methods on COCO and Roboflow100-VL. RF-DETR (nano) achieves 48.0 AP on COCO, beating D-FINE (nano) by 5.3 AP at similar latency, and RF-DETR (2x-large) outperforms GroundingDINO (tiny) by 1.2 AP on Roboflow100-VL while running 20x as fast. To the best of our knowledge, RF-DETR (2x-large) is the first real-time detector to surpass 60 AP on COCO. Our code is at https://github.com/roboflow/rf-detr

