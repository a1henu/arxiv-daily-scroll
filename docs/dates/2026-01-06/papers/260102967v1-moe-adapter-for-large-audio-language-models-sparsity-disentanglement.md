---
layout: default
title: MoE Adapter for Large Audio Language Models: Sparsity, Disentanglement, and Gradient-Conflict-Free
---

# MoE Adapter for Large Audio Language Models: Sparsity, Disentanglement, and Gradient-Conflict-Free
**arXiv**：[2601.02967v1](https://arxiv.org/abs/2601.02967) · [PDF](https://arxiv.org/pdf/2601.02967.pdf)  
**作者**：Yishu Lei, Shuwei He, Jing Hu, Dan Zhang, Xianlong Luo, Danxiang Zhu, Shikun Feng, Rui Liu, Jingzhou He, Yu Sun, Hua Wu, Haifeng Wang  

**一句话要点**：提出MoE-Adapter稀疏架构以解决音频大语言模型中的梯度冲突问题

**关键词**：音频大语言模型, 混合专家, 梯度冲突, 稀疏适配器, 多模态感知

## 3 点简述
- 核心问题：音频信息异质性强，现有密集适配器在建模时会产生梯度冲突
- 方法要点：采用稀疏MoE架构，通过动态门控机制将音频令牌路由到专用专家
- 实验效果：在音频语义和副语言任务上优于密集基线，计算成本相当

## 摘要（原文）

> Extending the input modality of Large Language Models~(LLMs) to the audio domain is essential for achieving comprehensive multimodal perception. However, it is well-known that acoustic information is intrinsically \textit{heterogeneous}, entangling attributes such as speech, music, and environmental context. Existing research is limited to a dense, parameter-shared adapter to model these diverse patterns, which induces \textit{gradient conflict} during optimization, as parameter updates required for distinct attributes contradict each other. To address this limitation, we introduce the \textit{\textbf{MoE-Adapter}}, a sparse Mixture-of-Experts~(MoE) architecture designed to decouple acoustic information. Specifically, it employs a dynamic gating mechanism that routes audio tokens to specialized experts capturing complementary feature subspaces while retaining shared experts for global context, thereby mitigating gradient conflicts and enabling fine-grained feature learning. Comprehensive experiments show that the MoE-Adapter achieves superior performance on both audio semantic and paralinguistic tasks, consistently outperforming dense linear baselines with comparable computational costs. Furthermore, we will release the related code and models to facilitate future research.

