---
layout: default
title: Entropy-Guided k-Guard Sampling for Long-Horizon Autoregressive Video Generation
---

# Entropy-Guided k-Guard Sampling for Long-Horizon Autoregressive Video Generation
**arXiv**：[2601.19488v1](https://arxiv.org/abs/2601.19488) · [PDF](https://arxiv.org/pdf/2601.19488.pdf)  
**作者**：Yizhao Han, Tianxing Shi, Zhao Wang, Zifan Xu, Zhiyuan Pu, Mingxiao Li, Qian Zhang, Wei Yin, Xiao-Xiao Long  

**一句话要点**：提出熵引导k保护采样以解决长序列自回归视频生成中的误差累积问题

**关键词**：自回归视频生成, 采样策略, 熵引导, 长序列生成, 误差累积

## 3 点简述
- 核心问题：视频令牌语义密度低且冗余高，静态采样策略在长序列生成中易导致误差累积
- 方法要点：基于预测分布熵自适应调整候选令牌数量，低熵区减少候选以抑制噪声，高熵区增加候选以缓解误差
- 实验或效果：模型无关、无需训练，实验显示在感知质量和结构稳定性上优于静态策略

## 摘要（原文）

> Autoregressive (AR) architectures have achieved significant successes in LLMs, inspiring explorations for video generation. In LLMs, top-p/top-k sampling strategies work exceptionally well: language tokens have high semantic density and low redundancy, so a fixed size of token candidates already strikes a balance between semantic accuracy and generation diversity. In contrast, video tokens have low semantic density and high spatio-temporal redundancy. This mismatch makes static top-k/top-p strategies ineffective for video decoders: they either introduce unnecessary randomness for low-uncertainty regions (static backgrounds) or get stuck in early errors for high-uncertainty regions (foreground objects). Prediction errors will accumulate as more frames are generated and eventually severely degrade long-horizon quality. To address this, we propose Entropy-Guided k-Guard (ENkG) sampling, a simple yet effective strategy that adapts sampling to token-wise dispersion, quantified by the entropy of each token's predicted distribution. ENkG uses adaptive token candidate sizes: for low-entropy regions, it employs fewer candidates to suppress redundant noise and preserve structural integrity; for high-entropy regions, it uses more candidates to mitigate error compounding. ENkG is model-agnostic, training-free, and adds negligible overhead. Experiments demonstrate consistent improvements in perceptual quality and structural stability compared to static top-k/top-p strategies.

