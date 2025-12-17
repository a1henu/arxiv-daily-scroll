---
layout: default
title: Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models
---

# Sparse-LaViDa: Sparse Multimodal Discrete Diffusion Language Models
**arXiv**：[2512.14008v1](https://arxiv.org/abs/2512.14008) · [PDF](https://arxiv.org/pdf/2512.14008.pdf)  
**作者**：Shufan Li, Jiuxiang Gu, Kangning Liu, Zhe Lin, Zijun Wei, Aditya Grover, Jason Kuen  

**一句话要点**：提出Sparse-LaViDa以加速掩码离散扩散模型推理，通过动态截断冗余掩码令牌并引入寄存器令牌保持生成质量。

**关键词**：掩码离散扩散模型, 推理加速, 动态截断, 寄存器令牌, 多模态生成, 注意力掩码

## 3 点简述
- 核心问题：掩码离散扩散模型推理速度慢，因需重复处理冗余掩码令牌。
- 方法要点：动态截断不必要掩码令牌，引入寄存器令牌作为紧凑表示，设计匹配截断过程的注意力掩码。
- 实验或效果：基于LaViDa-O，在文本到图像生成等任务中实现最高2倍加速，同时保持生成质量。

## 摘要（原文）

> Masked Discrete Diffusion Models (MDMs) have achieved strong performance across a wide range of multimodal tasks, including image understanding, generation, and editing. However, their inference speed remains suboptimal due to the need to repeatedly process redundant masked tokens at every sampling step. In this work, we propose Sparse-LaViDa, a novel modeling framework that dynamically truncates unnecessary masked tokens at each inference step to accelerate MDM sampling. To preserve generation quality, we introduce specialized register tokens that serve as compact representations for the truncated tokens. Furthermore, to ensure consistency between training and inference, we design a specialized attention mask that faithfully matches the truncated sampling procedure during training. Built upon the state-of-the-art unified MDM LaViDa-O, Sparse-LaViDa achieves up to a 2x speedup across diverse tasks including text-to-image generation, image editing, and mathematical reasoning, while maintaining generation quality.

