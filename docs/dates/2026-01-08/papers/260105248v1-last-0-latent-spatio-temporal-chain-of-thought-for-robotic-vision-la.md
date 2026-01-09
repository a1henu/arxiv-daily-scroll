---
layout: default
title: LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model
---

# LaST$_{0}$: Latent Spatio-Temporal Chain-of-Thought for Robotic Vision-Language-Action Model
**arXiv**：[2601.05248v1](https://arxiv.org/abs/2601.05248) · [PDF](https://arxiv.org/pdf/2601.05248.pdf)  
**作者**：Zhuoyang Liu, Jiaming Liu, Hao Chen, Ziyu Guo, Chengkai Hou, Chenyang Gu, Jiale Yu, Xiangju Mi, Renrui Zhang, Zhengping Che, Jian Tang, Pheng-Ann Heng, Shanghang Zhang  

**一句话要点**：提出LaST$_0$框架，通过潜在时空思维链提升机器人视觉-语言-动作模型的推理效率与动作准确性。

**关键词**：机器人视觉-语言-动作模型, 潜在时空思维链, 混合Transformer架构, 高效推理, 机器人操作, 隐式表示学习

## 3 点简述
- 现有VLA方法依赖显式语言推理，导致推理延迟高且难以捕捉物理动态。
- LaST$_0$引入潜在时空思维链空间，建模视觉动态、3D结构和机器人本体状态，实现高效隐式推理。
- 在模拟和真实世界任务中，LaST$_0$相比先前方法提升成功率8%和13%，并显著加速推理。

## 摘要（原文）

> Vision-Language-Action (VLA) models have recently demonstrated strong generalization capabilities in robotic manipulation. Some existing VLA approaches attempt to improve action accuracy by explicitly generating linguistic reasoning traces or future visual observations before action execution. However, explicit reasoning typically incurs non-negligible inference latency, which constrains the temporal resolution required for robotic manipulation. Moreover, such reasoning is confined to the linguistic space, imposing a representational bottleneck that struggles to faithfully capture ineffable physical attributes. To mitigate these limitations, we propose LaST$_0$, a framework that enables efficient reasoning before acting through a Latent Spatio-Temporal Chain-of-Thought (CoT), capturing fine-grained physical and robotic dynamics that are often difficult to verbalize. Specifically, we introduce a token-efficient latent CoT space that models future visual dynamics, 3D structural information, and robot proprioceptive states, and further extends these representations across time to enable temporally consistent implicit reasoning trajectories. Furthermore, LaST$_0$ adopts a dual-system architecture implemented via a Mixture-of-Transformers design, where a reasoning expert conducts low-frequency latent inference and an acting expert generates high-frequency actions conditioned on robotics-oriented latent representations. To facilitate coordination, LaST$_0$ is trained with heterogeneous operation frequencies, enabling adaptive switching between reasoning and action inference rates during deployment. Across ten simulated and six real-world manipulation tasks, LaST$_0$ improves mean success rates by 8% and 13% over prior VLA methods, respectively, while achieving substantially faster inference. Project website: https://sites.google.com/view/last0

