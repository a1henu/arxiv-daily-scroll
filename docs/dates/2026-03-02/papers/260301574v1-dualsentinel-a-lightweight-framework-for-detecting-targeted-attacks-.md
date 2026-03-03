---
layout: default
title: DualSentinel: A Lightweight Framework for Detecting Targeted Attacks in Black-box LLM via Dual Entropy Lull Pattern
---

# DualSentinel: A Lightweight Framework for Detecting Targeted Attacks in Black-box LLM via Dual Entropy Lull Pattern
**arXiv**：[2603.01574v1](https://arxiv.org/abs/2603.01574) · [PDF](https://arxiv.org/pdf/2603.01574.pdf)  
**作者**：Xiaoyi Pang, Xuanyi Hao, Pengyu Liu, Qi Luo, Song Guo, Zhibo Wang  

**一句话要点**：提出DualSentinel框架，通过双熵谷模式检测黑盒LLM中的定向攻击

**关键词**：大语言模型安全, 定向攻击检测, 熵谷模式, 轻量级防御, 黑盒设置

## 3 点简述
- 核心问题：黑盒LLM易受后门和提示注入等定向攻击，现有防御方法成本高且不实用
- 方法要点：基于熵谷模式，采用幅度趋势监控和任务翻转双重检查，轻量级实时检测攻击激活
- 实验或效果：评估显示高检测精度、近零误报和可忽略额外成本，提供实用防御路径

## 摘要（原文）

> Recent intelligent systems integrate powerful Large Language Models (LLMs) through APIs, but their trustworthiness may be critically undermined by targeted attacks like backdoor and prompt injection attacks, which secretly force LLMs to generate specific malicious sequences. Existing defensive approaches for such threats typically rely on high access rights, impose prohibitive costs, and hinder normal inference, rendering them impractical for real-world scenarios. To solve these limitations, we introduce DualSentinel, a lightweight and unified defense framework that can accurately and promptly detect the activation of targeted attacks alongside the LLM generation process. We first identify a characteristic of compromised LLMs, termed Entropy Lull: when a targeted attack successfully hijacks the generation process, the LLM exhibits a distinct period of abnormally low and stable token probability entropy, indicating it is following a fixed path rather than making creative choices. DualSentinel leverages this pattern by developing an innovative dual-check approach. It first employs a magnitude and trend-aware monitoring method to proactively and sensitively flag an entropy lull pattern at runtime. Upon such flagging, it triggers a lightweight yet powerful secondary verification based on task-flipping. An attack is confirmed only if the entropy lull pattern persists across both the original and the flipped task, proving that the LLM's output is coercively controlled. Extensive evaluations show that DualSentinel is both highly effective (superior detection accuracy with near-zero false positives) and remarkably efficient (negligible additional cost), offering a truly practical path toward securing deployed LLMs. The source code can be accessed at https://doi.org/10.5281/zenodo.18479273.

