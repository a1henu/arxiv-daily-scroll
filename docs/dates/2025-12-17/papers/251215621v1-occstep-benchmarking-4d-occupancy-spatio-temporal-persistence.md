---
layout: default
title: OccSTeP: Benchmarking 4D Occupancy Spatio-Temporal Persistence
---

# OccSTeP: Benchmarking 4D Occupancy Spatio-Temporal Persistence
**arXiv**：[2512.15621v1](https://arxiv.org/abs/2512.15621) · [PDF](https://arxiv.org/pdf/2512.15621.pdf)  
**作者**：Yu Zheng, Jie Hu, Kailun Yang, Jiaming Zhang  

**一句话要点**：提出OccSTeP基准与OccSTeP-WM模型，以解决自动驾驶中4D占用时空持续性预测问题。

**关键词**：4D占用预测, 自动驾驶场景理解, 时空持续性建模, 世界模型, 在线推理, 鲁棒性基准

## 3 点简述
- 核心问题：自动驾驶需在时间扰动下实现3D场景的持续性理解，包括反应式与主动式预测。
- 方法要点：OccSTeP-WM采用无分词器世界模型，基于稠密体素状态和线性复杂度注意力，融合时空上下文。
- 实验或效果：在OccSTeP基准上，语义mIoU提升6.56%，占用IoU提升9.26%，支持在线推理与鲁棒性能。

## 摘要（原文）

> Autonomous driving requires a persistent understanding of 3D scenes that is robust to temporal disturbances and accounts for potential future actions. We introduce a new concept of 4D Occupancy Spatio-Temporal Persistence (OccSTeP), which aims to address two tasks: (1) reactive forecasting: ''what will happen next'' and (2) proactive forecasting: "what would happen given a specific future action". For the first time, we create a new OccSTeP benchmark with challenging scenarios (e.g., erroneous semantic labels and dropped frames). To address this task, we propose OccSTeP-WM, a tokenizer-free world model that maintains a dense voxel-based scene state and incrementally fuses spatio-temporal context over time. OccSTeP-WM leverages a linear-complexity attention backbone and a recurrent state-space module to capture long-range spatial dependencies while continually updating the scene memory with ego-motion compensation. This design enables online inference and robust performance even when historical sensor input is missing or noisy. Extensive experiments prove the effectiveness of the OccSTeP concept and our OccSTeP-WM, yielding an average semantic mIoU of 23.70% (+6.56% gain) and occupancy IoU of 35.89% (+9.26% gain). The data and code will be open source at https://github.com/FaterYU/OccSTeP.

