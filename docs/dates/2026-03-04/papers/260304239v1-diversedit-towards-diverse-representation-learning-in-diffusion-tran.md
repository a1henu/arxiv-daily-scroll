---
layout: default
title: DiverseDiT: Towards Diverse Representation Learning in Diffusion Transformers
---

# DiverseDiT: Towards Diverse Representation Learning in Diffusion Transformers
**arXiv**：[2603.04239v1](https://arxiv.org/abs/2603.04239) · [PDF](https://arxiv.org/pdf/2603.04239.pdf)  
**作者**：Mengping Yang, Zhiyu Tan, Binglei Li, Xiaomeng Yang, Hesen Chen, Hao Li  

**一句话要点**：提出DiverseDiT以增强扩散变换器中的表示多样性，提升视觉合成性能

**关键词**：扩散变换器, 表示学习, 多样性增强, 视觉合成, 残差连接

## 3 点简述
- 核心问题：扩散变换器内部表示学习机制不明确，影响表示捕获能力
- 方法要点：通过长残差连接和表示多样性损失，促进块间表示多样性
- 实验或效果：在ImageNet上验证性能提升和收敛加速，兼容现有技术

## 摘要（原文）

> Recent breakthroughs in Diffusion Transformers (DiTs) have revolutionized the field of visual synthesis due to their superior scalability. To facilitate DiTs' capability of capturing meaningful internal representations, recent works such as REPA incorporate external pretrained encoders for representation alignment. However, the underlying mechanisms governing representation learning within DiTs are not well understood. To this end, we first systematically investigate the representation dynamics of DiTs. Through analyzing the evolution and influence of internal representations under various settings, we reveal that representation diversity across blocks is a crucial factor for effective learning. Based on this key insight, we propose DiverseDiT, a novel framework that explicitly promotes representation diversity. DiverseDiT incorporates long residual connections to diversify input representations across blocks and a representation diversity loss to encourage blocks to learn distinct features. Extensive experiments on ImageNet 256x256 and 512x512 demonstrate that our DiverseDiT yields consistent performance gains and convergence acceleration when applied to different backbones with various sizes, even when tested on the challenging one-step generation setting. Furthermore, we show that DiverseDiT is complementary to existing representation learning techniques, leading to further performance gains. Our work provides valuable insights into the representation learning dynamics of DiTs and offers a practical approach for enhancing their performance.

