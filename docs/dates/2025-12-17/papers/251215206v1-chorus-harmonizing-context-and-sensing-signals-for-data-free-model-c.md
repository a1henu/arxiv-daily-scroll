---
layout: default
title: Chorus: Harmonizing Context and Sensing Signals for Data-Free Model Customization in IoT
---

# Chorus: Harmonizing Context and Sensing Signals for Data-Free Model Customization in IoT
**arXiv**：[2512.15206v1](https://arxiv.org/abs/2512.15206) · [PDF](https://arxiv.org/pdf/2512.15206.pdf)  
**作者**：Liyu Zhang, Yejia Liu, Kwun Ho Liu, Runxi Huang, Xiaomin Ouyang  

**一句话要点**：提出Chorus方法，通过上下文感知和数据自由定制解决物联网中动态上下文变化下的模型适应问题

**关键词**：物联网模型定制, 上下文感知学习, 数据自由适应, 跨模态重建, 轻量门控头, 上下文缓存

## 3 点简述
- 核心问题：物联网传感器数据受动态上下文（如传感器放置、环境）影响，传统方法忽略或简单整合上下文，难以处理部署后的未见上下文变化
- 方法要点：通过无监督跨模态重建学习鲁棒上下文表示，并训练轻量门控头动态平衡传感器与上下文贡献，采用上下文缓存降低推理延迟
- 实验或效果：在IMU、语音和WiFi传感任务中，Chorus在未见上下文下性能提升达11.3%，并在智能手机和边缘设备上保持低延迟

## 摘要（原文）

> In real-world IoT applications, sensor data is usually collected under diverse and dynamic contextual conditions where factors such as sensor placements or ambient environments can significantly affect data patterns and downstream performance. Traditional domain adaptation or generalization methods often ignore such context information or use simplistic integration strategies, making them ineffective in handling unseen context shifts after deployment. In this paper, we propose Chorus, a context-aware, data-free model customization approach that adapts models to unseen deployment conditions without requiring target-domain data. The key idea is to learn effective context representations that capture their influence on sensor data patterns and to adaptively integrate them based on the degree of context shift. Specifically, Chorus first performs unsupervised cross-modal reconstruction between unlabeled sensor data and language-based context embeddings, while regularizing the context embedding space to learn robust, generalizable context representations. Then, it trains a lightweight gated head on limited labeled samples to dynamically balance sensor and context contributions-favoring context when sensor evidence is ambiguous and vice versa. To further reduce inference latency, Chorus employs a context-caching mechanism that reuses cached context representations and updates only upon detected context shifts. Experiments on IMU, speech, and WiFi sensing tasks under diverse context shifts show that Chorus outperforms state-of-the-art baselines by up to 11.3% in unseen contexts, while maintaining comparable latency on smartphone and edge devices.

