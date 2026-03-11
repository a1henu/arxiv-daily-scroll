---
layout: default
title: BridgeDiff: Bridging Human Observations and Flat-Garment Synthesis for Virtual Try-Off
---

# BridgeDiff: Bridging Human Observations and Flat-Garment Synthesis for Virtual Try-Off
**arXiv**：[2603.09236v1](https://arxiv.org/abs/2603.09236) · [PDF](https://arxiv.org/pdf/2603.09236.pdf)  
**作者**：Shuang Liu, Ao Yu, Linkang Cheng, Xiwen Huang, Li Zhao, Junhui Liu, Zhiting Lin, Yu Liu  

**一句话要点**：提出BridgeDiff框架，通过桥接人体观察与平面服装合成解决虚拟试衣中外观与布局不一致的问题。

**关键词**：虚拟试衣, 扩散模型, 平面服装合成, 结构约束, 图像重建, 注意力机制

## 3 点简述
- 核心问题：现有方法将虚拟试衣视为直接图像翻译，忽略人体外观与平面布局间的差距，导致未观察区域补全不一致和结构不稳定。
- 方法要点：引入Garment Condition Bridge Module捕获全局外观和语义身份，以及Flat Structure Constraint Module通过FC-Attention注入平面结构先验，提升合成稳定性。
- 实验或效果：在标准虚拟试衣基准测试中，BridgeDiff实现最先进性能，生成更高质量的平面服装重建，保持细粒度外观和结构完整性。

## 摘要（原文）

> Virtual try-off (VTOFF) aims to recover canonical flat-garment representations from images of dressed persons for standardized display and downstream virtual try-on. Prior methods often treat VTOFF as direct image translation driven by local masks or text-only prompts, overlooking the gap between on-body appearances and flat layouts. This gap frequently leads to inconsistent completion in unobserved regions and unstable garment structure. We propose BridgeDiff, a diffusion-based framework that explicitly bridges human-centric observations and flat-garment synthesis through two complementary components. First, the Garment Condition Bridge Module (GCBM) builds a garment-cue representation that captures global appearance and semantic identity, enabling robust inference of continuous details under partial visibility. Second, the Flat Structure Constraint Module (FSCM) injects explicit flat-garment structural priors via Flat-Constraint Attention (FC-Attention) at selected denoising stages, improving structural stability beyond text-only conditioning. Extensive experiments on standard VTOFF benchmarks show that BridgeDiff achieves state-of-the-art performance, producing higher-quality flat-garment reconstructions while preserving fine-grained appearance and structural integrity.

