---
layout: default
title: FlattenGPT: Depth Compression for Transformer with Layer Flattening
---

# FlattenGPT: Depth Compression for Transformer with Layer Flattening
**arXiv**：[2602.08858v1](https://arxiv.org/abs/2602.08858) · [PDF](https://arxiv.org/pdf/2602.08858.pdf)  
**作者**：Ruihan Xu, Qingpei Guo, Yao Zhu, Xiangyang Ji, Ming Yang, Shiliang Zhang  

**一句话要点**：提出FlattenGPT，通过层扁平化压缩Transformer深度以提升效率与性能平衡。

**关键词**：Transformer压缩, 深度剪枝, 层扁平化, 模型加速, 零样本性能

## 3 点简述
- 核心问题：现有深度压缩方法因整块剪枝丢弃关键信息，导致性能显著下降。
- 方法要点：扁平化相邻块以压缩深度，同时检测并移除参数冗余，保留所有块知识。
- 实验或效果：在LLaMA-2/3和Qwen-1.5等模型上，压缩20%时保持90-96%零样本性能，加速推理。

## 摘要（原文）

> Recent works have indicated redundancy across transformer blocks, prompting the research of depth compression to prune less crucial blocks. However, current ways of entire-block pruning suffer from risks of discarding meaningful cues learned in those blocks, leading to substantial performance degradation. As another line of model compression, channel pruning can better preserve performance, while it cannot reduce model depth and is challenged by inconsistent pruning ratios for individual layers. To pursue better model compression and acceleration, this paper proposes \textbf{FlattenGPT}, a novel way to detect and reduce depth-wise redundancies. By flatting two adjacent blocks into one, it compresses the network depth, meanwhile enables more effective parameter redundancy detection and removal. FlattenGPT allows to preserve the knowledge learned in all blocks, and remains consistent with the original transformer architecture. Extensive experiments demonstrate that FlattenGPT enhances model efficiency with a decent trade-off to performance. It outperforms existing pruning methods in both zero-shot accuracies and WikiText-2 perplexity across various model types and parameter sizes. On LLaMA-2/3 and Qwen-1.5 models, FlattenGPT retains 90-96\% of zero-shot performance with a compression ratio of 20\%. It also outperforms other pruning methods in accelerating LLM inference, making it promising for enhancing the efficiency of transformers.

