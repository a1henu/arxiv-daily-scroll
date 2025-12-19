---
layout: default
title: OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models
---

# OS-Oracle: A Comprehensive Framework for Cross-Platform GUI Critic Models
**arXiv**：[2512.16295v1](https://arxiv.org/abs/2512.16295) · [PDF](https://arxiv.org/pdf/2512.16295.pdf)  
**作者**：Zhenyu Wu, Jingjing Xie, Zehao Li, Bowen Yang, Qiushi Sun, Zhaoyang Liu, Zhoumianze Liu, Yu Qiao, Xiangyu Yue, Zun Wang, Zichen Ding  

**一句话要点**：提出OS-Oracle框架以解决跨平台GUI批评模型的数据与评估瓶颈

**关键词**：GUI批评模型, 跨平台评估, 数据合成, 策略优化, 视觉语言模型

## 3 点简述
- 核心问题：GUI批评模型缺乏高质量数据和公共基准，影响计算机使用代理的可靠决策。
- 方法要点：构建可扩展数据管道、两阶段训练范式（SFT与CP-GRPO）及OS-Critic Bench基准。
- 实验或效果：OS-Oracle-7B在OS-Critic Bench上达到开源VLM最佳性能，并提升GUI代理表现。

## 摘要（原文）

> With VLM-powered computer-using agents (CUAs) becoming increasingly capable at graphical user interface (GUI) navigation and manipulation, reliable step-level decision-making has emerged as a key bottleneck for real-world deployment. In long-horizon workflows, errors accumulate quickly and irreversible actions can cause unintended consequences, motivating critic models that assess each action before execution. While critic models offer a promising solution, their effectiveness is hindered by the lack of diverse, high-quality GUI feedback data and public critic benchmarks for step-level evaluation in computer use. To bridge these gaps, we introduce OS-Oracle that makes three core contributions: (1) a scalable data pipeline for synthesizing cross-platform GUI critic data; (2) a two-stage training paradigm combining supervised fine-tuning (SFT) and consistency-preserving group relative policy optimization (CP-GRPO); (3) OS-Critic Bench, a holistic benchmark for evaluating critic model performance across Mobile, Web, and Desktop platforms. Leveraging this framework, we curate a high-quality dataset containing 310k critic samples. The resulting critic model, OS-Oracle-7B, achieves state-of-the-art performance among open-source VLMs on OS-Critic Bench, and surpasses proprietary models on the mobile domain. Furthermore, when serving as a pre-critic, OS-Oracle-7B improves the performance of native GUI agents such as UI-TARS-1.5-7B in OSWorld and AndroidWorld environments. The code is open-sourced at https://github.com/numbmelon/OS-Oracle.

