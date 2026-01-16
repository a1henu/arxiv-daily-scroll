---
layout: default
title: Understanding and Preserving Safety in Fine-Tuned LLMs
---

# Understanding and Preserving Safety in Fine-Tuned LLMs
**arXiv**：[2601.10141v1](https://arxiv.org/abs/2601.10141) · [PDF](https://arxiv.org/pdf/2601.10141.pdf)  
**作者**：Jiawen Zhang, Yangfan Hu, Kejia Chen, Lipeng He, Jiachen Ma, Jian Lou, Dan Li, Jian Liu, Xiaohu Yang, Ruoxi Jia  

**一句话要点**：提出安全保持微调方法以解决大语言模型微调中的安全-效用困境

**关键词**：大语言模型微调, 安全对齐, 梯度分析, 安全保持微调, 越狱攻击, 低秩子空间

## 3 点简述
- 核心问题：微调大语言模型会显著降低安全对齐，导致安全-效用权衡困境。
- 方法要点：基于安全梯度低秩子空间与效用梯度高维空间冲突的几何分析，移除冲突梯度成分。
- 实验或效果：方法在对抗性微调下保持任务性能并恢复安全对齐，抵抗深度微调和动态越狱攻击。

## 摘要（原文）

> Fine-tuning is an essential and pervasive functionality for applying large language models (LLMs) to downstream tasks. However, it has the potential to substantially degrade safety alignment, e.g., by greatly increasing susceptibility to jailbreak attacks, even when the fine-tuning data is entirely harmless. Despite garnering growing attention in defense efforts during the fine-tuning stage, existing methods struggle with a persistent safety-utility dilemma: emphasizing safety compromises task performance, whereas prioritizing utility typically requires deep fine-tuning that inevitably leads to steep safety declination.
>   In this work, we address this dilemma by shedding new light on the geometric interaction between safety- and utility-oriented gradients in safety-aligned LLMs. Through systematic empirical analysis, we uncover three key insights: (I) safety gradients lie in a low-rank subspace, while utility gradients span a broader high-dimensional space; (II) these subspaces are often negatively correlated, causing directional conflicts during fine-tuning; and (III) the dominant safety direction can be efficiently estimated from a single sample. Building upon these novel insights, we propose safety-preserving fine-tuning (SPF), a lightweight approach that explicitly removes gradient components conflicting with the low-rank safety subspace. Theoretically, we show that SPF guarantees utility convergence while bounding safety drift. Empirically, SPF consistently maintains downstream task performance and recovers nearly all pre-trained safety alignment, even under adversarial fine-tuning scenarios. Furthermore, SPF exhibits robust resistance to both deep fine-tuning and dynamic jailbreak attacks. Together, our findings provide new mechanistic understanding and practical guidance toward always-aligned LLM fine-tuning.

