---
layout: default
title: PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning
---

# PCL-Reasoner-V1.5: Advancing Math Reasoning with Offline Reinforcement Learning
**arXiv**：[2601.14716v1](https://arxiv.org/abs/2601.14716) · [PDF](https://arxiv.org/pdf/2601.14716.pdf)  
**作者**：Yao Lu, Dengdong Fan, Jianzheng Nie, Fan Xu, Jie Chen, Bin Zhou, Yonghong Tian  

**一句话要点**：提出离线强化学习方法PCL-Reasoner-V1.5，以提升大语言模型在数学推理中的性能与训练稳定性。

**关键词**：数学推理, 离线强化学习, 大语言模型, 训练稳定性, 华为昇腾NPU

## 3 点简述
- 核心问题：在线强化学习如GRPO在训练大语言模型时存在稳定性与效率不足的问题。
- 方法要点：基于Qwen2.5-32B，通过监督微调后采用离线强化学习进行优化，提高训练稳定性。
- 实验或效果：在AIME 2024和2025上分别达到90.9%和85.6%的平均准确率，优于同类模型。

## 摘要（原文）

> We present PCL-Reasoner-V1.5, a 32-billion-parameter large language model (LLM) for mathematical reasoning. The model is built upon Qwen2.5-32B and refined via supervised fine-tuning (SFT) followed by reinforcement learning (RL). A central innovation is our proposed offline RL method, which provides superior training stability and efficiency over standard online RL methods such as GRPO. Our model achieves state-of-the-art performance among models post-trained on Qwen2.5-32B, attaining average accuracies of 90.9% on AIME 2024 and 85.6% on AIME 2025. Our work demonstrates offline RL as a stable and efficient paradigm for advancing reasoning in LLMs. All experiments were conducted on Huawei Ascend 910C NPUs.

