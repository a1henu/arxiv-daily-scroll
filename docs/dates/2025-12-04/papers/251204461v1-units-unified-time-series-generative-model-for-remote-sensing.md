---
layout: default
title: UniTS: Unified Time Series Generative Model for Remote Sensing
---

# UniTS: Unified Time Series Generative Model for Remote Sensing
**arXiv**：[2512.04461v1](https://arxiv.org/abs/2512.04461) · [PDF](https://arxiv.org/pdf/2512.04461.pdf)  
**作者**：Yuxiang Zhang, Shunlin Liang, Wenyuan Li, Han Ma, Jianglei Xu, Yichuan Ma, Jiangwei Xie, Wei Li, Mengmeng Zhang, Ran Tao, Xiang-Gen Xia  

**一句话要点**：提出UniTS统一时间序列生成模型，以解决遥感多任务中时空特征建模不统一的问题。

**关键词**：时间序列生成模型, 遥感图像处理, 流匹配, 扩散变换器, 多任务学习, 时空建模

## 3 点简述
- 核心问题：现有遥感方法需针对不同任务设计专门模型，缺乏多时间序列任务的统一时空建模。
- 方法要点：基于流匹配生成范式，通过扩散变换器与自适应条件注入器，实现从噪声到目标的确定性演化路径。
- 实验或效果：在TS-S12和TS-S12CR数据集上验证，UniTS在低层与高层任务中表现优异，尤其在云污染和模态缺失场景下超越现有方法。

## 摘要（原文）

> One of the primary objectives of satellite remote sensing is to capture the complex dynamics of the Earth environment, which encompasses tasks such as reconstructing continuous cloud-free time series images, detecting land cover changes, and forecasting future surface evolution. However, existing methods typically require specialized models tailored to different tasks, lacking unified modeling of spatiotemporal features across multiple time series tasks. In this paper, we propose a Unified Time Series Generative Model (UniTS), a general framework applicable to various time series tasks, including time series reconstruction, time series cloud removal, time series semantic change detection, and time series forecasting. Based on the flow matching generative paradigm, UniTS constructs a deterministic evolution path from noise to targets under the guidance of task-specific conditions, achieving unified modeling of spatiotemporal representations for multiple tasks. The UniTS architecture consists of a diffusion transformer with spatio-temporal blocks, where we design an Adaptive Condition Injector (ACor) to enhance the model's conditional perception of multimodal inputs, enabling high-quality controllable generation. Additionally, we design a Spatiotemporal-aware Modulator (STM) to improve the ability of spatio-temporal blocks to capture complex spatiotemporal dependencies. Furthermore, we construct two high-quality multimodal time series datasets, TS-S12 and TS-S12CR, filling the gap of benchmark datasets for time series cloud removal and forecasting tasks. Extensive experiments demonstrate that UniTS exhibits exceptional generative and cognitive capabilities in both low-level and high-level time series tasks. It significantly outperforms existing methods, particularly when facing challenges such as severe cloud contamination, modality absence, and forecasting phenological variations.

