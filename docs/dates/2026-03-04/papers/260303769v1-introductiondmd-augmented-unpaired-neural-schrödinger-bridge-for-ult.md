---
layout: default
title: IntroductionDMD-augmented Unpaired Neural Schrödinger Bridge for Ultra-Low Field MRI Enhancement
---

# IntroductionDMD-augmented Unpaired Neural Schrödinger Bridge for Ultra-Low Field MRI Enhancement
**arXiv**：[2603.03769v1](https://arxiv.org/abs/2603.03769) · [PDF](https://arxiv.org/pdf/2603.03769.pdf)  
**作者**：Youngmin Kim, Jaeyun Shin, Jeongchan Kim, Taehoon Lee, Jaemin Kim, Peter Hsu, Jelle Veraart, Jong Chul Ye  

**一句话要点**：提出DMD增强的无配对神经薛定谔桥框架，用于提升超低场MRI图像质量

**关键词**：超低场MRI增强, 无配对图像翻译, 神经薛定谔桥, 扩散模型, 结构保留正则化, 分布匹配

## 3 点简述
- 核心问题：超低场（64 mT）脑MRI图像质量差，且缺乏配对3 T数据用于训练。
- 方法要点：结合无配对神经薛定谔桥、DMD扩散引导分布匹配和结构保留正则化，增强真实感与解剖结构。
- 实验或效果：在无配对基准上提升分布级真实感，在配对队列中增加结构保真度，优于无配对基线。

## 摘要（原文）

> Ultra Low Field (64 mT) brain MRI improves accessibility but suffers from reduced image quality compared to 3 T. As paired 64 mT - 3 T scans are scarce, we propose an unpaired 64 mT $\rightarrow$ 3 T translation framework that enhances realism while preserving anatomy. Our method builds upon the Unpaired Neural Schrödinge Bridge (UNSB) with multi-step refinement. To strengthen target distribution alignment, we augment the adversarial objective with DMD2-style diffusion-guided distribution matching using a frozen 3T diffusion teacher. To explicitly constrain global structure beyond patch-level correspondence, we combine PatchNCE with an Anatomical Structure Preservation (ASP) regularizer that enforces soft foreground background consistency and boundary aware constraints. Evaluated on two disjoint cohorts, the proposed framework achieves an improved realism structure trade-off, enhancing distribution level realism on unpaired benchmarks while increasing structural fidelity on the paired cohort compared to unpaired baselines.

