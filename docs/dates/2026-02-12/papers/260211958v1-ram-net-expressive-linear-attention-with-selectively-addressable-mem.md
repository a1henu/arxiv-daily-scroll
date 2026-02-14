---
layout: default
title: RAM-Net: Expressive Linear Attention with Selectively Addressable Memory
---

# RAM-Net: Expressive Linear Attention with Selectively Addressable Memory
**arXiv**：[2602.11958v1](https://arxiv.org/abs/2602.11958) · [PDF](https://arxiv.org/pdf/2602.11958.pdf)  
**作者**：Kaicheng Xiao, Haotian Li, Liran Dong, Guoliang Xing  

**一句话要点**：提出RAM-Net以解决线性注意力中固定大小内存限制表达力的问题

**关键词**：线性注意力, 内存网络, 稀疏表示, 长程依赖, 计算效率, 检索任务

## 3 点简述
- 线性注意力压缩历史到固定内存导致信息损失和表达力受限
- 核心方法：将输入映射为高维稀疏向量作为地址，选择性访问大规模内存状态
- 实验显示在细粒度长程检索任务中超越基线，并在语言建模和常识推理中表现竞争性

## 摘要（原文）

> While linear attention architectures offer efficient inference, compressing unbounded history into a fixed-size memory inherently limits expressivity and causes information loss. To address this limitation, we introduce Random Access Memory Network (RAM-Net), a novel architecture designed to bridge the gap between the representational capacity of full attention and the memory efficiency of linear models. The core of RAM-Net maps inputs to high-dimensional sparse vectors serving as explicit addresses, allowing the model to selectively access a massive memory state. This design enables exponential state size scaling without additional parameters, which significantly mitigates signal interference and enhances retrieval fidelity. Moreover, the inherent sparsity ensures exceptional computational efficiency, as state updates are confined to minimal entries. Extensive experiments demonstrate that RAM-Net consistently surpasses state-of-the-art baselines in fine-grained long-range retrieval tasks and achieves competitive performance in standard language modeling and zero-shot commonsense reasoning benchmarks, validating its superior capability to capture complex dependencies with significantly reduced computational overhead.

