---
layout: default
title: FALCON: Actively Decoupled Visuomotor Policies for Loco-Manipulation with Foundation-Model-Based Coordination
---

# FALCON: Actively Decoupled Visuomotor Policies for Loco-Manipulation with Foundation-Model-Based Coordination
**arXiv**：[2512.04381v1](https://arxiv.org/abs/2512.04381) · [PDF](https://arxiv.org/pdf/2512.04381.pdf)  
**作者**：Chengyang He, Ge Sun, Yue Bai, Junkai Lu, Jiadong Zhao, Guillaume Sartoretti  

**一句话要点**：提出FALCON框架，通过视觉语言基础模型协调解耦的视觉运动策略，以解决移动操作任务中的异构观测融合问题。

**关键词**：移动操作, 视觉运动策略, 视觉语言基础模型, 解耦协调, 扩散策略, 对比学习

## 3 点简述
- 核心问题：单一策略融合移动和操作的异构观测导致性能下降，需恢复协调性。
- 方法要点：将移动和操作解耦为专用策略，用视觉语言基础模型编码全局观测和指令作为共享潜变量协调两者。
- 实验或效果：在挑战性移动操作任务中超越集中式和去中心化基线，提升鲁棒性和泛化能力。

## 摘要（原文）

> We present FoundAtion-model-guided decoupled LoCO-maNipulation visuomotor policies (FALCON), a framework for loco-manipulation that combines modular diffusion policies with a vision-language foundation model as the coordinator. Our approach explicitly decouples locomotion and manipulation into two specialized visuomotor policies, allowing each subsystem to rely on its own observations. This mitigates the performance degradation that arise when a single policy is forced to fuse heterogeneous, potentially mismatched observations from locomotion and manipulation. Our key innovation lies in restoring coordination between these two independent policies through a vision-language foundation model, which encodes global observations and language instructions into a shared latent embedding conditioning both diffusion policies. On top of this backbone, we introduce a phase-progress head that uses textual descriptions of task stages to infer discrete phase and continuous progress estimates without manual phase labels. To further structure the latent space, we incorporate a coordination-aware contrastive loss that explicitly encodes cross-subsystem compatibility between arm and base actions. We evaluate FALCON on two challenging loco-manipulation tasks requiring navigation, precise end-effector placement, and tight base-arm coordination. Results show that it surpasses centralized and decentralized baselines while exhibiting improved robustness and generalization to out-of-distribution scenarios.

