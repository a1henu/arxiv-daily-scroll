---
layout: default
title: Dissecting Outlier Dynamics in LLM NVFP4 Pretraining
---

# Dissecting Outlier Dynamics in LLM NVFP4 Pretraining
**arXiv**：[2602.02047v1](https://arxiv.org/abs/2602.02047) · [PDF](https://arxiv.org/pdf/2602.02047.pdf)  
**作者**：Peijie Dong, Ruibo Fan, Yuechen Tao, Di Mou, Wenhu Hu, Zhenheng Tang, Yinghao Yu, Jiamang Wang, Wenbo Su, Guodong Yang, Liping Zhang, Xiaowen Chu, Baochun Li, Bo Li  

**一句话要点**：提出Hot-Channel Patch在线补偿机制，结合CHON训练配方，减少NVFP4预训练中的损失差距。

**关键词**：低精度训练, 异常值分析, 量化补偿, 大语言模型, NVFP4预训练

## 3 点简述
- 核心问题：NVFP4量化在LLM预训练中因动态范围有限导致异常值敏感，造成与BF16的损失差距。
- 方法要点：通过纵向分析异常值动态，识别热通道，并开发HCP在线补偿和CHON训练配方。
- 实验或效果：在GLA-1.3B模型上，CHON将损失差距从0.94%降至0.58%，保持下游准确性。

## 摘要（原文）

> Training large language models using 4-bit arithmetic enhances throughput and memory efficiency. Yet, the limited dynamic range of FP4 increases sensitivity to outliers. While NVFP4 mitigates quantization error via hierarchical microscaling, a persistent loss gap remains compared to BF16. This study conducts a longitudinal analysis of outlier dynamics across architecture during NVFP4 pretraining, focusing on where they localize, why they occur, and how they evolve temporally. We find that, compared with Softmax Attention (SA), Linear Attention (LA) reduces per-tensor heavy tails but still exhibits persistent block-level spikes under block quantization. Our analysis attributes outliers to specific architectural components: Softmax in SA, gating in LA, and SwiGLU in FFN, with "post-QK" operations exhibiting higher sensitivity to quantization. Notably, outliers evolve from transient spikes early in training to a small set of persistent hot channels (i.e., channels with persistently large magnitudes) in later stages. Based on these findings, we introduce Hot-Channel Patch (HCP), an online compensation mechanism that identifies hot channels and reinjects residuals using hardware-efficient kernels. We then develop CHON, an NVFP4 training recipe integrating HCP with post-QK operation protection. On GLA-1.3B model trained for 60B tokens, CHON reduces the loss gap to BF16 from 0.94% to 0.58% while maintaining downstream accuracy.

