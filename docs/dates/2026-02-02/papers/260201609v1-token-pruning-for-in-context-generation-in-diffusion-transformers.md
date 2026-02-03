---
layout: default
title: Token Pruning for In-Context Generation in Diffusion Transformers
---

# Token Pruning for In-Context Generation in Diffusion Transformers
**arXiv**：[2602.01609v1](https://arxiv.org/abs/2602.01609) · [PDF](https://arxiv.org/pdf/2602.01609.pdf)  
**作者**：Junqing Lin, Xingyu Zheng, Pei Cheng, Bin Fu, Jingwei Sun, Guangzhong Sun  

**一句话要点**：提出ToPi训练无关的令牌剪枝框架，以解决扩散变换器中上下文生成的计算瓶颈问题。

**关键词**：扩散变换器, 上下文生成, 令牌剪枝, 计算效率, 图像到图像生成, 训练无关优化

## 3 点简述
- 核心问题：上下文生成导致序列长度剧增，现有令牌减少技术因忽略参考与目标令牌的角色不对称性而失效。
- 方法要点：通过离线校准驱动敏感性分析识别关键注意力层，并基于新影响度量与时间更新策略进行选择性剪枝。
- 实验或效果：在复杂图像生成任务中，实现超过30%的推理加速，同时保持结构保真度和视觉一致性。

## 摘要（原文）

> In-context generation significantly enhances Diffusion Transformers (DiTs) by enabling controllable image-to-image generation through reference examples. However, the resulting input concatenation drastically increases sequence length, creating a substantial computational bottleneck. Existing token reduction techniques, primarily tailored for text-to-image synthesis, fall short in this paradigm as they apply uniform reduction strategies, overlooking the inherent role asymmetry between reference contexts and target latents across spatial, temporal, and functional dimensions. To bridge this gap, we introduce ToPi, a training-free token pruning framework tailored for in-context generation in DiTs. Specifically, ToPi utilizes offline calibration-driven sensitivity analysis to identify pivotal attention layers, serving as a robust proxy for redundancy estimation. Leveraging these layers, we derive a novel influence metric to quantify the contribution of each context token for selective pruning, coupled with a temporal update strategy that adapts to the evolving diffusion trajectory. Empirical evaluations demonstrate that ToPi can achieve over 30\% speedup in inference while maintaining structural fidelity and visual consistency across complex image generation tasks.

