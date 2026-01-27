---
layout: default
title: GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models
---

# GAIA: A Data Flywheel System for Training GUI Test-Time Scaling Critic Models
**arXiv**：[2601.18197v1](https://arxiv.org/abs/2601.18197) · [PDF](https://arxiv.org/pdf/2601.18197.pdf)  
**作者**：Shaokang Wang, Pei Fu, Ruoceng Zhang, Shaojie Zhang, Xiuwen Xi, Jiahui Yang, Bin Qin, Ying Huang, Zhenbo Luo, Jian Luan  

**一句话要点**：提出GAIA数据飞轮系统以解决GUI代理操作不可逆性问题，提升测试时扩展性能

**关键词**：GUI代理, 数据飞轮系统, 测试时扩展, 直觉批评模型, 视觉语言模型

## 3 点简述
- 核心问题：大型视觉语言模型GUI代理操作不可逆，单次错误可导致灾难性偏差
- 方法要点：训练直觉批评模型评估动作正确性，通过数据飞轮循环收集样本增强批评能力
- 实验或效果：在多种数据集上验证，批评模型能提升闭源和开源模型的测试时性能，性能随数据循环逐步改善

## 摘要（原文）

> While Large Vision-Language Models (LVLMs) have significantly advanced GUI agents' capabilities in parsing textual instructions, interpreting screen content, and executing tasks, a critical challenge persists: the irreversibility of agent operations, where a single erroneous action can trigger catastrophic deviations. To address this, we propose the GUI Action Critic's Data Flywheel System (GAIA), a training framework that enables the models to have iterative critic capabilities, which are used to improve the Test-Time Scaling (TTS) of basic GUI agents' performance. Specifically, we train an Intuitive Critic Model (ICM) using positive and negative action examples from a base agent first. This critic evaluates the immediate correctness of the agent's intended actions, thereby selecting operations with higher success probability. Then, the initial critic guides agent actions to collect refined positive/negative samples, initiating the self-improving cycle. The augmented data then trains a second-round critic with enhanced discernment capability. We conduct experiments on various datasets and demonstrate that the proposed ICM can improve the test-time performance of various closed-source and open-source models, and the performance can be gradually improved as the data is recycled. The code and dataset will be publicly released.

