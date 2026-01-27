---
layout: default
title: Forward Consistency Learning with Gated Context Aggregation for Video Anomaly Detection
---

# Forward Consistency Learning with Gated Context Aggregation for Video Anomaly Detection
**arXiv**：[2601.18135v1](https://arxiv.org/abs/2601.18135) · [PDF](https://arxiv.org/pdf/2601.18135.pdf)  
**作者**：Jiahao Lyu, Minghua Zhao, Xuewen Huang, Yifei Chen, Shuangli Du, Jing Hu, Cheng Shi, Zhiyong Lv  

**一句话要点**：提出FoGA模型，通过前向一致性学习和门控上下文聚合，实现轻量级视频异常检测。

**关键词**：视频异常检测, 轻量级模型, 前向一致性学习, 门控上下文聚合, 边缘计算

## 3 点简述
- 核心问题：现有视频异常检测方法依赖大模型，忽视长期时序信息，难以部署于资源受限设备。
- 方法要点：基于Unet提取连续帧特征，生成即时和前向预测，引入门控上下文聚合模块动态融合特征。
- 实验或效果：模型参数约2M，运行速度达155 FPS，性能优于现有方法，平衡效率与准确性。

## 摘要（原文）

> As a crucial element of public security, video anomaly detection (VAD) aims to measure deviations from normal patterns for various events in real-time surveillance systems. However, most existing VAD methods rely on large-scale models to pursue extreme accuracy, limiting their feasibility on resource-limited edge devices. Moreover, mainstream prediction-based VAD detects anomalies using only single-frame future prediction errors, overlooking the richer constraints from longer-term temporal forward information. In this paper, we introduce FoGA, a lightweight VAD model that performs Forward consistency learning with Gated context Aggregation, containing about 2M parameters and tailored for potential edge devices. Specifically, we propose a Unet-based method that performs feature extraction on consecutive frames to generate both immediate and forward predictions. Then, we introduce a gated context aggregation module into the skip connections to dynamically fuse encoder and decoder features at the same spatial scale. Finally, the model is jointly optimized with a novel forward consistency loss, and a hybrid anomaly measurement strategy is adopted to integrate errors from both immediate and forward frames for more accurate detection. Extensive experiments demonstrate the effectiveness of the proposed method, which substantially outperforms state-of-the-art competing methods, running up to 155 FPS. Hence, our FoGA achieves an excellent trade-off between performance and the efficiency metric.

