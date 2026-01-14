---
layout: default
title: Demystifying the Slash Pattern in Attention: The Role of RoPE
---

# Demystifying the Slash Pattern in Attention: The Role of RoPE
**arXiv**：[2601.08297v1](https://arxiv.org/abs/2601.08297) · [PDF](https://arxiv.org/pdf/2601.08297.pdf)  
**作者**：Yuan Cheng, Fengzhuo Zhang, Yunlong Hou, Cunxiao Du, Chao Du, Tianyu Pang, Aixin Sun, Zhuoran Yang  

**一句话要点**：揭示注意力中斜线模式的成因：RoPE的作用

**关键词**：注意力机制, 斜线模式, RoPE, 大语言模型, 训练动态

## 3 点简述
- 核心问题：大语言模型中斜线注意力模式为何出现，其信息传递机制如何。
- 方法要点：通过实证分析查询、键和RoPE，结合理论建模证明斜线主导头的形成条件。
- 实验或效果：在开源模型上验证斜线主导头的内在性和泛化性，理论推导训练动态。

## 摘要（原文）

> Large Language Models (LLMs) often exhibit slash attention patterns, where attention scores concentrate along the $Δ$-th sub-diagonal for some offset $Δ$. These patterns play a key role in passing information across tokens. But why do they emerge? In this paper, we demystify the emergence of these Slash-Dominant Heads (SDHs) from both empirical and theoretical perspectives. First, by analyzing open-source LLMs, we find that SDHs are intrinsic to models and generalize to out-of-distribution prompts. To explain the intrinsic emergence, we analyze the queries, keys, and Rotary Position Embedding (RoPE), which jointly determine attention scores. Our empirical analysis reveals two characteristic conditions of SDHs: (1) Queries and keys are almost rank-one, and (2) RoPE is dominated by medium- and high-frequency components. Under these conditions, queries and keys are nearly identical across tokens, and interactions between medium- and high-frequency components of RoPE give rise to SDHs. Beyond empirical evidence, we theoretically show that these conditions are sufficient to ensure the emergence of SDHs by formalizing them as our modeling assumptions. Particularly, we analyze the training dynamics of a shallow Transformer equipped with RoPE under these conditions, and prove that models trained via gradient descent exhibit SDHs. The SDHs generalize to out-of-distribution prompts.

