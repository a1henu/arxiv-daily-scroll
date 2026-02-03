---
layout: default
title: $\textbf{AGT$^{AO}$}$: Robust and Stabilized LLM Unlearning via Adversarial Gating Training with Adaptive Orthogonality
---

# $\textbf{AGT$^{AO}$}$: Robust and Stabilized LLM Unlearning via Adversarial Gating Training with Adaptive Orthogonality
**arXiv**：[2602.01703v1](https://arxiv.org/abs/2602.01703) · [PDF](https://arxiv.org/pdf/2602.01703.pdf)  
**作者**：Pengyu Li, Lingling Zhang, Zhitao Gao, Yanrui Wu, Yuxuan Dong, Huan Liu, Bifan Wei, Jun Liu  

**一句话要点**：提出AGT^{AO}框架，通过对抗门控训练与自适应正交性解决大语言模型遗忘中的稳健性与稳定性问题。

**关键词**：大语言模型遗忘, 对抗训练, 梯度优化, 隐私保护, 模型稳健性

## 3 点简述
- 核心问题：大语言模型遗忘敏感数据时面临遗忘效果与模型效用之间的权衡困境。
- 方法要点：引入自适应正交性动态缓解梯度冲突，结合对抗门控训练模拟内部恢复以增强遗忘稳健性。
- 实验或效果：实验显示AGT^{AO}在遗忘效果（KUR≈0.01）与模型效用（MMLU 58.30）间取得优越平衡。

## 摘要（原文）

> While Large Language Models (LLMs) have achieved remarkable capabilities, they unintentionally memorize sensitive data, posing critical privacy and security risks. Machine unlearning is pivotal for mitigating these risks, yet existing paradigms face a fundamental dilemma: aggressive unlearning often induces catastrophic forgetting that degrades model utility, whereas conservative strategies risk superficial forgetting, leaving models vulnerable to adversarial recovery. To address this trade-off, we propose $\textbf{AGT$^{AO}$}$ (Adversarial Gating Training with Adaptive Orthogonality), a unified framework designed to reconcile robust erasure with utility preservation. Specifically, our approach introduces $\textbf{Adaptive Orthogonality (AO)}$ to dynamically mitigate geometric gradient conflicts between forgetting and retention objectives, thereby minimizing unintended knowledge degradation. Concurrently, $\textbf{Adversarial Gating Training (AGT)}$ formulates unlearning as a latent-space min-max game, employing a curriculum-based gating mechanism to simulate and counter internal recovery attempts. Extensive experiments demonstrate that $\textbf{AGT$^{AO}$}$ achieves a superior trade-off between unlearning efficacy (KUR $\approx$ 0.01) and model utility (MMLU 58.30). Code is available at https://github.com/TiezMind/AGT-unlearning.

