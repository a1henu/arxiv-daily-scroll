---
layout: default
title: RLinf-Co: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models
---

# RLinf-Co: Reinforcement Learning-Based Sim-Real Co-Training for VLA Models
**arXiv**：[2602.12628v1](https://arxiv.org/abs/2602.12628) · [PDF](https://arxiv.org/pdf/2602.12628.pdf)  
**作者**：Liangzhi Shi, Shuaihang Chen, Feng Gao, Yinuo Chen, Kang Chen, Tonghe Zhang, Hongzhi Zhang, Weinan Zhang, Chao Yu, Yu Wang  

**一句话要点**：提出基于强化学习的仿真-现实协同训练框架，以提升视觉-语言-动作模型在真实机器人部署中的性能与泛化能力。

**关键词**：强化学习, 仿真-现实协同训练, 视觉-语言-动作模型, 机器人操作, 泛化能力, 数据效率

## 3 点简述
- 核心问题：现有仿真-现实协同训练方法依赖监督微调，未充分利用大规模闭环交互，导致真实世界增益和泛化能力有限。
- 方法要点：采用两阶段设计，先通过混合演示进行监督微调预热，再在仿真中结合强化学习和真实数据辅助监督损失进行微调，以锚定策略并减轻灾难性遗忘。
- 实验或效果：在四个真实桌面操作任务上评估，相比仅真实微调和基于监督的协同训练，成功率提升显著，并展现出更强的泛化能力和数据效率。

## 摘要（原文）

> Simulation offers a scalable and low-cost way to enrich vision-language-action (VLA) training, reducing reliance on expensive real-robot demonstrations. However, most sim-real co-training methods rely on supervised fine-tuning (SFT), which treats simulation as a static source of demonstrations and does not exploit large-scale closed-loop interaction. Consequently, real-world gains and generalization are often limited. In this paper, we propose an \underline{\textit{RL}}-based sim-real \underline{\textit{Co}}-training \modify{(RL-Co)} framework that leverages interactive simulation while preserving real-world capabilities. Our method follows a generic two-stage design: we first warm-start the policy with SFT on a mixture of real and simulated demonstrations, then fine-tune it with reinforcement learning in simulation while adding an auxiliary supervised loss on real-world data to anchor the policy and mitigate catastrophic forgetting. We evaluate our framework on four real-world tabletop manipulation tasks using two representative VLA architectures, OpenVLA and $π_{0.5}$, and observe consistent improvements over real-only fine-tuning and SFT-based co-training, including +24% real-world success on OpenVLA and +20% on $π_{0.5}$. Beyond higher success rates, RL co-training yields stronger generalization to unseen task variations and substantially improved real-world data efficiency, providing a practical and scalable pathway for leveraging simulation to enhance real-robot deployment.

