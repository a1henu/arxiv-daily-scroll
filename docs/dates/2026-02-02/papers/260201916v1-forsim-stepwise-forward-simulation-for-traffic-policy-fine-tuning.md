---
layout: default
title: ForSim: Stepwise Forward Simulation for Traffic Policy Fine-Tuning
---

# ForSim: Stepwise Forward Simulation for Traffic Policy Fine-Tuning
**arXiv**：[2602.01916v1](https://arxiv.org/abs/2602.01916) · [PDF](https://arxiv.org/pdf/2602.01916.pdf)  
**作者**：Keyu Chen, Wenchao Sun, Hao Cheng, Zheng Fu, Sifa Zheng  

**一句话要点**：提出ForSim逐步闭环前向仿真范式，以提升自动驾驶交通仿真的真实性与交互性。

**关键词**：交通仿真, 自动驾驶, 闭环训练, 多模态交互, 前向仿真, 策略微调

## 3 点简述
- 核心问题：交通仿真存在协变量偏移和有限多模态行为反映能力，导致非反应式交互不真实。
- 方法要点：通过逐步闭环仿真，基于物理动力学匹配参考轨迹，保持多模态多样性并确保模态内一致性。
- 实验或效果：在RIFT框架中集成ForSim，实验证实能提升安全性，同时保持效率、真实性和舒适度。

## 摘要（原文）

> As the foundation of closed-loop training and evaluation in autonomous driving, traffic simulation still faces two fundamental challenges: covariate shift introduced by open-loop imitation learning and limited capacity to reflect the multimodal behaviors observed in real-world traffic. Although recent frameworks such as RIFT have partially addressed these issues through group-relative optimization, their forward simulation procedures remain largely non-reactive, leading to unrealistic agent interactions within the virtual domain and ultimately limiting simulation fidelity. To address these issues, we propose ForSim, a stepwise closed-loop forward simulation paradigm. At each virtual timestep, the traffic agent propagates the virtual candidate trajectory that best spatiotemporally matches the reference trajectory through physically grounded motion dynamics, thereby preserving multimodal behavioral diversity while ensuring intra-modality consistency. Other agents are updated with stepwise predictions, yielding coherent and interaction-aware evolution. When incorporated into the RIFT traffic simulation framework, ForSim operates in conjunction with group-relative optimization to fine-tune traffic policy. Extensive experiments confirm that this integration consistently improves safety while maintaining efficiency, realism, and comfort. These results underscore the importance of modeling closed-loop multimodal interactions within forward simulation and enhance the fidelity and reliability of traffic simulation for autonomous driving. Project Page: https://currychen77.github.io/ForSim/

