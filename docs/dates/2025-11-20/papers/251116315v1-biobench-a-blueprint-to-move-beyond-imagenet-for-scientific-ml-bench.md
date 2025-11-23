---
layout: default
title: BioBench: A Blueprint to Move Beyond ImageNet for Scientific ML Benchmarks
---

# BioBench: A Blueprint to Move Beyond ImageNet for Scientific ML Benchmarks
**arXiv**：[2511.16315v1](https://arxiv.org/abs/2511.16315) · [PDF](https://arxiv.org/pdf/2511.16315.pdf)  
**作者**：Samuel Stevens  

**一句话要点**：提出BioBench基准以解决ImageNet在科学图像评估中的不足

**关键词**：生态视觉基准, 图像分类评估, 科学机器学习, 多模态数据集, 模型转移性能

## 3 点简述
- ImageNet-1K线性探针准确率在科学图像任务中预测性能差，方差解释仅34%
- BioBench整合9个生态任务、4个分类界和6种采集模态，提供统一评估API
- 在A6000 GPU上6小时完成ViT-L模型评估，提供类平衡宏F1等指标

## 摘要（原文）

> ImageNet-1K linear-probe transfer accuracy remains the default proxy for visual representation quality, yet it no longer predicts performance on scientific imagery. Across 46 modern vision model checkpoints, ImageNet top-1 accuracy explains only 34% of variance on ecology tasks and mis-ranks 30% of models above 75% accuracy. We present BioBench, an open ecology vision benchmark that captures what ImageNet misses. BioBench unifies 9 publicly released, application-driven tasks, 4 taxonomic kingdoms, and 6 acquisition modalities (drone RGB, web video, micrographs, in-situ and specimen photos, camera-trap frames), totaling 3.1M images. A single Python API downloads data, fits lightweight classifiers to frozen backbones, and reports class-balanced macro-F1 (plus domain metrics for FishNet and FungiCLEF); ViT-L models evaluate in 6 hours on an A6000 GPU. BioBench provides new signal for computer vision in ecology and a template recipe for building reliable AI-for-science benchmarks in any domain. Code and predictions are available at https://github.com/samuelstevens/biobench and results at https://samuelstevens.me/biobench.

