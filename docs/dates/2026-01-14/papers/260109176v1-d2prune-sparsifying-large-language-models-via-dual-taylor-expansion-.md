---
layout: default
title: $D^2Prune$: Sparsifying Large Language Models via Dual Taylor Expansion and Attention Distribution Awareness
---

# $D^2Prune$: Sparsifying Large Language Models via Dual Taylor Expansion and Attention Distribution Awareness
**arXiv**：[2601.09176v1](https://arxiv.org/abs/2601.09176) · [PDF](https://arxiv.org/pdf/2601.09176.pdf)  
**作者**：Lang Xiong, Ning Liu, Ao Ren, Yuheng Bai, Haining Fang, BinYan Zhang, Zhe Jiang, Yujuan Tan, Duo Liu  

**一句话要点**：提出D^2Prune方法以解决大语言模型剪枝中激活分布偏移和注意力长尾分布问题

**关键词**：大语言模型剪枝, 双泰勒展开, 注意力分布感知, 激活分布偏移, 长尾分布, 模型压缩

## 3 点简述
- 核心问题：现有剪枝方法忽略校准与测试数据间的激活分布偏移及注意力模块的长尾分布特性，导致误差估计不准确
- 方法要点：采用双泰勒展开联合建模权重和激活扰动进行精确误差估计，并设计注意力感知动态更新策略以保持长尾注意力模式
- 实验或效果：在OPT-125M、LLaMA2/3、Qwen3等LLMs上优于SOTA方法，并推广至DeiT等ViT视觉模型，在ImageNet-1K上取得高精度

## 摘要（原文）

> Large language models (LLMs) face significant deployment challenges due to their massive computational demands. % While pruning offers a promising compression solution, existing methods suffer from two critical limitations: (1) They neglect activation distribution shifts between calibration data and test data, resulting in inaccurate error estimations; (2) They overlook the long-tail distribution characteristics of activations in the attention module. To address these limitations, this paper proposes a novel pruning method, $D^2Prune$. First, we propose a dual Taylor expansion-based method that jointly models weight and activation perturbations for precise error estimation, leading to precise pruning mask selection and weight updating and facilitating error minimization during pruning. % Second, we propose an attention-aware dynamic update strategy that preserves the long-tail attention pattern by jointly minimizing the KL divergence of attention distributions and the reconstruction error. Extensive experiments show that $D^2Prune$ consistently outperforms SOTA methods across various LLMs (e.g., OPT-125M, LLaMA2/3, and Qwen3). Moreover, the dynamic attention update mechanism also generalizes well to ViT-based vision models like DeiT, achieving superior accuracy on ImageNet-1K.

