---
layout: default
title: MEMEWEAVER: Inter-Meme Graph Reasoning for Sexism and Misogyny Detection
---

# MEMEWEAVER: Inter-Meme Graph Reasoning for Sexism and Misogyny Detection
**arXiv**：[2601.08684v1](https://arxiv.org/abs/2601.08684) · [PDF](https://arxiv.org/pdf/2601.08684.pdf)  
**作者**：Paolo Italiani, David Gimeno-Gomez, Luca Ragazzi, Gianluca Moro, Paolo Rosso  

**一句话要点**：提出MemeWeaver框架，通过跨模因图推理检测性别歧视和厌女症

**关键词**：性别歧视检测, 跨模因图推理, 多模态融合, 在线骚扰分析, 图神经网络

## 3 点简述
- 核心问题：现有方法忽视在线骚扰的社会动态，如图结构构建启发式、模态融合浅层和实例级推理有限。
- 方法要点：引入端到端可训练的多模态框架，采用跨模因图推理机制，系统评估视觉-文本融合策略。
- 实验或效果：在MAMI和EXIST基准上优于现有方法，训练收敛更快，学习图结构捕获语义模式。

## 摘要（原文）

> Women are twice as likely as men to face online harassment due to their gender. Despite recent advances in multimodal content moderation, most approaches still overlook the social dynamics behind this phenomenon, where perpetrators reinforce prejudices and group identity within like-minded communities. Graph-based methods offer a promising way to capture such interactions, yet existing solutions remain limited by heuristic graph construction, shallow modality fusion, and instance-level reasoning. In this work, we present MemeWeaver, an end-to-end trainable multimodal framework for detecting sexism and misogyny through a novel inter-meme graph reasoning mechanism. We systematically evaluate multiple visual--textual fusion strategies and show that our approach consistently outperforms state-of-the-art baselines on the MAMI and EXIST benchmarks, while achieving faster training convergence. Further analyses reveal that the learned graph structure captures semantically meaningful patterns, offering valuable insights into the relational nature of online hate.

