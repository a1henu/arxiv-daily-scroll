---
layout: default
title: YOLO-NAS-Bench: A Surrogate Benchmark with Self-Evolving Predictors for YOLO Architecture Search
---

# YOLO-NAS-Bench: A Surrogate Benchmark with Self-Evolving Predictors for YOLO Architecture Search
**arXiv**：[2603.09405v1](https://arxiv.org/abs/2603.09405) · [PDF](https://arxiv.org/pdf/2603.09405.pdf)  
**作者**：Zhe Li, Xiaoyu Ding, Jiaxin Zheng, Yongtao Wang  

**一句话要点**：提出YOLO-NAS-Bench基准与自进化预测器，以解决YOLO架构搜索的高评估成本问题。

**关键词**：神经架构搜索, 目标检测, YOLO基准, 代理预测器, 自进化机制, COCO数据集

## 3 点简述
- 目标检测的神经架构搜索因COCO训练成本高而受限，缺乏专用基准。
- 构建YOLO风格检测器的搜索空间，通过采样和LightGBM预测器建立代理基准。
- 引入自进化机制提升预测器性能，实验显示预测准确性和排名一致性显著提高。

## 摘要（原文）

> Neural Architecture Search (NAS) for object detection is severely bottlenecked by high evaluation cost, as fully training each candidate YOLO architecture on COCO demands days of GPU time. Meanwhile, existing NAS benchmarks largely target image classification, leaving the detection community without a comparable benchmark for NAS evaluation. To address this gap, we introduce YOLO-NAS-Bench, the first surrogate benchmark tailored to YOLO-style detectors. YOLO-NAS-Bench defines a search space spanning channel width, block depth, and operator type across both backbone and neck, covering the core modules of YOLOv8 through YOLO12. We sample 1,000 architectures via random, stratified, and Latin Hypercube strategies, train them on COCO-mini, and build a LightGBM surrogate predictor. To sharpen the predictor in the high-performance regime most relevant to NAS, we propose a Self-Evolving Mechanism that progressively aligns the predictor's training distribution with the high-performance frontier, by using the predictor itself to discover and evaluate informative architectures in each iteration. This method grows the pool to 1,500 architectures and raises the ensemble predictor's R2 from 0.770 to 0.815 and Sparse Kendall Tau from 0.694 to 0.752, demonstrating strong predictive accuracy and ranking consistency. Using the final predictor as the fitness function for evolutionary search, we discover architectures that surpass all official YOLOv8-YOLO12 baselines at comparable latency on COCO-mini, confirming the predictor's discriminative power for top-performing detection architectures.

