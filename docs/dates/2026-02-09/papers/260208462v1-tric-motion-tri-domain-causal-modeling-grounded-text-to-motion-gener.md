---
layout: default
title: TriC-Motion: Tri-Domain Causal Modeling Grounded Text-to-Motion Generation
---

# TriC-Motion: Tri-Domain Causal Modeling Grounded Text-to-Motion Generation
**arXiv**：[2602.08462v1](https://arxiv.org/abs/2602.08462) · [PDF](https://arxiv.org/pdf/2602.08462.pdf)  
**作者**：Yiyang Cao, Yunze Deng, Ziyu Lin, Bin Feng, Xinggang Wang, Wenyu Liu, Dandan Zheng, Jingdong Chen  

**一句话要点**：提出TriC-Motion，通过三域因果建模解决文本到运动生成中的多域联合优化与噪声干扰问题。

**关键词**：文本到运动生成, 三域建模, 因果干预, 扩散模型, 运动序列生成, 噪声解耦

## 3 点简述
- 核心问题：现有方法缺乏空间、时间和频率域的统一建模框架，且噪声导致运动无关线索与有效特征纠缠，影响生成质量。
- 方法要点：基于扩散模型，集成时空频三域建模与因果干预，包括域特定建模模块、分数引导融合和因果反事实解耦器。
- 实验或效果：在HumanML3D数据集上达到R@1 0.612，优于现有方法，生成高保真、连贯、多样且文本对齐的运动序列。

## 摘要（原文）

> Text-to-motion generation, a rapidly evolving field in computer vision, aims to produce realistic and text-aligned motion sequences. Current methods primarily focus on spatial-temporal modeling or independent frequency domain analysis, lacking a unified framework for joint optimization across spatial, temporal, and frequency domains. This limitation hinders the model's ability to leverage information from all domains simultaneously, leading to suboptimal generation quality. Additionally, in motion generation frameworks, motion-irrelevant cues caused by noise are often entangled with features that contribute positively to generation, thereby leading to motion distortion. To address these issues, we propose Tri-Domain Causal Text-to-Motion Generation (TriC-Motion), a novel diffusion-based framework integrating spatial-temporal-frequency-domain modeling with causal intervention. TriC-Motion includes three core modeling modules for domain-specific modeling, namely Temporal Motion Encoding, Spatial Topology Modeling, and Hybrid Frequency Analysis. After comprehensive modeling, a Score-guided Tri-domain Fusion module integrates valuable information from the triple domains, simultaneously ensuring temporal consistency, spatial topology, motion trends, and dynamics. Moreover, the Causality-based Counterfactual Motion Disentangler is meticulously designed to expose motion-irrelevant cues to eliminate noise, disentangling the real modeling contributions of each domain for superior generation. Extensive experimental results validate that TriC-Motion achieves superior performance compared to state-of-the-art methods, attaining an outstanding R@1 of 0.612 on the HumanML3D dataset. These results demonstrate its capability to generate high-fidelity, coherent, diverse, and text-aligned motion sequences. Code is available at: https://caoyiyang1105.github.io/TriC-Motion/.

