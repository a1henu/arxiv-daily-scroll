---
layout: default
title: RRPO: Robust Reward Policy Optimization for LLM-based Emotional TTS
---

# RRPO: Robust Reward Policy Optimization for LLM-based Emotional TTS
**arXiv**：[2512.04552v1](https://arxiv.org/abs/2512.04552) · [PDF](https://arxiv.org/pdf/2512.04552.pdf)  
**作者**：Cong Wang, Changfeng Gao, Yang Xiang, Zhihao Du, Keyu An, Han Zhao, Qian Chen, Xiangang Li, Yingming Gao, Ya Li  

**一句话要点**：提出RRPO框架以解决基于LLM的情感TTS中奖励黑客问题，提升情感表达与自然度。

**关键词**：情感文本转语音, 强化学习, 奖励黑客, 稳健奖励模型, 混合正则化, 跨语言泛化

## 3 点简述
- 核心问题：可微强化学习框架易受奖励黑客影响，导致声学伪影和感知质量下降。
- 方法要点：采用混合正则化方案开发稳健奖励模型，使奖励信号更可靠对齐人类感知。
- 实验或效果：主观评估显示RRPO有效缓解奖励黑客，在情感表达和自然度上显著优于基线。

## 摘要（原文）

> Differentiable reinforcement learning (RL) frameworks like DiffRO offer a powerful approach for controllable text-to-speech (TTS), but are vulnerable to reward hacking, particularly for nuanced tasks like emotion control. The policy model can exploit a vanilla Reward Model (RM) by generating acoustic artifacts to achieve spurious rewards, but at the cost of degrading perceptual quality. To address this, we propose Robust Reward Policy Optimization (RRPO), a novel framework that employs a hybrid regularization scheme. This scheme develops a robust RM whose reward signal is more reliably aligned with human perception, compelling the policy to abandon detrimental shortcuts and instead learn the complex features of genuine emotions. Our ablation study confirms the enhanced robustness of our RM, as evidenced by its strong cross-lingual generalization. The subjective evaluation demonstrates that this robust RM effectively mitigates reward hacking, leading to significant improvements in both emotional expressiveness and naturalness over all baselines. Demo page: https://lrwinr.github.io/RRPO-CosyVoice.

