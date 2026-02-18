---
layout: default
title: The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems
---

# The Vision Wormhole: Latent-Space Communication in Heterogeneous Multi-Agent Systems
**arXiv**：[2602.15382v1](https://arxiv.org/abs/2602.15382) · [PDF](https://arxiv.org/pdf/2602.15382.pdf)  
**作者**：Xiaoze Liu, Ruowang Zhang, Weichen Yu, Siheng Xiong, Liu He, Feijie Wu, Hoin Jung, Matt Fredrikson, Xiaoqian Wang, Jing Gao  

**一句话要点**：提出Vision Wormhole框架，利用视觉接口实现异构多智能体系统的高效无文本通信

**关键词**：异构多智能体系统, 视觉语言模型, 潜在空间通信, 通用视觉编解码器, 教师-学生蒸馏

## 3 点简述
- 核心问题：异构多智能体系统中离散文本通信效率低，现有潜在状态转移方法可扩展性差
- 方法要点：通过通用视觉编解码器将推理轨迹映射到共享潜在空间，并采用中心辐射拓扑降低对齐复杂度
- 实验或效果：在异构模型家族上验证，减少端到端运行时间，同时保持与文本通信相当的推理保真度

## 摘要（原文）

> Multi-Agent Systems (MAS) powered by Large Language Models have unlocked advanced collaborative reasoning, yet they remain shackled by the inefficiency of discrete text communication, which imposes significant runtime overhead and information quantization loss. While latent state transfer offers a high-bandwidth alternative, existing approaches either assume homogeneous sender-receiver architectures or rely on pair-specific learned translators, limiting scalability and modularity across diverse model families with disjoint manifolds. In this work, we propose the Vision Wormhole, a novel framework that repurposes the visual interface of Vision-Language Models (VLMs) to enable model-agnostic, text-free communication. By introducing a Universal Visual Codec, we map heterogeneous reasoning traces into a shared continuous latent space and inject them directly into the receiver's visual pathway, effectively treating the vision encoder as a universal port for inter-agent telepathy. Our framework adopts a hub-and-spoke topology to reduce pairwise alignment complexity from O(N^2) to O(N) and leverages a label-free, teacher-student distillation objective to align the high-speed visual channel with the robust reasoning patterns of the text pathway. Extensive experiments across heterogeneous model families (e.g., Qwen-VL, Gemma) demonstrate that the Vision Wormhole reduces end-to-end wall-clock time in controlled comparisons while maintaining reasoning fidelity comparable to standard text-based MAS. Code is available at https://github.com/xz-liu/heterogeneous-latent-mas

