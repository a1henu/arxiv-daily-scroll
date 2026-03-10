---
layout: default
title: AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models
---

# AtomVLA: Scalable Post-Training for Robotic Manipulation via Predictive Latent World Models
**arXiv**：[2603.08519v1](https://arxiv.org/abs/2603.08519) · [PDF](https://arxiv.org/pdf/2603.08519.pdf)  
**作者**：Xiaoquan Sun, Zetian Xu, Chen Cao, Zonghe Liu, Yihan Sun, Jingrui Pang, Ruijian Zhang, Zhen Yang, Kang Pang, Dingxin He, Mingqi Yuan, Jiayu Chen  

**一句话要点**：提出AtomVLA框架，通过原子子任务分解与预测世界模型，解决机器人操作中指令接地差距与长时程任务错误累积问题。

**关键词**：视觉-语言-动作模型, 机器人操作, 长时程任务, 预测世界模型, 离线后训练, 原子子任务分解

## 3 点简述
- 核心问题：当前VLA模型依赖粗粒度指令，缺乏中间指导，导致长时程任务中错误累积严重。
- 方法要点：利用大语言模型分解演示为原子子任务，结合预测世界模型在潜在空间评估动作块，实现高效离线后训练。
- 实验或效果：在LIBERO基准上平均成功率97.0%，真实世界实验中验证了长时程任务的广泛适用性。

## 摘要（原文）

> Vision-Language-Action (VLA) models demonstrate remarkable potential for generalizable robotic manipulation. The execution of complex multi-step behaviors in VLA models can be improved by robust instruction grounding, a critical component for effective control. However, current paradigms predominantly rely on coarse, high-level task instructions during supervised fine-tuning. This instruction grounding gap leaves models without explicit intermediate guidance, leading to severe compounding errors in long-horizon tasks. Therefore, bridging this instruction gap and providing scalable post-training for VLA models is urgent. To tackle this problem, we propose \method, the first subtask-aware VLA framework integrated with a scalable offline post-training pipeline. Our framework leverages a large language model to decompose high-level demonstrations into fine-grained atomic subtasks. This approach utilizes a pretrained predictive world model to score candidate action chunks against subtask goals in the latent space, mitigating error accumulation while significantly improving long-horizon robustness. Furthermore, this approach enables highly efficient Group Relative Policy Optimization without the prohibitive expenses associated with online rollouts on physical robots. Extensive simulations validate that our AtomVLA maintains strong robustness under perturbations. When evaluated against fundamental baseline models, it achieves an average success rate of 97.0\% on the LIBERO benchmark and 48.0\% on the LIBERO-PRO benchmark. Finally, experiments conducted in the real world using the Galaxea R1 Lite platform confirm its broad applicability across diverse tasks, especially long-horizon tasks. All datasets, checkpoints, and code will be released to the public domain following the acceptance of this work for future research.

