---
layout: default
title: YaPO: Learnable Sparse Activation Steering Vectors for Domain Adaptation
---

# YaPO: Learnable Sparse Activation Steering Vectors for Domain Adaptation
**arXiv**：[2601.08441v1](https://arxiv.org/abs/2601.08441) · [PDF](https://arxiv.org/pdf/2601.08441.pdf)  
**作者**：Abdelaziz Bounhar, Rania Hossam Elmohamady Elbadry, Hadi Abdine, Preslav Nakov, Michalis Vazirgiannis, Guokan Shang  

**一句话要点**：提出YaPO方法，通过稀疏激活导向向量实现大语言模型的细粒度对齐与领域适应。

**关键词**：大语言模型对齐, 稀疏激活导向, 领域适应, 细粒度控制, 稀疏自编码器, 文化对齐

## 3 点简述
- 核心问题：密集导向向量因神经元多语义性导致潜在因素纠缠，限制细粒度对齐效果。
- 方法要点：在稀疏自编码器潜在空间中学习稀疏导向向量，优化稀疏编码以实现解耦和可解释性。
- 实验或效果：YaPO收敛更快、性能更强、训练更稳定，适用于文化对齐等多种行为，且保持通用知识。

## 摘要（原文）

> Steering Large Language Models (LLMs) through activation interventions has emerged as a lightweight alternative to fine-tuning for alignment and personalization. Recent work on Bi-directional Preference Optimization (BiPO) shows that dense steering vectors can be learned directly from preference data in a Direct Preference Optimization (DPO) fashion, enabling control over truthfulness, hallucinations, and safety behaviors. However, dense steering vectors often entangle multiple latent factors due to neuron multi-semanticity, limiting their effectiveness and stability in fine-grained settings such as cultural alignment, where closely related values and behaviors (e.g., among Middle Eastern cultures) must be distinguished. In this paper, we propose Yet another Policy Optimization (YaPO), a \textit{reference-free} method that learns \textit{sparse steering vectors} in the latent space of a Sparse Autoencoder (SAE). By optimizing sparse codes, YaPO produces disentangled, interpretable, and efficient steering directions. Empirically, we show that YaPO converges faster, achieves stronger performance, and exhibits improved training stability compared to dense steering baselines. Beyond cultural alignment, YaPO generalizes to a range of alignment-related behaviors, including hallucination, wealth-seeking, jailbreak, and power-seeking. Importantly, YaPO preserves general knowledge, with no measurable degradation on MMLU. Overall, our results show that YaPO provides a general recipe for efficient, stable, and fine-grained alignment of LLMs, with broad applications to controllability and domain adaptation. The associated code and data are publicly available\footnote{https://github.com/MBZUAI-Paris/YaPO}.

