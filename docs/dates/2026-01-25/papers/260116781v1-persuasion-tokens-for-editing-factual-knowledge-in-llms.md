---
layout: default
title: Persuasion Tokens for Editing Factual Knowledge in LLMs
---

# Persuasion Tokens for Editing Factual Knowledge in LLMs
**arXiv**：[2601.16781v1](https://arxiv.org/abs/2601.16781) · [PDF](https://arxiv.org/pdf/2601.16781.pdf)  
**作者**：Paul Youssef, Jörg Schlötterer, Christin Seifert  

**一句话要点**：提出说服令牌以高效编辑大语言模型中的事实知识，无需事实特定演示。

**关键词**：知识编辑, 大语言模型, 上下文学习, 特殊令牌, 高效更新

## 3 点简述
- 核心问题：上下文知识编辑依赖冗长的事实特定演示，成本高且占用上下文窗口空间。
- 方法要点：训练特殊令牌（说服令牌）来复制上下文知识编辑演示的效果，实现高效知识编辑。
- 实验或效果：在多个数据集和模型上评估，性能与上下文知识编辑相当或更优，对干扰物鲁棒，增加令牌数提升性能。

## 摘要（原文）

> In-context knowledge editing (IKE) is a promising technique for updating Large Language Models (LLMs) with new information. However, IKE relies on lengthy, fact-specific demonstrations which are costly to create and consume significant context window space. In this paper, we introduce persuasion tokens (P-Tokens) -- special tokens trained to replicate the effect of IKE demonstrations, enabling efficient knowledge editing without requiring fact-specific demonstrations. We evaluate P-Tokens across two editing datasets and three LLMs, demonstrating performance comparable to, and often exceeding, IKE. We further find that editing performance is robust to distractors with small negative effects to neighboring facts, and that increasing the number of P-Tokens improves performance. Our work addresses key limitations of IKE and provides a more practical and scalable alternative for editing LLMs.

