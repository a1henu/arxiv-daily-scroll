---
layout: default
title: OMG-Bench: A New Challenging Benchmark for Skeleton-based Online Micro Hand Gesture Recognition
---

# OMG-Bench: A New Challenging Benchmark for Skeleton-based Online Micro Hand Gesture Recognition
**arXiv**：[2512.16727v1](https://arxiv.org/abs/2512.16727) · [PDF](https://arxiv.org/pdf/2512.16727.pdf)  
**作者**：Haochen Chang, Pengfei Ren, Buyuan Zhang, Da Li, Tianhao Han, Haoyang Zhang, Liang Xie, Hongbo Chen, Erwei Yin  

**一句话要点**：提出OMG-Bench基准与HMATr框架以解决骨架在线微手势识别难题

**关键词**：骨架手势识别, 在线微手势, 自监督数据生成, 分层记忆增强, Transformer框架, 基准数据集

## 3 点简述
- 核心问题：在线微手势识别缺乏大规模公开数据集，且手势动作细微、动态快速、连续执行，导致数据标注困难。
- 方法要点：开发多视图自监督流程自动生成骨架数据，结合启发式规则和专家精修进行半自动标注；提出HMATr框架，利用分层记忆库存储历史上下文，统一手势检测与分类。
- 实验或效果：HMATr在检测率上优于现有方法7.6%，为在线微手势识别建立了强基线。

## 摘要（原文）

> Online micro gesture recognition from hand skeletons is critical for VR/AR interaction but faces challenges due to limited public datasets and task-specific algorithms. Micro gestures involve subtle motion patterns, which make constructing datasets with precise skeletons and frame-level annotations difficult. To this end, we develop a multi-view self-supervised pipeline to automatically generate skeleton data, complemented by heuristic rules and expert refinement for semi-automatic annotation. Based on this pipeline, we introduce OMG-Bench, the first large-scale public benchmark for skeleton-based online micro gesture recognition. It features 40 fine-grained gesture classes with 13,948 instances across 1,272 sequences, characterized by subtle motions, rapid dynamics, and continuous execution. To tackle these challenges, we propose Hierarchical Memory-Augmented Transformer (HMATr), an end-to-end framework that unifies gesture detection and classification by leveraging hierarchical memory banks which store frame-level details and window-level semantics to preserve historical context. In addition, it employs learnable position-aware queries initialized from the memory to implicitly encode gesture positions and semantics. Experiments show that HMATr outperforms state-of-the-art methods by 7.6\% in detection rate, establishing a strong baseline for online micro gesture recognition. Project page: https://omg-bench.github.io/

