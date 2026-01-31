---
layout: default
title: On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression
---

# On the Adversarial Robustness of Large Vision-Language Models under Visual Token Compression
**arXiv**：[2601.21531v1](https://arxiv.org/abs/2601.21531) · [PDF](https://arxiv.org/pdf/2601.21531.pdf)  
**作者**：Xinwei Zhang, Hangcheng Liu, Li Bai, Hao Wang, Qingqing Ye, Tianwei Zhang, Haibo Hu  

**一句话要点**：提出CAGE攻击方法以解决视觉令牌压缩下大视觉语言模型的对抗鲁棒性评估问题

**关键词**：大视觉语言模型, 对抗鲁棒性, 视觉令牌压缩, 攻击方法, 安全评估

## 3 点简述
- 核心问题：现有攻击方法因优化-推理不匹配，高估了压缩后大视觉语言模型的鲁棒性
- 方法要点：CAGE通过预期特征破坏和秩失真对齐，无需访问压缩机制即可对齐扰动优化与压缩推理
- 实验或效果：在多种压缩机制和数据集上，CAGE一致降低鲁棒准确率，揭示忽略压缩的评估过于乐观

## 摘要（原文）

> Visual token compression is widely used to accelerate large vision-language models (LVLMs) by pruning or merging visual tokens, yet its adversarial robustness remains unexplored. We show that existing encoder-based attacks can substantially overestimate the robustness of compressed LVLMs, due to an optimization-inference mismatch: perturbations are optimized on the full-token representation, while inference is performed through a token-compression bottleneck. To address this gap, we propose the Compression-AliGnEd attack (CAGE), which aligns perturbation optimization with compression inference without assuming access to the deployed compression mechanism or its token budget. CAGE combines (i) expected feature disruption, which concentrates distortion on tokens likely to survive across plausible budgets, and (ii) rank distortion alignment, which actively aligns token distortions with rank scores to promote the retention of highly distorted evidence. Across diverse representative plug-and-play compression mechanisms and datasets, our results show that CAGE consistently achieves lower robust accuracy than the baseline. This work highlights that robustness assessments ignoring compression can be overly optimistic, calling for compression-aware security evaluation and defenses for efficient LVLMs.

