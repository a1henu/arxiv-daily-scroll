---
layout: default
title: When Less is More: The LLM Scaling Paradox in Context Compression
---

# When Less is More: The LLM Scaling Paradox in Context Compression
**arXiv**：[2602.09789v1](https://arxiv.org/abs/2602.09789) · [PDF](https://arxiv.org/pdf/2602.09789.pdf)  
**作者**：Ruishan Guo, Yibing Liu, Guoxin Ma, Yan Wang, Yueyang Zhang, Long Xia, Kecheng Chen, Zhiyuan Sun, Daiting Shi  

**一句话要点**：提出LLM缩放悖论，揭示在上下文压缩中增大模型尺寸会降低重建忠实度

**关键词**：上下文压缩, LLM缩放悖论, 知识覆盖, 语义漂移, 生成忠实度, 模型缩放

## 3 点简述
- 核心问题：在压缩器-解码器设置中，增大压缩器模型尺寸导致重建上下文忠实度下降，形成尺寸-忠实度悖论
- 方法要点：通过实验分析，悖论源于知识覆盖和语义漂移，与模型参数数量无关，而是语义容量和生成不确定性增加所致
- 实验或效果：在0.6B到90B模型上验证，显示缩放定律在开放生成忠实保存中失效，补充上下文压缩评估

## 摘要（原文）

> Scaling up model parameters has long been a prevalent training paradigm driven by the assumption that larger models yield superior generation capabilities. However, under lossy context compression in a compressor-decoder setup, we observe a Size-Fidelity Paradox: increasing the compressor size can lessen the faithfulness of reconstructed contexts though training loss decreases. Through extensive experiments across models from 0.6B to 90B, we coin this paradox arising from two dominant factors: 1) knowledge overwriting: larger models increasingly replace source facts with their own prior beliefs, e.g., ``the white strawberry'' $\to$ ``the red strawberry''; and 2) semantic drift: larger models tend to paraphrase or restructure content instead of reproducing it verbatim, e.g., ``Alice hit Bob'' $\to$ ``Bob hit Alice''. By holding model size fixed, we reflect on the emergent properties of compressed context representations. We show that the culprit is not parameter count itself, but the excessive semantic capacity and amplified generative uncertainty that accompany scaling. Specifically, the increased rank of context embeddings facilitates prior knowledge intrusion, whereas higher entropy over token prediction distributions promotes rewriting. Our results complement existing evaluations over context compression paradigm, underpinning a breakdown in scaling laws for faithful preservation in open-ended generation.

