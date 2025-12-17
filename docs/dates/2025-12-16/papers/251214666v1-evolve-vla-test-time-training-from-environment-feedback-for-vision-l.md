---
layout: default
title: EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models
---

# EVOLVE-VLA: Test-Time Training from Environment Feedback for Vision-Language-Action Models
**arXiv**：[2512.14666v1](https://arxiv.org/abs/2512.14666) · [PDF](https://arxiv.org/pdf/2512.14666.pdf)  
**作者**：Zechen Bai, Chen Gao, Mike Zheng Shou  

**一句话要点**：提出EVOLVE-VLA框架，通过环境反馈实现视觉-语言-动作模型的测试时训练，以解决静态监督微调的限制。

**关键词**：视觉-语言-动作模型, 测试时训练, 环境反馈, 进度估计, 自适应学习, 机器人操作

## 3 点简述
- 核心问题：视觉-语言-动作模型依赖监督微调，难以适应部署条件变化，需要大量任务特定演示。
- 方法要点：设计学习进度估计器提供密集反馈，结合累积估计和渐进视野扩展机制来平滑噪声信号。
- 实验或效果：在长视野任务上提升8.6%，1-shot学习提升22.0%，并在未见任务上实现20.8%成功率，展现出错误恢复和新策略能力。

## 摘要（原文）

> Achieving truly adaptive embodied intelligence requires agents that learn not just by imitating static demonstrations, but by continuously improving through environmental interaction, which is akin to how humans master skills through practice. Vision-Language-Action (VLA) models have advanced robotic manipulation by leveraging large language models, yet remain fundamentally limited by Supervised Finetuning (SFT): requiring hundreds of demonstrations per task, rigidly memorizing trajectories, and failing to adapt when deployment conditions deviate from training. We introduce EVOLVE-VLA, a test-time training framework enabling VLAs to continuously adapt through environment interaction with minimal or zero task-specific demonstrations. The key technical challenge is replacing oracle reward signals (unavailable at test time) with autonomous feedback. We address this through a learned progress estimator providing dense feedback, and critically, we design our framework to ``tame'' this inherently noisy signal via two mechanisms: (1) an accumulative progress estimation mechanism smoothing noisy point-wise estimates, and (2) a progressive horizon extension strategy enabling gradual policy evolution. EVOLVE-VLA achieves substantial gains: +8.6\% on long-horizon tasks, +22.0\% in 1-shot learning, and enables cross-task generalization -- achieving 20.8\% success on unseen tasks without task-specific demonstrations training (vs. 0\% for pure SFT). Qualitative analysis reveals emergent capabilities absent in demonstrations, including error recovery and novel strategies. This work represents a critical step toward VLAs that truly learn and adapt, moving beyond static imitation toward continuous self-improvements.

