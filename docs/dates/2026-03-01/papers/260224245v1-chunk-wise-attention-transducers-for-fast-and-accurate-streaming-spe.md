---
layout: default
title: Chunk-wise Attention Transducers for Fast and Accurate Streaming Speech-to-Text
---

# Chunk-wise Attention Transducers for Fast and Accurate Streaming Speech-to-Text
**arXiv**：[2602.24245v1](https://arxiv.org/abs/2602.24245) · [PDF](https://arxiv.org/pdf/2602.24245.pdf)  
**作者**：Hainan Xu, Vladimir Bataev, Travis M. Bartley, Jagadeesh Balam  

**一句话要点**：提出CHAT模型以提升流式语音识别的效率与准确性

**关键词**：流式语音识别, 注意力机制, RNN-T模型, 语音翻译, 效率优化

## 3 点简述
- 核心问题：RNN-T模型在流式语音处理中效率低且对齐严格，影响翻译性能。
- 方法要点：引入分块注意力机制，在固定音频块内使用交叉注意力，保持流式能力并增强局部对齐建模。
- 实验或效果：显著减少训练内存和加速推理，在语音识别和翻译任务中提升准确率。

## 摘要（原文）

> We propose Chunk-wise Attention Transducer (CHAT), a novel extension to RNN-T models that processes audio in fixed-size chunks while employing cross-attention within each chunk. This hybrid approach maintains RNN-T's streaming capability while introducing controlled flexibility for local alignment modeling. CHAT significantly reduces the temporal dimension that RNN-T must handle, yielding substantial efficiency improvements: up to 46.2% reduction in peak training memory, up to 1.36X faster training, and up to 1.69X faster inference. Alongside these efficiency gains, CHAT achieves consistent accuracy improvements over RNN-T across multiple languages and tasks -- up to 6.3% relative WER reduction for speech recognition and up to 18.0% BLEU improvement for speech translation. The method proves particularly effective for speech translation, where RNN-T's strict monotonic alignment hurts performance. Our results demonstrate that the CHAT model offers a practical solution for deploying more capable streaming speech models without sacrificing real-time constraints.

