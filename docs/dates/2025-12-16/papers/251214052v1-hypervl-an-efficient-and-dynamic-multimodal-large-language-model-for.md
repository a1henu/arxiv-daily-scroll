---
layout: default
title: HyperVL: An Efficient and Dynamic Multimodal Large Language Model for Edge Devices
---

# HyperVL: An Efficient and Dynamic Multimodal Large Language Model for Edge Devices
**arXiv**：[2512.14052v1](https://arxiv.org/abs/2512.14052) · [PDF](https://arxiv.org/pdf/2512.14052.pdf)  
**作者**：HyperAI Team, Yuchen Liu, Kaiyang Han, Zhiqiang Xia, Yuhang Dong, Chen Song, Kangyu Tang, Jiaming Xu, Xiushi Feng, WenXuan Yu, Li Peng, Mingyang Wang, Kai Wang, Changpeng Yang, Yang Li, Haoyu Lu, Hao Wang, Bingna Xu, Guangyao Liu, Long Huang, Kaibin Guo, Jinyang Wu, Dan Wu, Hongzhen Wang, Peng Zhou, Shuai Nie, Shande Wang, Runyu Shi, Ying Huang  

**一句话要点**：提出HyperVL以解决边缘设备上多模态大模型部署的效率和内存瓶颈问题。

**关键词**：边缘设备部署, 视觉分辨率压缩, 双一致性学习, 多模态大语言模型, 图像分块策略

## 3 点简述
- 核心问题：标准ViT编码器处理高分辨率输入时延迟和内存消耗过高，阻碍多模态大模型在设备端部署。
- 方法要点：采用图像分块策略限制峰值内存，引入视觉分辨率压缩器和双一致性学习以动态优化编码和切换视觉分支。
- 实验或效果：在多个基准测试中达到同类模型最优性能，并在真实移动设备上显著降低延迟和功耗。

## 摘要（原文）

> Current multimodal large lanauge models possess strong perceptual and reasoning capabilities, however high computational and memory requirements make them difficult to deploy directly on on-device environments. While small-parameter models are progressively endowed with strong general capabilities, standard Vision Transformer (ViT) encoders remain a critical bottleneck, suffering from excessive latency and memory consumption when processing high-resolution inputs.To address these challenges, we introduce HyperVL, an efficient multimodal large language model tailored for on-device inference. HyperVL adopts an image-tiling strategy to cap peak memory usage and incorporates two novel techniques: (1) a Visual Resolution Compressor (VRC) that adaptively predicts optimal encoding resolutions to eliminate redundant computation, and (2) Dual Consistency Learning (DCL), which aligns multi-scale ViT encoders within a unified framework, enabling dynamic switching between visual branches under a shared LLM. Extensive experiments demonstrate that HyperVL achieves state-of-the-art performance among models of comparable size across multiple benchmarks. Furthermore, it significantly significantly reduces latency and power consumption on real mobile devices, demonstrating its practicality for on-device multimodal inference.

