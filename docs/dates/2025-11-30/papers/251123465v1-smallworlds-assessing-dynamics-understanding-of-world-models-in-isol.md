---
layout: default
title: SmallWorlds: Assessing Dynamics Understanding of World Models in Isolated Environments
---

# SmallWorlds: Assessing Dynamics Understanding of World Models in Isolated Environments
**arXiv**：[2511.23465v1](https://arxiv.org/abs/2511.23465) · [PDF](https://arxiv.org/pdf/2511.23465.pdf)  
**作者**：Xinyi Li, Zaishuo Xia, Weyl Lu, Chenjie Hao, Yubei Chen  

**一句话要点**：提出SmallWorld基准以评估世界模型在孤立环境中的动态理解能力

**关键词**：世界模型评估, 动态建模, 基准测试, 表示学习, 孤立环境, 模型架构比较

## 3 点简述
- 当前世界模型缺乏统一可控的评估设置，难以判断其是否真正捕捉环境动态规则
- 引入SmallWorld基准，在孤立且精确控制动态的环境中评估模型能力，无需手工奖励信号
- 在完全可观测状态空间中对多种代表性架构进行实验，揭示模型捕捉环境结构和预测退化的表现

## 摘要（原文）

> Current world models lack a unified and controlled setting for systematic evaluation, making it difficult to assess whether they truly capture the underlying rules that govern environment dynamics. In this work, we address this open challenge by introducing the SmallWorld Benchmark, a testbed designed to assess world model capability under isolated and precisely controlled dynamics without relying on handcrafted reward signals. Using this benchmark, we conduct comprehensive experiments in the fully observable state space on representative architectures including Recurrent State Space Model, Transformer, Diffusion model, and Neural ODE, examining their behavior across six distinct domains. The experimental results reveal how effectively these models capture environment structure and how their predictions deteriorate over extended rollouts, highlighting both the strengths and limitations of current modeling paradigms and offering insights into future improvement directions in representation learning and dynamics modeling.

