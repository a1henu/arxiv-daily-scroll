---
layout: default
title: FlashMesh: Faster and Better Autoregressive Mesh Synthesis via Structured Speculation
---

# FlashMesh: Faster and Better Autoregressive Mesh Synthesis via Structured Speculation
**arXiv**：[2511.15618v1](https://arxiv.org/abs/2511.15618) · [PDF](https://arxiv.org/pdf/2511.15618.pdf)  
**作者**：Tingrui Shen, Yiheng Zhang, Chen Tang, Chuan Ping, Zixing Zhao, Le Wan, Yuwang Wang, Ronggang Wang, Shengfeng He  

**一句话要点**：提出FlashMesh以加速和提升自回归3D网格合成

**关键词**：3D网格生成, 自回归模型, 推测解码, 小时玻璃变换器, 加速推理

## 3 点简述
- 自回归模型生成3D网格时逐令牌解码导致推理缓慢，限制交互和大规模应用
- 采用预测-纠正-验证范式，利用网格令牌的结构和几何相关性进行多令牌推测
- 实验显示FlashMesh实现最高2倍加速，同时提高生成保真度

## 摘要（原文）

> Autoregressive models can generate high-quality 3D meshes by sequentially producing vertices and faces, but their token-by-token decoding results in slow inference, limiting practical use in interactive and large-scale applications. We present FlashMesh, a fast and high-fidelity mesh generation framework that rethinks autoregressive decoding through a predict-correct-verify paradigm. The key insight is that mesh tokens exhibit strong structural and geometric correlations that enable confident multi-token speculation. FlashMesh leverages this by introducing a speculative decoding scheme tailored to the commonly used hourglass transformer architecture, enabling parallel prediction across face, point, and coordinate levels. Extensive experiments show that FlashMesh achieves up to a 2 x speedup over standard autoregressive models while also improving generation fidelity. Our results demonstrate that structural priors in mesh data can be systematically harnessed to accelerate and enhance autoregressive generation.

