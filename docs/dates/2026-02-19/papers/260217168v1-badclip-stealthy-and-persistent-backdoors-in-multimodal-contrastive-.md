---
layout: default
title: BadCLIP++: Stealthy and Persistent Backdoors in Multimodal Contrastive Learning
---

# BadCLIP++: Stealthy and Persistent Backdoors in Multimodal Contrastive Learning
**arXiv**：[2602.17168v1](https://arxiv.org/abs/2602.17168) · [PDF](https://arxiv.org/pdf/2602.17168.pdf)  
**作者**：Siyuan Liang, Yongcheng Jing, Yingjie Wang, Jiaxing Huang, Ee-chien Chang, Dacheng Tao  

**一句话要点**：提出BadCLIP++框架以解决多模态对比学习模型后门攻击的隐蔽性和持久性问题。

**关键词**：多模态对比学习, 后门攻击, 隐蔽性增强, 持久性优化, 防御鲁棒性, 物理攻击

## 3 点简述
- 核心问题：现有方法在强检测或持续微调下失效，源于跨模态不一致和低中毒率梯度稀释。
- 方法要点：引入语义融合QR微触发器和目标对齐子集选择增强隐蔽性；通过半径收缩、质心对齐和曲率控制稳定嵌入与参数。
- 实验效果：0.3%中毒率下攻击成功率99.99%，在十九种防御下保持高成功率且清洁精度下降小于0.8%。

## 摘要（原文）

> Research on backdoor attacks against multimodal contrastive learning models faces two key challenges: stealthiness and persistence. Existing methods often fail under strong detection or continuous fine-tuning, largely due to (1) cross-modal inconsistency that exposes trigger patterns and (2) gradient dilution at low poisoning rates that accelerates backdoor forgetting. These coupled causes remain insufficiently modeled and addressed. We propose BadCLIP++, a unified framework that tackles both challenges. For stealthiness, we introduce a semantic-fusion QR micro-trigger that embeds imperceptible patterns near task-relevant regions, preserving clean-data statistics while producing compact trigger distributions. We further apply target-aligned subset selection to strengthen signals at low injection rates. For persistence, we stabilize trigger embeddings via radius shrinkage and centroid alignment, and stabilize model parameters through curvature control and elastic weight consolidation, maintaining solutions within a low-curvature wide basin resistant to fine-tuning. We also provide the first theoretical analysis showing that, within a trust region, gradients from clean fine-tuning and backdoor objectives are co-directional, yielding a non-increasing upper bound on attack success degradation. Experiments demonstrate that with only 0.3% poisoning, BadCLIP++ achieves 99.99% attack success rate (ASR) in digital settings, surpassing baselines by 11.4 points. Across nineteen defenses, ASR remains above 99.90% with less than 0.8% drop in clean accuracy. The method further attains 65.03% success in physical attacks and shows robustness against watermark removal defenses.

