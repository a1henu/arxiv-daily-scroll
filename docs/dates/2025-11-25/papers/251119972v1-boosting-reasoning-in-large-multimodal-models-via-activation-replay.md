---
layout: default
title: Boosting Reasoning in Large Multimodal Models via Activation Replay
---

# Boosting Reasoning in Large Multimodal Models via Activation Replay
**arXiv**：[2511.19972v1](https://arxiv.org/abs/2511.19972) · [PDF](https://arxiv.org/pdf/2511.19972.pdf)  
**作者**：Yun Xing, Xiaobin Hu, Qingdong He, Jiangning Zhang, Shuicheng Yan, Shijian Lu, Yu-Gang Jiang  

**一句话要点**：提出激活重放以提升后训练大型多模态模型的推理能力

**关键词**：大型多模态模型, 推理能力提升, 激活重放, 后训练优化, 多模态推理

## 3 点简述
- 核心问题：RLVR后训练机制未明，影响低熵激活，可能阻碍推理。
- 方法要点：无需训练，测试时重放基础模型低熵激活调节RLVR模型。
- 实验或效果：提升数学、视觉代理和视频推理性能，改善Pass@K指标。

## 摘要（原文）

> Recently, Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as an effective approach to incentivizing reasoning capability in Large Multimodal Models (LMMs), while the underlying mechanisms behind this post-training paradigm are poorly understood. We begin by exploring how input activations are affected by RLVR through the perspective of logit lens. Our systematic investigations across multiple post-trained LMMs suggest that RLVR shifts low-entropy activations unexpectedly, while high-entropy ones are less affected. We further demonstrate that such phenomena are associated with LMM reasoning by controlled experiments, suggesting a potentially beneficial role of modulating low-entropy activations. To this end, we propose Activation Replay, a novel simple yet effective training-free approach that boosts multimodal reasoning of post-trained LMMs without requiring expensive policy optimization. Our design involves manipulation of visual tokens at test time, replaying low-entropy activations from the input context of base LMMs to regulating the RLVR counterparts. Activation Replay triggers better reasoning across diverse scenarios, including mathematics, o3-like visual agents, and video reasoning. We further show that Activation Replay boosts Pass@K and mitigates narrower reasoning coverage of RLVR. Our design is compared against alternative choices, such as replaying high-entropy activations instead of low-entropy ones, or direct cross-model intervention instead of manipulating input tokens, demonstrating the superiority of our implementation. Codes will be made publicly available.

