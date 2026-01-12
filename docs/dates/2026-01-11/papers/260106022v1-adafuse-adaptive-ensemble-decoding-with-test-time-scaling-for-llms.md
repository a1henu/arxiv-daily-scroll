---
layout: default
title: AdaFuse: Adaptive Ensemble Decoding with Test-Time Scaling for LLMs
---

# AdaFuse: Adaptive Ensemble Decoding with Test-Time Scaling for LLMs
**arXiv**：[2601.06022v1](https://arxiv.org/abs/2601.06022) · [PDF](https://arxiv.org/pdf/2601.06022.pdf)  
**作者**：Chengming Cui, Tianxin Wei, Ziyi Chen, Ruizhong Qiu, Zhichen Zeng, Zhining Liu, Xuying Ning, Duo Zhou, Jingrui He  

**一句话要点**：提出AdaFuse自适应集成解码框架，通过动态融合单元和测试时缩放提升LLM推理性能

**关键词**：大语言模型, 集成解码, 自适应融合, 测试时缩放, 不确定性估计, 推理优化

## 3 点简述
- 现有集成方法依赖固定融合粒度，缺乏生成中适应性和任务间灵活性
- AdaFuse基于不确定性准则动态选择融合单元，结合多样性感知缩放策略探索候选
- 在开放域问答、算术推理和机器翻译任务上平均相对提升6.88%，优于基线

## 摘要（原文）

> Large language models (LLMs) exhibit complementary strengths arising from differences in pretraining data, model architectures, and decoding behaviors. Inference-time ensembling provides a practical way to combine these capabilities without retraining. However, existing ensemble approaches suffer from fundamental limitations. Most rely on fixed fusion granularity, which lacks the flexibility required for mid-generation adaptation and fails to adapt to different generation characteristics across tasks. To address these challenges, we propose AdaFuse, an adaptive ensemble decoding framework that dynamically selects semantically appropriate fusion units during generation. Rather than committing to a fixed granularity, AdaFuse adjusts fusion behavior on the fly based on the decoding context, with words serving as basic building blocks for alignment. To be specific, we introduce an uncertainty-based criterion to decide whether to apply ensembling at each decoding step. Under confident decoding states, the model continues generation directly. In less certain states, AdaFuse invokes a diversity-aware scaling strategy to explore alternative candidate continuations and inform ensemble decisions. This design establishes a synergistic interaction between adaptive ensembling and test-time scaling, where ensemble decisions guide targeted exploration, and the resulting diversity in turn strengthens ensemble quality. Experiments on open-domain question answering, arithmetic reasoning, and machine translation demonstrate that AdaFuse consistently outperforms strong ensemble baselines, achieving an average relative improvement of 6.88%. The code is available at https://github.com/CCM0111/AdaFuse.

