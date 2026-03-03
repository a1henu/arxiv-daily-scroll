---
layout: default
title: FreeAct: Freeing Activations for LLM Quantization
---

# FreeAct: Freeing Activations for LLM Quantization
**arXiv**：[2603.01776v1](https://arxiv.org/abs/2603.01776) · [PDF](https://arxiv.org/pdf/2603.01776.pdf)  
**作者**：Xiaohao Liu, Xiaobo Xia, Manyi Zhang, Ji-Fu Li, Xianzhi Yu, Fei Shen, Xiu Su, See-Kiong Ng, Tat-Seng Chua  

**一句话要点**：提出FreeAct框架，通过动态激活变换解决扩散和多模态大语言模型量化中的分布差异问题。

**关键词**：大语言模型量化, 动态激活变换, 扩散大语言模型, 多模态大语言模型, 秩不足分析

## 3 点简述
- 核心问题：现有量化方法采用静态一对一变换，无法处理输入激活的动态分布差异，尤其在扩散和多模态大语言模型中。
- 方法要点：利用激活的秩不足特性，解耦激活与权重的变换，为不同令牌类型分配动态变换矩阵，保持权重变换统一。
- 实验或效果：在扩散和多模态大语言模型上实验，FreeAct显著优于基线，性能提升最高达5.3%。

## 摘要（原文）

> Quantization is pivotal for mitigating the significant memory and computational overhead of Large Language Models (LLMs). While emerging transformation-based methods have successfully enhanced quantization by projecting feature spaces onto smoother manifolds using orthogonal matrices, they typically enforce a rigid one-to-one transformation constraint. This static approach fails to account for the dynamic patterns inherent in input activations, particularly within diffusion LLMs (dLLMs) and Multimodal LLMs (MLLMs), where varying token types exhibit distinct distributions. To advance this, we propose FreeAct, a novel quantization framework that relaxes the static one-to-one constraint to accommodate dynamic activation disparities. Theoretically, we leverage the rank-deficient nature of activations to derive a solution space that extends beyond simple inverse matrices, enabling the decoupling of activation transformations from weights. Methodologically, FreeAct identifies token-specific dynamics (i.e., vision v.s. text, or masked tokens) and allocates distinct transformation matrices to the activation side, while maintaining a unified, static transformation for the weights. Extensive experiments across dLLMs and MLLMs demonstrate that FreeAct significantly outperforms baselines, up to 5.3% performance improvement, with in-depth analyses. Our code will be publicly released.

