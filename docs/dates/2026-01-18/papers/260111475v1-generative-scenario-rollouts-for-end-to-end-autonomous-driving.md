---
layout: default
title: Generative Scenario Rollouts for End-to-End Autonomous Driving
---

# Generative Scenario Rollouts for End-to-End Autonomous Driving
**arXiv**：[2601.11475v1](https://arxiv.org/abs/2601.11475) · [PDF](https://arxiv.org/pdf/2601.11475.pdf)  
**作者**：Rajeev Yasarla, Deepti Hegde, Shizhong Han, Hsin-Pai Cheng, Yunxiao Shi, Meysam Sadeghigooghari, Shweta Mahajan, Apratim Bhattacharyya, Litian Liu, Risheek Garrepalli, Thomas Svantesson, Fatih Porikli, Hong Cai  

**一句话要点**：提出GeRo框架，通过语言条件自回归生成实现端到端自动驾驶的规划与场景生成。

**关键词**：端到端自动驾驶, 视觉-语言-动作模型, 生成式场景推演, 语言条件生成, 自回归规划, 多智能体规划

## 3 点简述
- 当前VLA模型依赖稀疏轨迹模仿学习，未充分利用生成潜力。
- GeRo训练VLA模型编码动态为潜在令牌，并基于语言条件自回归生成未来场景。
- 在Bench2Drive上提升驾驶分数和成功率，实现最先进的闭环和开环性能。

## 摘要（原文）

> Vision-Language-Action (VLA) models are emerging as highly effective planning models for end-to-end autonomous driving systems. However, current works mostly rely on imitation learning from sparse trajectory annotations and under-utilize their potential as generative models. We propose Generative Scenario Rollouts (GeRo), a plug-and-play framework for VLA models that jointly performs planning and generation of language-grounded future traffic scenes through an autoregressive rollout strategy. First, a VLA model is trained to encode ego vehicle and agent dynamics into latent tokens under supervision from planning, motion, and language tasks, facilitating text-aligned generation. Next, GeRo performs language-conditioned autoregressive generation. Given multi-view images, a scenario description, and ego-action questions, it generates future latent tokens and textual responses to guide long-horizon rollouts. A rollout-consistency loss stabilizes predictions using ground truth or pseudo-labels, mitigating drift and preserving text-action alignment. This design enables GeRo to perform temporally consistent, language-grounded rollouts that support long-horizon reasoning and multi-agent planning. On Bench2Drive, GeRo improves driving score and success rate by +15.7 and +26.2, respectively. By integrating reinforcement learning with generative rollouts, GeRo achieves state-of-the-art closed-loop and open-loop performance, demonstrating strong zero-shot robustness. These results highlight the promise of generative, language-conditioned reasoning as a foundation for safer and more interpretable end-to-end autonomous driving.

