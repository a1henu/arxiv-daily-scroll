---
layout: default
title: Learning Human-Like RL Agents Through Trajectory Optimization With Action Quantization
---

# Learning Human-Like RL Agents Through Trajectory Optimization With Action Quantization
**arXiv**：[2511.15055v1](https://arxiv.org/abs/2511.15055) · [PDF](https://arxiv.org/pdf/2511.15055.pdf)  
**作者**：Jian-Ting Guo, Yu-Cheng Chen, Ping-Chun Hsieh, Kuo-Hao Ho, Po-Wei Huang, Ti-Rong Wu, I-Chen Wu  

**一句话要点**：提出宏动作量化框架以优化轨迹，实现类人强化学习行为。

**关键词**：强化学习, 轨迹优化, 宏动作量化, 人类相似行为, 向量量化VAE, D4RL基准

## 3 点简述
- 核心问题：奖励驱动强化学习代理常产生非自然行为，影响可解释性和可信度。
- 方法要点：通过轨迹优化和向量量化VAE将人类演示蒸馏为宏动作。
- 实验效果：在D4RL Adroit基准上显著提升轨迹相似度和人类相似度排名。

## 摘要（原文）

> Human-like agents have long been one of the goals in pursuing artificial intelligence. Although reinforcement learning (RL) has achieved superhuman performance in many domains, relatively little attention has been focused on designing human-like RL agents. As a result, many reward-driven RL agents often exhibit unnatural behaviors compared to humans, raising concerns for both interpretability and trustworthiness. To achieve human-like behavior in RL, this paper first formulates human-likeness as trajectory optimization, where the objective is to find an action sequence that closely aligns with human behavior while also maximizing rewards, and adapts the classic receding-horizon control to human-like learning as a tractable and efficient implementation. To achieve this, we introduce Macro Action Quantization (MAQ), a human-like RL framework that distills human demonstrations into macro actions via Vector-Quantized VAE. Experiments on D4RL Adroit benchmarks show that MAQ significantly improves human-likeness, increasing trajectory similarity scores, and achieving the highest human-likeness rankings among all RL agents in the human evaluation study. Our results also demonstrate that MAQ can be easily integrated into various off-the-shelf RL algorithms, opening a promising direction for learning human-like RL agents. Our code is available at https://rlg.iis.sinica.edu.tw/papers/MAQ.

