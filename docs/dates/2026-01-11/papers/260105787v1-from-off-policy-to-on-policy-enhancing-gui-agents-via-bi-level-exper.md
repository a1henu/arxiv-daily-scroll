---
layout: default
title: From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation
---

# From Off-Policy to On-Policy: Enhancing GUI Agents via Bi-level Expert-to-Policy Assimilation
**arXiv**：[2601.05787v1](https://arxiv.org/abs/2601.05787) · [PDF](https://arxiv.org/pdf/2601.05787.pdf)  
**作者**：Zezhou Wang, Ziyun Zhang, Xiaoyi Zhang, Zhuzhong Qian, Yan Lu  

**一句话要点**：提出BEPA方法，通过双层专家轨迹同化提升GUI代理在可验证奖励强化学习中的性能。

**关键词**：GUI代理, 强化学习, 专家轨迹同化, 端到端策略, 可验证奖励, 计算机视觉

## 3 点简述
- GUI代理面临专家轨迹少且与策略不匹配的瓶颈，影响端到端策略训练。
- BEPA利用基础策略生成可达轨迹和动态缓存，将离线专家轨迹转化为策略对齐指导。
- 在OSWorld-Verified等基准上显著提升成功率，例如UITARS1.5-7B从22.87%增至32.13%。

## 摘要（原文）

> Vision-language models are increasingly deployed as computer-use agents (CUAs) that operate desktops and browsers. Top-performing CUAs are framework-based systems that decompose planning and execution, while end-to-end screenshot-to-action policies are easier to deploy but lag behind on benchmarks such as OSWorld-Verified. GUI datasets like OSWorld pose two bottlenecks: they expose only a few hundred interactive, verifiable tasks and environments, and expert trajectories must be gathered by interacting with these environments, making such data hard to scale. We therefore ask how reinforcement learning from verifiable rewards (RLVR) can best exploit a small pool of exist expert trajectories to train end-to-end policies. Naively mixing these off-policy traces into on-policy RLVR is brittle: even after format conversion, expert trajectories exhibit structural mismatch and distribution shift from the learner. We propose BEPA (Bi-Level Expert-to-Policy Assimilation), which turns static expert traces into policy-aligned guidance via self-rolled reachable trajectories under the base policy (LEVEL-1) and a per-task, dynamically updated cache used in RLVR (LEVEL-2). On OSWorld-Verified, BEPA improves UITARS1.5-7B success from 22.87% to 32.13% and raises a held-out split from 5.74% to 10.30%, with consistent gains on MMBench-GUI and Online-Mind2Web. Our code and data are available at: https://github.com/LEON-gittech/Verl_GUI.git

