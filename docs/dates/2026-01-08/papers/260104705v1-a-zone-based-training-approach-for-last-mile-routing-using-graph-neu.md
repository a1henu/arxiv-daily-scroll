---
layout: default
title: A zone-based training approach for last-mile routing using Graph Neural Networks and Pointer Networks
---

# A zone-based training approach for last-mile routing using Graph Neural Networks and Pointer Networks
**arXiv**：[2601.04705v1](https://arxiv.org/abs/2601.04705) · [PDF](https://arxiv.org/pdf/2601.04705.pdf)  
**作者**：Àngel Ruiz-Fas, Carlos Granell, José Francisco Ramos, Joaquín Huerta, Sergio Trilles  

**一句话要点**：提出基于地理分区的训练方法，使用图神经网络和指针网络优化最后一公里路由问题。

**关键词**：最后一公里路由, 图神经网络, 指针网络, 地理分区训练, 编码器-解码器架构, 旅行时间不对称

## 3 点简述
- 核心问题：最后一公里配送中，旅行时间高度不对称（如单行道、拥堵）导致传统启发式方法难以适应。
- 方法要点：采用编码器-解码器架构，图神经网络编码器生成节点嵌入，指针网络解码器顺序选择停靠点，并基于地理分区进行训练。
- 实验或效果：在亚马逊最后一公里路由挑战数据集上评估，分区训练相比通用训练减少了平均预测路径长度，且停靠点越多效果越显著。

## 摘要（原文）

> Rapid e-commerce growth has pushed last-mile delivery networks to their limits, where small routing gains translate into lower costs, faster service, and fewer emissions. Classical heuristics struggle to adapt when travel times are highly asymmetric (e.g., one-way streets, congestion). A deep learning-based approach to the last-mile routing problem is presented to generate geographical zones composed of stop sequences to minimize last-mile delivery times.
>   The presented approach is an encoder-decoder architecture. Each route is represented as a complete directed graph whose nodes are stops and whose edge weights are asymmetric travel times. A Graph Neural Network encoder produces node embeddings that captures the spatial relationships between stops. A Pointer Network decoder then takes the embeddings and the route's start node to sequentially select the next stops, assigning a probability to each unvisited node as the next destination.
>   Cells of a Discrete Global Grid System which contain route stops in the training data are obtained and clustered to generate geographical zones of similar size in which the process of training and inference are divided. Subsequently, a different instance of the model is trained per zone only considering the stops of the training routes which are included in that zone.
>   This approach is evaluated using the Los Angeles routes from the 2021 Amazon Last Mile Routing Challenge. Results from general and zone-based training are compared, showing a reduction in the average predicted route length in the zone-based training compared to the general training. The performance improvement of the zone-based approach becomes more pronounced as the number of stops per route increases.

