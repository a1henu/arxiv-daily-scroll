---
layout: default
title: TractRLFusion: A GPT-Based Multi-Critic Policy Fusion Framework for Fiber Tractography
---

# TractRLFusion: A GPT-Based Multi-Critic Policy Fusion Framework for Fiber Tractography
**arXiv**：[2601.13897v1](https://arxiv.org/abs/2601.13897) · [PDF](https://arxiv.org/pdf/2601.13897.pdf)  
**作者**：Ankita Joshi, Ashutosh Sharma, Anoushkrit Goel, Ranjeet Ranjan Jha, Chirag Ahuja, Arnav Bhavsar, Aditya Nigam  

**一句话要点**：提出基于GPT的多策略融合框架TractRLFusion，以提升纤维追踪的准确性和解剖可靠性。

**关键词**：纤维追踪, 强化学习, 策略融合, GPT模型, 多批评器微调

## 3 点简述
- 核心问题：纤维追踪中准确重建白质纤维束并减少虚假连接是持续挑战。
- 方法要点：采用GPT基础的多策略融合框架，结合两阶段训练数据选择和多批评器微调。
- 实验或效果：在多个数据集上优于现有方法，提高了准确性和解剖可靠性。

## 摘要（原文）

> Tractography plays a pivotal role in the non-invasive reconstruction of white matter fiber pathways, providing vital information on brain connectivity and supporting precise neurosurgical planning. Although traditional methods relied mainly on classical deterministic and probabilistic approaches, recent progress has benefited from supervised deep learning (DL) and deep reinforcement learning (DRL) to improve tract reconstruction. A persistent challenge in tractography is accurately reconstructing white matter tracts while minimizing spurious connections. To address this, we propose TractRLFusion, a novel GPT-based policy fusion framework that integrates multiple RL policies through a data-driven fusion strategy. Our method employs a two-stage training data selection process for effective policy fusion, followed by a multi-critic fine-tuning phase to enhance robustness and generalization. Experiments on HCP, ISMRM, and TractoInferno datasets demonstrate that TractRLFusion outperforms individual RL policies as well as state-of-the-art classical and DRL methods in accuracy and anatomical reliability.

