---
layout: default
title: DR.Experts: Differential Refinement of Distortion-Aware Experts for Blind Image Quality Assessment
---

# DR.Experts: Differential Refinement of Distortion-Aware Experts for Blind Image Quality Assessment
**arXiv**：[2602.09531v1](https://arxiv.org/abs/2602.09531) · [PDF](https://arxiv.org/pdf/2602.09531.pdf)  
**作者**：Bohan Fu, Guanyi Qin, Fazhan Zhang, Zihao Huang, Mingxuan Li, Runze Hu  

**一句话要点**：提出DR.Experts框架，通过失真先验增强解决盲图像质量评估中失真线索捕获不足的问题。

**关键词**：盲图像质量评估, 失真先验, 视觉语言模型, 混合专家, 失真显著性, 人类感知对齐

## 3 点简述
- 核心问题：现有BIQA模型因缺乏可靠失真先验，难以有效捕捉细微失真线索，导致与人类主观判断不一致。
- 方法要点：利用退化感知视觉语言模型获取失真先验，通过失真显著性差分模块精炼，并采用动态失真加权模块融合特征以对齐人类感知。
- 实验或效果：在五个BIQA基准测试中表现优异，展示了在泛化性和数据效率方面的优势。

## 摘要（原文）

> Blind Image Quality Assessment, aiming to replicate human perception of visual quality without reference, plays a key role in vision tasks, yet existing models often fail to effectively capture subtle distortion cues, leading to a misalignment with human subjective judgments. We identify that the root cause of this limitation lies in the lack of reliable distortion priors, as methods typically learn shallow relationships between unified image features and quality scores, resulting in their insensitive nature to distortions and thus limiting their performance. To address this, we introduce DR.Experts, a novel prior-driven BIQA framework designed to explicitly incorporate distortion priors, enabling a reliable quality assessment. DR.Experts begins by leveraging a degradation-aware vision-language model to obtain distortion-specific priors, which are further refined and enhanced by the proposed Distortion-Saliency Differential Module through distinguishing them from semantic attentions, thereby ensuring the genuine representations of distortions. The refined priors, along with semantics and bridging representation, are then fused by a proposed mixture-of-experts style module named the Dynamic Distortion Weighting Module. This mechanism weights each distortion-specific feature as per its perceptual impact, ensuring that the final quality prediction aligns with human perception. Extensive experiments conducted on five challenging BIQA benchmarks demonstrate the superiority of DR.Experts over current methods and showcase its excellence in terms of generalization and data efficiency.

