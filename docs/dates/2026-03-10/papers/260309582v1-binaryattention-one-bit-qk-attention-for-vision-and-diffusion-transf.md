---
layout: default
title: BinaryAttention: One-Bit QK-Attention for Vision and Diffusion Transformers
---

# BinaryAttention: One-Bit QK-Attention for Vision and Diffusion Transformers
**arXiv**：[2603.09582v1](https://arxiv.org/abs/2603.09582) · [PDF](https://arxiv.org/pdf/2603.09582.pdf)  
**作者**：Chaodong Xiao, Zhengqiang Zhang, Lei Zhang  

**一句话要点**：提出BinaryAttention，一种1位QK注意力方法，以加速视觉和扩散Transformer的计算。

**关键词**：注意力二值化, 位运算加速, 量化感知训练, 视觉Transformer, 扩散Transformer, 低比特计算

## 3 点简述
- 核心问题：Transformer注意力模块的计算复杂度高，是视觉任务的主要瓶颈。
- 方法要点：通过二值化查询和键，仅保留符号并用位运算替代浮点点积，结合可学习偏置和量化感知训练减少信息损失。
- 实验或效果：在A100 GPU上比FlashAttention2快2倍以上，在视觉和扩散Transformer基准测试中匹配或超越全精度注意力。

## 摘要（原文）

> Transformers have achieved widespread and remarkable success, while the computational complexity of their attention modules remains a major bottleneck for vision tasks. Existing methods mainly employ 8-bit or 4-bit quantization to balance efficiency and accuracy. In this paper, with theoretical justification, we indicate that binarization of attention preserves the essential similarity relationships, and propose BinaryAttention, an effective method for fast and accurate 1-bit qk-attention. Specifically, we retain only the sign of queries and keys in computing the attention, and replace the floating dot products with bit-wise operations, significantly reducing the computational cost. We mitigate the inherent information loss under 1-bit quantization by incorporating a learnable bias, and enable end-to-end acceleration. To maintain the accuracy of attention, we adopt quantization-aware training and self-distillation techniques, mitigating quantization errors while ensuring sign-aligned similarity. BinaryAttention is more than 2x faster than FlashAttention2 on A100 GPUs. Extensive experiments on vision transformer and diffusion transformer benchmarks demonstrate that BinaryAttention matches or even exceeds full-precision attention, validating its effectiveness. Our work provides a highly efficient and effective alternative to full-precision attention, pushing the frontier of low-bit vision and diffusion transformers. The codes and models can be found at https://github.com/EdwardChasel/BinaryAttention.

