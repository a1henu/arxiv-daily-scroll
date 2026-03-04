---
layout: default
title: Beyond One-Size-Fits-All: Adaptive Subgraph Denoising for Zero-Shot Graph Learning with Large Language Models
---

# Beyond One-Size-Fits-All: Adaptive Subgraph Denoising for Zero-Shot Graph Learning with Large Language Models
**arXiv**：[2603.02938v1](https://arxiv.org/abs/2603.02938) · [PDF](https://arxiv.org/pdf/2603.02938.pdf)  
**作者**：Fengzhi Li, Liang Zhang, Yuan Zuo, Ruiqing Zhao, YanSong Liu, Yunfei Ma, Fanyu Meng, Junlan Feng  

**一句话要点**：提出GraphSSR框架，通过自适应子图去噪解决零样本图学习中LLM推理的结构噪声问题。

**关键词**：零样本图学习, 大语言模型推理, 自适应子图提取, 结构去噪, 强化学习优化, 图神经网络

## 3 点简述
- 核心问题：传统GNN在零样本图任务中泛化差，现有LLM方法因任务无关子图提取引入结构噪声，影响预测准确性。
- 方法要点：引入SSR管道（采样-选择-推理），动态提取和去噪子图，结合SSR-SFT数据合成和SSR-RL强化学习优化推理过程。
- 实验或效果：未知，但框架旨在提升LLM在零样本图学习中的推理准确性和泛化能力。

## 摘要（原文）

> Graph-based tasks in the zero-shot setting remain a significant challenge due to data scarcity and the inability of traditional Graph Neural Networks (GNNs) to generalize to unseen domains or label spaces. While recent advancements have transitioned toward leveraging Large Language Models (LLMs) as predictors to enhance GNNs, these methods often suffer from cross-modal alignment issues. A recent paradigm (i.e., Graph-R1) overcomes the aforementioned architectural dependencies by adopting a purely text-based format and utilizing LLM-based graph reasoning, showing improved zero-shot generalization. However, it employs a task-agnostic, one-size-fits-all subgraph extraction strategy, which inevitably introduces significant structural noise--irrelevant neighbors and edges--that distorts the LLMs' receptive field and leads to suboptimal predictions. To address this limitation, we introduce GraphSSR, a novel framework designed for adaptive subgraph extraction and denoising in zero-shot LLM-based graph reasoning. Specifically, we propose the SSR pipeline, which dynamically tailors subgraph extraction to specific contexts through a "Sample-Select-Reason" process, enabling the model to autonomously filter out task-irrelevant neighbors and overcome the one-size-fits-all issue. To internalize this capability, we develop SSR-SFT, a data synthesis strategy that generates high-quality SSR-style graph reasoning traces for supervised fine-tuning of LLMs. Furthermore, we propose SSR-RL, a two-stage reinforcement learning framework that explicitly regulates sampling and selection operations within the proposed SSR pipeline designed for adaptive subgraph denoising. By incorporating Authenticity-Reinforced and Denoising-Reinforced RL, we guide the model to achieve accurate predictions using parsimonious, denoised subgraphs for reasoning.

