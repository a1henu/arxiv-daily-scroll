---
layout: default
title: AgentIAD: Tool-Augmented Single-Agent for Industrial Anomaly Detection
---

# AgentIAD: Tool-Augmented Single-Agent for Industrial Anomaly Detection
**arXiv**：[2512.13671v1](https://arxiv.org/abs/2512.13671) · [PDF](https://arxiv.org/pdf/2512.13671.pdf)  
**作者**：Junwen Miao, Penghui Du, Yi Liu, Yu Wang, Yan Wang  

**一句话要点**：提出AgentIAD工具增强单代理框架，以解决工业异常检测中样本稀缺和缺陷细微的问题。

**关键词**：工业异常检测, 工具增强代理, 视觉语言模型, 强化学习, 多阶段视觉检查, 可解释性

## 3 点简述
- 核心问题：工业异常检测因正常样本稀缺和缺陷局部细微而困难，单次视觉语言模型易忽略小异常且缺乏显式比较机制。
- 方法要点：采用工具驱动代理框架，配备感知缩放器和比较检索器，通过监督微调和强化学习两阶段训练，结合感知和行为奖励设计。
- 实验或效果：在MMAD数据集上达到97.62%分类准确率，超越先前基于MLLM的方法，并产生透明可解释的检测轨迹。

## 摘要（原文）

> Industrial anomaly detection (IAD) is difficult due to the scarcity of normal reference samples and the subtle, localized nature of many defects. Single-pass vision-language models (VLMs) often overlook small abnormalities and lack explicit mechanisms to compare against canonical normal patterns. We propose AgentIAD, a tool-driven agentic framework that enables multi-stage visual inspection. The agent is equipped with a Perceptive Zoomer (PZ) for localized fine-grained analysis and a Comparative Retriever (CR) for querying normal exemplars when evidence is ambiguous. To teach these inspection behaviors, we construct structured perceptive and comparative trajectories from the MMAD dataset and train the model in two stages: supervised fine-tuning followed by reinforcement learning. A two-part reward design drives this process: a perception reward that supervises classification accuracy, spatial alignment, and type correctness, and a behavior reward that encourages efficient tool use. Together, these components enable the model to refine its judgment through step-wise observation, zooming, and verification. AgentIAD achieves a new state-of-the-art 97.62% classification accuracy on MMAD, surpassing prior MLLM-based approaches while producing transparent and interpretable inspection traces.

