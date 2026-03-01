---
layout: default
title: Stable Adaptive Thinking via Advantage Shaping and Length-Aware Gradient Regulation
---

# Stable Adaptive Thinking via Advantage Shaping and Length-Aware Gradient Regulation
**arXiv**：[2602.22556v1](https://arxiv.org/abs/2602.22556) · [PDF](https://arxiv.org/pdf/2602.22556.pdf)  
**作者**：Zihang Xu, Haozhi Xie, Ziqi Miao, Wuxuan Gong, Chen Qian, Lijun Li  

**一句话要点**：提出两阶段框架以稳定大型推理模型的自适应思考，解决过思考与效率权衡问题。

**关键词**：大型推理模型, 自适应思考, 优势塑造, 梯度调节, 强化学习, 效率优化

## 3 点简述
- 核心问题：大型推理模型在低复杂度查询中常出现过思考行为，现有方法在精度-效率权衡和异构推理行为鲁棒性上受限。
- 方法要点：采用混合微调初始化，结合正确性保持优势塑造和长度感知梯度调节进行自适应强化学习。
- 实验或效果：在Qwen2.5-1.5B和7B上实验，精度提升达+3.7点，生成令牌减少超40%，验证了方法的鲁棒性和泛化性。

## 摘要（原文）

> Large reasoning models (LRMs) achieve strong performance through extended reasoning traces, but they often exhibit overthinking behavior for low-complexity queries. Existing efforts to mitigate this issue are fundamentally limited by unstable accuracy-efficiency trade-offs and poor robustness to heterogeneous reasoning behaviors. To address these challenges, we propose a two-stage framework for stable adaptive thinking in LRMs. The framework first applies Hybrid Fine-Tuning to expose the model to both thinking and no-thinking behaviors, establishing well-conditioned initialization. It then performs adaptive reinforcement learning with Correctness-Preserving Advantage Shaping (CPAS) to avoid suppressing correct long-chain reasoning, and Length-Aware Gradient Regulation (LAGR) to stabilize optimization under severe reasoning-length heterogeneity. Extensive experiments on Qwen2.5-1.5B and 7B show consistent improvements over strong baselines, achieving up to +3.7/+3.6 accuracy points while reducing generated tokens by 40.6%/43.9%. Further analyses across varying problem difficulties and out-of-distribution tasks confirm the robustness and generalization of our approach.

