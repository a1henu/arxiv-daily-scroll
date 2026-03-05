---
layout: default
title: ArthroCut: Autonomous Policy Learning for Robotic Bone Resection in Knee Arthroplasty
---

# ArthroCut: Autonomous Policy Learning for Robotic Bone Resection in Knee Arthroplasty
**arXiv**：[2603.03957v1](https://arxiv.org/abs/2603.03957) · [PDF](https://arxiv.org/pdf/2603.03957.pdf)  
**作者**：Xu Lu, Yiling Zhang, Wenquan Cheng, Longfei Ma, Fang Chen, Hongen Liao  

**一句话要点**：提出ArthroCut框架，通过自主策略学习实现膝关节置换手术中机器人骨切除的上下文感知动作生成。

**关键词**：自主策略学习, 膝关节置换手术, 多模态数据集, 令牌化动作生成, 机器人骨切除, 实时决策

## 3 点简述
- 核心问题：手术机器人自主性和实时决策能力在实践中受限，需从辅助执行升级为自主动作生成。
- 方法要点：基于自建多模态数据集微调Qwen-VL骨干，整合术前影像和实时手术令牌，在语法/安全约束下生成可解释动作。
- 实验或效果：在膝关节假体实验中，平均成功率86%，显著优于基线，显示令牌组合提升多平面切除稳定性。

## 摘要（原文）

> Despite rapid commercialization of surgical robots, their autonomy and real-time decision-making remain limited in practice. To address this gap, we propose ArthroCut, an autonomous policy learning framework that upgrades knee arthroplasty robots from assistive execution to context-aware action generation. ArthroCut fine-tunes a Qwen--VL backbone on a self-built, time-synchronized multimodal dataset from 21 complete cases (23,205 RGB--D pairs), integrating preoperative CT/MR, intraoperative NDI tracking of bones and end effector, RGB--D surgical video, robot state, and textual intent. The method operates on two complementary token families -- Preoperative Imaging Tokens (PIT) to encode patient-specific anatomy and planned resection planes, and Time-Aligned Surgical Tokens (TAST) to fuse real-time visual, geometric, and kinematic evidence -- and emits an interpretable action grammar under grammar/safety-constrained decoding. In bench-top experiments on a knee prosthesis across seven trials, ArthroCut achieves an average success rate of 86% over the six standard resections, significantly outperforming strong baselines trained under the same protocol. Ablations show that TAST is the principal driver of reliability while PIT provides essential anatomical grounding, and their combination yields the most stable multi-plane execution. These results indicate that aligning preoperative geometry with time-aligned intraoperative perception and translating that alignment into tokenized, constrained actions is an effective path toward robust, interpretable autonomy in orthopedic robotic surgery.

