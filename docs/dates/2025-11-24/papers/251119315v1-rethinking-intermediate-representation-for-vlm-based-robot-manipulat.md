---
layout: default
title: Rethinking Intermediate Representation for VLM-based Robot Manipulation
---

# Rethinking Intermediate Representation for VLM-based Robot Manipulation
**arXiv**：[2511.19315v1](https://arxiv.org/abs/2511.19315) · [PDF](https://arxiv.org/pdf/2511.19315.pdf)  
**作者**：Weiliang Tang, Jialin Gao, Jia-Hui Pan, Gang Wang, Li Erran Li, Yunhui Liu, Mingyu Ding, Pheng-Ann Heng, Chi-Wing Fu  

**一句话要点**：提出SEAM中间表示以提升VLM机器人操作的可理解性与泛化性

**关键词**：视觉语言模型, 机器人操作, 中间表示, 开放词汇分割, 检索增强学习, 语义组装

## 3 点简述
- 核心问题：VLM中间表示在可理解性与泛化性间存在权衡
- 方法要点：基于上下文无关语法设计SEAM表示，分解为词汇与语法
- 实验或效果：在真实世界实验中实现SOTA性能，并定义新评估指标

## 摘要（原文）

> Vision-Language Model (VLM) is an important component to enable robust robot manipulation. Yet, using it to translate human instructions into an action-resolvable intermediate representation often needs a tradeoff between VLM-comprehensibility and generalizability. Inspired by context-free grammar, we design the Semantic Assembly representation named SEAM, by decomposing the intermediate representation into vocabulary and grammar. Doing so leads us to a concise vocabulary of semantically-rich operations and a VLM-friendly grammar for handling diverse unseen tasks. In addition, we design a new open-vocabulary segmentation paradigm with a retrieval-augmented few-shot learning strategy to localize fine-grained object parts for manipulation, effectively with the shortest inference time over all state-of-the-art parallel works. Also, we formulate new metrics for action-generalizability and VLM-comprehensibility, demonstrating the compelling performance of SEAM over mainstream representations on both aspects. Extensive real-world experiments further manifest its SOTA performance under varying settings and tasks.

