---
layout: default
title: Parameter Aware Mamba Model for Multi-task Dense Prediction
---

# Parameter Aware Mamba Model for Multi-task Dense Prediction
**arXiv**：[2511.14503v1](https://arxiv.org/abs/2511.14503) · [PDF](https://arxiv.org/pdf/2511.14503.pdf)  
**作者**：Xinzhuo Yu, Yunzhi Zhuge, Sitong Gong, Lu Zhang, Pingping Zhang, Huchuan Lu  

**一句话要点**：提出参数感知Mamba模型以增强多任务密集预测中的任务交互

**关键词**：多任务学习, 密集预测, 状态空间模型, 任务交互, 参数专家, 序列建模

## 3 点简述
- 核心问题：多任务密集预测中任务间交互建模不足，现有方法依赖卷积和注意力机制
- 方法要点：利用状态空间模型参数专家集成任务先验，通过S4模型全局整合任务关系
- 实验或效果：在NYUD-v2和PASCAL-Context基准测试中验证有效性，代码已开源

## 摘要（原文）

> Understanding the inter-relations and interactions between tasks is crucial for multi-task dense prediction. Existing methods predominantly utilize convolutional layers and attention mechanisms to explore task-level interactions. In this work, we introduce a novel decoder-based framework, Parameter Aware Mamba Model (PAMM), specifically designed for dense prediction in multi-task learning setting. Distinct from approaches that employ Transformers to model holistic task relationships, PAMM leverages the rich, scalable parameters of state space models to enhance task interconnectivity. It features dual state space parameter experts that integrate and set task-specific parameter priors, capturing the intrinsic properties of each task. This approach not only facilitates precise multi-task interactions but also allows for the global integration of task priors through the structured state space sequence model (S4). Furthermore, we employ the Multi-Directional Hilbert Scanning method to construct multi-angle feature sequences, thereby enhancing the sequence model's perceptual capabilities for 2D data. Extensive experiments on the NYUD-v2 and PASCAL-Context benchmarks demonstrate the effectiveness of our proposed method. Our code is available at https://github.com/CQC-gogopro/PAMM.

