---
layout: default
title: CC-VQA: Conflict- and Correlation-Aware Method for Mitigating Knowledge Conflict in Knowledge-Based Visual Question Answering
---

# CC-VQA: Conflict- and Correlation-Aware Method for Mitigating Knowledge Conflict in Knowledge-Based Visual Question Answering
**arXiv**：[2602.23952v1](https://arxiv.org/abs/2602.23952) · [PDF](https://arxiv.org/pdf/2602.23952.pdf)  
**作者**：Yuyang Hong, Jiaqi Gu, Yujin Lou, Lubin Fan, Qi Yang, Ying Wang, Kun Ding, Yue Wu, Shiming Xiang, Jieping Ye  

**一句话要点**：提出CC-VQA方法，通过视觉中心冲突推理与相关性引导编解码，缓解知识型视觉问答中的知识冲突问题。

**关键词**：知识型视觉问答, 知识冲突缓解, 视觉语义分析, 相关性引导解码, 训练免费方法

## 3 点简述
- 核心问题：静态视觉语言模型知识与动态检索信息冲突，导致忽略检索上下文或整合不一致。
- 方法要点：视觉中心上下文冲突推理分析视觉语义冲突，相关性引导编码解码压缩低相关语句并自适应解码。
- 实验或效果：在E-VQA、InfoSeek和OK-VQA基准上实现SOTA，准确率提升3.3%至6.4%。

## 摘要（原文）

> Knowledge-based visual question answering (KB-VQA) demonstrates significant potential for handling knowledge-intensive tasks. However, conflicts arise between static parametric knowledge in vision language models (VLMs) and dynamically retrieved information due to the static model knowledge from pre-training. The outputs either ignore retrieved contexts or exhibit inconsistent integration with parametric knowledge, posing substantial challenges for KB-VQA. Current knowledge conflict mitigation methods primarily adapted from language-based approaches, focusing on context-level conflicts through engineered prompting strategies or context-aware decoding mechanisms. However, these methods neglect the critical role of visual information in conflicts and suffer from redundant retrieved contexts, which impair accurate conflict identification and effective mitigation. To address these limitations, we propose \textbf{CC-VQA}: a novel training-free, conflict- and correlation-aware method for KB-VQA. Our method comprises two core components: (1) Vision-Centric Contextual Conflict Reasoning, which performs visual-semantic conflict analysis across internal and external knowledge contexts; and (2) Correlation-Guided Encoding and Decoding, featuring positional encoding compression for low-correlation statements and adaptive decoding using correlation-weighted conflict scoring. Extensive evaluations on E-VQA, InfoSeek, and OK-VQA benchmarks demonstrate that CC-VQA achieves state-of-the-art performance, yielding absolute accuracy improvements of 3.3\% to 6.4\% compared to existing methods. Code is available at https://github.com/cqu-student/CC-VQA.

