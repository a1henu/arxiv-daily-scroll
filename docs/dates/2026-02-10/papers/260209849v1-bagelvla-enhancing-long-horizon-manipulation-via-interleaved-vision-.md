---
layout: default
title: BagelVLA: Enhancing Long-Horizon Manipulation via Interleaved Vision-Language-Action Generation
---

# BagelVLA: Enhancing Long-Horizon Manipulation via Interleaved Vision-Language-Action Generation
**arXiv**：[2602.09849v1](https://arxiv.org/abs/2602.09849) · [PDF](https://arxiv.org/pdf/2602.09849.pdf)  
**作者**：Yucheng Hu, Jianke Zhang, Yuanfei Luo, Yanjiang Guo, Xiaoyu Chen, Xinshu Sun, Kun Feng, Qingzhou Lu, Sheng Chen, Yangang Zhang, Wei Li, Jianyu Chen  

**一句话要点**：提出BagelVLA模型，通过交错视觉-语言-动作生成增强长时程操作能力

**关键词**：视觉-语言-动作模型, 长时程操作, 多模态集成, 残差流引导, 动作生成

## 3 点简述
- 现有VLA模型在复杂长时程操作中，语言规划与视觉预测常孤立处理，导致性能受限
- BagelVLA统一集成语言规划、视觉预测和动作生成，并引入残差流引导以低延迟耦合模态
- 实验表明，BagelVLA在模拟和真实基准上显著优于基线，尤其在多阶段推理任务中

## 摘要（原文）

> Equipping embodied agents with the ability to reason about tasks, foresee physical outcomes, and generate precise actions is essential for general-purpose manipulation. While recent Vision-Language-Action (VLA) models have leveraged pre-trained foundation models, they typically focus on either linguistic planning or visual forecasting in isolation. These methods rarely integrate both capabilities simultaneously to guide action generation, leading to suboptimal performance in complex, long-horizon manipulation tasks. To bridge this gap, we propose BagelVLA, a unified model that integrates linguistic planning, visual forecasting, and action generation within a single framework. Initialized from a pretrained unified understanding and generative model, BagelVLA is trained to interleave textual reasoning and visual prediction directly into the action execution loop. To efficiently couple these modalities, we introduce Residual Flow Guidance (RFG), which initializes from current observation and leverages single-step denoising to extract predictive visual features, guiding action generation with minimal latency. Extensive experiments demonstrate that BagelVLA outperforms existing baselines by a significant margin on multiple simulated and real-world benchmarks, particularly in tasks requiring multi-stage reasoning.

