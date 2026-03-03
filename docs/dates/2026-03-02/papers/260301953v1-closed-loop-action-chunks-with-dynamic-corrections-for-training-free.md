---
layout: default
title: Closed-Loop Action Chunks with Dynamic Corrections for Training-Free Diffusion Policy
---

# Closed-Loop Action Chunks with Dynamic Corrections for Training-Free Diffusion Policy
**arXiv**：[2603.01953v1](https://arxiv.org/abs/2603.01953) · [PDF](https://arxiv.org/pdf/2603.01953.pdf)  
**作者**：Pengyuan Wu, Pingrui Zhang, Zhigang Wang, Dong Wang, Bin Zhao, Xuelong Li  

**一句话要点**：提出DCDP框架，通过动态闭环动作块与实时校正，提升扩散策略在动态场景中的适应性。

**关键词**：扩散策略, 动态场景适应, 闭环控制, 动作校正, 机器人操作, 实时响应

## 3 点简述
- 扩散策略在动态场景中响应延迟或失败，适应能力不足。
- DCDP集成自监督动态特征编码器、交叉注意力融合和非对称编码解码器，实现实时闭环校正。
- 在动态PushT仿真中，适应性提升19%，额外计算仅需5%，模块化设计支持即插即用。

## 摘要（原文）

> Diffusion-based policies have achieved remarkable results in robotic manipulation but often struggle to adapt rapidly in dynamic scenarios, leading to delayed responses or task failures. We present DCDP, a Dynamic Closed-Loop Diffusion Policy framework that integrates chunk-based action generation with real-time correction. DCDP integrates a self-supervised dynamic feature encoder, cross-attention fusion, and an asymmetric action encoder-decoder to inject environmental dynamics before action execution, achieving real-time closed-loop action correction and enhancing the system's adaptability in dynamic scenarios. In dynamic PushT simulations, DCDP improves adaptability by 19\% without retraining while requiring only 5\% additional computation. Its modular design enables plug-and-play integration, achieving both temporal coherence and real-time responsiveness in dynamic robotic scenarios, including real-world manipulation tasks. The project page is at: https://github.com/wupengyuan/dcdp

