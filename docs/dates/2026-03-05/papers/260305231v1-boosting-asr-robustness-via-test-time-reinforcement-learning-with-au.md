---
layout: default
title: Boosting ASR Robustness via Test-Time Reinforcement Learning with Audio-Text Semantic Rewards
---

# Boosting ASR Robustness via Test-Time Reinforcement Learning with Audio-Text Semantic Rewards
**arXiv**：[2603.05231v1](https://arxiv.org/abs/2603.05231) · [PDF](https://arxiv.org/pdf/2603.05231.pdf)  
**作者**：Linghan Fang, Tianxin Xie, Li Liu  

**一句话要点**：提出ASR-TRA测试时强化适应框架，通过音频-文本语义奖励提升ASR在噪声和口音数据上的鲁棒性。

**关键词**：自动语音识别, 测试时适应, 强化学习, 语义奖励, 鲁棒性提升, 噪声口音处理

## 3 点简述
- 核心问题：ASR系统对未见噪声和口音数据敏感，现有测试时适应方法易因高置信度错误导致确认偏差。
- 方法要点：引入可学习解码器提示和温度控制随机解码生成候选，利用音频-文本语义奖励模型评分，通过强化学习更新参数。
- 实验或效果：在LibriSpeech噪声和L2 Arctic口音数据集上，相比基线实现更高准确率和更低延迟，增强稳定性和可解释性。

## 摘要（原文）

> Recently, Automatic Speech Recognition (ASR) systems (e.g., Whisper) have achieved remarkable accuracy improvements but remain highly sensitive to real-world unseen data (data with large distribution shifts), including noisy environments and diverse accents. To address this issue, test-time adaptation (TTA) has shown great potential in improving the model adaptability at inference time without ground-truth labels, and existing TTA methods often rely on pseudo-labeling or entropy minimization. However, by treating model confidence as a learning signal, these methods may reinforce high-confidence errors, leading to confirmation bias that undermines adaptation. To overcome these limitations, we present ASR-TRA, a novel Test-time Reinforcement Adaptation framework inspired by causal intervention. More precisely, our method introduces a learnable decoder prompt and utilizes temperature-controlled stochastic decoding to generate diverse transcription candidates. These are scored by a reward model that measures audio-text semantic alignment, and the resulting feedback is used to update both model and prompt parameters via reinforcement learning. Comprehensive experiments on LibriSpeech with synthetic noise and L2 Arctic accented English datasets demonstrate that our method achieves higher accuracy while maintaining lower latency than existing TTA baselines. Ablation studies further confirm the effectiveness of combining audio and language-based rewards, highlighting our method's enhanced stability and interpretability. Overall, our approach provides a practical and robust solution for deploying ASR systems in challenging real-world conditions.

