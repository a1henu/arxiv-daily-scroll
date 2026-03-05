---
layout: default
title: All-in-One Image Restoration via Causal-Deconfounding Wavelet-Disentangled Prompt Network
---

# All-in-One Image Restoration via Causal-Deconfounding Wavelet-Disentangled Prompt Network
**arXiv**：[2603.03839v1](https://arxiv.org/abs/2603.03839) · [PDF](https://arxiv.org/pdf/2603.03839.pdf)  
**作者**：Bingnan Wang, Bin Qin, Jiangmeng Li, Fanjiang Xu, Fuchun Sun, Hui Xiong  

**一句话要点**：提出CWP-Net以解决全场景图像修复中的虚假相关性和退化模式偏差问题

**关键词**：全场景图像修复, 因果去混淆, 小波解耦, 退化模式估计, 图像恢复

## 3 点简述
- 核心问题：全场景图像修复存在虚假相关性和退化模式偏差，影响模型效果和泛化能力
- 方法要点：通过小波注意力模块解耦退化与语义特征，并利用小波提示块进行因果去混淆
- 实验或效果：在两种全场景设置下，实验证明CWP-Net优于现有方法，性能优越

## 摘要（原文）

> Image restoration represents a promising approach for addressing the inherent defects of image content distortion. Standard image restoration approaches suffer from high storage cost and the requirement towards the known degradation pattern, including type and degree, which can barely be satisfied in dynamic practical scenarios. In contrast, all-in-one image restoration (AiOIR) eliminates multiple degradations within a unified model to circumvent the aforementioned issues. However, according to our causal analysis, we disclose that two significant defects still exacerbate the effectiveness and generalization of AiOIR models: 1) the spurious correlation between non-degradation semantic features and degradation patterns; 2) the biased estimation of degradation patterns. To obtain the true causation between degraded images and restored images, we propose Causal-deconfounding Wavelet-disentangled Prompt Network (CWP-Net) to perform effective AiOIR. CWP-Net introduces two modules for decoupling, i.e., wavelet attention module of encoder and wavelet attention module of decoder. These modules explicitly disentangle the degradation and semantic features to tackle the issue of spurious correlation. To address the issue stemming from the biased estimation of degradation patterns, CWP-Net leverages a wavelet prompt block to generate the alternative variable for causal deconfounding. Extensive experiments on two all-in-one settings prove the effectiveness and superior performance of our proposed CWP-Net over the state-of-the-art AiOIR methods.

