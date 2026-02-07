---
layout: default
title: Characterizing Human Semantic Navigation in Concept Production as Trajectories in Embedding Space
---

# Characterizing Human Semantic Navigation in Concept Production as Trajectories in Embedding Space
**arXiv**：[2602.05971v1](https://arxiv.org/abs/2602.05971) · [PDF](https://arxiv.org/pdf/2602.05971.pdf)  
**作者**：Felipe D. Toro-Hernández, Jesuino Vieira Filho, Rodrigo M. Cabral-Carvalho  

**一句话要点**：提出基于嵌入空间轨迹的框架，以量化人类语义导航在概念生成中的动态特征

**关键词**：语义导航, 嵌入空间轨迹, 概念生成, 几何度量, 跨语言分析, 临床评估

## 3 点简述
- 核心问题：人类如何在语义空间中导航以生成概念，涉及几何与动态特性
- 方法要点：使用累积嵌入构建语义轨迹，提取距离、熵、速度等几何与动力学指标
- 实验或效果：在跨语言数据集中区分临床组与概念类型，减少人工预处理需求

## 摘要（原文）

> Semantic representations can be framed as a structured, dynamic knowledge space through which humans navigate to retrieve and manipulate meaning. To investigate how humans traverse this geometry, we introduce a framework that represents concept production as navigation through embedding space. Using different transformer text embedding models, we construct participant-specific semantic trajectories based on cumulative embeddings and extract geometric and dynamical metrics, including distance to next, distance to centroid, entropy, velocity, and acceleration. These measures capture both scalar and directional aspects of semantic navigation, providing a computationally grounded view of semantic representation search as movement in a geometric space. We evaluate the framework on four datasets across different languages, spanning different property generation tasks: Neurodegenerative, Swear verbal fluency, Property listing task in Italian, and in German. Across these contexts, our approach distinguishes between clinical groups and concept types, offering a mathematical framework that requires minimal human intervention compared to typical labor-intensive linguistic pre-processing methods. Comparison with a non-cumulative approach reveals that cumulative embeddings work best for longer trajectories, whereas shorter ones may provide too little context, favoring the non-cumulative alternative. Critically, different embedding models yielded similar results, highlighting similarities between different learned representations despite different training pipelines. By framing semantic navigation as a structured trajectory through embedding space, bridging cognitive modeling with learned representation, thereby establishing a pipeline for quantifying semantic representation dynamics with applications in clinical research, cross-linguistic analysis, and the assessment of artificial cognition.

