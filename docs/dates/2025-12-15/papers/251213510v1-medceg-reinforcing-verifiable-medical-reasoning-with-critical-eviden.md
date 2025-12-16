---
layout: default
title: MedCEG: Reinforcing Verifiable Medical Reasoning with Critical Evidence Graph
---

# MedCEG: Reinforcing Verifiable Medical Reasoning with Critical Evidence Graph
**arXiv**：[2512.13510v1](https://arxiv.org/abs/2512.13510) · [PDF](https://arxiv.org/pdf/2512.13510.pdf)  
**作者**：Linjie Mu, Yannian Gu, Zhongzhen Huang, Yakun Zhu, Shaoting Zhang, Xiaofan Zhang  

**一句话要点**：提出MedCEG框架，通过关键证据图增强医学语言模型的可验证推理能力。

**关键词**：医学推理, 关键证据图, 强化学习, 临床可靠性, 语言模型增强

## 3 点简述
- 核心问题：医学推理中强化学习常忽视准确性和有效性，导致临床可靠性受限。
- 方法要点：构建关键证据图监督推理过程，引入临床推理程序奖励评估节点覆盖、结构正确性和链完整性。
- 实验或效果：在挑战性临床案例数据集上，MedCEG超越现有方法，生成临床有效推理链。

## 摘要（原文）

> Large language models with reasoning capabilities have demonstrated impressive performance across a wide range of domains. In clinical applications, a transparent, step-by-step reasoning process provides physicians with strong evidence to support decision-making. While reinforcement learning has effectively enhanced reasoning performance in medical contexts, the clinical reliability of these reasoning processes remains limited because their accuracy and validity are often overlooked during training. To address this gap, we propose MedCEG, a framework that augments medical language models with clinically valid reasoning pathways by explicitly supervising the reasoning process through a Critical Evidence Graph (CEG). We curate a dataset of challenging clinical cases and algorithmically construct a CEG for each sample to represent a high-quality verifiable reasoning pathway. To guide the reasoning process, we introduce a Clinical Reasoning Procedure Reward, which evaluates Node Coverage, Structural Correctness, and Chain Completeness, thereby providing a holistic assessment of reasoning quality. Experimental results show that MedCEG surpasses existing methods in performance while producing clinically valid reasoning chains, representing a solid advancement in reliable medical AI reasoning. The code and models are available at https://github.com/LinjieMu/MedCEG.

