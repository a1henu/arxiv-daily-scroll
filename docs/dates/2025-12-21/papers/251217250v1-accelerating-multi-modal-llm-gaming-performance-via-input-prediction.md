---
layout: default
title: Accelerating Multi-modal LLM Gaming Performance via Input Prediction and Mishit Correction
---

# Accelerating Multi-modal LLM Gaming Performance via Input Prediction and Mishit Correction
**arXiv**：[2512.17250v1](https://arxiv.org/abs/2512.17250) · [PDF](https://arxiv.org/pdf/2512.17250.pdf)  
**作者**：Ziyang Lin, Zixuan Sun, Sanhorn Chen, Xiaoyang Chen, Roy Zhao  

**一句话要点**：提出推测与校正框架，通过输入预测与失误校正加速多模态LLM游戏性能

**关键词**：推测执行, 模型预测控制, 潜在空间规划, 延迟优化, 游戏控制

## 3 点简述
- 实时顺序控制代理常受推理延迟瓶颈，导致控制不稳定和性能下降。
- 采用推测执行理念，结合预训练世界模型和潜在空间MPC规划器生成动作队列和潜在预测。
- 实验在DMC Humanoid-Walk任务中减少规划推理次数，提升步延迟，保持控制性能。

## 摘要（原文）

> Real-time sequential control agents are often bottlenecked by inference latency. Even modest per-step planning delays can destabilize control and degrade overall performance. We propose a speculation-and-correction framework that adapts the predict-then-verify philosophy of speculative execution to model-based control with TD-MPC2. At each step, a pretrained world model and latent-space MPC planner generate a short-horizon action queue together with predicted latent rollouts, allowing the agent to execute multiple planned actions without immediate replanning. When a new observation arrives, the system measures the mismatch between the encoded real latent state and the queued predicted latent. For small to moderate mismatch, a lightweight learned corrector applies a residual update to the speculative action, distilled offline from a replanning teacher. For large mismatch, the agent safely falls back to full replanning and clears stale action queues. We study both a gated two-tower MLP corrector and a temporal Transformer corrector to address local errors and systematic drift. Experiments on the DMC Humanoid-Walk task show that our method reduces the number of planning inferences from 500 to 282, improves end-to-end step latency by 25 percent, and maintains strong control performance with only a 7.1 percent return reduction. Ablation results demonstrate that speculative execution without correction is unreliable over longer horizons, highlighting the necessity of mismatch-aware correction for robust latency reduction.

