---
layout: default
title: Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment
---

# Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment
**arXiv**：[2511.04555v1](https://arxiv.org/abs/2511.04555) · [PDF](https://arxiv.org/pdf/2511.04555.pdf)  
**作者**：Tao Lin, Yilei Zhong, Yuxin Du, Jingjing Zhang, Jiting Liu, Yinxinyu Chen, Encheng Gu, Ziyan Liu, Hongyi Cai, Yanwen Zou, Lixing Zou, Zhaoye Zhou, Gen Li, Bo Zhao  

**一句话要点**：提出轻量级视觉-语言-动作模型Evo-1，以解决计算成本高和泛化差的问题。

**关键词**：视觉-语言-动作模型, 轻量级架构, 跨调制扩散, 两阶段训练, 语义对齐, 机器人控制

## 3 点简述
- 当前VLA模型参数庞大、依赖机器人数据预训练，导致计算成本高和部署困难。
- Evo-1采用跨调制扩散变换器和优化集成模块，通过两阶段训练保持语义对齐。
- 在多个基准测试中实现SOTA，真实世界评估成功率达78%，推理高效。

## 摘要（原文）

> Vision-Language-Action (VLA) models have emerged as a powerful framework that
> unifies perception, language, and control, enabling robots to perform diverse
> tasks through multimodal understanding. However, current VLA models typically
> contain massive parameters and rely heavily on large-scale robot data
> pretraining, leading to high computational costs during training, as well as
> limited deployability for real-time inference. Moreover, most training
> paradigms often degrade the perceptual representations of the vision-language
> backbone, resulting in overfitting and poor generalization to downstream tasks.
> In this work, we present Evo-1, a lightweight VLA model that reduces
> computation and improves deployment efficiency, while maintaining strong
> performance without pretraining on robot data. Evo-1 builds on a native
> multimodal Vision-Language model (VLM), incorporating a novel cross-modulated
> diffusion transformer along with an optimized integration module, together
> forming an effective architecture. We further introduce a two-stage training
> paradigm that progressively aligns action with perception, preserving the
> representations of the VLM. Notably, with only 0.77 billion parameters, Evo-1
> achieves state-of-the-art results on the Meta-World and RoboTwin suite,
> surpassing the previous best models by 12.4% and 6.9%, respectively, and also
> attains a competitive result of 94.8% on LIBERO. In real-world evaluations,
> Evo-1 attains a 78% success rate with high inference frequency and low memory
> overhead, outperforming all baseline methods. We release code, data, and model
> weights to facilitate future research on lightweight and efficient VLA models.

