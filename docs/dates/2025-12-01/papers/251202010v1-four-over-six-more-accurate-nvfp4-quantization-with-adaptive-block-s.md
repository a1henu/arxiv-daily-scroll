---
layout: default
title: Four Over Six: More Accurate NVFP4 Quantization with Adaptive Block Scaling
---

# Four Over Six: More Accurate NVFP4 Quantization with Adaptive Block Scaling
**arXiv**：[2512.02010v1](https://arxiv.org/abs/2512.02010) · [PDF](https://arxiv.org/pdf/2512.02010.pdf)  
**作者**：Jack Cook, Junxian Guo, Guangxuan Xiao, Yujun Lin, Song Han  

**一句话要点**：提出4/6自适应块缩放方法以提升NVFP4量化精度，解决训练发散与推理性能下降问题。

**关键词**：NVFP4量化, 自适应块缩放, 低精度训练, 大语言模型, 浮点格式优化, 推理加速

## 3 点简述
- NVFP4量化在训练和推理中易导致发散与性能下降，主要源于块内近最大值量化误差。
- 4/6方法为每个值块评估两个缩放因子，使可表示值分布更均匀，改善近最大值表示。
- 实验表明4/6在预训练中防止发散，提升下游精度，并兼容NVIDIA Blackwell GPU高效实现。

## 摘要（原文）

> As large language models have grown larger, low-precision numerical formats such as NVFP4 have become increasingly popular due to the speed and memory benefits they provide. However, to accelerate computation with NVFP4, all matrix multiplication operands--weights and activations in the forward pass, and weights, activations, and gradients in the backward pass--must be quantized to NVFP4, often leading to divergence during training and performance degradation during inference. NVFP4 by evaluating multiple potential scale factors for each block of values. To address this issue, in this work we introduce Four Over Six (4/6), a modification to the NVFP4 quantization algorithm that evaluates two potential scale factors for each block of values. Unlike integer formats, floating-point formats such as FP4 have the most quantization error on near-maximal values in each block, which we find to be primarily responsible for downstream performance degradation. We find that for some blocks, scaling to smaller FP4 values makes the distribution of representable values more uniform, improving representation of near-maximal values. Importantly, 4/6 can be implemented efficiently on NVIDIA Blackwell GPUs, making it viable to use while training LLMs with NVFP4. In pre-training experiments with transformer and hybrid model architectures, we find that 4/6 prevents divergence in several cases, bringing training loss significantly closer to BF16 compared to models trained with current state-of-the-art NVFP4 training recipes. We also find that 4/6 can be easily incorporated into many different post-training quantization methods and generally improves downstream accuracy. We hope this inspires future work in training and deploying models with NVFP4.

