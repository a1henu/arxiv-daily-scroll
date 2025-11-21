---
layout: default
title: UniDGF: A Unified Detection-to-Generation Framework for Hierarchical Object Visual Recognition
---

# UniDGF: A Unified Detection-to-Generation Framework for Hierarchical Object Visual Recognition
**arXiv**：[2511.15984v1](https://arxiv.org/abs/2511.15984) · [PDF](https://arxiv.org/pdf/2511.15984.pdf)  
**作者**：Xinyu Nan, Lingtao Mao, Huangyu Dai, Zexin Zheng, Xinyu Sun, Zihan Liang, Ben Chen, Yuqing Ding, Chenyi Lei, Wenwu Ou, Han Li  

**一句话要点**：提出检测引导生成框架以解决电商场景中细粒度对象识别问题

**关键词**：对象检测, 细粒度识别, 生成式框架, 属性识别, 层次分类, 电商视觉

## 3 点简述
- 核心问题：现有方法依赖全局相似性，难以捕捉细粒度类别和属性多样性
- 方法要点：基于检测提取ROI特征，使用BART生成器预测层次类别和属性序列
- 实验或效果：在电商和开源数据集上优于相似性方法和多阶段系统

## 摘要（原文）

> Achieving visual semantic understanding requires a unified framework that simultaneously handles object detection, category prediction, and attribute recognition. However, current advanced approaches rely on global similarity and struggle to capture fine-grained category distinctions and category-specific attribute diversity, especially in large-scale e-commerce scenarios. To overcome these challenges, we introduce a detection-guided generative framework that predicts hierarchical category and attribute tokens. For each detected object, we extract refined ROI-level features and employ a BART-based generator to produce semantic tokens in a coarse-to-fine sequence covering category hierarchies and property-value pairs, with support for property-conditioned attribute recognition. Experiments on both large-scale proprietary e-commerce datasets and open-source datasets demonstrate that our approach significantly outperforms existing similarity-based pipelines and multi-stage classification systems, achieving stronger fine-grained recognition and more coherent unified inference.

