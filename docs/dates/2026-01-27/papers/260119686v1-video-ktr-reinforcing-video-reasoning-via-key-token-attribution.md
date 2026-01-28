---
layout: default
title: Video-KTR: Reinforcing Video Reasoning via Key Token Attribution
---

# Video-KTR: Reinforcing Video Reasoning via Key Token Attribution
**arXiv**：[2601.19686v1](https://arxiv.org/abs/2601.19686) · [PDF](https://arxiv.org/pdf/2601.19686.pdf)  
**作者**：Ziyue Wang, Sheng Jin, Zhongrong Zuo, Jiawei Wu, Han Qiu, Qi She, Hao Zhang, Xudong Jiang  

**一句话要点**：提出Video-KTR框架，通过关键令牌强化解决视频推理中细粒度模态关联不足的问题。

**关键词**：视频推理, 强化学习, 令牌级归因, 多模态模型, 可解释性

## 3 点简述
- 现有视频推理方法依赖粗粒度奖励或单因素令牌选择，忽视视觉、时序与语言输出的细粒度关联。
- Video-KTR结合视觉感知、时序敏感性和预测不确定性三种归因信号，执行选择性令牌级强化学习。
- 在五个基准测试中达到领先或竞争性结果，提升推理准确性和可解释性，验证了信号互补性和更新鲁棒性。

## 摘要（原文）

> Reinforcement learning (RL) has shown strong potential for enhancing reasoning in multimodal large language models, yet existing video reasoning methods often rely on coarse sequence-level rewards or single-factor token selection, neglecting fine-grained links among visual inputs, temporal dynamics, and linguistic outputs, limiting both accuracy and interpretability. We propose Video-KTR, a modality-aware policy shaping framework that performs selective, token-level RL by combining three attribution signals: (1) visual-aware tokens identified via counterfactual masking to reveal perceptual dependence; (2) temporal-aware tokens detected through frame shuffling to expose temporal sensitivity; and (3) high-entropy tokens signaling predictive uncertainty. By reinforcing only these key tokens, Video-KTR focuses learning on semantically informative, modality-sensitive content while filtering out low-value tokens. Across five challenging benchmarks, Video-KTR achieves state-of-the-art or highly competitive results, achieving 42.7\% on Video-Holmes (surpassing GPT-4o) with consistent gains on both reasoning and general video understanding tasks. Ablation studies verify the complementary roles of the attribution signals and the robustness of targeted token-level updates. Overall, Video-KTR improves accuracy and interpretability, offering a simple, drop-in extension to RL for complex video reasoning. Our code and models are available at https://github.com/zywang0104/Video-KTR.

