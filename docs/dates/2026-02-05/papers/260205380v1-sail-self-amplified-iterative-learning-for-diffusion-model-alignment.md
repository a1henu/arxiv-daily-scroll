---
layout: default
title: SAIL: Self-Amplified Iterative Learning for Diffusion Model Alignment with Minimal Human Feedback
---

# SAIL: Self-Amplified Iterative Learning for Diffusion Model Alignment with Minimal Human Feedback
**arXiv**：[2602.05380v1](https://arxiv.org/abs/2602.05380) · [PDF](https://arxiv.org/pdf/2602.05380.pdf)  
**作者**：Xiaoxuan He, Siming Fu, Wanli Li, Zhiyuan Li, Dacheng Yin, Kang Rong, Fengyun Rao, Bo Zhang  

**一句话要点**：提出SAIL框架，通过自增强迭代学习实现扩散模型对齐，仅需少量人类反馈。

**关键词**：扩散模型对齐, 自增强学习, 迭代优化, 人类偏好学习, 最小化反馈

## 3 点简述
- 核心问题：扩散模型对齐需大量人类偏好数据或奖励模型，成本高昂且不切实际。
- 方法要点：SAIL利用模型自身作为教师，通过迭代生成、自标注和精炼，实现自增强学习。
- 实验或效果：在多个基准测试中优于现有方法，仅需6%的偏好数据，无需外部奖励模型。

## 摘要（原文）

> Aligning diffusion models with human preferences remains challenging, particularly when reward models are unavailable or impractical to obtain, and collecting large-scale preference datasets is prohibitively expensive. \textit{This raises a fundamental question: can we achieve effective alignment using only minimal human feedback, without auxiliary reward models, by unlocking the latent capabilities within diffusion models themselves?} In this paper, we propose \textbf{SAIL} (\textbf{S}elf-\textbf{A}mplified \textbf{I}terative \textbf{L}earning), a novel framework that enables diffusion models to act as their own teachers through iterative self-improvement. Starting from a minimal seed set of human-annotated preference pairs, SAIL operates in a closed-loop manner where the model progressively generates diverse samples, self-annotates preferences based on its evolving understanding, and refines itself using this self-augmented dataset. To ensure robust learning and prevent catastrophic forgetting, we introduce a ranked preference mixup strategy that carefully balances exploration with adherence to initial human priors. Extensive experiments demonstrate that SAIL consistently outperforms state-of-the-art methods across multiple benchmarks while using merely 6\% of the preference data required by existing approaches, revealing that diffusion models possess remarkable self-improvement capabilities that, when properly harnessed, can effectively replace both large-scale human annotation and external reward models.

