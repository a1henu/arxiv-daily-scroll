---
layout: default
title: When to Lock Attention: Training-Free KV Control in Video Diffusion
---

# When to Lock Attention: Training-Free KV Control in Video Diffusion
**arXiv**：[2603.09657v1](https://arxiv.org/abs/2603.09657) · [PDF](https://arxiv.org/pdf/2603.09657.pdf)  
**作者**：Tianyi Zeng, Jincheng Gao, Tianyi Wang, Zijie Meng, Miao Zhang, Jun Yin, Haoyuan Sun, Junfeng Jiao, Christian Claudel, Junbo Tan, Xueqian Wang  

**一句话要点**：提出KV-Lock框架以解决视频编辑中背景一致性与前景质量平衡的挑战

**关键词**：视频扩散模型, KV控制, 训练免调优, 背景一致性, 前景生成, 幻觉检测

## 3 点简述
- 核心问题：视频编辑中全图信息注入易致背景伪影，而严格背景锁定限制前景生成能力
- 方法要点：基于幻觉检测动态调度背景KV融合比和CFG尺度，无需训练即可集成到DiT模型
- 实验或效果：在多种视频编辑任务中，提升前景质量同时保持高背景保真度，优于现有方法

## 摘要（原文）

> Maintaining background consistency while enhancing foreground quality remains a core challenge in video editing. Injecting full-image information often leads to background artifacts, whereas rigid background locking severely constrains the model's capacity for foreground generation. To address this issue, we propose KV-Lock, a training-free framework tailored for DiT-based video diffusion models. Our core insight is that the hallucination metric (variance of denoising prediction) directly quantifies generation diversity, which is inherently linked to the classifier-free guidance (CFG) scale. Building upon this, KV-Lock leverages diffusion hallucination detection to dynamically schedule two key components: the fusion ratio between cached background key-values (KVs) and newly generated KVs, and the CFG scale. When hallucination risk is detected, KV-Lock strengthens background KV locking and simultaneously amplifies conditional guidance for foreground generation, thereby mitigating artifacts and improving generation fidelity. As a training-free, plug-and-play module, KV-Lock can be easily integrated into any pre-trained DiT-based models. Extensive experiments validate that our method outperforms existing approaches in improved foreground quality with high background fidelity across various video editing tasks.

