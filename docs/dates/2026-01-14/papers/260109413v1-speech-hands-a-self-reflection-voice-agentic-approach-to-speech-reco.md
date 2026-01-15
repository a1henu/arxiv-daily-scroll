---
layout: default
title: Speech-Hands: A Self-Reflection Voice Agentic Approach to Speech Recognition and Audio Reasoning with Omni Perception
---

# Speech-Hands: A Self-Reflection Voice Agentic Approach to Speech Recognition and Audio Reasoning with Omni Perception
**arXiv**：[2601.09413v1](https://arxiv.org/abs/2601.09413) · [PDF](https://arxiv.org/pdf/2601.09413.pdf)  
**作者**：Zhen Wan, Chao-Han Huck Yang, Jinchuan Tian, Hanrong Ye, Ankita Pasad, Szu-wei Fu, Arushi Goel, Ryo Hachiuma, Shizhe Diao, Kunal Dhawan, Sreyan Ghosh, Yusuke Hirota, Zhehuai Chen, Rafael Valle, Ehsan Hosseini Asl, Chenhui Chu, Shinji Watanabe, Yu-Chiang Frank Wang, Boris Ginsburg  

**一句话要点**：提出语音代理框架Speech-Hands，通过自反思决策解决音频理解中模型易受噪声误导的问题。

**关键词**：语音识别, 音频推理, 代理框架, 自反思学习, 全感知模型

## 3 点简述
- 核心问题：全模型在语音识别和外部声音理解任务上微调时，性能可能因噪声假设而下降。
- 方法要点：引入可学习的自反思原语，让模型决定何时信任自身或咨询外部感知。
- 实验或效果：在OpenASR基准上WER降低12.1%，音频问答准确率达77.37%，展现强泛化能力。

## 摘要（原文）

> We introduce a voice-agentic framework that learns one critical omni-understanding skill: knowing when to trust itself versus when to consult external audio perception. Our work is motivated by a crucial yet counterintuitive finding: naively fine-tuning an omni-model on both speech recognition and external sound understanding tasks often degrades performance, as the model can be easily misled by noisy hypotheses. To address this, our framework, Speech-Hands, recasts the problem as an explicit self-reflection decision. This learnable reflection primitive proves effective in preventing the model from being derailed by flawed external candidates. We show that this agentic action mechanism generalizes naturally from speech recognition to complex, multiple-choice audio reasoning. Across the OpenASR leaderboard, Speech-Hands consistently outperforms strong baselines by 12.1% WER on seven benchmarks. The model also achieves 77.37% accuracy and high F1 on audio QA decisions, showing robust generalization and reliability across diverse audio question answering datasets. By unifying perception and decision-making, our work offers a practical path toward more reliable and resilient audio intelligence.

