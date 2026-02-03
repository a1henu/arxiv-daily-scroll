---
layout: default
title: Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation
---

# Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation
**arXiv**：[2602.02214v1](https://arxiv.org/abs/2602.02214) · [PDF](https://arxiv.org/pdf/2602.02214.pdf)  
**作者**：Hongzhou Zhu, Min Zhao, Guande He, Hang Su, Chongxuan Li, Jun Zhu  

**一句话要点**：提出Causal Forcing方法，通过自回归教师模型解决实时交互视频生成中的架构差距问题。

**关键词**：实时视频生成, 自回归模型, 扩散模型蒸馏, 因果注意力, ODE初始化, 交互式生成

## 3 点简述
- 核心问题：现有方法从双向视频扩散模型蒸馏到自回归模型时，存在架构差距，导致性能下降。
- 方法要点：使用自回归教师模型进行ODE初始化，确保帧级单射性，从而恢复教师流图。
- 实验或效果：在Dynamic Degree、VisionReward和Instruction Following指标上超越基线，提升显著。

## 摘要（原文）

> To achieve real-time interactive video generation, current methods distill pretrained bidirectional video diffusion models into few-step autoregressive (AR) models, facing an architectural gap when full attention is replaced by causal attention. However, existing approaches do not bridge this gap theoretically. They initialize the AR student via ODE distillation, which requires frame-level injectivity, where each noisy frame must map to a unique clean frame under the PF-ODE of an AR teacher. Distilling an AR student from a bidirectional teacher violates this condition, preventing recovery of the teacher's flow map and instead inducing a conditional-expectation solution, which degrades performance. To address this issue, we propose Causal Forcing that uses an AR teacher for ODE initialization, thereby bridging the architectural gap. Empirical results show that our method outperforms all baselines across all metrics, surpassing the SOTA Self Forcing by 19.3\% in Dynamic Degree, 8.7\% in VisionReward, and 16.7\% in Instruction Following. Project page and the code: \href{https://thu-ml.github.io/CausalForcing.github.io/}{https://thu-ml.github.io/CausalForcing.github.io/}

