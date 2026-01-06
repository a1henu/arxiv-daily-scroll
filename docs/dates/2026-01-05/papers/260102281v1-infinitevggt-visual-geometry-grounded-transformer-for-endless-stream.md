---
layout: default
title: InfiniteVGGT: Visual Geometry Grounded Transformer for Endless Streams
---

# InfiniteVGGT: Visual Geometry Grounded Transformer for Endless Streams
**arXiv**：[2601.02281v1](https://arxiv.org/abs/2601.02281) · [PDF](https://arxiv.org/pdf/2601.02281.pdf)  
**作者**：Shuai Yuan, Yantai Yang, Xiaotian Yang, Xupeng Zhang, Zhonghao Zhao, Lingming Zhang, Zhipeng Zhang  

**一句话要点**：提出InfiniteVGGT以解决无限长视频流中3D几何理解的长期稳定性问题

**关键词**：无限长视频流, 3D几何理解, 因果变换器, 滚动记忆, KV缓存, Long3D基准

## 3 点简述
- 核心问题：现有流式方法无法处理无限长输入或长期序列中易发生灾难性漂移
- 方法要点：采用因果视觉几何变换器，通过有界自适应KV缓存和免训练剪枝策略实现滚动记忆
- 实验或效果：在Long3D基准测试中优于现有流式方法，支持约10,000帧的连续3D几何估计评估

## 摘要（原文）

> The grand vision of enabling persistent, large-scale 3D visual geometry understanding is shackled by the irreconcilable demands of scalability and long-term stability. While offline models like VGGT achieve inspiring geometry capability, their batch-based nature renders them irrelevant for live systems. Streaming architectures, though the intended solution for live operation, have proven inadequate. Existing methods either fail to support truly infinite-horizon inputs or suffer from catastrophic drift over long sequences. We shatter this long-standing dilemma with InfiniteVGGT, a causal visual geometry transformer that operationalizes the concept of a rolling memory through a bounded yet adaptive and perpetually expressive KV cache. Capitalizing on this, we devise a training-free, attention-agnostic pruning strategy that intelligently discards obsolete information, effectively ``rolling'' the memory forward with each new frame. Fully compatible with FlashAttention, InfiniteVGGT finally alleviates the compromise, enabling infinite-horizon streaming while outperforming existing streaming methods in long-term stability. The ultimate test for such a system is its performance over a truly infinite horizon, a capability that has been impossible to rigorously validate due to the lack of extremely long-term, continuous benchmarks. To address this critical gap, we introduce the Long3D benchmark, which, for the first time, enables a rigorous evaluation of continuous 3D geometry estimation on sequences about 10,000 frames. This provides the definitive evaluation platform for future research in long-term 3D geometry understanding. Code is available at: https://github.com/AutoLab-SAI-SJTU/InfiniteVGGT

