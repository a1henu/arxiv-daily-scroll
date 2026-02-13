---
layout: default
title: LUVE : Latent-Cascaded Ultra-High-Resolution Video Generation with Dual Frequency Experts
---

# LUVE : Latent-Cascaded Ultra-High-Resolution Video Generation with Dual Frequency Experts
**arXiv**：[2602.11564v1](https://arxiv.org/abs/2602.11564) · [PDF](https://arxiv.org/pdf/2602.11564.pdf)  
**作者**：Chen Zhao, Jiawei Chen, Hongyu Li, Zhuoliang Kang, Shilin Lu, Xiaoming Wei, Kai Zhang, Jian Yang, Ying Tai  

**一句话要点**：提出LUVE框架，通过潜在空间级联与双频专家解决超高清视频生成的挑战。

**关键词**：超高清视频生成, 潜在空间级联, 双频专家, 视频扩散模型, 内容细化

## 3 点简述
- 核心问题：超高清视频生成面临运动建模、语义规划和细节合成的复合困难。
- 方法要点：采用三阶段架构，包括低分辨率运动生成、潜在空间上采样和双频专家内容细化。
- 实验或效果：实验显示LUVE在超高清视频生成中实现卓越的真实感和内容保真度。

## 摘要（原文）

> Recent advances in video diffusion models have significantly improved visual quality, yet ultra-high-resolution (UHR) video generation remains a formidable challenge due to the compounded difficulties of motion modeling, semantic planning, and detail synthesis. To address these limitations, we propose \textbf{LUVE}, a \textbf{L}atent-cascaded \textbf{U}HR \textbf{V}ideo generation framework built upon dual frequency \textbf{E}xperts. LUVE employs a three-stage architecture comprising low-resolution motion generation for motion-consistent latent synthesis, video latent upsampling that performs resolution upsampling directly in the latent space to mitigate memory and computational overhead, and high-resolution content refinement that integrates low-frequency and high-frequency experts to jointly enhance semantic coherence and fine-grained detail generation. Extensive experiments demonstrate that our LUVE achieves superior photorealism and content fidelity in UHR video generation, and comprehensive ablation studies further validate the effectiveness of each component. The project is available at \href{https://unicornanrocinu.github.io/LUVE_web/}{https://github.io/LUVE/}.

