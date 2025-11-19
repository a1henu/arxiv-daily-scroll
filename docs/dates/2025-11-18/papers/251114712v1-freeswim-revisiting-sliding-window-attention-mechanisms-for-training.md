---
layout: default
title: FreeSwim: Revisiting Sliding-Window Attention Mechanisms for Training-Free Ultra-High-Resolution Video Generation
---

# FreeSwim: Revisiting Sliding-Window Attention Mechanisms for Training-Free Ultra-High-Resolution Video Generation
**arXiv**：[2511.14712v1](https://arxiv.org/abs/2511.14712) · [PDF](https://arxiv.org/pdf/2511.14712.pdf)  
**作者**：Yunfeng Wu, Jiayi Song, Zhenxiong Tan, Zihao He, Songhua Liu  

**一句话要点**：提出FreeSwim方法以训练免费生成超高分辨率视频，通过滑动窗口注意力机制解决计算复杂度问题。

**关键词**：超高分辨率视频生成, 滑动窗口注意力, 训练免费方法, 扩散Transformer, 交叉注意力机制, 视频合成

## 3 点简述
- 核心问题：Transformer注意力机制在超高分辨率视频生成中计算复杂度高，导致训练成本巨大。
- 方法要点：采用向内滑动窗口注意力与双路径管道，结合交叉注意力覆盖策略，确保局部细节与全局一致性。
- 实验或效果：在VBench上表现优异，生成视频细节丰富、效率高，无需额外训练。

## 摘要（原文）

> The quadratic time and memory complexity of the attention mechanism in modern Transformer based video generators makes end-to-end training for ultra high resolution videos prohibitively expensive. Motivated by this limitation, we introduce a training-free approach that leverages video Diffusion Transformers pretrained at their native scale to synthesize higher resolution videos without any additional training or adaptation. At the core of our method lies an inward sliding window attention mechanism, which originates from a key observation: maintaining each query token's training scale receptive field is crucial for preserving visual fidelity and detail. However, naive local window attention, unfortunately, often leads to repetitive content and exhibits a lack of global coherence in the generated results. To overcome this challenge, we devise a dual-path pipeline that backs up window attention with a novel cross-attention override strategy, enabling the semantic content produced by local attention to be guided by another branch with a full receptive field and, therefore, ensuring holistic consistency. Furthermore, to improve efficiency, we incorporate a cross-attention caching strategy for this branch to avoid the frequent computation of full 3D attention. Extensive experiments demonstrate that our method delivers ultra-high-resolution videos with fine-grained visual details and high efficiency in a training-free paradigm. Meanwhile, it achieves superior performance on VBench, even compared to training-based alternatives, with competitive or improved efficiency. Codes are available at: https://github.com/WillWu111/FreeSwim

