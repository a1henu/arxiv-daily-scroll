---
layout: default
title: SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning
---

# SeqWalker: Sequential-Horizon Vision-and-Language Navigation with Hierarchical Planning
**arXiv**：[2601.04699v1](https://arxiv.org/abs/2601.04699) · [PDF](https://arxiv.org/pdf/2601.04699.pdf)  
**作者**：Zebin Han, Xudong Wang, Baichen Liu, Qi Lyu, Zhenduo Shang, Jiahua Dong, Lianqing Liu, Zhi Han  

**一句话要点**：提出SeqWalker模型，通过分层规划解决顺序视野视觉语言导航中的多任务指令挑战。

**关键词**：视觉语言导航, 分层规划, 顺序视野导航, 多任务指令, 轨迹校正

## 3 点简述
- 核心问题：多任务指令导致信息过载，降低导航模型性能。
- 方法要点：采用高层规划器动态选择子指令，低层规划器结合探索验证策略纠正轨迹错误。
- 实验或效果：扩展IVLN数据集建立新基准，实验证明SeqWalker的优越性。

## 摘要（原文）

> Sequential-Horizon Vision-and-Language Navigation (SH-VLN) presents a challenging scenario where agents should sequentially execute multi-task navigation guided by complex, long-horizon language instructions. Current vision-and-language navigation models exhibit significant performance degradation with such multi-task instructions, as information overload impairs the agent's ability to attend to observationally relevant details. To address this problem, we propose SeqWalker, a navigation model built on a hierarchical planning framework. Our SeqWalker features: i) A High-Level Planner that dynamically selects global instructions into contextually relevant sub-instructions based on the agent's current visual observations, thus reducing cognitive load; ii) A Low-Level Planner incorporating an Exploration-Verification strategy that leverages the inherent logical structure of instructions for trajectory error correction. To evaluate SH-VLN performance, we also extend the IVLN dataset and establish a new benchmark. Extensive experiments are performed to demonstrate the superiority of the proposed SeqWalker.

