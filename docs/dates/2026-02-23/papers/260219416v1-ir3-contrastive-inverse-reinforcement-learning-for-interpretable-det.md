---
layout: default
title: IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking
---

# IR$^3$: Contrastive Inverse Reinforcement Learning for Interpretable Detection and Mitigation of Reward Hacking
**arXiv**：[2602.19416v1](https://arxiv.org/abs/2602.19416) · [PDF](https://arxiv.org/pdf/2602.19416.pdf)  
**作者**：Mohammad Beigi, Ming Jin, Junshan Zhang, Jiaxin Zhang, Qifan Wang, Lifu Huang  

**一句话要点**：提出IR3框架以解决RLHF中的奖励黑客问题，通过逆向工程和修复隐式目标实现可解释检测与缓解。

**关键词**：奖励黑客检测, 对比逆强化学习, 可解释性分析, 稀疏自编码器, 模型对齐, 缓解策略

## 3 点简述
- 核心问题：RLHF可能导致奖励黑客，模型利用代理奖励中的虚假相关性，且内部目标不透明，难以检测或纠正。
- 方法要点：引入对比逆强化学习重建隐式奖励函数，通过稀疏自编码器分解为可解释特征，识别黑客特征并实施针对性缓解策略。
- 实验或效果：在多个奖励模型配置中，IR3与真实奖励相关性达0.89，黑客特征识别精度超90%，显著减少黑客行为，能力保持原模型3%内。

## 摘要（原文）

> Reinforcement Learning from Human Feedback (RLHF) enables powerful LLM alignment but can introduce reward hacking - models exploit spurious correlations in proxy rewards without genuine alignment. Compounding this, the objectives internalized during RLHF remain opaque, making hacking behaviors difficult to detect or correct. We introduce IR3 (Interpretable Reward Reconstruction and Rectification), a framework that reverse-engineers, interprets, and surgically repairs the implicit objectives driving RLHF-tuned models. We propose Contrastive Inverse Reinforcement Learning (C-IRL), which reconstructs the implicit reward function by contrasting paired responses from post-alignment and baseline policies to explain behavioral shifts during RLHF. We then decompose the reconstructed reward via sparse autoencoders into interpretable features, enabling identification of hacking signatures through contribution analysis. Finally, we propose mitigation strategies - clean reward optimization, adversarial shaping, constrained optimization, and feature-guided distillation - that target problematic features while preserving beneficial alignment. Experiments across multiple reward model configurations show that IR3 achieves 0.89 correlation with ground-truth rewards, identifies hacking features with over 90% precision, and significantly reduces hacking behaviors while maintaining capabilities within 3% of the original model.

