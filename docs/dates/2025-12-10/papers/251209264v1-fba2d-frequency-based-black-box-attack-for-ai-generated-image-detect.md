---
layout: default
title: FBA$^2$D: Frequency-based Black-box Attack for AI-generated Image Detection
---

# FBA$^2$D: Frequency-based Black-box Attack for AI-generated Image Detection
**arXiv**：[2512.09264v1](https://arxiv.org/abs/2512.09264) · [PDF](https://arxiv.org/pdf/2512.09264.pdf)  
**作者**：Xiaojing Chen, Dan Li, Lijun Peng, Jun YanŁetter, Zhiqing Guo, Junyang Chen, Xiao Lan, Zhongjie Ba, Yunfeng DiaoŁetter  

**一句话要点**：提出基于频率的黑盒攻击方法FBA²D，以解决AI生成图像检测器的决策型攻击问题。

**关键词**：AI生成图像检测, 黑盒攻击, 频率域攻击, 决策型攻击, 对抗样本

## 3 点简述
- 核心问题：AI生成内容检测器在真实黑盒场景下易受决策型攻击，现有研究多假设模型信息已知。
- 方法要点：利用离散余弦变换进行频域划分，选择频带作为查询子空间，结合对抗样本汤方法加速攻击。
- 实验或效果：在Synthetic LSUN和GenImage数据集上验证了方法的有效性，提升了查询效率和图像质量。

## 摘要（原文）

> The prosperous development of Artificial Intelligence-Generated Content (AIGC) has brought people's anxiety about the spread of false information on social media. Designing detectors for filtering is an effective defense method, but most detectors will be compromised by adversarial samples. Currently, most studies exposing AIGC security issues assume information on model structure and data distribution. In real applications, attackers query and interfere with models that provide services in the form of application programming interfaces (APIs), which constitutes the black-box decision-based attack paradigm. However, to the best of our knowledge, decision-based attacks on AIGC detectors remain unexplored. In this study, we propose \textbf{FBA$^2$D}: a frequency-based black-box attack method for AIGC detection to fill the research gap. Motivated by frequency-domain discrepancies between generated and real images, we develop a decision-based attack that leverages the Discrete Cosine Transform (DCT) for fine-grained spectral partitioning and selects frequency bands as query subspaces, improving both query efficiency and image quality. Moreover, attacks on AIGC detectors should mitigate initialization failures, preserve image quality, and operate under strict query budgets. To address these issues, we adopt an ``adversarial example soup'' method, averaging candidates from successive surrogate iterations and using the result as the initialization to accelerate the query-based attack. The empirical study on the Synthetic LSUN dataset and GenImage dataset demonstrate the effectiveness of our prosed method. This study shows the urgency of addressing practical AIGC security problems.

