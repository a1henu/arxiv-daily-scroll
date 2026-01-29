---
layout: default
title: Efficient Autoregressive Video Diffusion with Dummy Head
---

# Efficient Autoregressive Video Diffusion with Dummy Head
**arXiv**：[2601.20499v1](https://arxiv.org/abs/2601.20499) · [PDF](https://arxiv.org/pdf/2601.20499.pdf)  
**作者**：Hang Guo, Zhaoyang Jia, Jiahao Li, Bin Li, Yuanhao Cai, Jiangshan Wang, Yawei Li, Yan Lu  

**一句话要点**：提出Dummy Forcing方法以提升自回归视频扩散模型的推理效率

**关键词**：自回归视频扩散, 多头自注意力, 缓存压缩, 推理加速, 视频生成

## 3 点简述
- 发现多头自注意力中约25%的头部几乎仅关注当前帧，导致历史帧利用不足
- 通过异构内存分配和动态头部编程控制上下文访问，减少冗余并压缩缓存
- 无需额外训练，实现最高2.0倍加速，视频生成达24.3 FPS且质量下降小于0.5%

## 摘要（原文）

> The autoregressive video diffusion model has recently gained considerable research interest due to its causal modeling and iterative denoising. In this work, we identify that the multi-head self-attention in these models under-utilizes historical frames: approximately 25% heads attend almost exclusively to the current frame, and discarding their KV caches incurs only minor performance degradation. Building upon this, we propose Dummy Forcing, a simple yet effective method to control context accessibility across different heads. Specifically, the proposed heterogeneous memory allocation reduces head-wise context redundancy, accompanied by dynamic head programming to adaptively classify head types. Moreover, we develop a context packing technique to achieve more aggressive cache compression. Without additional training, our Dummy Forcing delivers up to 2.0x speedup over the baseline, supporting video generation at 24.3 FPS with less than 0.5% quality drop. Project page is available at https://csguoh.github.io/project/DummyForcing/.

