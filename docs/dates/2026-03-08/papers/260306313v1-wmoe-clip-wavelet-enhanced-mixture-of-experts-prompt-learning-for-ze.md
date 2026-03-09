---
layout: default
title: WMoE-CLIP: Wavelet-Enhanced Mixture-of-Experts Prompt Learning for Zero-Shot Anomaly Detection
---

# WMoE-CLIP: Wavelet-Enhanced Mixture-of-Experts Prompt Learning for Zero-Shot Anomaly Detection
**arXiv**：[2603.06313v1](https://arxiv.org/abs/2603.06313) · [PDF](https://arxiv.org/pdf/2603.06313.pdf)  
**作者**：Peng Chen, Chao Huang  

**一句话要点**：提出小波增强的专家混合提示学习方法，以解决零样本异常检测中语义捕获不足和特征局限问题。

**关键词**：零样本异常检测, 小波分解, 专家混合提示学习, 跨模态交互, 变分自编码器, 多频特征提取

## 3 点简述
- 核心问题：现有方法依赖固定文本提示，难以捕捉复杂语义，且仅关注空间域特征，限制了对细微异常的检测能力。
- 方法要点：使用变分自编码器建模全局语义并融入提示，结合小波分解提取多频特征，通过跨模态交互动态优化文本嵌入，引入语义感知的专家混合模块聚合上下文信息。
- 实验或效果：在14个工业和医学数据集上进行了广泛实验，验证了方法的有效性，具体性能指标未知。

## 摘要（原文）

> Vision-language models have recently shown strong generalization in zero-shot anomaly detection (ZSAD), enabling the detection of unseen anomalies without task-specific supervision. However, existing approaches typically rely on fixed textual prompts, which struggle to capture complex semantics, and focus solely on spatial-domain features, limiting their ability to detect subtle anomalies. To address these challenges, we propose a wavelet-enhanced mixture-of-experts prompt learning method for ZSAD. Specifically, a variational autoencoder is employed to model global semantic representations and integrate them into prompts to enhance adaptability to diverse anomaly patterns. Wavelet decomposition extracts multi-frequency image features that dynamically refine textual embeddings through cross-modal interactions. Furthermore, a semantic-aware mixture-of-experts module is introduced to aggregate contextual information. Extensive experiments on 14 industrial and medical datasets demonstrate the effectiveness of the proposed method.

