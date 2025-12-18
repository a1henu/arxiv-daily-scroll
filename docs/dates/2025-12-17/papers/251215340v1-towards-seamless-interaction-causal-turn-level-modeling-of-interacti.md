---
layout: default
title: Towards Seamless Interaction: Causal Turn-Level Modeling of Interactive 3D Conversational Head Dynamics
---

# Towards Seamless Interaction: Causal Turn-Level Modeling of Interactive 3D Conversational Head Dynamics
**arXiv**：[2512.15340v1](https://arxiv.org/abs/2512.15340) · [PDF](https://arxiv.org/pdf/2512.15340.pdf)  
**作者**：Junjie Chen, Fei Wang, Zhihao Huang, Qing Zhou, Kun Li, Dan Guo, Linfeng Zhang, Xun Yang  

**一句话要点**：提出TIMAR因果框架以解决3D对话头部动态生成中的时序连贯性问题

**关键词**：3D对话头部生成, 因果建模, 多模态融合, 扩散模型, 时序连贯性, 交互式机器人

## 3 点简述
- 核心问题：现有方法将对话中的说话与倾听视为独立过程或依赖非因果建模，导致跨轮次时序不连贯
- 方法要点：TIMAR融合多模态信息，采用轮次级因果注意力积累历史，结合轻量扩散头预测连续3D头部动态
- 实验或效果：在DualTalk基准测试中，Fréchet距离和MSE降低15-30%，并在分布外数据上取得类似提升

## 摘要（原文）

> Human conversation involves continuous exchanges of speech and nonverbal cues such as head nods, gaze shifts, and facial expressions that convey attention and emotion. Modeling these bidirectional dynamics in 3D is essential for building expressive avatars and interactive robots. However, existing frameworks often treat talking and listening as independent processes or rely on non-causal full-sequence modeling, hindering temporal coherence across turns. We present TIMAR (Turn-level Interleaved Masked AutoRegression), a causal framework for 3D conversational head generation that models dialogue as interleaved audio-visual contexts. It fuses multimodal information within each turn and applies turn-level causal attention to accumulate conversational history, while a lightweight diffusion head predicts continuous 3D head dynamics that captures both coordination and expressive variability. Experiments on the DualTalk benchmark show that TIMAR reduces Fréchet Distance and MSE by 15-30% on the test set, and achieves similar gains on out-of-distribution data. The source code will be released in the GitHub repository https://github.com/CoderChen01/towards-seamleass-interaction.

