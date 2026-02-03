---
layout: default
title: PRISM: Performer RS-IMLE for Single-pass Multisensory Imitation Learning
---

# PRISM: Performer RS-IMLE for Single-pass Multisensory Imitation Learning
**arXiv**：[2602.02396v1](https://arxiv.org/abs/2602.02396) · [PDF](https://arxiv.org/pdf/2602.02396.pdf)  
**作者**：Amisha Bhaskar, Pratap Tokekar, Stefano Di Cairano, Alexander Schperberg  

**一句话要点**：提出PRISM单通道策略，基于IMLE的批量全局拒绝采样变体，用于实时多感官机器人模仿学习。

**关键词**：机器人模仿学习, 多感官融合, 单通道策略, IMLE变体, 实时控制, 轨迹优化

## 3 点简述
- 机器人模仿学习需处理多模态动作分布、实时控制与多感官输入，现有方法常仅满足部分需求。
- PRISM结合时间多感官编码器与Performer架构的线性注意力生成器，实现单通道策略生成。
- 在真实硬件与大规模仿真基准测试中，PRISM在成功率与控制频率上优于现有方法，并减少轨迹抖动。

## 摘要（原文）

> Robotic imitation learning typically requires models that capture multimodal action distributions while operating at real-time control rates and accommodating multiple sensing modalities. Although recent generative approaches such as diffusion models, flow matching, and Implicit Maximum Likelihood Estimation (IMLE) have achieved promising results, they often satisfy only a subset of these requirements. To address this, we introduce PRISM, a single-pass policy based on a batch-global rejection-sampling variant of IMLE. PRISM couples a temporal multisensory encoder (integrating RGB, depth, tactile, audio, and proprioception) with a linear-attention generator using a Performer architecture. We demonstrate the efficacy of PRISM on a diverse real-world hardware suite, including loco-manipulation using a Unitree Go2 with a 7-DoF arm D1 and tabletop manipulation with a UR5 manipulator. Across challenging physical tasks such as pre-manipulation parking, high-precision insertion, and multi-object pick-and-place, PRISM outperforms state-of-the-art diffusion policies by 10-25% in success rate while maintaining high-frequency (30-50 Hz) closed-loop control. We further validate our approach on large-scale simulation benchmarks, including CALVIN, MetaWorld, and Robomimic. In CALVIN (10% data split), PRISM improves success rates by approximately 25% over diffusion and approximately 20% over flow matching, while simultaneously reducing trajectory jerk by 20x-50x. These results position PRISM as a fast, accurate, and multisensory imitation policy that retains multimodal action coverage without the latency of iterative sampling.

