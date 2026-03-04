---
layout: default
title: Real-Time Generation of Game Video Commentary with Multimodal LLMs: Pause-Aware Decoding Approaches
---

# Real-Time Generation of Game Video Commentary with Multimodal LLMs: Pause-Aware Decoding Approaches
**arXiv**：[2603.02655v1](https://arxiv.org/abs/2603.02655) · [PDF](https://arxiv.org/pdf/2603.02655.pdf)  
**作者**：Anum Afzal, Yuki Saito, Hiroya Takamura, Katsuhito Sudoh, Shinnosuke Takamichi, Graham Neubig, Florian Matthes, Tatsuya Ishigaki  

**一句话要点**：提出基于多模态大语言模型的实时游戏视频解说生成方法，通过暂停感知解码优化时机决策。

**关键词**：实时视频解说生成, 多模态大语言模型, 暂停感知解码, 游戏视频分析, 动态间隔预测

## 3 点简述
- 核心问题：实时视频解说需同时决定内容与时机，现有方法多忽略时机决策。
- 方法要点：提出固定间隔和动态间隔解码策略，无需微调即可实现暂停感知生成。
- 实验效果：在日英赛车与格斗游戏数据集上，动态间隔解码能更贴近人类解说时机与内容。

## 摘要（原文）

> Real-time video commentary generation provides textual descriptions of ongoing events in videos. It supports accessibility and engagement in domains such as sports, esports, and livestreaming. Commentary generation involves two essential decisions: what to say and when to say it. While recent prompting-based approaches using multimodal large language models (MLLMs) have shown strong performance in content generation, they largely ignore the timing aspect. We investigate whether in-context prompting alone can support real-time commentary generation that is both semantically relevant and well-timed. We propose two prompting-based decoding strategies: 1) a fixed-interval approach, and 2) a novel dynamic interval-based decoding approach that adjusts the next prediction timing based on the estimated duration of the previous utterance. Both methods enable pause-aware generation without any fine-tuning. Experiments on Japanese and English datasets of racing and fighting games show that the dynamic interval-based decoding can generate commentary more closely aligned with human utterance timing and content using prompting alone. We release a multilingual benchmark dataset, trained models, and implementations to support future research on real-time video commentary generation.

