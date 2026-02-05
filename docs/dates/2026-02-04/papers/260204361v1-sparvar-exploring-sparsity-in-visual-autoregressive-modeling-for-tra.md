---
layout: default
title: SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration
---

# SparVAR: Exploring Sparsity in Visual AutoRegressive Modeling for Training-Free Acceleration
**arXiv**：[2602.04361v1](https://arxiv.org/abs/2602.04361) · [PDF](https://arxiv.org/pdf/2602.04361.pdf)  
**作者**：Zekun Li, Ning Wang, Tongxin Bai, Changwang Mei, Peisong Wang, Shuang Qiu, Jian Cheng  

**一句话要点**：提出SparVAR框架，利用VAR注意力稀疏性实现免训练加速，保持高分辨率图像生成质量。

**关键词**：视觉自回归建模, 稀疏注意力, 免训练加速, 高分辨率图像生成, 计算效率优化

## 3 点简述
- 核心问题：VAR建模中注意力计算复杂度随分辨率四次方增长，导致高延迟，现有加速方法常跳过高分辨率尺度损害图像细节。
- 方法要点：基于VAR注意力的强注意力汇、跨尺度激活相似性和局部性，动态预测稀疏注意力模式，实现高效稀疏计算。
- 实验或效果：在8B模型生成1024×1024图像时，将时间降至1秒，相比FlashAttention加速1.57倍，结合尺度跳过策略可达2.28倍加速，保持视觉质量。

## 摘要（原文）

> Visual AutoRegressive (VAR) modeling has garnered significant attention for its innovative next-scale prediction paradigm. However, mainstream VAR paradigms attend to all tokens across historical scales at each autoregressive step. As the next scale resolution grows, the computational complexity of attention increases quartically with resolution, causing substantial latency. Prior accelerations often skip high-resolution scales, which speeds up inference but discards high-frequency details and harms image quality. To address these problems, we present SparVAR, a training-free acceleration framework that exploits three properties of VAR attention: (i) strong attention sinks, (ii) cross-scale activation similarity, and (iii) pronounced locality. Specifically, we dynamically predict the sparse attention pattern of later high-resolution scales from a sparse decision scale, and construct scale self-similar sparse attention via an efficient index-mapping mechanism, enabling high-efficiency sparse attention computation at large scales. Furthermore, we propose cross-scale local sparse attention and implement an efficient block-wise sparse kernel, which achieves $\mathbf{> 5\times}$ faster forward speed than FlashAttention. Extensive experiments demonstrate that the proposed SparseVAR can reduce the generation time of an 8B model producing $1024\times1024$ high-resolution images to the 1s, without skipping the last scales. Compared with the VAR baseline accelerated by FlashAttention, our method achieves a $\mathbf{1.57\times}$ speed-up while preserving almost all high-frequency details. When combined with existing scale-skipping strategies, SparseVAR attains up to a $\mathbf{2.28\times}$ acceleration, while maintaining competitive visual generation quality. Code is available at https://github.com/CAS-CLab/SparVAR.

