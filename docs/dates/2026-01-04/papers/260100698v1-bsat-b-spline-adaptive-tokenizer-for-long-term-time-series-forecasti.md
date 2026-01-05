---
layout: default
title: BSAT: B-Spline Adaptive Tokenizer for Long-Term Time Series Forecasting
---

# BSAT: B-Spline Adaptive Tokenizer for Long-Term Time Series Forecasting
**arXiv**：[2601.00698v1](https://arxiv.org/abs/2601.00698) · [PDF](https://arxiv.org/pdf/2601.00698.pdf)  
**作者**：Maximilian Reinwardt, Michael Eichelbeck, Matthias Althoff  

**一句话要点**：提出BSAT自适应分词器以解决长时序预测中注意力复杂度高和均匀分块不匹配的问题。

**关键词**：长时序预测, 自适应分词, B样条拟合, 混合位置编码, Transformer优化, 内存高效模型

## 3 点简述
- 核心问题：Transformer在长时序预测中面临自注意力二次复杂度和均匀分块与数据语义结构不匹配的挑战。
- 方法要点：BSAT通过B样条拟合自适应分割时序，在高曲率区域放置令牌，并采用混合位置编码L-RoPE。
- 实验或效果：在多个公开基准测试中表现竞争性，高压缩率下性能强，适合内存受限场景。

## 摘要（原文）

> Long-term time series forecasting using transformers is hampered by the quadratic complexity of self-attention and the rigidity of uniform patching, which may be misaligned with the data's semantic structure. In this paper, we introduce the \textit{B-Spline Adaptive Tokenizer (BSAT)}, a novel, parameter-free method that adaptively segments a time series by fitting it with B-splines. BSAT algorithmically places tokens in high-curvature regions and represents each variable-length basis function as a fixed-size token, composed of its coefficient and position. Further, we propose a hybrid positional encoding that combines a additive learnable positional encoding with Rotary Positional Embedding featuring a layer-wise learnable base: L-RoPE. This allows each layer to attend to different temporal dependencies. Our experiments on several public benchmarks show that our model is competitive with strong performance at high compression rates. This makes it particularly well-suited for use cases with strong memory constraints.

