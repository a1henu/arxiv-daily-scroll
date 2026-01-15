---
layout: default
title: Parallelizable memory recurrent units
---

# Parallelizable memory recurrent units
**arXiv**：[2601.09495v1](https://arxiv.org/abs/2601.09495) · [PDF](https://arxiv.org/pdf/2601.09495.pdf)  
**作者**：Florent De Geeter, Gaspard Lambrechts, Damien Ernst, Guillaume Drion  

**一句话要点**：提出记忆循环单元以结合非线性RNN的持久记忆与状态空间模型的并行计算能力

**关键词**：循环神经网络, 并行计算, 持久记忆, 状态空间模型, 长序列处理

## 3 点简述
- 核心问题：状态空间模型因单稳态性缺乏持久记忆能力，而Transformer在序列生成时效率低
- 方法要点：引入多稳态性实现持久记忆，消除瞬态动力学以支持并行扫描算法
- 实验或效果：BMRU在长依赖任务中表现良好，可与状态空间模型结合构建混合网络

## 摘要（原文）

> With the emergence of massively parallel processing units, parallelization has become a desirable property for new sequence models. The ability to parallelize the processing of sequences with respect to the sequence length during training is one of the main factors behind the uprising of the Transformer architecture. However, Transformers lack efficiency at sequence generation, as they need to reprocess all past timesteps at every generation step. Recently, state-space models (SSMs) emerged as a more efficient alternative. These new kinds of recurrent neural networks (RNNs) keep the efficient update of the RNNs while gaining parallelization by getting rid of nonlinear dynamics (or recurrence). SSMs can reach state-of-the art performance through the efficient training of potentially very large networks, but still suffer from limited representation capabilities. In particular, SSMs cannot exhibit persistent memory, or the capacity of retaining information for an infinite duration, because of their monostability. In this paper, we introduce a new family of RNNs, the memory recurrent units (MRUs), that combine the persistent memory capabilities of nonlinear RNNs with the parallelizable computations of SSMs. These units leverage multistability as a source of persistent memory, while getting rid of transient dynamics for efficient computations. We then derive a specific implementation as proof-of-concept: the bistable memory recurrent unit (BMRU). This new RNN is compatible with the parallel scan algorithm. We show that BMRU achieves good results in tasks with long-term dependencies, and can be combined with state-space models to create hybrid networks that are parallelizable and have transient dynamics as well as persistent memory.

