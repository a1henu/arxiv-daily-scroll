---
layout: default
title: OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving
---

# OmniGen: Unified Multimodal Sensor Generation for Autonomous Driving
**arXiv**：[2512.14225v1](https://arxiv.org/abs/2512.14225) · [PDF](https://arxiv.org/pdf/2512.14225.pdf)  
**作者**：Tao Tang, Enhui Ma, xia zhou, Letian Wang, Tianyi Yan, Xueyang Zhang, Kun Zhan, Peng Jia, XianPeng Lang, Jia-Wang Bian, Kaicheng Yu, Xiaodan Liang  

**一句话要点**：提出OmniGen以解决自动驾驶中多模态传感器数据生成的对齐与效率问题

**关键词**：多模态传感器生成, 自动驾驶数据合成, 体渲染解码, 扩散变换器, BEV空间统一

## 3 点简述
- 核心问题：现有生成方法多聚焦单模态，导致多模态数据效率低且不对齐
- 方法要点：利用共享BEV空间统一特征，设计UAE方法通过体渲染联合解码LiDAR与多视角相机数据
- 实验或效果：实验显示OmniGen在多模态一致性和可控生成方面表现良好

## 摘要（原文）

> Autonomous driving has seen remarkable advancements, largely driven by extensive real-world data collection. However, acquiring diverse and corner-case data remains costly and inefficient. Generative models have emerged as a promising solution by synthesizing realistic sensor data. However, existing approaches primarily focus on single-modality generation, leading to inefficiencies and misalignment in multimodal sensor data. To address these challenges, we propose OminiGen, which generates aligned multimodal sensor data in a unified framework. Our approach leverages a shared Bird\u2019s Eye View (BEV) space to unify multimodal features and designs a novel generalizable multimodal reconstruction method, UAE, to jointly decode LiDAR and multi-view camera data. UAE achieves multimodal sensor decoding through volume rendering, enabling accurate and flexible reconstruction. Furthermore, we incorporate a Diffusion Transformer (DiT) with a ControlNet branch to enable controllable multimodal sensor generation. Our comprehensive experiments demonstrate that OminiGen achieves desired performances in unified multimodal sensor data generation with multimodal consistency and flexible sensor adjustments.

