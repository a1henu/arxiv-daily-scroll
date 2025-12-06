---
layout: default
title: EMMA: Efficient Multimodal Understanding, Generation, and Editing with a Unified Architecture
---

# EMMA: Efficient Multimodal Understanding, Generation, and Editing with a Unified Architecture
**arXiv**：[2512.04810v1](https://arxiv.org/abs/2512.04810) · [PDF](https://arxiv.org/pdf/2512.04810.pdf)  
**作者**：Xin He, Longhui Wei, Jianbo Ouyang, Lingxi Xie, Qi Tian  

**一句话要点**：提出EMMA统一架构，以高效实现多模态理解、生成与编辑任务

**关键词**：多模态统一架构, 高效自动编码器, 通道级拼接, 共享-解耦网络, 专家混合机制, 多模态理解生成

## 3 点简述
- 核心问题：统一多模态架构中视觉令牌过多导致效率低下和任务训练不平衡
- 方法要点：采用32倍压缩比自动编码器减少生成令牌，通道级拼接降低视觉令牌，共享-解耦网络和专家混合机制提升性能
- 实验或效果：EMMA-4B在效率和性能上超越BAGEL-7B等统一方法，与Qwen3-VL等专家模型竞争

## 摘要（原文）

> We propose EMMA, an efficient and unified architecture for multimodal understanding, generation and editing. Specifically, EMMA primarily consists of 1) An efficient autoencoder with a 32x compression ratio, which significantly reduces the number of tokens required for generation. This also ensures the training balance between understanding and generation tasks by applying the same compression ratio to images. 2) Channel-wise concatenation instead of token-wise concatenation among visual understanding and generation tokens, which further reduces the visual tokens in unified architectures. 3) A shared-and-decoupled network that enables mutual improvements across tasks while meeting the task-specific modeling requirements. 4) A mixture-of-experts mechanism adopted for visual understanding encoder, which substantially improves perceptual capabilities with a few parameters increase. Extensive experiments have shown that EMMA-4B can significantly outperform state-of-the-art unified multimodal approaches (e.g., BAGEL-7B) in both efficiency and performance, while also achieving competitive results compared to recent multimodal understanding and generation experts (e.g., Qwen3-VL and Qwen-Image). We believe that EMMA lays a solid foundation for the future development of unified multimodal architectures.

