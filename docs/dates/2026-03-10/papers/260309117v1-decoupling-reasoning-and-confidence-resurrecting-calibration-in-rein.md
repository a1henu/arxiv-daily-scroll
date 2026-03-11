---
layout: default
title: Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards
---

# Decoupling Reasoning and Confidence: Resurrecting Calibration in Reinforcement Learning from Verifiable Rewards
**arXiv**：[2603.09117v1](https://arxiv.org/abs/2603.09117) · [PDF](https://arxiv.org/pdf/2603.09117.pdf)  
**作者**：Zhengzhao Ma, Xueru Wen, Boxi Cao, Yaojie Lu, Hongyu Lin, Jinglin Yang, Min He, Xianpei Han, Le Sun  

**一句话要点**：提出DCPO框架以解决强化学习可验证奖励中的校准退化问题

**关键词**：强化学习可验证奖励, 校准退化, 梯度冲突, 解耦优化, 大语言模型推理, 过度自信缓解

## 3 点简述
- 核心问题：RLVR增强LLM推理但导致校准退化，模型对错误答案过度自信
- 方法要点：理论分析揭示准确性与校准误差的梯度冲突，提出DCPO解耦推理与校准目标
- 实验或效果：DCPO保持与GRPO相当的准确性，同时实现最佳校准性能，显著缓解过度自信

## 摘要（原文）

> Reinforcement Learning from Verifiable Rewards (RLVR) significantly enhances large language models (LLMs) reasoning but severely suffers from calibration degeneration, where models become excessively over-confident in incorrect answers. Previous studies devote to directly incorporating calibration objective into existing optimization target. However, our theoretical analysis demonstrates that there exists a fundamental gradient conflict between the optimization for maximizing policy accuracy and minimizing calibration error. Building on this insight, we propose DCPO, a simple yet effective framework that systematically decouples reasoning and calibration objectives. Extensive experiments demonstrate that our DCPO not only preserves accuracy on par with GRPO but also achieves the best calibration performance and substantially mitigates the over-confidence issue. Our study provides valuable insights and practical solution for more reliable LLM deployment.

