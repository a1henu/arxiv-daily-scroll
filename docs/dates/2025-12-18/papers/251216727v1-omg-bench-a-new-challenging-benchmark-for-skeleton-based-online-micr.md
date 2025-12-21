---
layout: default
title: OMG-Bench: A New Challenging Benchmark for Skeleton-based Online Micro Hand Gesture Recognition
---

# OMG-Bench: A New Challenging Benchmark for Skeleton-based Online Micro Hand Gesture Recognition
**arXiv**：[2512.16727v1](https://arxiv.org/abs/2512.16727) · [PDF](https://arxiv.org/pdf/2512.16727.pdf)  
**作者**：Haochen Chang, Pengfei Ren, Buyuan Zhang, Da Li, Tianhao Han, Haoyang Zhang, Liang Xie, Hongbo Chen, Erwei Yin  

**一句话要点**：提出OMG-Bench基准与HMATr框架以解决骨架在线微手势识别难题

**关键词**：骨架手势识别, 在线微手势, 自监督数据生成, 分层记忆网络, Transformer框架, 基准数据集

## 3 点简述
- 在线微手势识别因数据集稀缺和动作细微而具挑战性
- 通过多视角自监督流程生成骨架数据并半自动标注构建OMG-Bench
- HMATr利用分层记忆库统一检测与分类，检测率提升7.6%

## 摘要（原文）

> Online micro gesture recognition from hand skeletons is critical for VR/AR interaction but faces challenges due to limited public datasets and task-specific algorithms. Micro gestures involve subtle motion patterns, which make constructing datasets with precise skeletons and frame-level annotations difficult. To this end, we develop a multi-view self-supervised pipeline to automatically generate skeleton data, complemented by heuristic rules and expert refinement for semi-automatic annotation. Based on this pipeline, we introduce OMG-Bench, the first large-scale public benchmark for skeleton-based online micro gesture recognition. It features 40 fine-grained gesture classes with 13,948 instances across 1,272 sequences, characterized by subtle motions, rapid dynamics, and continuous execution. To tackle these challenges, we propose Hierarchical Memory-Augmented Transformer (HMATr), an end-to-end framework that unifies gesture detection and classification by leveraging hierarchical memory banks which store frame-level details and window-level semantics to preserve historical context. In addition, it employs learnable position-aware queries initialized from the memory to implicitly encode gesture positions and semantics. Experiments show that HMATr outperforms state-of-the-art methods by 7.6\% in detection rate, establishing a strong baseline for online micro gesture recognition. Project page: https://omg-bench.github.io/

