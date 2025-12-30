---
layout: default
title: Act2Goal: From World Model To General Goal-conditioned Policy
---

# Act2Goal: From World Model To General Goal-conditioned Policy
**arXiv**：[2512.23541v1](https://arxiv.org/abs/2512.23541) · [PDF](https://arxiv.org/pdf/2512.23541.pdf)  
**作者**：Pengfei Zhou, Liliang Chen, Shengcong Chen, Di Chen, Wenzhi Zhao, Rongjun Jin, Guanghui Ren, Jianlan Luo  

**一句话要点**：提出Act2Goal，通过目标条件世界模型与多尺度时序控制解决长时程机器人操作任务。

**关键词**：目标条件策略, 视觉世界模型, 多尺度时序控制, 机器人操作, 零样本泛化, 在线适应

## 3 点简述
- 核心问题：视觉目标条件策略在长时程操作中因缺乏任务进展建模而表现不佳。
- 方法要点：结合目标条件视觉世界模型生成中间状态序列，并利用多尺度时序哈希分解轨迹以实现精细控制。
- 实验或效果：在零样本泛化任务中显著提升成功率，并通过无奖励在线适应实现快速自主改进。

## 摘要（原文）

> Specifying robotic manipulation tasks in a manner that is both expressive and precise remains a central challenge. While visual goals provide a compact and unambiguous task specification, existing goal-conditioned policies often struggle with long-horizon manipulation due to their reliance on single-step action prediction without explicit modeling of task progress. We propose Act2Goal, a general goal-conditioned manipulation policy that integrates a goal-conditioned visual world model with multi-scale temporal control. Given a current observation and a target visual goal, the world model generates a plausible sequence of intermediate visual states that captures long-horizon structure. To translate this visual plan into robust execution, we introduce Multi-Scale Temporal Hashing (MSTH), which decomposes the imagined trajectory into dense proximal frames for fine-grained closed-loop control and sparse distal frames that anchor global task consistency. The policy couples these representations with motor control through end-to-end cross-attention, enabling coherent long-horizon behavior while remaining reactive to local disturbances. Act2Goal achieves strong zero-shot generalization to novel objects, spatial layouts, and environments. We further enable reward-free online adaptation through hindsight goal relabeling with LoRA-based finetuning, allowing rapid autonomous improvement without external supervision. Real-robot experiments demonstrate that Act2Goal improves success rates from 30% to 90% on challenging out-of-distribution tasks within minutes of autonomous interaction, validating that goal-conditioned world models with multi-scale temporal control provide structured guidance necessary for robust long-horizon manipulation. Project page: https://act2goal.github.io/

