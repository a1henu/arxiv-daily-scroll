---
layout: default
title: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling
---

# Diffusion Forcing for Multi-Agent Interaction Sequence Modeling
**arXiv**：[2512.17900v1](https://arxiv.org/abs/2512.17900) · [PDF](https://arxiv.org/pdf/2512.17900.pdf)  
**作者**：Vongani H. Maluleke, Kie Horiuchi, Lea Wilken, Evonne Ng, Jitendra Malik, Angjoo Kanazawa  

**一句话要点**：提出MAGNet统一自回归扩散框架，以解决多智能体交互序列建模中的灵活生成挑战。

**关键词**：多智能体运动生成, 扩散模型, 自回归序列建模, 交互序列生成, 智能体耦合建模

## 3 点简述
- 核心问题：多智能体交互建模因长时程、强依赖和可变组规模而困难，现有方法缺乏通用性。
- 方法要点：基于Diffusion Forcing，引入显式智能体耦合建模，支持自回归去噪和灵活条件采样。
- 实验或效果：在二元基准上媲美专用方法，可扩展至三元及以上场景，生成协调的同步和社交交互。

## 摘要（原文）

> Understanding and generating multi-person interactions is a fundamental challenge with broad implications for robotics and social computing. While humans naturally coordinate in groups, modeling such interactions remains difficult due to long temporal horizons, strong inter-agent dependencies, and variable group sizes. Existing motion generation methods are largely task-specific and do not generalize to flexible multi-agent generation. We introduce MAGNet (Multi-Agent Diffusion Forcing Transformer), a unified autoregressive diffusion framework for multi-agent motion generation that supports a wide range of interaction tasks through flexible conditioning and sampling. MAGNet performs dyadic prediction, partner inpainting, and full multi-agent motion generation within a single model, and can autoregressively generate ultra-long sequences spanning hundreds of v. Building on Diffusion Forcing, we introduce key modifications that explicitly model inter-agent coupling during autoregressive denoising, enabling coherent coordination across agents. As a result, MAGNet captures both tightly synchronized activities (e.g, dancing, boxing) and loosely structured social interactions. Our approach performs on par with specialized methods on dyadic benchmarks while naturally extending to polyadic scenarios involving three or more interacting people, enabled by a scalable architecture that is agnostic to the number of agents. We refer readers to the supplemental video, where the temporal dynamics and spatial coordination of generated interactions are best appreciated. Project page: https://von31.github.io/MAGNet/

