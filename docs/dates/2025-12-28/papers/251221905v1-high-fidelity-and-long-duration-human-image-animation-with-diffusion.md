---
layout: default
title: High-Fidelity and Long-Duration Human Image Animation with Diffusion Transformer
---

# High-Fidelity and Long-Duration Human Image Animation with Diffusion Transformer
**arXiv**：[2512.21905v1](https://arxiv.org/abs/2512.21905) · [PDF](https://arxiv.org/pdf/2512.21905.pdf)  
**作者**：Shen Zheng, Jiaran Cai, Yuansheng Guan, Shenneng Huang, Xingpei Ma, Junjie Cao, Hanfeng Zhao, Qiang Zhang, Shunsi Zhang, Xiao-Ping Zhang  

**一句话要点**：提出基于扩散变换器的框架以解决长时高保真人像动画生成问题

**关键词**：人像动画, 扩散变换器, 长视频生成, 高保真细节, 骨架对齐, 数据增强

## 3 点简述
- 核心问题：现有方法难以生成长时视频，且面部和手部细节合成不足。
- 方法要点：设计混合隐式引导信号和锐度引导因子，引入位置偏移自适应模块支持任意长度视频生成。
- 实验或效果：通过数据增强和骨架对齐减少身份形状变化影响，实验显示优于现有方法。

## 摘要（原文）

> Recent progress in diffusion models has significantly advanced the field of human image animation. While existing methods can generate temporally consistent results for short or regular motions, significant challenges remain, particularly in generating long-duration videos. Furthermore, the synthesis of fine-grained facial and hand details remains under-explored, limiting the applicability of current approaches in real-world, high-quality applications. To address these limitations, we propose a diffusion transformer (DiT)-based framework which focuses on generating high-fidelity and long-duration human animation videos. First, we design a set of hybrid implicit guidance signals and a sharpness guidance factor, enabling our framework to additionally incorporate detailed facial and hand features as guidance. Next, we incorporate the time-aware position shift fusion module, modify the input format within the DiT backbone, and refer to this mechanism as the Position Shift Adaptive Module, which enables video generation of arbitrary length. Finally, we introduce a novel data augmentation strategy and a skeleton alignment model to reduce the impact of human shape variations across different identities. Experimental results demonstrate that our method outperforms existing state-of-the-art approaches, achieving superior performance in both high-fidelity and long-duration human image animation.

