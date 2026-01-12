---
layout: default
title: Overcoming Joint Intractability with Lossless Hierarchical Speculative Decoding
---

# Overcoming Joint Intractability with Lossless Hierarchical Speculative Decoding
**arXiv**：[2601.05724v1](https://arxiv.org/abs/2601.05724) · [PDF](https://arxiv.org/pdf/2601.05724.pdf)  
**作者**：Yuxuan Zhou, Fei Huang, Heng Li, Fengyi Wu, Tianyu Wang, Jianwei Zhang, Junyang Lin, Zhi-Qi Cheng  

**一句话要点**：提出分层推测解码以解决推测解码中联合难处理性问题，提升推理速度与分布保真度。

**关键词**：推测解码, 无损验证, 推理加速, 分布保真度, 分层方法, 联合难处理性

## 3 点简述
- 核心问题：推测解码中验证是瓶颈，现有方法因联合难处理性而受限，影响接受令牌数与分布保真度。
- 方法要点：引入分层推测解码，通过平衡可访问分支的概率质量，实现无损验证，克服联合难处理性。
- 实验或效果：大规模实验显示，在多种模型和基准上提升接受率，集成到EAGLE-3中性能增益超12%，保持分布保真度。

## 摘要（原文）

> Verification is a key bottleneck in improving inference speed while maintaining distribution fidelity in Speculative Decoding. Recent work has shown that sequence-level verification leads to a higher number of accepted tokens compared to token-wise verification. However, existing solutions often rely on surrogate approximations or are constrained by partial information, struggling with joint intractability. In this work, we propose Hierarchical Speculative Decoding (HSD), a provably lossless verification method that significantly boosts the expected number of accepted tokens and overcomes joint intractability by balancing excess and deficient probability mass across accessible branches. Our extensive large-scale experiments demonstrate that HSD yields consistent improvements in acceptance rates across diverse model families and benchmarks. Moreover, its strong explainability and generality make it readily integrable into a wide range of speculative decoding frameworks. Notably, integrating HSD into EAGLE-3 yields over a 12% performance gain, establishing state-of-the-art decoding efficiency without compromising distribution fidelity. Code is available at https://github.com/ZhouYuxuanYX/Hierarchical-Speculative-Decoding.

