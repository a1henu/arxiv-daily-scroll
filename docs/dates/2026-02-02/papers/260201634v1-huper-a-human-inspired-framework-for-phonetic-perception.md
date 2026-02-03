---
layout: default
title: HuPER: A Human-Inspired Framework for Phonetic Perception
---

# HuPER: A Human-Inspired Framework for Phonetic Perception
**arXiv**：[2602.01634v1](https://arxiv.org/abs/2602.01634) · [PDF](https://arxiv.org/pdf/2602.01634.pdf)  
**作者**：Chenxu Guo, Jiachen Lian, Yisi Liu, Baihe Huang, Shriyaa Narayanan, Cheol Jun Cho, Gopala Anumanchipalli  

**一句话要点**：提出HuPER框架，通过自适应推理建模语音感知，在有限数据下实现高性能和多语言零样本迁移。

**关键词**：语音感知建模, 自适应推理, 多语言零样本迁移, 声学-语音证据, 开源框架

## 3 点简述
- 核心问题：语音感知建模需结合声学证据与语言知识，适应多变声学条件。
- 方法要点：采用人类启发式自适应推理，整合声学-语音证据和语言知识。
- 实验或效果：仅用100小时数据，在五个英语基准上达到SOTA，零样本迁移至95种未见语言。

## 摘要（原文）

> We propose HuPER, a human-inspired framework that models phonetic perception as adaptive inference over acoustic-phonetics evidence and linguistic knowledge. With only 100 hours of training data, HuPER achieves state-of-the-art phonetic error rates on five English benchmarks and strong zero-shot transfer to 95 unseen languages. HuPER is also the first framework to enable adaptive, multi-path phonetic perception under diverse acoustic conditions. All training data, models, and code are open-sourced. Code and demo avaliable at https://github.com/HuPER29/HuPER.

