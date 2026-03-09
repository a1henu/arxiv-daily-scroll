---
layout: default
title: REACT++: Efficient Cross-Attention for Real-Time Scene Graph Generation
---

# REACT++: Efficient Cross-Attention for Real-Time Scene Graph Generation
**arXiv**：[2603.06386v1](https://arxiv.org/abs/2603.06386) · [PDF](https://arxiv.org/pdf/2603.06386.pdf)  
**作者**：Maëlic Neau, Zoe Falomir  

**一句话要点**：提出REACT++模型，通过高效特征提取和原型空间交叉注意力，平衡实时场景图生成的性能与速度。

**关键词**：场景图生成, 实时推理, 交叉注意力, 原型空间, 高效特征提取

## 3 点简述
- 核心问题：现有方法难以同时优化关系预测精度、物体检测精度和推理速度。
- 方法要点：基于REACT架构，引入原型空间中的主体到客体交叉注意力机制。
- 实验或效果：相比REACT，推理速度提升20%，关系预测精度平均提高10%。

## 摘要（原文）

> Scene Graph Generation (SGG) is a task that encodes visual relationships between objects in images as graph structures. SGG shows significant promise as a foundational component for downstream tasks, such as reasoning for embodied agents. To enable real-time applications, SGG must address the trade-off between performance and inference speed. However, current methods tend to focus on one of the following: (1) improving relation prediction accuracy, (2) enhancing object detection accuracy, or (3) reducing latency, without aiming to balance all three objectives simultaneously. To address this limitation, we build on the powerful Real-time Efficiency and Accuracy Compromise for Tradeoffs in Scene Graph Generation (REACT) architecture and propose REACT++, a new state-of-the-art model for real-time SGG. By leveraging efficient feature extraction and subject-to-object cross-attention within the prototype space, REACT++ balances latency and representational power. REACT++ achieves the highest inference speed among existing SGG models, improving relation prediction accuracy without sacrificing object detection performance. Compared to the previous REACT version, REACT++ is 20% faster with a gain of 10% in relation prediction accuracy on average. The code is available at https://github.com/Maelic/SGG-Benchmark.

