---
layout: default
title: Rethinking LoRA for Privacy-Preserving Federated Learning in Large Models
---

# Rethinking LoRA for Privacy-Preserving Federated Learning in Large Models
**arXiv**：[2602.19926v1](https://arxiv.org/abs/2602.19926) · [PDF](https://arxiv.org/pdf/2602.19926.pdf)  
**作者**：Jin Liu, Yinbin Miao, Ning Xi, Junkang Liu  

**一句话要点**：提出LA-LoRA以解决差分隐私联邦学习中LoRA的性能下降问题

**关键词**：差分隐私联邦学习, 低秩适应, 大模型微调, 参数高效微调, 梯度解耦, 鲁棒性增强

## 3 点简述
- 核心问题：LoRA在差分隐私联邦学习中因梯度耦合、噪声放大和模型锐度导致性能下降
- 方法要点：LA-LoRA通过解耦梯度交互和对齐客户端更新方向增强鲁棒性
- 实验或效果：在Swin Transformer和RoBERTa上实现SOTA性能，在严格隐私预算下提升测试准确率16.83%

## 摘要（原文）

> Fine-tuning large vision models (LVMs) and large language models (LLMs) under differentially private federated learning (DPFL) is hindered by a fundamental privacy-utility trade-off. Low-Rank Adaptation (LoRA), a promising parameter-efficient fine-tuning (PEFT) method, reduces computational and communication costs by introducing two trainable low-rank matrices while freezing pre-trained weights. However, directly applying LoRA in DPFL settings leads to performance degradation, especially in LVMs. Our analysis reveals three previously underexplored challenges: (1) gradient coupling caused by the simultaneous update of two asymmetric low-rank matrices, (2) compounded noise amplification under differential privacy, and (3) sharpness of the global aggregated model in the parameter space. To address these issues, we propose LA-LoRA (\textbf{L}ocal \textbf{A}lternating \textbf{LoRA}), a novel approach that decouples gradient interactions and aligns update directions across clients to enhance robustness under stringent privacy constraints. Theoretically, LA-LoRA strengthens convergence guarantees in noisy federated environments. Extensive experiments demonstrate that LA-LoRA achieves state-of-the-art (SOTA) performance on Swin Transformer and RoBERTa models, showcasing robustness to DP noise and broad applicability across both LVMs and LLMs. For example, when fine-tuning the Swin-B model on the Tiny-ImageNet dataset under a strict privacy budget ($ε= 1$), LA-LoRA outperforms the best baseline, RoLoRA, by 16.83\% in test accuracy. Code is provided in \repolink.

