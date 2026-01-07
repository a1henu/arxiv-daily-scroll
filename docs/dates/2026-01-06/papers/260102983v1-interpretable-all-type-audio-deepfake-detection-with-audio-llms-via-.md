---
layout: default
title: Interpretable All-Type Audio Deepfake Detection with Audio LLMs via Frequency-Time Reinforcement Learning
---

# Interpretable All-Type Audio Deepfake Detection with Audio LLMs via Frequency-Time Reinforcement Learning
**arXiv**：[2601.02983v1](https://arxiv.org/abs/2601.02983) · [PDF](https://arxiv.org/pdf/2601.02983.pdf)  
**作者**：Yuankun Xie, Xiaoxuan Guo, Jiayi Zhou, Tao Wang, Jian Liu, Ruibo Fu, Xiaopeng Wang, Haonan Cheng, Long Ye  

**一句话要点**：提出频率-时间强化学习框架，通过音频大语言模型实现可解释的全类型音频深度伪造检测。

**关键词**：音频深度伪造检测, 音频大语言模型, 强化学习, 可解释人工智能, 频率-时间分析, 思维链

## 3 点简述
- 核心问题：音频大语言模型生成高质量合成音频，增加跨语音、环境声、歌声和音乐的全类型音频深度伪造风险，需可解释检测器。
- 方法要点：构建频率-时间结构化思维链数据，提出两阶段训练范式FT-GRPO，结合监督微调和基于规则的强化微调。
- 实验或效果：FT-GRPO在全类型音频深度伪造检测上达到先进性能，并生成可解释、基于频率-时间的推理依据。

## 摘要（原文）

> Recent advances in audio large language models (ALLMs) have made high-quality synthetic audio widely accessible, increasing the risk of malicious audio deepfakes across speech, environmental sounds, singing voice, and music. Real-world audio deepfake detection (ADD) therefore requires all-type detectors that generalize across heterogeneous audio and provide interpretable decisions. Given the strong multi-task generalization ability of ALLMs, we first investigate their performance on all-type ADD under both supervised fine-tuning (SFT) and reinforcement fine-tuning (RFT). However, SFT using only binary real/fake labels tends to reduce the model to a black-box classifier, sacrificing interpretability. Meanwhile, vanilla RFT under sparse supervision is prone to reward hacking and can produce hallucinated, ungrounded rationales. To address this, we propose an automatic annotation and polishing pipeline that constructs Frequency-Time structured chain-of-thought (CoT) rationales, producing ~340K cold-start demonstrations. Building on CoT data, we propose Frequency Time-Group Relative Policy Optimization (FT-GRPO), a two-stage training paradigm that cold-starts ALLMs with SFT and then applies GRPO under rule-based frequency-time constraints. Experiments demonstrate that FT-GRPO achieves state-of-the-art performance on all-type ADD while producing interpretable, FT-grounded rationales. The data and code are available online.

