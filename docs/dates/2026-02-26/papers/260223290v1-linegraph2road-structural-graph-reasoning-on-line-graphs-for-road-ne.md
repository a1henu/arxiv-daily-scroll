---
layout: default
title: LineGraph2Road: Structural Graph Reasoning on Line Graphs for Road Network Extraction
---

# LineGraph2Road: Structural Graph Reasoning on Line Graphs for Road Network Extraction
**arXiv**：[2602.23290v1](https://arxiv.org/abs/2602.23290) · [PDF](https://arxiv.org/pdf/2602.23290.pdf)  
**作者**：Zhengyang Wei, Renzhi Jing, Yiyi He, Jenny Suckale  

**一句话要点**：提出LineGraph2Road框架，通过线图结构推理改进卫星图像道路网络提取的连通性预测。

**关键词**：道路网络提取, 图Transformer, 线图推理, 卫星图像分析, 连通性预测, 结构表示学习

## 3 点简述
- 核心问题：现有方法在道路提取中难以捕获长距离依赖和复杂拓扑结构，影响连通性预测准确性。
- 方法要点：将连通性预测建模为稀疏欧几里得图上的边二分类，并在线图上应用图Transformer以增强结构表示学习。
- 实验或效果：在City-scale、SpaceNet和Global-scale基准测试中，TOPO-F1和APLS指标达到先进水平，并引入立交桥/地下通道头和多级交叉解析策略。

## 摘要（原文）

> The accurate and automatic extraction of roads from satellite imagery is critical for applications in navigation and urban planning, significantly reducing the need for manual annotation. Many existing methods decompose this task into keypoint extraction and connectedness prediction, but often struggle to capture long-range dependencies and complex topologies. Here, we propose LineGraph2Road, a framework that improves connectedness prediction by formulating it as binary classification over edges in a constructed global but sparse Euclidean graph, where nodes are keypoints extracted from segmentation masks and edges connect node pairs within a predefined distance threshold, representing potential road segments. To better learn structural link representation, we transform the original graph into its corresponding line graph and apply a Graph Transformer on it for connectedness prediction. This formulation overcomes the limitations of endpoint-embedding fusion on set-isomorphic links, enabling rich link representations and effective relational reasoning over the global structure. Additionally, we introduce an overpass/underpass head to resolve multi-level crossings and a coupled NMS strategy to preserve critical connections. We evaluate LineGraph2Road on three benchmarks: City-scale, SpaceNet, and Global-scale, and show that it achieves state-of-the-art results on two key metrics, TOPO-F1 and APLS. It also captures fine visual details critical for real-world deployment. We will make our code publicly available.

