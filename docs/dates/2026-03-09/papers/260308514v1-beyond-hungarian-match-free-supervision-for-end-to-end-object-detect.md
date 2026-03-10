---
layout: default
title: Beyond Hungarian: Match-Free Supervision for End-to-End Object Detection
---

# Beyond Hungarian: Match-Free Supervision for End-to-End Object Detection
**arXiv**：[2603.08514v1](https://arxiv.org/abs/2603.08514) · [PDF](https://arxiv.org/pdf/2603.08514.pdf)  
**作者**：Shoumeng Qiu, Xinrun Li, Yang Long  

**一句话要点**：提出基于交叉注意力的查询选择模块，以消除DETR检测器中匈牙利匹配的计算开销。

**关键词**：端到端目标检测, DETR检测器, 匹配自由训练, 交叉注意力, 查询选择, 可微分学习

## 3 点简述
- 核心问题：DETR检测器依赖匈牙利算法进行查询与真值匹配，导致计算开销大且训练动态复杂。
- 方法要点：通过交叉注意力机制，利用编码的真值信息探测解码器查询，实现可微分的隐式对应学习。
- 实验或效果：训练效率显著提升，匹配延迟减少超50%，性能优于现有先进方法。

## 摘要（原文）

> Recent DEtection TRansformer (DETR) based frameworks have achieved remarkable success in end-to-end object detection. However, the reliance on the Hungarian algorithm for bipartite matching between queries and ground truths introduces computational overhead and complicates the training dynamics. In this paper, we propose a novel matching-free training scheme for DETR-based detectors that eliminates the need for explicit heuristic matching. At the core of our approach is a dedicated Cross-Attention-based Query Selection (CAQS) module. Instead of discrete assignment, we utilize encoded ground-truth information to probe the decoder queries through a cross-attention mechanism. By minimizing the weighted error between the queried results and the ground truths, the model autonomously learns the implicit correspondences between object queries and specific targets. This learned relationship further provides supervision signals for the learning of queries. Experimental results demonstrate that our proposed method bypasses the traditional matching process, significantly enhancing training efficiency, reducing the matching latency by over 50\%, effectively eliminating the discrete matching bottleneck through differentiable correspondence learning, and also achieving superior performance compared to existing state-of-the-art methods.

