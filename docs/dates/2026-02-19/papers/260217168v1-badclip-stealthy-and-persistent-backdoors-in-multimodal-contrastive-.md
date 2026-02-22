---
layout: default
title: BadCLIP++: Stealthy and Persistent Backdoors in Multimodal Contrastive Learning
---

# BadCLIP++: Stealthy and Persistent Backdoors in Multimodal Contrastive Learning
**arXiv**：[2602.17168v1](https://arxiv.org/abs/2602.17168) · [PDF](https://arxiv.org/pdf/2602.17168.pdf)  
**作者**：Siyuan Liang, Yongcheng Jing, Yingjie Wang, Jiaxing Huang, Ee-chien Chang, Dacheng Tao  

**一句话要点**：提出BadCLIP++框架以解决多模态对比学习模型后门攻击的隐蔽性和持久性问题。

**关键词**：多模态对比学习, 后门攻击, 隐蔽触发器, 持久性防御, 物理攻击, 梯度分析

## 3 点简述
- 核心问题：现有方法在强检测或持续微调下失效，源于跨模态不一致和低投毒率梯度稀释。
- 方法要点：引入语义融合QR微触发器增强隐蔽性，通过半径收缩和曲率控制提升持久性。
- 实验或效果：在0.3%投毒率下攻击成功率99.99%，对19种防御保持高成功率且清洁精度下降小于0.8%。

## 摘要（原文）

> Research on backdoor attacks against multimodal contrastive learning models faces two key challenges: stealthiness and persistence. Existing methods often fail under strong detection or continuous fine-tuning, largely due to (1) cross-modal inconsistency that exposes trigger patterns and (2) gradient dilution at low poisoning rates that accelerates backdoor forgetting. These coupled causes remain insufficiently modeled and addressed. We propose BadCLIP++, a unified framework that tackles both challenges. For stealthiness, we introduce a semantic-fusion QR micro-trigger that embeds imperceptible patterns near task-relevant regions, preserving clean-data statistics while producing compact trigger distributions. We further apply target-aligned subset selection to strengthen signals at low injection rates. For persistence, we stabilize trigger embeddings via radius shrinkage and centroid alignment, and stabilize model parameters through curvature control and elastic weight consolidation, maintaining solutions within a low-curvature wide basin resistant to fine-tuning. We also provide the first theoretical analysis showing that, within a trust region, gradients from clean fine-tuning and backdoor objectives are co-directional, yielding a non-increasing upper bound on attack success degradation. Experiments demonstrate that with only 0.3% poisoning, BadCLIP++ achieves 99.99% attack success rate (ASR) in digital settings, surpassing baselines by 11.4 points. Across nineteen defenses, ASR remains above 99.90% with less than 0.8% drop in clean accuracy. The method further attains 65.03% success in physical attacks and shows robustness against watermark removal defenses.

